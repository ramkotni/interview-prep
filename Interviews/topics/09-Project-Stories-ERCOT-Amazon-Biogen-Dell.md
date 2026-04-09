# Project Stories: ERCOT, Amazon, Biogen, Dell, IBM, Wells Fargo

Use one project story per round. Keep it 2 minutes.

## Story format
1. Problem context
2. Architecture summary
3. Your ownership
4. NFR actions
5. Business outcome

## 1) ERCOT (RIOO/GINR)
- **Problem:** Compliance-heavy submission and approval workflow for market/grid operations.
- **Architecture:** Angular role-based UI + Spring Boot APIs + Oracle + audit trail + integrations.
- **Your ownership:** Full-stack implementation, workflow logic, performance tuning, production support.
- **NFR focus:** Auditability, correctness, security (RBAC), predictable performance.
- **Outcome:** Stable compliance-ready workflow and reliable deadline handling.

## 2) Amazon Robotics
- **Problem:** High-volume real-time event processing for operational visibility.
- **Architecture:** Event-driven microservices, AWS integrations, async pipeline, monitoring.
- **Your ownership:** Backend service optimization, reliability improvements, incident handling.
- **NFR focus:** Throughput, low latency, high availability, fast recovery.
- **Outcome:** Better reliability under peak traffic and faster incident recovery.

## 3) Biogen
- **Problem:** Regulated data workflows requiring strict traceability.
- **Architecture:** Secure layered services with validation and auditable records.
- **Your ownership:** Service logic, integrations, quality and compliance controls.
- **NFR focus:** Data integrity, compliance, secure access, operational stability.
- **Outcome:** Improved audit readiness and reduced compliance risk.

## 4) Dell Technologies
- **Problem:** PLM to ERP/MES data consistency and modernization.
- **Architecture:** Agile PLM as source of truth with API/batch integration patterns.
- **Your ownership:** Java extensions, integration reliability, design reviews.
- **NFR focus:** Consistency, integration reliability, scalability.
- **Outcome:** Improved product data flow and faster engineering-to-manufacturing cycle.

## 5) IBM
- **Problem:** Enterprise platform stability at scale.
- **Architecture:** N-tier Java systems with integration-heavy workflows.
- **Your ownership:** Core service development, performance tuning, code quality.
- **NFR focus:** Maintainability, reliability, steady performance.
- **Outcome:** Better platform stability and long-term maintainability.

## 6) Wells Fargo
- **Problem:** Secure and compliant transaction processing.
- **Architecture:** Secure service layer with strict controls and auditing.
- **Your ownership:** Backend services, transaction workflows, quality/performance checks.
- **NFR focus:** Security, correctness, availability, compliance.
- **Outcome:** Reliable operations under strict regulatory expectations.

## Project selection guide by interview type
- Product company: Amazon + system scale + latency + resilience
- Regulated domain: ERCOT + Biogen + audit/security narrative
- Enterprise modernization: Dell + IBM + integration reliability
- Banking/financial: Wells + transaction correctness + security
