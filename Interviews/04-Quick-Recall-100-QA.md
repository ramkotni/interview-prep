# Quick Recall 100 Q&A (Easy Memory Version)

Use this for daily fast recall. Each answer is intentionally short.

## A) Self Intro + Leadership (1-15)
1. Tell me about yourself. -> 18 years in Java full-stack, microservices, Angular, cloud, and production reliability.
2. What is your key strength? -> End-to-end ownership from design to production.
3. Why senior role? -> I combine hands-on coding with architecture and incident leadership.
4. Leadership style? -> Hands-on, clear priorities, and unblock teams quickly.
5. How do you mentor? -> Design reviews, pairing, and ownership transfer.
6. How do you prioritize? -> Business impact, risk, dependency, deadline.
7. Handling conflict? -> Align on facts, options, and measurable outcomes.
8. Stakeholder communication? -> Risk, timeline, and business impact in plain language.
9. Handling pressure? -> Stabilize first, root cause next, prevention last.
10. Code quality approach? -> Reviews, tests, quality gates, observability.
11. Handling scope changes? -> Re-estimate impact and re-align priorities.
12. What motivates you? -> Solving business-critical engineering problems.
13. Biggest value to team? -> Predictable delivery with strong technical depth.
14. How do you run retrospectives? -> Turn problems into owner-based action items.
15. Definition of release success? -> Stable production and expected business outcome.

## B) Java Core (16-35)
16. Why Java? -> Stability, ecosystem maturity, and JVM performance.
17. `HashMap` vs `ConcurrentHashMap`? -> Non-thread-safe vs concurrent-safe map.
18. `volatile` vs `synchronized`? -> Visibility only vs visibility + mutual exclusion.
19. Deadlock prevention? -> Lock ordering and timeout strategy.
20. Why `ExecutorService`? -> Controlled thread pooling and better resource usage.
21. Why `CompletableFuture`? -> Non-blocking composition of async tasks.
22. What is immutability? -> Object state cannot change after creation.
23. Why immutability? -> Thread safety and predictable behavior.
24. Checked vs unchecked exceptions? -> Compile-time handled vs runtime.
25. `equals`/`hashCode` contract? -> Equal objects must have equal hash code.
26. Streams use case? -> Declarative collection processing.
27. `map` vs `flatMap`? -> Transform value vs flatten nested structure.
28. Parallel streams caution? -> Use only after benchmark; avoid blocking workloads.
29. Memory leak diagnosis? -> Heap dump + retained object analysis.
30. GC impact handling? -> Reduce allocation churn and tune after code fix.
31. Thread-safe design? -> Minimize shared state, use concurrent structures.
32. Fail-fast iterator? -> Detect structural modification during iteration.
33. `Comparable` vs `Comparator`? -> Natural ordering vs custom ordering.
34. Java record use? -> Immutable DTO/data carrier.
35. Pre-merge checklist? -> Tests pass, edge cases, logs, readability.

## C) Spring + APIs + Microservices (36-60)
36. Why Spring Boot? -> Fast bootstrap and production-ready capabilities.
37. `@RestController` use? -> Build JSON REST APIs.
38. Constructor injection? -> Better testability and immutability.
39. Validation style? -> Bean validation + global exception handling.
40. API error standard? -> Stable error code, message, correlation id.
41. JWT flow? -> Login, token issue, header validation per request.
42. RBAC? -> Role-based endpoint and method authorization.
43. Idempotency? -> Same request gives same final outcome.
44. PUT vs PATCH? -> Full replace vs partial update.
45. API versioning? -> Versioned paths/headers with backward compatibility.
46. N+1 problem fix? -> Fetch joins/projections/entity graphs.
47. DB migration strategy? -> Flyway/Liquibase in CI/CD.
48. Externalized config? -> Profiles + env vars + secret manager.
49. Circuit breaker? -> Stop repeated calls to failing dependency.
50. Safe retries? -> Backoff + jitter + idempotent operations only.
51. Saga pattern? -> Distributed transaction with compensation.
52. API gateway role? -> Routing, auth, throttling, policy.
53. Service discovery role? -> Dynamic instance resolution.
54. Tracing strategy? -> Correlation id + distributed trace.
55. Bulkhead pattern? -> Resource isolation to limit blast radius.
56. Timeout strategy? -> Per dependency based on SLO.
57. Microservice testing? -> Unit + integration + contract + e2e.
58. Secure file upload? -> Validate type/size and scan async.
59. API best practices? -> Pagination, filtering, status codes, clear contracts.
60. Spring production checklist? -> Health, logs, metrics, limits, rollback.

## D) Angular + Frontend (61-78)
61. Why Angular? -> Structured enterprise frontend framework.
62. Core building blocks? -> Module, component, service, router, DI.
63. Data binding types? -> Interpolation, property, event, two-way.
64. `constructor` vs `ngOnInit`? -> DI vs initialization logic.
65. Lifecycle hooks to know? -> OnInit, OnChanges, AfterViewInit, OnDestroy.
66. Service role? -> API and shared business logic.
67. HTTP interceptor use? -> Token injection and centralized error handling.
68. Route guards use? -> Access protection by auth/roles.
69. Reactive forms benefit? -> Scalable validation for complex forms.
70. RxJS `switchMap` use? -> Cancel stale requests (search).
71. RxJS `mergeMap` use? -> Parallel independent requests.
72. Memory leak prevention? -> Unsubscribe or `async` pipe.
73. Lazy loading benefit? -> Faster initial load.
74. `OnPush` strategy? -> Reduce change-detection cost.
75. Large list optimization? -> Virtual scroll + pagination + trackBy.
76. Angular vs React? -> Structure-first vs flexibility-first.
77. Frontend security rule? -> UI checks + mandatory backend auth.
78. Frontend production checklist? -> Perf, accessibility, errors, observability.

## E) Cloud + Kafka + DevOps + NoSQL (79-92)
79. AWS compute choice? -> EC2/ECS/EKS based on control vs ops overhead.
80. S3 use? -> Durable object storage.
81. IAM best practice? -> Least privilege and role-based access.
82. CloudWatch use? -> Metrics, logs, alerts.
83. Kafka key benefit? -> Decouple services and absorb load spikes.
84. Partition key importance? -> Parallelism and order behavior.
85. Consumer group role? -> Scale consumers horizontally.
86. DLQ role? -> Isolate and replay failed messages safely.
87. Idempotent consumer? -> Avoid duplicate side effects.
88. Zero-downtime deploy? -> Blue-green/canary + rollback.
89. CI/CD stages? -> Build, test, quality gate, deploy, verify.
90. NoSQL when? -> Flexible schema and high scale access patterns.
91. MongoDB use case? -> Document-heavy evolving domain models.
92. DynamoDB use case? -> Predictable low-latency key-value access.

## F) System Design + NFR + Projects (93-100)
93. Design interview start? -> Clarify requirements and NFR targets first.
94. Top NFRs? -> Availability, latency, throughput, security, operability.
95. High availability strategy? -> Multi-instance + health checks + failover.
96. Resilience strategy? -> Timeout, retry, circuit breaker, fallback.
97. Observability strategy? -> Logs, metrics, traces, SLO alerts.
98. ERCOT one line? -> Compliance and auditability with secure workflows.
99. Amazon one line? -> Throughput and low-latency event processing.
100. Biogen/Dell one line? -> Regulated integrity (Biogen) and integration consistency (Dell).
