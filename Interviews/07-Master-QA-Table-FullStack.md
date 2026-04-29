# Master Q&A Table - Senior Java Full Stack

## Direct Interview Q&A
1. Tell me about yourself -> 18 years in Java full-stack, Spring Boot, Angular, cloud, and production reliability.
2. Why senior role -> I combine architecture decisions, coding depth, incident handling, and mentoring.
3. HashMap vs ConcurrentHashMap -> HashMap is not thread-safe; ConcurrentHashMap supports concurrent access safely.
4. volatile vs synchronized -> volatile gives visibility; synchronized gives visibility plus mutual exclusion.
5. Retry strategy -> Retry only idempotent operations with backoff and jitter.

## Architecture Section
- ERCOT: Angular -> Gateway/Auth -> Spring Boot workflow -> Oracle + audit
- Amazon: Producers -> Kafka -> Consumers -> Cache/DB -> Downstream
- Biogen: UI/API -> Validation -> DB + Audit -> Reporting
- Dell: PLM -> Integration -> ERP/MES -> Reconciliation/Replay
