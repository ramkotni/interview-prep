# Last 1 Hour Cheat Sheet (Senior Java Full-Stack)

Use this before interview rounds.

## 1) 60-second intro script
"I have around 18 years of experience in Java full-stack engineering. I build and scale Spring Boot microservices, Angular/React frontends, and cloud-native platforms on AWS. I focus on architecture, reliability, security, and delivery speed, and I also mentor teams and drive production readiness. In projects like ERCOT and Amazon Robotics, I handled both high business criticality and strong NFR needs such as performance, auditability, and resilience."

## 2) Top 20 must-answer lines
1. Java strength: "I use Java for stable, secure, and maintainable distributed systems."
2. Spring style: "Controller -> Service -> Repository with DTO validation and global exception handling."
3. API quality: "Versioned contracts, idempotency, pagination, proper status codes, clear error model."
4. Security: "JWT/OAuth2, RBAC, least privilege, secrets management, audit logging."
5. Microservices: "Domain-based boundaries, async where coupling is high, resilient sync calls."
6. Resilience: "Timeout + retry with backoff + circuit breaker + fallback."
7. Angular structure: "Feature modules, services, guards, interceptors, reactive forms."
8. Angular performance: "Lazy loading, OnPush, trackBy, virtual scroll."
9. DB tuning: "Indexes, query plans, pagination, caching, remove chatty calls."
10. Kafka: "Decouple workflows, consumer groups, retry/DLQ, idempotent consumers."
11. Cloud: "Stateless services + autoscaling + observability + safe rollback."
12. CI/CD: "Build, tests, quality gates, progressive deploy, rollback plan."
13. Observability: "Logs + metrics + traces with correlation IDs."
14. System design: "Clarify requirements first, then NFR-driven architecture."
15. NFR list: "Availability, latency, throughput, security, compliance, operability."
16. ERCOT line: "Moderate users but high audit/compliance criticality."
17. Amazon line: "High event throughput and low-latency processing focus."
18. Biogen line: "Data integrity and auditability first due to regulation."
19. Dell line: "Data consistency across PLM-ERP-MES integrations was key."
20. Leadership: "I remove blockers, make trade-offs explicit, and mentor ownership."

## 3) System design answer skeleton (2 min)
1. Requirements: functional + constraints
2. NFR targets: latency, availability, RPO/RTO, security, scale
3. High-level architecture
4. Data model + API contracts
5. Failure handling and observability
6. Trade-offs and rollout strategy

## 4) NFR quick table (memorize)
- Performance: cache hot paths, reduce round trips, tune DB
- Availability: multi-instance, health checks, auto-healing
- Scalability: stateless services, async queues, partitioning
- Security: authN/authZ, encryption, least privilege, audits
- Reliability: retries, circuit breakers, idempotency
- Maintainability: modular code, standards, runbooks

## 5) Red flags to avoid in interviews
- Do not say "it depends" without giving criteria.
- Do not claim exact numbers unless confident; give ranges.
- Do not skip trade-offs.
- Do not explain only happy path; include failure path.
- Do not discuss frontend security without backend enforcement.

## 6) Quick NoSQL pitch (30 sec)
"I use NoSQL based on access patterns. MongoDB is useful for flexible JSON documents and evolving schemas, DynamoDB for predictable low-latency key-value access at scale, and Cassandra for high write throughput and multi-region availability. I still design keys/indexes first and handle consistency trade-offs carefully."

## 7) Final closing line
"I can contribute as a hands-on senior engineer who designs clean architecture, delivers reliable systems, and drives teams to ship fast without sacrificing quality or compliance."
