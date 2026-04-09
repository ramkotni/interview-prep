# Top 75 Tricky Interview Q&A (Senior Answers)

These are high-probability tough questions.

## Architecture and Design
1. Why not microservices everywhere? -> Added complexity is justified only when independent scaling/deployment is needed.
2. Monolith first or microservices first? -> Start with modular monolith unless domain/scale strongly demands microservices.
3. Strong vs eventual consistency? -> Strong for money/compliance workflows; eventual for high-scale async operations.
4. How do you prevent cascading failures? -> Timeouts, retry budget, circuit breaker, bulkhead isolation.
5. How do you handle traffic spikes? -> Autoscale stateless services, queue buffering, priority load shedding.
6. What is your API versioning strategy? -> Backward compatibility first, explicit deprecation and migration window.
7. How do you define service boundaries? -> Business capabilities and ownership boundaries, not technical layers.
8. How do you design for rollback? -> Immutable artifact, compatibility-first DB/API changes, quick rollback path.
9. How do you avoid tight coupling? -> Contract-driven APIs and event-driven integration.
10. How do you validate architecture choices? -> Prototype critical path and load test before broad rollout.

## Reliability and Incidents
11. First 5 minutes in Sev-1? -> Contain blast radius, assign owners, establish communication channel.
12. Hotfix vs rollback? -> Rollback if safe and faster; hotfix only when rollback risk is higher.
13. How do you run RCA? -> Timeline, trigger, contributing factors, corrective and preventive actions.
14. How do you improve on-call quality? -> Better alerts, clear runbooks, ownership rotation and drills.
15. Alert fatigue fix? -> Reduce noisy alerts and keep only actionable signals.
16. How do you measure reliability? -> SLI/SLO, error budget burn, incident rate and MTTR.
17. How do you reduce MTTR? -> Observability, clear escalation paths, and automation.
18. How do you prevent repeat incidents? -> Add tests/guardrails and track preventive actions.
19. How do you manage dependency outage? -> Graceful degradation and async fallback patterns.
20. How do you lead during incident pressure? -> Calm communication and clear decision ownership.

## Java/Spring Deep
21. Why constructor injection? -> Safer, explicit dependencies, and better tests.
22. Why not overuse `@Transactional`? -> Large transaction scopes reduce throughput and increase lock risk.
23. How do you tune Spring performance? -> Reduce serialization overhead, optimize DB calls, tune pools.
24. How do you protect from N+1 issues? -> Proper fetching strategy and query-level design.
25. How do you handle DB connection exhaustion? -> Pool sizing, leak detection, and query optimization.
26. Retry pitfalls? -> Non-idempotent retries create duplicate side effects.
27. How do you secure service-to-service communication? -> Token-based auth and least-privilege policies.
28. Why global exception handling? -> Stable error contract and cleaner controllers.
29. How do you avoid breaking clients? -> API compatibility and contract tests.
30. When to use async processing? -> For non-blocking tasks and decoupled workflows.

## Angular and Frontend
31. Why Angular in enterprise? -> Strong conventions reduce large-team entropy.
32. How do you prevent memory leaks? -> Controlled subscriptions and cleanup.
33. `switchMap` vs `mergeMap` decision? -> Cancel stale request vs keep parallel requests.
34. How do you optimize initial load? -> Lazy modules and bundle optimization.
35. How do you secure frontend apps? -> Never trust UI alone; backend enforces auth.
36. How do you handle large tables? -> Server pagination + virtual scrolling.
37. How do you reduce API chatter? -> Debounce, cache, and avoid duplicate calls.
38. How do you maintain state at scale? -> Predictable store patterns with clear ownership.
39. How do you handle global errors? -> Interceptor + user-safe messaging.
40. How do you test frontend critical paths? -> Component tests + integration smoke tests.

## Cloud/Kafka/DevOps
41. How do you choose EC2 vs container platform? -> Control needs vs operational abstraction.
42. How do you keep secrets secure? -> Secret manager and runtime injection.
43. Why Kafka instead of direct API calls? -> Better decoupling and burst handling.
44. How do you avoid hot partitions in Kafka? -> High-cardinality key and partition-aware design.
45. How do you handle poison messages? -> DLQ and controlled replay.
46. How do you avoid deployment risk? -> Canary/blue-green and health-based promotion.
47. How do you ensure environment parity? -> Infra as code and immutable builds.
48. How do you optimize cloud cost? -> Rightsizing, scaling policies, lifecycle controls.
49. How do you measure pipeline quality? -> Build success rate, lead time, change failure rate.
50. How do you secure CI/CD? -> Signed artifacts, least privilege, and audit trail.

## NoSQL and Data
51. SQL or NoSQL? -> Choose based on consistency and access patterns.
52. MongoDB good for what? -> Flexible document models and evolving schema domains.
53. DynamoDB good for what? -> Predictable low-latency key-value access at massive scale.
54. Cassandra good for what? -> High write throughput and multi-region resilience.
55. NoSQL modeling rule? -> Model around read/write access paths.
56. How do you handle NoSQL consistency? -> Use business-specific consistency levels and reconciliation.
57. How do you avoid unbounded data growth? -> TTL, archival, and data lifecycle policy.
58. NoSQL anti-pattern to avoid? -> Trying to do relational joins at scale.
59. How do you migrate SQL to NoSQL? -> Incremental dual-write/read path with validation.
60. How do you maintain auditability with NoSQL? -> Append-only events and immutable audit records.

## Leadership and Strategy
61. How do you decide build vs buy? -> Evaluate time, cost, risk, and strategic ownership.
62. How do you align engineering to business? -> Map technical work to measurable outcomes.
63. How do you handle disagreement with architect/manager? -> Present options with evidence and trade-offs.
64. How do you coach low-performing team member? -> Clear expectations, feedback loops, and support plan.
65. How do you manage distributed teams? -> Clear ownership and async documentation.
66. How do you prevent over-engineering? -> Build for current constraints with extension points.
67. How do you measure team engineering health? -> Delivery metrics + quality + incident trends.
68. How do you prioritize technical debt? -> Risk and business impact based prioritization.
69. How do you communicate delays? -> Early warning plus mitigation options.
70. How do you create trust quickly? -> Consistent delivery and transparent communication.

## Final Round Questions
71. Why this company? -> Align role goals with your strengths and domain outcomes.
72. What is your 90-day plan? -> Learn domain, deliver one measurable win, reduce one key risk.
73. Where do you see yourself next? -> Senior IC/architect with delivery and mentoring impact.
74. Why should we choose you? -> Proven full-stack depth + reliability leadership + business focus.
75. Any questions for us? -> Ask about architecture challenges, reliability goals, and team expectations.
