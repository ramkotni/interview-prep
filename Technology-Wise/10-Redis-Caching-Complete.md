# REDIS CACHING - COMPREHENSIVE INTERVIEW Q&A

## Expert Level Q&A | Production Experience

---

## Q1: Redis Fundamentals

**A:** In-memory data store for caching and session management.

### Data Structures:
```
- String: Text/binary data
- List: Ordered collection (linked list)
- Set: Unordered unique collection
- Sorted Set: Ordered by score
- Hash: Key-value pairs
- Stream: Log-like append-only collection
```

### Common Commands:
```bash
# String operations
SET key "value"
GET key
GETEX key EX 3600  # Get with expiration
MGET key1 key2 key3
MSET key1 val1 key2 val2

# Expiration
EXPIRE key 3600  # Expire in 1 hour
TTL key  # Time to live
PERSIST key  # Remove expiration

# List operations
LPUSH mylist "value1"  # Push to left
RPUSH mylist "value2"  # Push to right
LLEN mylist  # List length
LRANGE mylist 0 -1  # Get all values
LPOP mylist  # Pop from left

# Set operations
SADD myset "member1"
SCARD myset  # Set size
SMEMBERS myset  # Get all members
SINTER set1 set2  # Intersection
SUNION set1 set2  # Union

# Hash operations
HSET user:1 name "John" email "john@example.com"
HGET user:1 name
HGETALL user:1
HINCRBY user:1 age 1

# Increment/Decrement
INCR counter
DECR counter
INCRBY counter 10
DECRBY counter 5
```

---

## Q2: Caching Patterns

**A:** Different strategies for caching data.

### Cache-Aside (Most Common):
```java
@Service
public class UserService {
    
    @Autowired
    private RedisTemplate<String, User> redisTemplate;
    
    @Autowired
    private UserRepository userRepository;
    
    public User getUser(Long userId) {
        String cacheKey = "user:" + userId;
        
        // Try cache first
        User user = redisTemplate.opsForValue().get(cacheKey);
        if (user != null) {
            return user;  // Cache hit!
        }
        
        // Cache miss - fetch from DB
        user = userRepository.findById(userId)
            .orElseThrow(() -> new NotFoundException("User not found"));
        
        // Store in cache for 1 hour
        redisTemplate.opsForValue().set(
            cacheKey, 
            user, 
            Duration.ofHours(1)
        );
        
        return user;
    }
}
```

### Write-Through (Data Consistency):
```java
public void updateUser(Long userId, User userData) {
    // Update database first
    User updated = userRepository.save(userData);
    
    // Then update cache
    String cacheKey = "user:" + userId;
    redisTemplate.opsForValue().set(
        cacheKey, 
        updated, 
        Duration.ofHours(1)
    );
}
```

### Write-Behind (High Performance):
```java
@Service
public class UserEmailService {
    
    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;
    
    public void sendEmail(Long userId, String message) {
        // Update cache immediately
        String cacheKey = "pending-emails:" + userId;
        redisTemplate.opsForList().rightPush(cacheKey, message);
        
        // Queue for async processing
        kafkaTemplate.send("email-queue", userId + "", message);
        
        // Database update happens asynchronously
    }
}
```

### Cache Invalidation Patterns:
```java
// 1. TTL (Time To Live) - Automatic expiration
redisTemplate.opsForValue().set(key, value, Duration.ofMinutes(5));

// 2. Event-based invalidation
@EventListener
public void onUserUpdated(UserUpdatedEvent event) {
    String cacheKey = "user:" + event.getUserId();
    redisTemplate.delete(cacheKey);  // Invalidate cache
}

// 3. Lazy invalidation (on miss)
public User getUser(Long userId) {
    String cacheKey = "user:" + userId;
    User user = (User) redisTemplate.opsForValue().get(cacheKey);
    
    if (user == null) {
        user = userRepository.findById(userId).get();
        // Cache is automatically invalidated and refreshed
        redisTemplate.opsForValue().set(cacheKey, user, Duration.ofHours(1));
    }
    return user;
}
```

---

## Q3: Session Management

**A:** Store session data in Redis for scalability.

### Spring Session Configuration:
```java
@Configuration
@EnableRedisHttpSession  // Enable Redis session storage
public class SessionConfig {
    
    @Bean
    public LettuceConnectionFactory connectionFactory() {
        return new LettuceConnectionFactory();
    }
}

// application.properties
spring.session.store-type=redis
spring.redis.host=localhost
spring.redis.port=6379
spring.session.redis.namespace=spring:session
server.servlet.session.timeout=30m
```

### Accessing Session:
```java
@RestController
public class LoginController {
    
    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest request, HttpSession session) {
        // Authenticate user
        User user = authenticateUser(request.getEmail(), request.getPassword());
        
        // Store in session
        session.setAttribute("user", user);
        session.setAttribute("userId", user.getId());
        session.setAttribute("loginTime", System.currentTimeMillis());
        
        return ResponseEntity.ok("Login successful");
    }
    
    @GetMapping("/profile")
    public ResponseEntity<?> getProfile(HttpSession session) {
        Long userId = (Long) session.getAttribute("userId");
        if (userId == null) {
            throw new UnauthorizedException("Not logged in");
        }
        // User is authenticated
        return ResponseEntity.ok(getUserProfile(userId));
    }
}
```

### Redis Session Structure:
```
spring:session:sessions:abc123  # Session data
spring:session:sessions:index:...  # Session index for queries
spring:session:expirations:...  # Session expiration times
```

---

## Q4: Distributed Locking

**A:** Prevent concurrent updates with Redis locks.

```java
@Service
public class OrderService {
    
    @Autowired
    private RedisTemplate<String, String> redisTemplate;
    
    public void processOrder(Long orderId) {
        String lockKey = "order-lock:" + orderId;
        String lockValue = UUID.randomUUID().toString();
        
        // Try to acquire lock
        Boolean acquired = redisTemplate.opsForValue()
            .setIfAbsent(lockKey, lockValue, Duration.ofSeconds(30));
        
        if (Boolean.TRUE.equals(acquired)) {
            try {
                // Critical section - only one thread at a time
                Order order = orderRepository.findById(orderId).get();
                order.setStatus("PROCESSING");
                orderRepository.save(order);
                
                // Process payment
                paymentService.processPayment(order);
                
                order.setStatus("COMPLETED");
                orderRepository.save(order);
                
            } finally {
                // Release lock only if we still own it
                String currentValue = redisTemplate.opsForValue().get(lockKey);
                if (lockValue.equals(currentValue)) {
                    redisTemplate.delete(lockKey);
                }
            }
        } else {
            throw new RuntimeException("Order is being processed by another thread");
        }
    }
}

// Using Redisson library (easier)
@Service
public class OrderServiceWithRedisson {
    
    @Autowired
    private RedissonClient redissonClient;
    
    public void processOrder(Long orderId) {
        RLock lock = redissonClient.getLock("order-lock:" + orderId);
        
        try {
            if (lock.tryLock(10, 30, TimeUnit.SECONDS)) {
                // Process order
            }
        } finally {
            if (lock.isHeldByCurrentThread()) {
                lock.unlock();
            }
        }
    }
}
```

---

## Q5: Rate Limiting

**A:** Limit API requests using Redis tokens.

### Token Bucket Algorithm:
```java
@Component
public class RateLimitInterceptor implements HandlerInterceptor {
    
    @Autowired
    private RedisTemplate<String, String> redisTemplate;
    
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
        String clientId = request.getHeader("X-Client-ID");
        String limitKey = "rate-limit:" + clientId;
        
        // Get remaining tokens
        String countStr = (String) redisTemplate.opsForValue().get(limitKey);
        long count = countStr != null ? Long.parseLong(countStr) : 100;  // 100 requests per minute
        
        if (count <= 0) {
            response.setStatus(429);  // Too Many Requests
            return false;
        }
        
        // Decrement token count
        redisTemplate.opsForValue().decrement(limitKey);
        
        // Reset after 1 minute
        if (!redisTemplate.hasKey(limitKey)) {
            redisTemplate.opsForValue().set(limitKey, "99", Duration.ofMinutes(1));
        }
        
        response.addHeader("X-RateLimit-Remaining", String.valueOf(count - 1));
        return true;
    }
}
```

---

## Q6: Pub/Sub Messaging

**A:** Publish-subscribe pattern for event notification.

```java
@Service
public class RedisPubSubService {
    
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    
    // Publish message
    public void publishUserUpdate(Long userId) {
        UserUpdateEvent event = new UserUpdateEvent(userId);
        redisTemplate.convertAndSend("user-updates", event);
    }
}

@Configuration
public class RedisPubSubConfig {
    
    @Bean
    public MessageListenerAdapter messageListenerAdapter() {
        return new MessageListenerAdapter(new MessageListener());
    }
    
    @Bean
    public RedisMessageListenerContainer redisContainer(
        LettuceConnectionFactory connectionFactory,
        MessageListenerAdapter adapter) {
        
        RedisMessageListenerContainer container = new RedisMessageListenerContainer();
        container.setConnectionFactory(connectionFactory);
        container.addMessageListener(adapter, new PatternTopic("user-updates"));
        return container;
    }
}

@Component
public class MessageListener implements MessageListener {
    
    @Override
    public void onMessage(Message message, byte[] pattern) {
        try {
            UserUpdateEvent event = (UserUpdateEvent) SerializationUtils.deserialize(message.getBody());
            System.out.println("User updated: " + event.getUserId());
            // Handle event
        } catch (Exception e) {
            System.err.println("Error processing message: " + e.getMessage());
        }
    }
}
```

---

## Q7: Redis Persistence

**A:** Ensure data survival after restarts.

### RDB (Redis Database):
```
- Snapshots of entire dataset
- Smaller file size
- Faster recovery
- Risk: Data loss between snapshots
```

### AOF (Append Only File):
```
- Logs every write operation
- Better durability
- Larger file size
- Slower performance
```

### Configuration:
```conf
# redis.conf

# RDB Snapshots
save 900 1        # 900 seconds (15 min), 1 key changed
save 300 10       # 300 seconds (5 min), 10 keys changed
save 60 10000     # 60 seconds (1 min), 10000 keys changed

# AOF
appendonly yes
appendfsync everysec  # Fsync every second (good balance)

# Both - Hybrid
rdb-compression yes
aof-use-rdb-preamble yes
```

---

## Q8: Performance Optimization

✅ **Best Practices:**
- Use connection pooling (Lettuce)
- Pipeline multiple commands
- Use Redis Streams instead of Pub/Sub for reliability
- Monitor memory usage (SET eviction policies)
- Use appropriate data types
- Avoid large values
- Use bit operations for optimization
- Cluster for horizontal scaling

✅ **Eviction Policies:**
```
- noeviction: Return error when limit reached
- allkeys-lru: Evict least recently used key
- volatile-lru: Evict LRU key with TTL
- allkeys-lfu: Evict least frequently used
- random: Random eviction
- ttl: Evict key with shortest TTL
```

---

**Last Updated:** May 8, 2026


