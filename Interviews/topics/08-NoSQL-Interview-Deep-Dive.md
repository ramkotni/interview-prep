# NoSQL Interview Deep Dive (MongoDB, DynamoDB, Cassandra)

Use this file to answer NoSQL questions with senior-level confidence.

## 1) When do I choose NoSQL?
- Schema changes frequently
- Massive scale and high write/read throughput
- Need flexible document model or key-value access
- Global distribution and availability requirements

## 2) SQL vs NoSQL (interview-ready)
- SQL: strong relational model and ACID joins/transactions
- NoSQL: horizontal scale, flexible schema, access-pattern-first design
- Senior answer: choose by data model + query patterns + consistency needs

## 3) MongoDB essentials
- Document model (`BSON`) for nested business objects
- Great for evolving product/catalog/user-profile type data
- Index strategy still critical (compound index by query pattern)
- Supports transactions but use carefully for performance

### MongoDB sample schema
```json
{
  "_id": "order_1001",
  "customerId": "cust_200",
  "status": "CREATED",
  "items": [
    {"sku": "sku_1", "qty": 2, "price": 25.0}
  ],
  "totalAmount": 50.0,
  "createdAt": "2026-04-09T10:00:00Z"
}
```

## 4) DynamoDB essentials
- Key-value/document database for predictable low latency at scale
- Design starts with access patterns (PK/SK, GSIs)
- Great for session stores, event metadata, high-throughput lookups
- Understand partition key distribution to avoid hot partitions

### DynamoDB sample key design
- PK: `TENANT#<tenantId>`
- SK: `ORDER#<orderId>`
- GSI1PK: `STATUS#<status>`
- GSI1SK: `CREATED_AT#<timestamp>`

## 5) Cassandra essentials
- Wide-column model, high write throughput, multi-region strengths
- Tune consistency per query (`ONE`, `QUORUM`, etc.)
- Data model is query-driven and denormalized by design
- Good for time-series/event-heavy systems

## 6) Consistency models you must explain
- Strong consistency: immediate correctness, higher coordination cost
- Eventual consistency: better availability/latency, requires reconciliation strategy
- Interview tip: map consistency choice to business criticality

## 7) NoSQL anti-patterns
- Starting schema without access-pattern analysis
- Using random partition keys causing hotspots
- Ignoring TTL/archival strategy for ever-growing tables
- Treating NoSQL like relational joins-heavy engine

## 8) NoSQL + microservices best practices
- One service owns one data store boundary
- Prefer event-driven data sync over shared DB
- Use idempotent consumers for eventual consistency updates
- Add observability around stale data and replication lag

## 9) NoSQL interview questions with quick answers
1. Why NoSQL here? -> "Scale and access pattern fit better than relational joins."
2. How do you prevent hot partition? -> "High-cardinality partition key and traffic-aware key design."
3. How do you handle duplicates? -> "Idempotency keys and upsert-safe writes."
4. How do you model for reads? -> "Query-first denormalized design."
5. How do you do TTL and retention? -> "Policy-based TTL with archival for compliance."

## 10) NoSQL in your profile talk track
"I have worked with MongoDB, Cassandra, and DynamoDB in full-stack systems. My approach is to design data models based on access patterns, partition strategy, and consistency requirements. I combine NoSQL with event-driven architecture and idempotent processing to keep systems scalable and reliable under load."
