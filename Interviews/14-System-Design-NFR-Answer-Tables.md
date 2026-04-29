# System Design and NFR Answer Tables

| NFR | Direct Answer |
|---|---|
| Availability | Multi-instance stateless services with failover and rollback |
| Latency | Query tuning, reduce sync dependencies, cache hot paths |
| Throughput | Horizontal scaling and queue buffering |
| Security | JWT/OAuth2, RBAC, least privilege, audit logs |
| Resilience | Timeout, bounded retry, circuit breaker, bulkhead |

## Architecture Section by Project
- ERCOT: secure workflow + audit-first
- Amazon: Kafka event microservices
- Biogen: regulated validation architecture
- Dell: PLM integration with reconciliation/replay
