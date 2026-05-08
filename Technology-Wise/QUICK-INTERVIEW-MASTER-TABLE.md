# 🎯 QUICK INTERVIEW GUIDE - MASTER TABLE

## All Projects, Architectures & Key Mental Models (One-Page Reference)

---

## 📊 COMPREHENSIVE PROJECT REFERENCE TABLE

| # | **Project Name** | **Company** | **Duration** | **Team Size** | **Core Architecture** | **Key Technologies** | **Scalability** | **Challenge** | **Solution** | **Impact** | **Mental Model** | **Interview Talking Points** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1** | **Grid Frequency Calculator** | ERCOT | 2 years | 8 | Real-time Reactive Pipeline | Java 17, Spring Boot, Kafka, Redis | 1M events/sec | Real-time frequency monitoring (57-63Hz) | Event-driven architecture with reactive streams, Redis for state | 99.99% uptime, 0 false alerts | Send/Transform/Filter pattern | "Real-time critical system handling power grid stability - one alert saves thousands of dollars" |
| **2** | **Amazon Robotics Order Processing** | Amazon | 18 months | 12 | Microservices + Event-Driven | Java 8, Spring Cloud, Kafka, AWS RDS | 10M orders/day peak | N+1 queries causing 5% error rate ($50K/hr loss) | Circuit breaker + query optimization + caching | 5% → 0.02% error rate (25x improvement) | Bulkhead + Circuit Breaker pattern | "Diagnosed and fixed cascade failure in 30 min, prevented $200K loss through aggressive optimization" |
| **3** | **Digital Asset Management System** | Wipro/Apple | 1.5 years | 6 | Full-Stack: React + Spring + MongoDB | React, Redux, Spring Boot, MongoDB, AWS S3, Lambda | 100K concurrent uploads | File indexing and search speed | Elasticsearch + S3 + Lambda for async processing | Search latency: 2s → 100ms | CQRS (Command Query Responsibility) | "Optimized file search using Elasticsearch, massive UX improvement" |
| **4** | **Parking System Design** | Infosys (Interview) | Design exercise | 2-3 | Design Pattern-Based | Java, Observer, Strategy, Factory patterns | 1000+ spots | Concurrent reservation + fairness | Atomic operations + locking | 100% reservation accuracy | Observer + Strategy Pattern | "Built parking system with Observer for notifications, Strategy for allocation algorithms" |
| **5** | **REST API Full Stack** | Multiple | Ongoing | 4-5 | REST + Spring Boot + React | Spring Boot, React, PostgreSQL, Docker, Kubernetes | 100K RPS | API versioning + backward compatibility | Version in URL + MediaType strategy | 0 breaking changes | REST Constraints (Client-Server, Stateless, Cacheable) | "Implemented 3 API versions without breaking existing clients" |
| **6** | **Microservices Migration** | Wells Fargo | 6 months | 10 | Strangler Fig Pattern | Spring Boot, Kafka, AWS, Docker, K8s | Phased migration (20% → 100%) | Monolith coupling + data consistency | Proxy with gradual routing, Saga for transactions | Reduced deployment time: 2h → 15min | Strangler Fig + Saga Pattern | "Migrated monolith to microservices using strangler fig, zero downtime" |
| **7** | **Kafka Event Streaming** | Multiple | 1+ years | 5-6 | Pub/Sub Event-Driven | Kafka, Spring Cloud Stream, Schema Registry | 500M events/day | Message ordering + exactly-once semantics | Partition by key + idempotency | 99.99% delivery guarantee | Event Sourcing + CQRS | "Implemented exactly-once semantics with distributed transactions and compensation" |
| **8** | **AWS Multi-Region Deployment** | ERCOT/Amazon | Ongoing | 4 | Cloud Infrastructure | AWS (EC2, RDS, Lambda, S3), CloudFormation, Route53 | Global failover < 2min | Cross-region consistency | Multi-AZ RDS + Route53 health checks | RTO/RPO < 2min/0 data loss | Active-Active vs Active-Passive | "Implemented multi-region failover, $0 data loss on DR tests" |
| **9** | **Docker & Kubernetes Deployment** | Amazon/ERCOT | 1.5 years | 6 | Container Orchestration | Docker, Kubernetes, Helm, StatefulSets | Auto-scaling 2-50 replicas | Rolling updates + resource limits | Deployment YAML with maxSurge=1, maxUnavailable=0 | 0 downtime deployments | Pod + Deployment + Service model | "Deployed 10K microservice instances with rolling updates" |
| **10** | **Redis Caching Layer** | ERCOT/Multiple | 1+ years | 3-4 | Cache-Aside Pattern | Redis, Spring Data Redis, Caffeine | Sub-millisecond access | Cache invalidation + stampede prevention | TTL + event-based invalidation + Redlock | Latency: 500ms → 5ms (100x) | Cache-Aside vs Write-Through | "Implemented distributed caching with automatic expire and invalidation" |
| **11** | **CI/CD Pipeline** | ERCOT/Amazon | 2 years | 5 | GitOps + Infrastructure as Code | Jenkins, GitLab CI, Docker, Kubernetes, Terraform | 50+ deployments/day | Secret management + staging validation | Secret Manager + automated smoke tests | Deployment time: 2h → 15min | CI/CD Stages (Build → Test → Package → Deploy) | "Built CI/CD reducing deployment time 8x, enabling 50 deploys/day" |
| **12** | **Monitoring & Observability** | ERCOT | 1+ years | 2-3 | 3-Pillars: Logs + Metrics + Traces | CloudWatch, Prometheus, Grafana, ELK Stack | 100K metrics/sec | Alert fatigue + correlation | Correlation IDs + structured logging + SLOs | <5min MTTR (Mean Time To Recovery) | 4 Golden Signals (Latency, Traffic, Errors, Saturation) | "Implemented distributed tracing reducing debug time 50%, MTTR < 5min" |

---

## 🏗️ ARCHITECTURE MENTAL MODELS (Quick Reference)

### **Model 1: Microservices Resilience Pattern**
```
┌─────────────┐
│ Load        │
│ Balancer    │
└──────┬──────┘
       │
   ┌───┴────┬──────┬──────┐
   │        │      │      │
 ┌─▼──┐  ┌─▼──┐ ┌─▼──┐ ┌─▼──┐
 │Srv1│  │Srv2│ │Srv3│ │Srv4│
 │CB  │  │CB  │ │CB  │ │CB  │
 │RI  │  │RI  │ │RI  │ │RI  │
 └────┘  └────┘ └────┘ └────┘
   ▲        ▲      ▲      ▲
   │        └──────┼──────┘
   │     Circuit     Retry
   │     Breaker    Logic
   └─────────────────────────────
   Bulkhead: Separate thread pools
   Fallback: Cache previous response

KEY: Circuit Breaker + Retry + Timeout + Bulkhead + Fallback
```

### **Model 2: Data Consistency in Distributed Systems**
```
STRONG CONSISTENCY          EVENTUAL CONSISTENCY
(Monolith/ACID)             (Microservices/Event-Driven)

Txn 1: UPDATE balance       Event: balance_updated
Txn 2: READ balance         Event: invoice_created
       ↓ reads updated       Event: email_sent
                             ↓ all eventually consistent

Trade-off: Consistency vs Availability & Partition Tolerance
(CAP Theorem)
```

### **Model 3: Caching Strategy**
```
Request Flow:
1. Check Cache (Redis in-memory, <5ms)
2. Cache HIT → Return immediately
3. Cache MISS → DB Query, Update Cache (with TTL)
4. On Data Change → Invalidate Cache

Cache-Aside Pattern: App manages cache logic
Write-Through: Write to cache + DB atomically
Write-Behind: Write cache first, async to DB
```

### **Model 4: Event-Driven System**
```
Producer → Kafka Topic → Consumer
  │         ↓              │
Event   [Partitions]   Process
Stream   [Replication]  Handle
         [Durability]
         
Key insight: Partition by entity ID
→ Same entity always same partition
→ Order guaranteed per entity
→ Parallel processing different entities
```

### **Model 5: System Design Scaling (Three Layers)**
```
Layer 1: Vertical (Single machine)
- Add CPU, RAM, Disk
- Limit: ~1M concurrent connections

Layer 2: Horizontal (Multiple machines)
- Load balancing (Round-robin, least-conn, etc.)
- Database replication (read replicas)
- Scale: Up to 100M connections

Layer 3: Global (Multi-region)
- CDN for static assets
- Data replication (cross-region)
- Geo-routing
- Scale: Unlimited + disaster recovery
```

---

## 🎯 KEY MENTAL MODELS FOR INTERVIEWS

| **Concept** | **When to Use** | **Mental Model** | **Interview Example** |
|---|---|---|---|
| **Circuit Breaker** | Service down/degraded | CLOSED (normal) → OPEN (fail-fast) → HALF_OPEN (test) | "Prevent cascade failure when payment service down" |
| **Bulkhead** | Resource isolation | Separate thread pools per service | "Payment threads don't block order threads" |
| **Saga Pattern** | Distributed transactions | Choreography (event-driven) or Orchestration (coordinator) | "Order → Payment → Inventory with compensation" |
| **CQRS** | Read/write scaling | Separate read model from write model | "Event streaming updates read cache, queries use cache" |
| **Event Sourcing** | Audit trail + replay | Store events not state, rebuild state from events | "Replay order events to see state at any time" |
| **Cache-Aside** | General caching | App checks cache, miss goes to DB, updates cache | "Check Redis, miss hits DB, caches with TTL" |
| **Eventual Consistency** | High availability | Accept temporary inconsistency, converge eventually | "Order acknowledged before inventory updated" |
| **API Gateway** | Request routing | Single entry point, authentication, rate limiting | "Route /orders to order-service, /payments to payment-service" |
| **Service Discovery** | Dynamic services | Services register/deregister automatically | "New service instance auto-added to load balancer" |
| **3-Pillars Observability** | Debug production | Logs (what) + Metrics (how much) + Traces (flow) | "Alert on metric, drill to logs, correlate traces" |

---

## 💼 INTERVIEW QUICK REFERENCE

### **When They Ask "Tell Me About Your Experience":**
```
"I have 18 years building large-scale systems:
- 2 years at ERCOT: Real-time grid monitoring, 99.99% uptime
- 4 years at Amazon: Robotics order processing, 10M orders/day
- 3 years at Wipro: Full-stack DAM system, 100K concurrent users
- Built microservices, Kafka pipelines, Kubernetes clusters
- Expertise: Java, Spring Boot, Microservices, AWS, DevOps
- Key wins: 25x error reduction, 8x deployment speedup, 100x latency improvement"
```

### **When They Ask "Describe Your Biggest Project":**
```
PROJECT: Amazon Robotics Order Processing
SCALE: 10M orders/day, 12 person team, 2 years
CHALLENGE: 5% error rate due to N+1 queries ($50K/hour loss)
SOLUTION: 
  1. Analyzed CloudWatch logs (30 min) → found N+1
  2. Optimized queries with JOINs
  3. Added Redis caching layer
  4. Implemented circuit breaker for resilience
RESULT: 5% → 0.02% error rate (25x improvement)
IMPACT: Prevented $200K loss, Improved UX, System handles peak
```

### **When They Ask "What Was Your Biggest Challenge":**
```
CHALLENGE: Cascade failure in microservices (payment service down)
PROBLEM: Order service timeout, customers can't checkout
SOLUTION:
  1. Implemented circuit breaker (fail-fast, not timeout)
  2. Used fallback (mark order pending, retry later)
  3. Added bulkhead (payment threads isolated)
  4. Monitoring alerts (catch issues early)
LEARNING: Resilience requires multiple layers
```

### **When They Ask "System Design":**
```
Always follow:
1. CLARIFY requirements (scale, consistency, availability)
2. HIGH-LEVEL design (services, databases, caches)
3. DEEP-DIVE (largest bottleneck first)
4. SCALE (vertical → horizontal → global)
5. TRADE-OFFS (consistency vs availability, latency vs cost)

Example: Design Twitter Feed
- Requirements: 1B users, 100M daily active, <1sec latency
- High-level: User service + Tweet service + Feed service
- Bottleneck: Feed generation (billions of combinations)
- Solution: Cache hot feeds in Redis, use fanout on write
- Trade-off: More disk (cache) vs faster reads
```

---

## 🔥 ONE-LINE MENTAL MODELS (Interview Gold)

| **Model** | **One-Liner** | **Use Case** |
|---|---|---|
| **Microservices** | Independent scalability but operational complexity | When parts of system need different scale |
| **Event-Driven** | Eventual consistency enables massive scale | When you need 10M+ events/second |
| **Cache-Aside** | Miss goes DB, Update cache, TTL = eventual consistency | When you have hot data accessed frequently |
| **Circuit Breaker** | CLOSED→OPEN→HALF_OPEN prevents cascade failure | When dependent service can go down |
| **Saga Pattern** | Sequence of transactions with compensation for failure | When you have multi-service transactions |
| **CQRS** | Separate read/write models = scale reads independently | When reads massively outnumber writes |
| **Bulkhead** | Isolate resource pools = one failure doesn't cascade | When you have multiple competing workloads |
| **Load Balancing** | Distribute traffic = one server doesn't become bottleneck | When single machine can't handle QPS |
| **Database Replication** | Multiple copies = read scaling but consistency challenges | When read queries overwhelm single DB |
| **CDN** | Cache on edge = reduce latency to users globally | When users are geographically distributed |

---

## 📈 PROJECTS BY IMPACT (Ranked)

| **Rank** | **Project** | **Scale** | **Complexity** | **Impact** | **Key Takeaway** |
|---|---|---|---|---|---|
| 🥇 | Amazon Robotics | 10M/day | Microservices + Kafka | 25x error reduction | Think systems thinking (cascade failures) |
| 🥈 | ERCOT Grid Frequency | 1M events/sec | Real-time reactive | 99.99% availability | Real-time systems need different approach |
| 🥉 | DAM System | 100K concurrent | Full-stack + distributed | 100x latency improvement | Caching is king for read-heavy systems |
| 4 | Kubernetes Deployment | 10K instances | Container orchestration | 0 downtime deploys | Infrastructure as code enables velocity |
| 5 | CI/CD Pipeline | 50 deploys/day | DevOps automation | 8x faster deployment | Automation multiplies team productivity |

---

## 🧠 MENTAL MODELS: SYSTEM DESIGN DECISION TREE

```
REQUIREMENT
    ↓
Need High Availability?
├─ YES → Multi-AZ/Region
│   └─ Need < 2min failover? → Multi-AZ RDS
│   └─ Global scaling? → CDN + Global load balancing
└─ NO → Single region OK

Need High Throughput?
├─ YES → Horizontal scaling needed
│   ├─ Compute → Load balancer + auto-scaling
│   ├─ DB reads → Read replicas + cache
│   └─ Events → Kafka partitions + consumer groups
└─ NO → Vertical scaling sufficient

Need Strong Consistency?
├─ YES → Monolith or wait for eventual consistency
│   └─ Accept higher latency/costs
└─ NO → Eventual consistency enables scale
    └─ Event-driven + Kafka

Need to Scale Reads > Writes?
├─ YES → Cache layer (Redis)
│   └─ Separate read database (CQRS)
└─ NO → Standard DB replication fine

Need Resilience?
├─ YES → Circuit breaker + retries + bulkhead
│   └─ Add monitoring + alerting
└─ NO → Monolith risk acceptable
```

---

## 🎯 INTERVIEW CONVERSATION STARTERS

**"Let me tell you about how I think about systems..."** (Pick relevant)

1. **Resilience:** "I always start by thinking about failure points - what if this service goes down? That's why I use circuit breakers, retries, and bulkheads."

2. **Scale:** "For handling millions of requests, I think in layers - cache hot data, partition by entity, replicate globally. Each layer has trade-offs."

3. **Consistency:** "In distributed systems, you choose between consistency and availability. I prefer eventual consistency for better uptime, then handle it through events and compensating transactions."

4. **Monitoring:** "I obsess over the 4 golden signals - latency, traffic, errors, saturation. Catch issues before they impact users through correlation IDs and structured logging."

5. **DevOps:** "I believe in infrastructure as code and automation - every deployment should be identical and repeatable. That's why CI/CD and Kubernetes matter."

---

## 📋 QUICK PREP CHECKLIST (Before Interview)

```
TECHNICAL:
☐ Can explain each project in 2 min
☐ Know metrics (scale, latency, availability)
☐ Have one code example for key technology
☐ Can draw architecture on whiteboard
☐ Ready with "biggest challenge + solution"

MENTAL MODELS:
☐ Circuit breaker pattern explained
☐ CAP theorem understood
☐ When to use caching vs DB
☐ How to scale distributed system
☐ Eventual vs strong consistency

BEHAVIORAL:
☐ 3-5 STAR stories prepared
☐ Failure + recovery story ready
☐ Team collaboration example
☐ Learning from mistakes story
☐ Technical decision story

QUESTIONS YOU'LL GET (Practice Answers):
☐ "Tell me about yourself" (30 sec)
☐ "Tell me about your biggest project" (3 min)
☐ "What was your biggest challenge" (3 min)
☐ "Design a system like Twitter" (45 min)
☐ "Tell me about a difficult decision" (2 min)
```

---

## 🎓 FINAL WISDOM

### **The Core Skill:**
```
Technical Knowledge: 40%
Communication: 30%
Problem-Solving: 20%
Culture Fit: 10%

So PRACTICE answering out loud, use analogies,
explain your thinking, show work on whiteboard
```

### **System Design Framework (Always Use):**
```
1. CLARIFY (Requirements) - 5 minutes
2. HIGH-LEVEL (Architecture) - 10 minutes
3. DETAIL (Bottleneck) - 20 minutes
4. OPTIMIZE (Scale/Trade-offs) - 10 minutes
```

### **The Edge You Have:**
```
Most candidates know technologies.
YOU know how they work TOGETHER.
YOU have production experience.
YOU can talk about trade-offs.
YOU can explain failures and recovery.

That's your unfair advantage.
```

---

**Last Updated:** May 8, 2026  
**Status:** ✅ QUICK REFERENCE READY  
**Use:** 5 minutes before any interview! 🚀


