# DATABASES - COMPREHENSIVE INTERVIEW Q&A

## MySQL, PostgreSQL, Oracle, MongoDB, Cassandra

---

## Q1: SQL Database Design

**A:** Relational databases use tables with relationships.

### Normalization Goals:
- **1NF:** Eliminate repeating groups
- **2NF:** Eliminate partial dependencies
- **3NF:** Eliminate transitive dependencies
- **Goal:** Reduce redundancy, improve data integrity

### Example Schema:
```sql
-- Users table
CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(100) UNIQUE NOT NULL,
  name VARCHAR(100) NOT NULL,
  status ENUM('ACTIVE', 'INACTIVE') DEFAULT 'ACTIVE',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_email (email),
  INDEX idx_status (status)
);

-- Orders table
CREATE TABLE orders (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  order_date DATE NOT NULL,
  total_amount DECIMAL(10, 2),
  status ENUM('PENDING', 'COMPLETED', 'CANCELLED'),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  INDEX idx_user_id (user_id),
  INDEX idx_status (status)
);

-- Order items (many-to-many through junction table)
CREATE TABLE order_items (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  order_id BIGINT NOT NULL,
  product_id BIGINT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2),
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  INDEX idx_order_id (order_id)
);
```

### JPA Entity Mapping:
```java
@Entity
@Table(name = "users", indexes = {
    @Index(name = "idx_email", columnList = "email", unique = true),
    @Index(name = "idx_status", columnList = "status")
})
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, unique = true, length = 100)
    private String email;
    
    @Column(nullable = false)
    private String name;
    
    @Enumerated(EnumType.STRING)
    @Column(columnDefinition = "VARCHAR(20) DEFAULT 'ACTIVE'")
    private UserStatus status;
    
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Order> orders = new ArrayList<>();
    
    @CreationTimestamp
    private LocalDateTime createdAt;
    
    @UpdateTimestamp
    private LocalDateTime updatedAt;
}

@Entity
@Table(name = "orders")
public class Order {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    private User user;
    
    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL)
    private List<OrderItem> items;
    
    private LocalDate orderDate;
    private BigDecimal totalAmount;
}
```

---

## Q2: Query Optimization

**A:** Writing efficient SQL queries is critical for performance.

### Best Practices:
```sql
-- ❌ N+1 Query Problem
-- This fetches user, then for each user fetches orders
SELECT * FROM users;
-- Then loop: SELECT * FROM orders WHERE user_id = ?

-- ✅ JOIN to fetch in one query
SELECT u.*, o.* 
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.status = 'ACTIVE';

-- ❌ Full table scan (slow)
SELECT * FROM orders WHERE YEAR(order_date) = 2024;

-- ✅ Use indexes (fast)
SELECT * FROM orders WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01';

-- ❌ Expensive aggregation without index
SELECT COUNT(*) FROM orders GROUP BY user_id;

-- ✅ With proper index
CREATE INDEX idx_user_date ON orders(user_id, order_date);
```

### EXPLAIN Analysis:
```sql
-- See execution plan
EXPLAIN SELECT u.*, COUNT(o.id) order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
LIMIT 10;

-- Result shows:
-- type: ALL (full scan) - slow
-- type: RANGE (index range) - fast
-- rows: 1000000 (scanned rows)
-- Extra: Using index - using index for query
```

---

## Q3: PostgreSQL Advanced Features

**A:** PostgreSQL has powerful advanced capabilities.

### JSON Support:
```sql
-- Store JSON
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  metadata JSONB  -- JSONB is better than JSON (indexed)
);

INSERT INTO users VALUES (1, 'John', '{"city":"NYC","age":30}');

-- Query JSON
SELECT * FROM users WHERE metadata->>'city' = 'NYC';
SELECT * FROM users WHERE metadata@>'{"age":30}';  -- Contains
```

### Window Functions:
```sql
-- Row number within partition
SELECT 
  order_id,
  user_id,
  amount,
  ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY amount DESC) as rank
FROM orders;

-- Running total
SELECT
  order_id,
  amount,
  SUM(amount) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total
FROM orders;
```

### Full-Text Search:
```sql
-- Create index
CREATE INDEX idx_product_search ON products USING gin(to_tsvector('english', description));

-- Search
SELECT * FROM products 
WHERE to_tsvector('english', description) @@ plainto_tsquery('english', 'laptop computer');
```

---

## Q4: MongoDB (NoSQL)

**A:** Document database for flexible schemas.

### Document Structure:
```json
{
  "_id": "ObjectId",
  "name": "John",
  "email": "john@example.com",
  "orders": [
    {
      "id": "12345",
      "total": 100,
      "items": ["item1", "item2"]
    }
  ],
  "profile": {
    "city": "NYC",
    "phone": "555-1234"
  }
}
```

### MongoDB Queries:

```javascript
// Insert
db.users.insertOne({ name: "John", email: "john@example.com" })

// Find
db.users.find({ name: "John" })

// Filter with operators
db.users.find({ 
  $and: [
    { status: "active" },
    { age: { $gt: 18 } }
  ]
})

// Aggregation pipeline (powerful!)
db.orders.aggregate([
  { $match: { user_id: "123" } },
  { $group: { _id: "$user_id", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
])

// Update
db.users.updateOne(
  { _id: ObjectId("...") },
  { $set: { status: "inactive" } }
)

// Delete
db.users.deleteOne({ _id: ObjectId("...") })
```

### Spring Data MongoDB Integration:
```java
@Document(collection = "users")
@Data
public class User {
    @Id
    private String id;
    
    @NotNull
    private String name;
    
    @Indexed(unique = true)
    private String email;
    
    @DBRef  // Reference to another document
    private List<Order> orders;
}

@Repository
public interface UserRepository extends MongoRepository<User, String> {
    Optional<User> findByEmail(String email);
    List<User> findByStatus(String status);
    
    @Query("{ 'email': ?0 }")
    Optional<User> findUserByEmail(String email);
}

@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private MongoTemplate mongoTemplate;
    
    public void updateUserStatus(String userId, String status) {
        mongoTemplate.update(
            Query.query(Criteria.where("_id").is(userId)),
            Update.update("status", status),
            User.class
        );
    }
}
```

---

## Q5: Cassandra (Distributed)

**A:** Highly scalable, fault-tolerant NoSQL database.

### Key Characteristics:
- **Distributed:** No single point of failure
- **Write optimized:** Fast writes, slower reads
- **Consistently hashed:** Data partitioned by partition key
- **Replication:** Configurable replication factor

### CQL (Cassandra Query Language):
```sql
-- Create keyspace (like database)
CREATE KEYSPACE IF NOT EXISTS myapp
  WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor': 3
  };

-- Create table
CREATE TABLE IF NOT EXISTS myapp.users (
  user_id UUID PRIMARY KEY,
  name TEXT,
  email TEXT,
  created_at TIMESTAMP,
  INDEX idx_email ON email
);

-- Insert
INSERT INTO myapp.users (user_id, name, email, created_at) 
VALUES (uuid(), 'John', 'john@example.com', toTimestamp(now()));

-- Query
SELECT * FROM myapp.users WHERE user_id = ?;

-- Clustering columns for range queries
CREATE TABLE IF NOT EXISTS myapp.orders (
  user_id UUID,
  order_date TIMESTAMP,
  order_id UUID,
  amount DECIMAL,
  PRIMARY KEY (user_id, order_date)
) WITH CLUSTERING ORDER BY (order_date DESC);

-- Get user's last 10 orders
SELECT * FROM myapp.orders 
WHERE user_id = ? 
LIMIT 10;
```

---

## Q6: Database Optimization Techniques

### Indexing:
```sql
-- Single column index
CREATE INDEX idx_email ON users(email);

-- Composite index (best if queries filter on both)
CREATE INDEX idx_user_status ON users(user_id, status);

-- Partial index (only specific rows)
CREATE INDEX idx_active_users ON users(status) 
WHERE status = 'ACTIVE';

-- Full-text search index (PostgreSQL)
CREATE INDEX idx_search ON products USING gin(to_tsvector('english', description));
```

### Query Optimization:
```
1. ADD INDEXES on frequently filtered columns
2. AVOID SELECT * - fetch only needed columns
3. USE JOINS instead of multiple queries
4. ADD LIMITS to prevent large result sets
5. USE EXPLAIN to analyze query plans
6. PARTITION large tables (sharding)
7. ADD CACHING layer (Redis) for hot data
```

### Connection Pooling:
```properties
# Tomcat Connection Pool
spring.datasource.tomcat.max-active=20
spring.datasource.tomcat.max-idle=5
spring.datasource.tomcat.min-idle=2
spring.datasource.tomcat.test-on-borrow=true
spring.datasource.tomcat.validation-query=SELECT 1
```

---

## Q7: Comparison Table

| Database | Best For | Scaling | Schema |
|----------|----------|---------|--------|
| **MySQL** | OLTP, Standard web apps | Vertical | Fixed |
| **PostgreSQL** | Complex queries, JSON | Vertical | Fixed |
| **MongoDB** | Flexible schema, rapid development | Horizontal | Flexible |
| **Cassandra** | Massive scale, write-heavy | Horizontal | Flexible |
| **Oracle** | Enterprise, complex transactions | Vertical | Fixed |

---

**Last Updated:** May 8, 2026


