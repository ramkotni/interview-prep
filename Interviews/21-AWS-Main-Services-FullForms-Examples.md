
---

# SECTION 6 – MESSAGING, INTEGRATION, ANALYTICS

## Amazon SQS – Simple Queue Service

| Item | Details |
|------|---------|
| Full Form | Simple Queue Service |
| Category | Messaging / Queue |
| What it does | Decouples services using durable queues |
| Use case | Order processing, async job handling, retry-based workflows |
| Example | A payment service sends invoice-generation jobs to SQS so invoice processing happens asynchronously |
| Why use it | Prevents tight coupling and absorbs traffic spikes |

## Amazon SNS – Simple Notification Service

| Item | Details |
|------|---------|
| Full Form | Simple Notification Service |
| Category | Messaging / Pub-Sub |
| What it does | Publishes messages to multiple subscribers like email, SMS, Lambda, SQS |
| Use case | Alerts, fan-out notifications, broadcast events |
| Example | After an order is shipped, SNS sends email notification, SMS, and pushes message to fulfillment systems |
| Why use it | One publisher can notify many consumers at the same time |

## Amazon EventBridge

| Item | Details |
|------|---------|
| Full Form | Amazon EventBridge |
| Category | Event Bus / Integration |
| What it does | Routes events between AWS services and applications using rules |
| Use case | Event-driven architecture, SaaS integration, scheduled workflows |
| Example | When a file lands in S3, EventBridge triggers a Lambda for validation and an SNS alert to operations |
| Why use it | Native event routing without custom polling or glue code |

## Amazon Kinesis

| Item | Details |
|------|---------|
| Full Form | Amazon Kinesis |
| Category | Streaming Data |
| What it does | Collects and processes real-time streaming data |
| Use case | Log streaming, clickstream analytics, IoT telemetry |
| Example | A website streams click events into Kinesis and processes them for real-time dashboards |
| Why use it | Managed streaming for near real-time data processing on AWS |

## Amazon MSK

| Item | Details |
|------|---------|
| Full Form | Amazon Managed Streaming for Apache Kafka |
| Category | Managed Kafka |
| What it does | Provides managed Apache Kafka clusters on AWS |
| Use case | High-throughput event streaming, microservice messaging, event replay |
| Example | Amazon Robotics-style tracking events are written to Kafka topics hosted in MSK |
| Why use it | You keep Kafka features without managing brokers manually |

---

# SECTION 7 – SECURITY AND IDENTITY

## IAM – Identity and Access Management

| Item | Details |
|------|---------|
| Full Form | Identity and Access Management |
| Category | Security / Access Control |
| What it does | Manages users, roles, policies, and permissions in AWS |
| Use case | Least-privilege access for developers, services, and automation |
| Example | ECS tasks use an IAM role to read from S3 without storing access keys in code |
| Why use it | Central foundation for AWS security |

## AWS KMS – Key Management Service

| Item | Details |
|------|---------|
| Full Form | Key Management Service |
| Category | Security / Encryption |
| What it does | Creates and manages encryption keys used by AWS services and applications |
| Use case | Encrypting S3, RDS, EBS, secrets, and application data |
| Example | Customer files stored in S3 are encrypted with KMS-managed keys |
| Why use it | Centralized key control, rotation, and auditability |

## AWS Secrets Manager

| Item | Details |
|------|---------|
| Full Form | AWS Secrets Manager |
| Category | Security / Secret Management |
| What it does | Stores and rotates secrets such as DB passwords, API keys, and tokens |
| Use case | Secure secret storage instead of hardcoding credentials |
| Example | Spring Boot service reads DB credentials from Secrets Manager during startup |
| Why use it | Better than storing passwords in config files or code |

## AWS WAF

| Item | Details |
|------|---------|
| Full Form | Web Application Firewall |
| Category | Security / Edge Protection |
| What it does | Protects web apps from common web exploits like SQL injection and XSS |
| Use case | Public APIs, internet-facing apps, sensitive portals |
| Example | An Angular + Spring Boot app behind ALB uses WAF rules to block malicious traffic |
| Why use it | Adds application-layer protection before requests hit your app |

## Amazon Cognito

| Item | Details |
|------|---------|
| Full Form | Amazon Cognito |
| Category | Identity / Authentication |
| What it does | Handles user sign-up, sign-in, token issuance, and federation |
| Use case | Customer-facing authentication for web/mobile apps |
| Example | Users log in to an Angular app through Cognito and receive JWT tokens for API access |
| Why use it | Managed auth without building login systems from scratch |

---

# SECTION 8 – MONITORING, LOGGING, OPERATIONS

## Amazon CloudWatch

| Item | Details |
|------|---------|
| Full Form | Amazon CloudWatch |
| Category | Monitoring / Observability |
| What it does | Collects metrics, logs, alarms, dashboards, and events |
| Use case | CPU monitoring, application logs, alerting, dashboarding |
| Example | CloudWatch alarms notify the team when ECS CPU crosses 80 percent |
| Why use it | Default AWS monitoring backbone |

## AWS CloudTrail

| Item | Details |
|------|---------|
| Full Form | AWS CloudTrail |
| Category | Audit / Governance |
| What it does | Records AWS API activity and account-level actions |
| Use case | Compliance, security investigations, audit history |
| Example | You can see who deleted an S3 bucket or changed an IAM policy |
| Why use it | Essential for traceability and compliance |

## AWS X-Ray

| Item | Details |
|------|---------|
| Full Form | AWS X-Ray |
| Category | Tracing / Observability |
| What it does | Traces requests across distributed services |
| Use case | Debugging latency in microservices and serverless systems |
| Example | A request from API Gateway to Lambda to DynamoDB can be traced end-to-end using X-Ray |
| Why use it | Helps locate bottlenecks and dependency failures quickly |

---

# SECTION 9 – DEVOPS AND AUTOMATION

## AWS CodeCommit

| Item | Details |
|------|---------|
| Full Form | AWS CodeCommit |
| Category | DevOps / Source Control |
| What it does | Managed Git repository service |
| Use case | Store application source code securely in AWS |
| Example | Teams push Spring Boot microservice code into CodeCommit repositories |
| Why use it | Useful when AWS-native source hosting is preferred |

## AWS CodeBuild

| Item | Details |
|------|---------|
| Full Form | AWS CodeBuild |
| Category | DevOps / Build |
| What it does | Compiles code, runs tests, and produces artifacts |
| Use case | CI pipeline build stage |
| Example | Maven project is built and tested in CodeBuild after each commit |
| Why use it | Managed build environment without maintaining build servers |

## AWS CodeDeploy

| Item | Details |
|------|---------|
| Full Form | AWS CodeDeploy |
| Category | DevOps / Deployment |
| What it does | Automates deployments to EC2, ECS, and Lambda |
| Use case | Blue-green and rolling deployments |
| Example | ECS service is updated gradually to reduce release risk |
| Why use it | Safer deployment automation with rollback support |

## AWS CodePipeline

| Item | Details |
|------|---------|
| Full Form | AWS CodePipeline |
| Category | DevOps / CI-CD |
| What it does | Orchestrates end-to-end delivery pipelines |
| Use case | Source -> build -> test -> deploy workflow |
| Example | A code push triggers CodePipeline, which runs CodeBuild and deploys to ECS |
| Why use it | Automates release flow across AWS services |

## AWS CloudFormation

| Item | Details |
|------|---------|
| Full Form | AWS CloudFormation |
| Category | Infrastructure as Code |
| What it does | Provisions AWS infrastructure using templates |
| Use case | Repeatable environment creation |
| Example | Dev, QA, and Prod VPCs and ECS clusters are created from templates |
| Why use it | Infrastructure becomes version-controlled and repeatable |

## AWS Systems Manager

| Item | Details |
|------|---------|
| Full Form | AWS Systems Manager |
| Category | Operations / Management |
| What it does | Manages instances, parameters, patching, automation, and remote access |
| Use case | Central ops control without SSHing manually into servers |
| Example | Ops team uses Session Manager to access EC2 securely without opening port 22 |
| Why use it | Reduces manual ops work and improves security |

---

# SECTION 10 – INTERVIEW-READY AWS ANSWERS

## Why S3?
S3 is used for durable scalable object storage. It is ideal for files logs backups static website assets and archives.
In enterprise systems I use S3 for storing logs build artifacts uploaded files and cold audit archives because it is highly durable and cost-effective.

## Why EC2 vs ECS vs EKS?
EC2 gives maximum control at the VM level but requires more maintenance.
ECS is simpler for teams that want managed container orchestration on AWS.
EKS is best when we need Kubernetes features portability and advanced autoscaling.

## Why RDS instead of self-managed database?
RDS reduces operational overhead by handling backups patching failover and monitoring.
It lets the team focus on application development instead of database administration.

## Why DynamoDB?
DynamoDB is best for key-value access patterns needing single-digit millisecond latency at any scale.
It is excellent for tracking systems session stores and high-scale lookup workloads.

## Why IAM roles instead of access keys in code?
IAM roles remove the need to store credentials in source code or config files.
They improve security rotate automatically and align with least-privilege principles.

## Why CloudWatch and CloudTrail together?
CloudWatch tells you how the system is behaving using metrics logs and alarms.
CloudTrail tells you who changed what in AWS. Together they provide observability plus auditability.

## Final AWS Summary
AWS services are grouped by function: compute storage database networking security monitoring and DevOps.
In interviews the best way to answer is to say the service full form what it does why it was chosen and one project example.
