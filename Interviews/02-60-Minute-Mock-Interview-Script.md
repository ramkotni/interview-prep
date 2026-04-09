# 60-Minute Mock Interview Script (Senior Java Full-Stack)

Use this as a real practice loop. Time-box every answer.

## Round 1 - Introduction and leadership (0-10 mins)
1. Introduce yourself in 60 seconds.
2. Describe your current role and ownership.
3. Tell me about one production incident and your response.
4. Tell me about a time you resolved a team conflict.

Probe follow-ups:
- What trade-off did you make?
- What would you do differently now?

## Round 2 - Java + Spring + APIs (10-25 mins)
5. `HashMap` vs `ConcurrentHashMap` in production use.
6. `volatile` vs `synchronized` with practical example.
7. How do you structure Spring Boot services for testability?
8. How do you secure REST APIs with JWT/OAuth2?
9. Design an order API: create/update/get/list.
10. How do you ensure idempotency for create APIs?

Probe follow-ups:
- Show error response contract.
- How would you version this API?
- How do you handle retries safely?

## Round 3 - Angular + full-stack integration (25-40 mins)
11. Explain Angular architecture in enterprise projects.
12. How do you use guards, interceptors, and reactive forms?
13. `switchMap` vs `mergeMap` in API-heavy UIs.
14. How do you optimize large table/list performance?
15. How do you debug production UI slowness?

Probe follow-ups:
- What metrics do you capture from frontend?
- How do you prevent memory leaks?

## Round 4 - System design + NFR (40-55 mins)
16. Design a scalable tracking platform (or order platform).
17. Define NFR targets and monitoring plan.
18. How do you avoid cascading failures?
19. How do you handle backpressure during spikes?
20. How do you plan disaster recovery?

Probe follow-ups:
- Single region vs multi region?
- Strong consistency vs eventual consistency?
- Cost vs performance trade-off?

## Round 5 - Project deep dive (55-60 mins)
21. ERCOT: architecture + NFR handling.
22. Amazon: throughput + latency optimization.
23. Biogen: compliance and auditability strategy.
24. Dell: PLM integration reliability.

## Self-evaluation rubric (after mock)
Score each from 1-5:
1. Clarity
2. Senior-level depth
3. Trade-off quality
4. NFR awareness
5. Project credibility
6. Confidence and pace

## Weak answer fixer template
- Problem: what was weak?
- Better framing: context -> approach -> NFR -> outcome
- New 30-second answer:

## Daily repetition plan
- Day 1: Full 60 minutes
- Day 2: Only rounds 2 + 4
- Day 3: Only rounds 1 + 5
- Day 4: Full 60 minutes again
