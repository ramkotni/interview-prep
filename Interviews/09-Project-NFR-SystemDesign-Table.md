# Project-wise NFR + System Design Table

| Project | Top NFRs | What I Implemented | Outcome |
|---|---|---|---|
| ERCOT | Compliance, auditability, security | RBAC, strict validation, audit metadata | Better audit readiness |
| Amazon Robotics | Throughput, low latency, resilience | Kafka tuning, consumer scaling, retry + DLQ | Lower lag and better peak stability |
| Biogen | Integrity, compliance, security | Multi-layer validation, traceability | Reduced compliance risk |
| Dell | Consistency, reliability, scalability | Reconciliation and replay-safe integration | Better PLM to ERP/MES consistency |

## Architecture Section
- ERCOT: audit-first workflow architecture
- Amazon: Kafka-centered event-driven architecture
- Biogen: regulated validation-heavy architecture
- Dell: integration architecture with recovery controls
