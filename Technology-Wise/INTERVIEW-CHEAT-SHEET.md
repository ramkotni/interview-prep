# 📋 INTERVIEW CHEAT SHEET (Print This!)

## One-Page Quick Reference - Keep in Your Pocket! 🎯

---

## 🔥 YOUR TOP 5 PROJECT STORIES (Memorized Order)

### **#1: AMAZON ROBOTICS (Cascade Failure Fix)**
- **Impact:** 5% error rate → 0.02% (25x) | Prevented $200K loss
- **Challenge:** N+1 database queries (100K queries for 10K orders)
- **Solution:** Optimized JOIN + Redis cache + Circuit breaker
- **Time:** Diagnosed in 30 min, deployed hotfix
- **Key Quote:** "Thinking systematically about cascade failures, not just fixing bugs"

### **#2: ERCOT GRID FREQUENCY (Real-Time Critical System)**
- **Impact:** 99.99% uptime | 1M events/sec | <100ms latency
- **Challenge:** Real-time processing at massive scale, zero false alerts
- **Solution:** Kafka + Spring Reactive + Redis state + ML anomaly detection
- **Key Quote:** "Built system handling 1M events/sec non-blocking, protecting entire power grid"

### **#3: DAM SYSTEM (Elasticsearch Search Optimization)**
- **Impact:** Search latency 500ms → 100ms (5x) | 100K concurrent uploads
- **Challenge:** Sub-100ms search over 100M assets
- **Solution:** CQRS pattern + Elasticsearch + Redis permissions cache
- **Key Quote:** "Separated read/write models, scaled search independently"

### **#4: WELLS FARGO (Strangler Fig Migration)**
- **Impact:** Deploy time 2+ hours → 15 min (8x) | Zero downtime
- **Challenge:** Migrating 15-year-old monolith (10M LOC) to microservices
- **Solution:** Gradual traffic shift 1% → 100%, easy rollback capability
- **Key Quote:** "Migrated monolith to microservices gradually, zero unplanned downtime"

### **#5: CI/CD PIPELINE (Deployment Automation)**
- **Impact:** 8 deploys/week → 50 deploys/day | 2h → 15 min deployment
- **Challenge:** Safe, frequent deployments without breaking things
- **Solution:** GitOps + Infrastructure as Code + Automated testing
- **Key Quote:** "Infrastructure as code enabled 6x velocity increase"

---

## 🧠 MENTAL MODELS (Memorize These!)

| Pattern | When | Mental Model |
|---|---|---|
| **Circuit Breaker** | Service fails | CLOSED→OPEN→HALF_OPEN prevents cascade |
| **Bulkhead** | Resource isolation | Separate pools = failures don't cascade |
| **Saga** | Distributed txns | Sequence of local txns + compensation |
| **CQRS** | Read > Write | Separate read/write models, scale reads |
| **Event Sourcing** | Audit trail | Store events not state, replay to rebuild |
| **Cache-Aside** | Read-heavy | Check cache, miss hits DB, cache result |
| **Strangler Fig** | Migration | New services alongside old, gradual switch |
| **Multi-AZ** | Availability | Replicate across zones, automatic failover |

**KEY: CAP Theorem** - Can't have all 3: Consistency, Availability, Partition Tolerance
→ Choose: Usually Consistency + Partition, use Saga for eventual consistency

---

## 💯 30-SECOND ELEVATOR PITCH

```
"I'm a senior engineer with 18 years building large-scale systems:
 - Amazon Robotics: 10M orders/day, microservices architecture
 - ERCOT: Real-time critical system, 99.99% uptime, 1M events/sec
 - Wipro: Full-stack system, 100K concurrent users
 
Key expertise: Microservices, Kafka, Spring Boot, AWS, Kubernetes
 - Reduced error rate 25x (debugging+optimization)
 - Improved latency 100x (caching strategy)
 - Accelerated deployment 8x (CI/CD infrastructure)
 
I think systematically about system impact: resilience, scalability, observability."
```

---

## 🚨 GOTCHAS & QUICK ANSWERS

| They Ask | Quick Answer |
|---|---|
| "Biggest failure?" | Scale failed (good lesson) → added caching/sharding → problem solved |
| "Difficult decision?" | Monolith vs microservices → chose strangler fig (safest) → worked great |
| "How do you scale?" | Vertical → Horizontal (LB) → Distributed (cache/DB replicas) → Global (CDN/multi-region) |
| "When to use X?" | Kafka: events, ordering needed. RabbitMQ: task queue. |
| "Consistency problem?" | Use eventual consistency + Saga pattern + compensation |
| "Design Twitter?" | (Deep breath) Cache + Kafka + fan-out-on-write + CDN |

---

## ⚡ 4 GOLDEN SIGNALS (To Monitor Any System)

```
1. LATENCY - How fast? (p99 < 500ms good)
2. TRAFFIC - How much? (RPS, understand limits)
3. ERRORS - What fails? (< 0.1% error rate)
4. SATURATION - What's bottleneck? (CPU/Mem < 70%)

Alert if: Any signal unhealthy for 5+ minutes
```

---

## 🎯 SYSTEM DESIGN FLOW (45 minutes)

```
1. CLARIFY (5 min)
   - Scale (DAU, QPS, data size)
   - Consistency needs (strong vs eventual)
   - Availability target (99.9% vs 99.99%)

2. HIGH-LEVEL (10 min)
   - Draw boxes: Web, API, DB, Cache, Queue
   - Data flow arrows
   - Identify bottleneck

3. DEEP-DIVE (20 min)
   - Scale largest bottleneck
   - Database: replicas, sharding, indexing
   - Cache: Redis patterns
   - Queue: Kafka partition strategy

4. TRADE-OFFS (10 min)
   - Cost vs latency
   - Consistency vs availability
   - Complexity vs maintenance
```

---

## 📊 TECH QUICK FACTS

| Tech | Use When | Limit |
|---|---|---|
| **Spring Boot** | Java microservices | 10K RPS/instance |
| **Kafka** | Events, ordering | Partition by key for order |
| **Redis** | Cache/sessions | Memory cost, 1M QPS potential |
| **PostgreSQL** | ACID, relationships | ~10K QPS single instance |
| **MongoDB** | Flexible schema | ~5K QPS single instance |
| **Elasticsearch** | Full-text search | Denormalized copy, eventual consistency |
| **AWS RDS** | Managed DB | Multi-AZ for 99.95% uptime |
| **Docker** | Containerization | Layer caching for faster builds |
| **Kubernetes** | Orchestration | Rolling updates for zero downtime |
| **CloudWatch** | AWS monitoring | 4 golden signals |

---

## 🎓 COMMON MISTAKES (To Avoid)

❌ Don't: Say you know something you don't  
✅ Do: "I haven't done that, but here's how I'd approach it"

❌ Don't: Jump to solution without understanding problem  
✅ Do: Ask clarifying questions first

❌ Don't: Ignore trade-offs  
✅ Do: "Pro: X | Con: Y | Depends on..."

❌ Don't: Design for 1B users on day 1  
✅ Do: Start simple, scale incrementally

❌ Don't: Memorize answers verbatim  
✅ Do: Practice explaining concepts in your own words

---

## ✨ INTERVIEW PERFORMANCE TIPS

1. **Listen actively** - Don't interrupt, clarify requirements
2. **Think out loud** - Show reasoning, not just answer
3. **Draw pictures** - 10-second diagram > 100-word explanation
4. **Use numbers** - "Kafka handles 1M events/sec" vs "handles lots"
5. **Admit uncertainty** - "I haven't done that, but..." > confidence bluffing
6. **Focus on impact** - Always connect to business metrics
7. **Ask questions** - "Would you prioritize latency or cost?" shows depth
8. **Practice answers** - Say out loud before interview (3x minimum)

---

## 🎖️ CLOSING STATEMENT (At End of Interview)

```
"I really enjoyed our system design discussion. 
The approach I'd take is:
1. Start with requirements & constraints
2. Design for today's scale, plan for tomorrow's
3. Monitor everything (observability is critical)
4. Keep things simple until complexity is justified

I'm excited about this role because [company/team reason].
Do you have any remaining questions about my experience?"
```

---

## 📱 KEEP THIS HANDY

- **Print this document** before interview
- **Memorize your 5 STAR stories** (practice saying them)
- **Know the 4 golden signals** (metrics/latency/errors/saturation)
- **Practice system design** (talk through Twitter/Uber example)
- **Sleep well** night before (better than cramming)

---

## 🚀 YOU'VE GOT THIS!

You have:
✅ 18 years experience  
✅ Real projects affecting millions of users  
✅ Proven ability to solve hard problems  
✅ Track record of 25x improvements  
✅ Leadership experience & mentoring  

**Go show them what you've got! 💪**

---

**Print this page | Memorize the 5 stories | Practice explaining concepts out loud | Crush the interview! 🎯**


