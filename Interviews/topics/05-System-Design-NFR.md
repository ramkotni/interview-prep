# System Design and NFR Playbook

## Design flow (use in interviews)
1. Clarify requirements and assumptions
2. Define scale and NFR targets
3. Draw high-level architecture
4. Define APIs and data model
5. Handle failure, retries, and backpressure
6. Add observability and deployment strategy
7. Explain trade-offs

## NFR checklist
- Availability (SLA/SLO)
- Latency and throughput
- Scalability (horizontal/partitioning)
- Security and compliance
- Reliability and DR (RPO/RTO)
- Operability and maintainability

## Common design questions to practice
1. Design order management system
2. Design real-time tracking system
3. Design notification service
4. Design high-volume ingestion pipeline
5. Design audit-heavy workflow system

## Must-not-miss points
- Explicitly call out bottlenecks
- State trade-offs between consistency and availability
- Include deployment and rollback plan

## Reference
- Detailed Q&A: `Interviews/Senior-FullStack-Daily-Interview-QA.md` (Q141-Q160)
