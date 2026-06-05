# Ram Mohan Kotni — Sr Cloud Platform Engineer
**Austin, TX** | **(603) 858-7546** | **mohankotni77@gmail.com** | **LinkedIn: /in/ramkotni/**

---

## PROFESSIONAL SUMMARY

Senior Cloud Platform Engineer with 18+ years of progressive experience in platform engineering, cloud infrastructure, and distributed systems architecture. Expert-level proficiency with AWS and Oracle Cloud Infrastructure, advanced infrastructure as code (Terraform, CloudFormation), container orchestration (Kubernetes, ECS/Fargate), CI/CD pipelines (Jenkins, GitLab), and event-driven platforms (Kafka). Proven track record designing scalable, secure, resilient enterprise platforms. Strong expertise in disaster recovery, business continuity, incident response, root cause analysis, and SRE/observability patterns. Known for translating architectural vision into production-ready solutions while enabling engineering teams and achieving operational excellence.

---

## TECHNICAL SKILLS

**Cloud Platforms:** AWS (EC2, Lambda, RDS, ECS, Fargate, S3, CloudWatch, IAM, VPC), Oracle Cloud Infrastructure, hybrid architectures, multi-cloud strategy

**Infrastructure as Code:** Terraform, AWS CloudFormation, OpenTofu, Ansible, configuration management, GitOps workflows

**Container Orchestration:** Kubernetes (K8s), Docker, containerd, ECS, Fargate, container networking, RBAC, Helm charts, persistent volumes

**DevOps & CI/CD Pipelines:** Jenkins, GitLab CI/CD, AWS CodePipeline, CodeBuild, CodeDeploy, blue-green deployments, canary releases, automated testing, security scanning

**Event-Driven & Streaming:** Kafka (Confluent), Apache Kafka, topic design, replication, disaster recovery, AWS Kinesis, EventBridge, SQS

**Monitoring & Observability:** CloudWatch, Prometheus, Grafana, Dynatrace, ELK Stack (Elasticsearch, Logstash, Kibana), Splunk, custom metrics, alerting, SLO/SLI definition

**Databases & Data:** Oracle Database, AWS RDS (Aurora, PostgreSQL, MySQL), NoSQL (MongoDB, DynamoDB, Cassandra), backup/recovery strategies, performance tuning

**Security & Compliance:** IAM policies, RBAC, secrets management, encryption (at rest/in transit), container security, network security, WAF, compliance frameworks (SOC2, HIPAA, GxP)

**Scripting & Automation:** Python, Bash, Java, custom infrastructure automation, health checks, deployment validators

**Architectural Patterns:** Microservices, event sourcing, CQRS, SLA/RTO/RPO design, capacity planning, cost optimization, resilience patterns

**Ways of Working:** Architecture review boards, incident response leadership, team mentoring, knowledge transfer, cross-functional collaboration

---

## PROFESSIONAL EXPERIENCE

### ERCOT — Electric Reliability Council of Texas | Austin, TX
**Senior Cloud Platform Engineer** | Apr 2025 – Present

- Own technical operation of enterprise platforms across on-premises and cloud environments, maintaining 99.9%+ availability SLA for critical generator interconnection systems (RIOO-IS/RARF)
- Lead low-level and domain-centric design translating EA direction into practical, scalable platform solutions across container orchestration, middleware, platform services, Lambdas, event processors
- Design and implement infrastructure as code using Terraform and CloudFormation provisioning 200+ AWS resources with full environment versioning and team self-service capabilities
- Build Ansible-based deployment automation enabling consistent environment provisioning across 12+ staging/production environments, reducing deployment time from 4 hours to 15 minutes
- Lead incident identification, triage, and resolution for platform-related incidents, coordinating with IT Infrastructure and Information Security teams to minimize downtime and implement preventive measures
- Design and maintain CI/CD pipelines using Jenkins supporting 40+ engineering teams with 200+ weekly deployments using blue-green and canary deployment patterns
- Implement serverless architecture using AWS Lambda for event processors and scheduled tasks, optimizing provisioning time and compute costs by 45%
- Design and implement comprehensive observability using CloudWatch, Prometheus, Grafana with 50+ dashboards, defined SLOs (99.5% uptime), and automated alerting reducing incident MTTR by 50%
- Own Kafka-based event streaming platform supporting 100+ daily events with replication strategies aligned to RTO/RPO targets ensuring message delivery SLA compliance
- Lead quarterly disaster recovery testing validating RTO (4 hours) and RPO (1 hour) targets; design automated failover for critical services ensuring <30 second recovery time
- Partner with Information Security implementing container security (image scanning, network policies), serverless security (Lambda permissions, cold-start monitoring), IAM least-privilege policies
- Enable developer self-service through internal platform tooling, templated Terraform modules, and paved paths reducing infrastructure request turnaround from 3 days to 2 hours
- Mentor 6 platform engineers in infrastructure as code, incident response, observability practices through hands-on guidance and bi-weekly architecture reviews

### Amazon Robotics | Boston, MA
**Senior Cloud Infrastructure Engineer** | Feb 2023 – Mar 2025

- Architected AWS-based container platform serving 100+ microservices with 500+ Kubernetes pods for manufacturing, warehouse, and logistics operations achieving 99.95% platform availability
- Led migration from monolithic deployments to containerized microservices on ECS/Fargate enabling daily deployments versus weekly, reducing infrastructure costs by 35%
- Designed and built reusable Terraform modules (200+ resources) for VPC infrastructure, RDS clusters, Lambda functions, event pipelines enabling team-wide self-service provisioning
- Implemented GitOps workflows enabling developers to provision infrastructure through code review and pull requests, reducing manual provisioning effort by 40%
- Authored 200+ Ansible playbooks for environment provisioning, security hardening, patch management ensuring consistent infrastructure state across all environments
- Built multi-stage Jenkins CI/CD pipelines supporting 200+ weekly deployments with automated testing, security scanning (OWASP), and compliance validation gates
- Implemented blue-green and canary deployment strategies enabling zero-downtime releases with automatic rollback capability
- Designed Fargate-based production deployments optimizing container CPU/memory allocation and spot instance usage achieving 30% cost reduction
- Implemented containerized application networking using AWS App Mesh with circuit breakers, retry logic, traffic management policies
- Built comprehensive monitoring and observability stack using CloudWatch, Prometheus, Grafana with 60+ dashboards covering platform health, business metrics, cost tracking
- Defined SLOs (99.9% availability, <500ms p99 latency, <0.05% error rate) aligned to business requirements with automated alerting and escalation procedures
- Led incident response for 40+ production incidents achieving average MTTR of 25 minutes; performed detailed RCAs identifying systemic improvements
- Implemented chaos engineering practices using Netflix Chaos Monkey validating system resilience, identifying and resolving 15+ infrastructure vulnerabilities
- Operated Kafka cluster supporting 500+ messages/sec across warehouse operations with topic-based event sourcing, implementing exactly-once delivery semantics
- Designed producer/consumer patterns with consumer groups for parallel processing achieving P99 latency <100ms
- Implemented multi-AZ active-active architecture for critical services with automated failover ensuring <30 second recovery time and zero data loss with cross-region RDS replicas
- Analyzed cloud spending and implemented cost optimization opportunities: reserved instances (15% savings), spot instances (70% for batch), rightsizing (25% reduction) totaling 500k+ annual savings
- Implemented AWS IAM policies following least privilege principles with role-based access, resource-level permissions, MFA enforcement
- Secured containerized workloads through ECR image scanning, vulnerability remediation automation, network policies restricting pod-to-pod communication
- Configured Lambda functions with least-privilege permissions, environment variable encryption, VPC integration for secure resource access

### Biogen | North Carolina, US
**Cloud Infrastructure Lead** | Jun 2022 – Jan 2023

- Led cloud infrastructure architecture for supply chain and compliance systems supporting pharma operations across 5 sites with 99.95% uptime requirement
- Migrated on-premises VMware infrastructure to AWS cloud using Terraform IaC (600+ resources) achieving 99.95% uptime and 40% cost reduction
- Designed hybrid architecture connecting on-premises Oracle systems to AWS RDS with secure cross-site networking using VPN and encryption at transit
- Implemented Kubernetes cluster for containerized microservices supporting supply chain workflows with full RBAC and network policy configuration
- Established CI/CD pipeline using GitLab CI/CD with automated testing, security scanning, compliance validation gates
- Built observability stack using Elasticsearch, Logstash, Kibana (ELK) for centralized logging, Prometheus for metrics, Grafana for visualization
- Designed disaster recovery strategy (RTO: 2 hours, RPO: 1 hour) for mission-critical systems with automated failover and validation
- Implemented cross-region RDS replicas ensuring data synchronization with <1 second lag; validated restore procedures monthly
- Configured AWS WAF for API protection against SQL injection, XSS attacks, bot patterns
- Implemented encryption strategies: S3 encryption (SSE-S3), RDS encryption at rest, TLS for data in transit
- Achieved HIPAA/GxP compliance through audit logging, access control, encryption, and regular compliance audits

### Dell Technologies | Remote
**Application Architect & DevOps Lead** | Jul 2015 – May 2022

- Architected enterprise cloud infrastructure supporting 1000+ daily API requests for product data and integration workflows on AWS
- Led migration from monolithic on-premises deployments to Spring Boot microservices on ECS/Fargate improving deployment frequency from monthly to daily
- Designed infrastructure patterns for scalability: auto-scaling groups, load balancers, service discovery, caching (Redis, ElastiCache)
- Implemented infrastructure as code using Terraform managing 500+ AWS resources across 5 environments achieving 95% IaC coverage
- Developed comprehensive Ansible playbooks for environment provisioning, security hardening, patch management, monitoring setup
- Established GitOps practice enabling teams to provision infrastructure through code review reducing manual time by 60%
- Designed and maintained Jenkins CI/CD pipelines supporting 200+ weekly deployments across 30+ microservices
- Implemented multi-stage pipelines with code analysis (SonarQube), automated testing, security scanning (OWASP), containerization, deployment
- Enabled blue-green deployments with automatic traffic switching achieving zero-downtime deployments with instant rollback capability
- Implemented comprehensive monitoring using CloudWatch, APM tools, custom dashboards (50+) tracking platform health and business metrics
- Defined SLOs (99.5% uptime) and SLIs (<200ms p99 latency, <0.1% error rate) with automated alerting
- Managed 50+ production incidents with average MTTR of 30 minutes; documented RCAs identifying systemic improvements
- Implemented chaos engineering validating system resilience through controlled failure injection
- Managed RDS landscape (Oracle, PostgreSQL, MySQL) with performance optimization, automated backups, cross-region replicas, point-in-time recovery
- Implemented AWS IAM architecture with role-based access control and cross-account access patterns
- Designed network security: VPC segmentation, security group policies, WAF configuration for API protection
- Achieved SOC2 Type II compliance through audit logging, access control, encryption, regular compliance audits

### IBM | New York, US
**Senior Infrastructure Engineer** | May 2012 – Jul 2015

- Managed on-premises Linux server infrastructure supporting 200+ production services with 99.99% uptime SLA
- Implemented monitoring using Nagios and Splunk achieving rapid incident detection and resolution
- Optimized Oracle and DB2 database performance through query optimization, indexing, resource allocation
- Led disaster recovery initiatives designing backup strategies, failover automation, recovery testing (RTO: 4 hours, RPO: 1 hour)
- Managed and mentored 20+ technical team members providing architectural guidance and knowledge transfer

### Innominds | San Jose, CA
**Senior Java Developer / DevOps Engineer** | Dec 2009 – Mar 2012

- Built cloud infrastructure automation tools using Python and Bash for VM provisioning and networking configuration
- Implemented continuous integration pipelines using Hudson/Jenkins supporting agile development teams
- Optimized application performance through JVM tuning, database query optimization, caching strategies

### Wells Fargo | Iowa
**Infrastructure & DevOps Engineer** | Nov 2007 – May 2009

- Managed on-premises infrastructure supporting financial services systems with high availability requirements
- Implemented disaster recovery for critical systems ensuring compliance with regulatory requirements

---

## KEY TECHNICAL ACHIEVEMENTS

**Platform Reliability:** Improved platform availability to 99.95%+ through multi-AZ architecture, automated health checks, container orchestration (K8s). Reduced incident MTTR by 50%.

**Infrastructure as Code Leadership:** Built Terraform/Ansible IaC platform enabling 50 engineers self-service provisioning. Achieved 100% infrastructure versioning. Reduced request turnaround from 3 days to 2 hours.

**CI/CD Transformation:** Designed Jenkins/GitLab CI/CD pipelines enabling 200+ weekly deployments (vs. monthly before). Implemented canary releases reducing failed deployments by 90%.

**Event-Driven Architecture:** Architected Kafka platform supporting 500+ msg/sec. Designed topic/partition strategies aligned with RTO/RPO targets. Implemented exactly-once delivery semantics.

**Disaster Recovery Excellence:** Designed multi-AZ active-active architecture with <30 sec failover time, zero data loss. Established quarterly DR testing validating RTO/RPO targets.

**Observability at Scale:** Built comprehensive observability stack (CloudWatch, Prometheus, Grafana, Dynatrace) with 60+ dashboards, SLO/SLI definition, automated alerting reducing on-call burden 40%.

**Cost Optimization:** Identified infrastructure optimization opportunities saving 500k+ annually through reserved instances, spot instances, rightsizing. Implemented cost allocation enabling team-driven optimization.

**Container Security:** Implemented layered security (image scanning, network policies, RBAC, secrets management) achieving zero high-severity vulnerabilities in production.

**Incident Response Excellence:** Led 30+ platform outages averaging 25-45 minute MTTR. Rigorous RCA process identifying systemic improvements preventing recurrence.

**Team Development:** Mentored 10+ engineers in platform engineering, cloud architecture, DevOps practices. Led bi-weekly architecture reviews ensuring design consistency.

---

## CERTIFICATIONS

- AWS Certified Solutions Architect – Associate
- AWS Certified SysOps Administrator – Associate
- Certified Kubernetes Administrator (CKA)
- Oracle Cloud Infrastructure Architect Associate
- Oracle Certified Professional, Java SE Programmer
- Agile Scrum Master Certification

---

## EDUCATION

**Master of Computer Applications (MCA)** – MK University, 2001
**Bachelor of Science (Mathematics)** – Andhra University, 1998

---

## TECHNICAL PROFICIENCY MATRIX

**Expert:** AWS infrastructure (EC2, Lambda, RDS, ECS, Fargate, CloudWatch, IAM), Terraform/CloudFormation IaC, Kubernetes orchestration, Docker containerization, Jenkins/GitLab CI/CD, Prometheus/Grafana monitoring, Kafka/event streaming, Python/Bash scripting

**Advanced:** Oracle Cloud Infrastructure, AWS advanced services (Kinesis, AppFlow, Systems Manager), Ansible automation, Dynatrace monitoring, ELK Stack, AWS IAM/security patterns, database performance tuning (Oracle, PostgreSQL)

**Intermediate:** OpenTofu, OpenShift, GitHub Actions, Splunk, DataDog monitoring, Pulumi, AWS CDK

---

## PROFESSIONAL QUALITIES

- **Strategic Thinker:** Design scalable, resilient platforms balancing cost, performance, and reliability
- **Operational Excellence:** Proactive monitoring, incident response leadership, rigorous RCA driving systemic improvements
- **Infrastructure Automation Advocate:** IaC-first approach ensuring reproducibility, auditability, and team self-service
- **Mentoring & Leadership:** Build team capability through architecture reviews, knowledge transfer, hands-on guidance
- **Resilience Engineering:** Design systems anticipating failures; implement chaos engineering validating assumptions
- **Developer Enablement:** Create paved paths and internal tooling reducing friction and accelerating time-to-market

---

**References and detailed project portfolios available upon request.**

