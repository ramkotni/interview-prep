# AWS Services – Complete Guide
## Full Forms, Functionality, Explanation & Real Examples
## Based on 18 Years Experience – Interview Ready

---

# SECTION 1 – COMPUTE SERVICES

## EC2 – Elastic Compute Cloud
| Aspect | Detail |
|--------|--------|
| Full Form | Elastic Compute Cloud |
| What it is | Virtual machines (instances) in the cloud |
| Use Case | Run Java Spring Boot apps, batch jobs, custom server workloads |
| Instance Types | t3 (general), c5 (compute), r5 (memory), m5 (balanced) |
| Pricing | On-demand, Reserved (1-3yr discount), Spot (cheapest, interruptible) |
| Key Features | AMI (machine image), Security Groups, Elastic IPs, Auto Scaling |
| My Usage | Ran Spring Boot microservices on EC2 before migrating to ECS |

Example: Launch a t3.medium EC2 instance, install Java 17, deploy Spring Boot JAR.
Security Group allows port 8080 inbound only from ALB. IAM Role grants S3 read access.

## ECS – Elastic Container Service
| Aspect | Detail |
|--------|--------|
| Full Form | Elastic Container Service |
| What it is | Managed container orchestration service on AWS |
| Use Case | Run Docker containers without managing Kubernetes cluster |
| Launch Types | EC2 (you manage instances) or Fargate (serverless containers) |
| Key Features | Task definitions, Services, ALB integration, auto-scaling |
| My Usage | ERCOT Biogen Dell – Spring Boot microservices deployed as ECS Fargate tasks |

Example: Define ECS Task with Docker image from ECR. ECS Service keeps 3 tasks running.
ALB routes /api/* to ECS Service. CloudWatch triggers scale-out when CPU exceeds 70 percent.

## EKS – Elastic Kubernetes Service
| Aspect | Detail |
|--------|--------|
| Full Form | Elastic Kubernetes Service |
| What it is | Managed Kubernetes control plane on AWS |
| Use Case | Complex microservices needing full K8s ecosystem (HPA, ingress, operators) |
| Key Features | Node groups, Fargate profiles, IRSA, cluster autoscaler, ArgoCD |
| My Usage | Amazon Robotics – K8s autoscaling for burst scan event processing |

Example: EKS cluster with 3 node groups. TrackingService HPA scales 2 to 20 pods on Kafka lag metric.
ArgoCD syncs Git repo to deploy new image versions with zero downtime rolling update.

## Lambda – AWS Lambda
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – serverless function execution service |
| What it is | Run code without provisioning or managing servers |
| Use Case | Event-driven tasks, S3 triggers, API Gateway backend, cron jobs |
| Limits | 15 min max timeout, 10GB memory, cold start latency |
| Key Features | Event sources, layers, concurrency limits, VPC support |
| My Usage | S3 file processing triggers, compliance report generation jobs |

Example: S3 upload triggers Lambda. Lambda reads CSV validates records writes to DynamoDB.
Total execution 3 seconds. No server to manage. Scales to thousands of concurrent invocations.

## Fargate – AWS Fargate
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – serverless compute engine for containers |
| What it is | Run ECS or EKS containers without managing EC2 instances |
| Use Case | Teams that want containers without EC2 ops overhead |
| Key Features | Pay per vCPU/memory per second; no node patching needed |
| My Usage | ERCOT microservices – Fargate eliminated EC2 patch management overhead |

---

# SECTION 2 – STORAGE SERVICES

## S3 – Simple Storage Service
| Aspect | Detail |
|--------|--------|
| Full Form | Simple Storage Service |
| What it is | Unlimited scalable object storage for any type of file |
| Use Case | Store files logs images artifacts backups reports audit exports |
| Storage Classes | Standard, Intelligent-Tiering, Standard-IA, Glacier, Glacier Deep Archive |
| Key Features | Versioning, lifecycle policies, bucket policies, presigned URLs, event notifications |
| Durability | 99.999999999 percent (11 nines) across multiple AZs |
| My Usage | All projects – audit log exports compliance reports build artifacts archive storage |

Example: Spring Boot generates PDF audit report. Uploads to S3 with presigned URL.
Lifecycle policy moves files older than 90 days to Glacier to reduce cost.
S3 event triggers Lambda to process uploaded CSV file automatically.

## EBS – Elastic Block Store
| Aspect | Detail |
|--------|--------|
| Full Form | Elastic Block Store |
| What it is | Persistent block storage volumes attached to EC2 instances |
| Use Case | OS disk database storage high-IOPS workloads on EC2 |
| Volume Types | gp3 (general SSD), io2 (high IOPS), st1 (throughput HDD), sc1 (cold) |
| My Usage | EC2-based Oracle DB data volumes before moving to RDS |

## EFS – Elastic File System
| Aspect | Detail |
|--------|--------|
| Full Form | Elastic File System |
| What it is | Managed scalable NFS file system shared across multiple EC2/ECS tasks |
| Use Case | Shared config files shared uploads multiple containers reading same files |
| My Usage | Shared configuration files across ECS tasks in ERCOT |

## Glacier / S3 Glacier
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – cold archive storage |
| What it is | Very low cost storage for data rarely accessed |
| Retrieval Time | Minutes to hours depending on tier |
| Use Case | Long-term audit retention (7yr ERCOT, 15yr Biogen, 10yr Wells Fargo) |
| My Usage | Automated S3 lifecycle policy archives audit logs to Glacier after 90 days |

---

# SECTION 3 – DATABASE SERVICES

## RDS – Relational Database Service
| Aspect | Detail |
|--------|--------|
| Full Form | Relational Database Service |
| What it is | Managed relational databases with automated backups patching failover |
| Engines | PostgreSQL MySQL Oracle SQL Server MariaDB |
| Key Features | Multi-AZ (HA), Read Replicas, automated backups, point-in-time restore |
| My Usage | Biogen PostgreSQL RDS with Multi-AZ for clinical data availability |

Example: RDS PostgreSQL Multi-AZ. Primary fails – RDS auto-fails over to standby in 60-120 sec.
Read replica offloads reporting queries. Automated daily snapshot retained 7 days.

## Aurora – Amazon Aurora
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – AWS-built cloud-native relational DB |
| What it is | MySQL/PostgreSQL compatible with 5x MySQL performance |
| Key Features | Auto-scaling storage up to 128TB, up to 15 read replicas, serverless option |
| Use Case | High-performance relational workloads needing RDS-like simplicity |
| My Usage | Evaluated for Wells Fargo high-transaction workloads |

## DynamoDB – Amazon DynamoDB
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – fully managed NoSQL key-value and document DB |
| What it is | Single-digit millisecond latency at any scale; serverless |
| Key Features | On-demand scaling, DynamoDB Streams, TTL, Global Tables, DAX cache |
| Use Case | High-speed key-value lookups; Amazon Robotics package tracking state |
| My Usage | Amazon Robotics – 100M+ package records; keyed by packageId |

Example: TrackingService does PutItem with packageId as partition key.
GetItem returns latest status in under 5ms. DynamoDB Streams triggers Lambda for notifications.
Global Tables replicate to us-east-1 and eu-west-1 for disaster recovery.

## ElastiCache – Amazon ElastiCache
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – managed in-memory caching service |
| Engines | Redis and Memcached |
| What it is | Sub-millisecond caching layer in front of databases |
| Use Case | Cache hot DB reads, store sessions, idempotency keys, rate limit counters |
| My Usage | Amazon Robotics (tracking cache), Wells Fargo (idempotency keys), IBM (sessions) |

Example: Spring Boot checks Redis before querying DynamoDB.
Cache hit ratio 70 percent at peak. TTL 30 seconds for tracking state.
Wells Fargo stores transaction idempotency key in Redis with 24hr TTL to prevent duplicate payments.

## Redshift – Amazon Redshift
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – cloud data warehouse |
| What it is | Petabyte-scale columnar data warehouse for analytics and reporting |
| Use Case | Business intelligence large-scale aggregation historical reporting |
| Key Features | Columnar storage, Redshift Spectrum (query S3), concurrency scaling |
| My Usage | Evaluated for ERCOT regulatory reporting dashboards |

## DocumentDB – Amazon DocumentDB
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – MongoDB-compatible managed document DB |
| What it is | AWS-managed document database compatible with MongoDB drivers |
| Use Case | Teams using MongoDB who want AWS-managed operations |
| My Usage | Alternative evaluated when MongoDB Atlas costs were high |

---

# SECTION 7 – MONITORING AND OBSERVABILITY

## CloudWatch – Amazon CloudWatch
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – monitoring and observability service |
| What it is | Collect monitor analyze metrics logs and set alarms for AWS resources |
| Key Features | Metrics, Logs, Alarms, Dashboards, Log Insights, Synthetics, Container Insights |
| Use Case | Monitor ECS CPU/memory, set alarm on API error rate, query logs for errors |
| My Usage | All projects – central metrics logs alarms; SLO breach alerts to PagerDuty |

Example: CloudWatch Alarm on ECS service CPUUtilization above 80 percent for 5 minutes.
Alarm action triggers SNS notification to PagerDuty. CloudWatch Log Insights query:
fields timestamp, message | filter level=ERROR | stats count() by service

## CloudTrail – AWS CloudTrail
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – audit log of all AWS API calls |
| What it is | Record every AWS API action taken in your account for audit and compliance |
| Use Case | Who deleted the S3 bucket? Who changed the security group? Compliance audit trail |
| Key Features | Management events, data events, insight events, 90-day history, S3 archival |
| My Usage | ERCOT Wells Fargo – CloudTrail enables compliance audit of all AWS actions |

## X-Ray – AWS X-Ray
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – distributed tracing service |
| What it is | Trace requests through microservices to find performance bottlenecks |
| Use Case | Find which service in the chain caused latency spike or error |
| Key Features | Service map, trace segments, annotations, sampling rules |
| My Usage | Amazon Robotics – X-Ray traces end-to-end package scan event processing |

Example: Slow API response. X-Ray service map shows TrackingService->EnrichmentService call
took 450ms out of 500ms total. Root cause identified: N+1 DynamoDB query in enrichment.

## Config – AWS Config
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – resource configuration tracking service |
| What it is | Track configuration changes of AWS resources and evaluate compliance |
| Use Case | Was this security group open to 0.0.0.0/0? When did RDS encryption get disabled? |
| My Usage | ERCOT – AWS Config rules enforce encryption and least-privilege network access |

---

# SECTION 8 – CI/CD AND DEVELOPER TOOLS

## ECR – Elastic Container Registry
| Aspect | Detail |
|--------|--------|
| Full Form | Elastic Container Registry |
| What it is | Managed Docker container image registry on AWS |
| Key Features | Image scanning (Inspector), lifecycle policies, cross-account access, immutable tags |
| Use Case | Store Docker images built by CI/CD pipeline; pull to ECS/EKS at deploy time |
| My Usage | All container projects – Jenkins pushes image to ECR; ECS pulls at deploy |

Example: Jenkins pipeline builds Spring Boot Docker image tags with git commit SHA.
Pushes to ECR repo. ECS task definition references ECR image URI. Deploy updates task.

## CodePipeline – AWS CodePipeline
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – managed CI/CD pipeline orchestration |
| What it is | Automate build test deploy pipeline stages for application releases |
| Stages | Source (CodeCommit/GitHub), Build (CodeBuild), Deploy (ECS/Lambda/Elastic Beanstalk) |
| My Usage | Smaller projects used CodePipeline; larger ones used Jenkins |

## CodeBuild – AWS CodeBuild
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – managed build service |
| What it is | Compile source code run tests produce deployment artifacts |
| Use Case | Maven/Gradle build, Docker image build, unit test execution |
| My Usage | Biogen – CodeBuild for Maven build and Docker image creation |

## Terraform on AWS
| Aspect | Detail |
|--------|--------|
| What it is | Infrastructure as Code tool to provision AWS resources declaratively |
| Use Case | Create VPC ECS cluster RDS MSK IAM roles all in version-controlled code |
| Key Features | State management, plan/apply workflow, modules, remote state in S3 |
| My Usage | Amazon Robotics Dell – Terraform manages all AWS infrastructure |

Example: terraform apply creates VPC subnets ECS cluster MSK cluster RDS instance.
State stored in S3 with DynamoDB state lock. PR review checks terraform plan output.

---

# SECTION 9 – ADDITIONAL SERVICES

## SES – Simple Email Service
| Aspect | Detail |
|--------|--------|
| Full Form | Simple Email Service |
| What it is | Managed email sending service for transactional and marketing emails |
| Use Case | Send workflow approval notifications compliance alerts account updates |
| My Usage | ERCOT – SES sends email notifications for workflow state changes |

## Elastic Beanstalk – AWS Elastic Beanstalk
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – PaaS for deploying web applications |
| What it is | Deploy and scale web applications without managing infrastructure |
| Use Case | Rapid deployment of Spring Boot apps without ECS/K8s complexity |
| My Usage | Early prototypes and non-production environments |

## Systems Manager – AWS Systems Manager (SSM)
| Aspect | Detail |
|--------|--------|
| Full Form | Systems Manager |
| What it is | Manage EC2 instances and on-premise servers at scale |
| Key Features | Parameter Store, Session Manager (no SSH needed), Patch Manager, Run Command |
| Parameter Store | Store config values and non-secret parameters; integrates with Spring Boot |
| My Usage | All projects – SSM Parameter Store for non-secret config; Session Manager for EC2 access |

Example: Spring Boot reads database URL from SSM Parameter Store at startup.
Ops team SSHs to EC2 via SSM Session Manager – no bastion host or open port 22 needed.

## Athena – Amazon Athena
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – serverless SQL query service for S3 |
| What it is | Query data stored in S3 using standard SQL without loading it to a database |
| Use Case | Ad hoc analysis of audit logs compliance reports large CSV/JSON files in S3 |
| My Usage | ERCOT – Athena queries S3-archived audit logs for compliance investigations |

Example: SELECT actor, action, COUNT(*) FROM audit_logs WHERE date='2026-01-15'
GROUP BY actor, action ORDER BY COUNT(*) DESC
Query runs on S3 data directly. Pay per query. No database to manage.

## Auto Scaling – AWS Auto Scaling
| Aspect | Detail |
|--------|--------|
| Full Form | No acronym – automatic capacity management |
| What it is | Automatically adjust compute capacity based on demand |
| Types | EC2 Auto Scaling, ECS Service Auto Scaling, Application Auto Scaling |
| Policies | Target Tracking (maintain metric), Step Scaling, Scheduled Scaling |
| My Usage | All projects – ECS auto-scaling on CPU and Kafka consumer lag |

Example: ECS service target tracking: maintain CPUUtilization at 60 percent.
Burst traffic scales ECS tasks from 3 to 15 in 2 minutes. Off-peak scales back to 3.

---

# SECTION 10 – AWS QUICK REFERENCE TABLE

| Service | Full Form | One-Line Purpose |
|---------|-----------|-----------------|
| EC2 | Elastic Compute Cloud | Virtual machines in the cloud |
| ECS | Elastic Container Service | Managed Docker container orchestration |
| EKS | Elastic Kubernetes Service | Managed Kubernetes cluster |
| Lambda | N/A | Serverless function execution |
| Fargate | N/A | Serverless containers for ECS/EKS |
| S3 | Simple Storage Service | Unlimited object storage |
| EBS | Elastic Block Store | Persistent disk for EC2 |
| EFS | Elastic File System | Shared NFS file system |
| Glacier | N/A | Cold archive storage |
| RDS | Relational Database Service | Managed relational databases |
| Aurora | N/A | High-performance cloud-native SQL DB |
| DynamoDB | N/A | Serverless NoSQL key-value DB |
| ElastiCache | N/A | Managed Redis/Memcached cache |
| Redshift | N/A | Cloud data warehouse |
| VPC | Virtual Private Cloud | Isolated private network |
| ALB | Application Load Balancer | Layer 7 HTTP load balancer |
| NLB | Network Load Balancer | Layer 4 TCP load balancer |
| Route 53 | N/A (DNS port 53) | Managed DNS with failover |
| CloudFront | N/A | Global CDN for static/dynamic content |
| API Gateway | N/A | Managed REST/HTTP/WebSocket API |
| SQS | Simple Queue Service | Managed message queue |
| SNS | Simple Notification Service | Pub/sub fan-out notifications |
| MSK | Managed Streaming for Kafka | Fully managed Apache Kafka |
| EventBridge | N/A | Serverless event bus and cron |
| Step Functions | N/A | Serverless workflow orchestration |
| IAM | Identity and Access Management | User roles policies permissions |
| Cognito | N/A | App user authentication service |
| Secrets Manager | N/A | Managed secret storage and rotation |
| KMS | Key Management Service | Encryption key management |
| WAF | Web Application Firewall | Block SQL injection XSS attacks |
| Shield | N/A | DDoS protection |
| GuardDuty | N/A | Intelligent threat detection |
| Inspector | N/A | Vulnerability scanning |
| CloudWatch | N/A | Metrics logs alarms dashboards |
| CloudTrail | N/A | API call audit logging |
| X-Ray | N/A | Distributed tracing |
| Config | N/A | Resource configuration compliance |
| ECR | Elastic Container Registry | Docker image registry |
| CodePipeline | N/A | CI/CD pipeline orchestration |
| CodeBuild | N/A | Managed build service |
| SES | Simple Email Service | Transactional email sending |
| SSM | Systems Manager | EC2 management parameter store |
| Athena | N/A | SQL queries on S3 data |
| Auto Scaling | N/A | Automatic capacity adjustment |
| Direct Connect | N/A | Dedicated private network link |
| Terraform | N/A (not AWS native) | Infrastructure as code for AWS |

---

# SECTION 11 – INTERVIEW ANSWERS USING AWS SERVICES

## How did you ensure high availability?
Multi-AZ RDS with automatic failover. ECS Service across 2 AZs with ALB health checks.
Route 53 failover routing to DR region. Auto Scaling maintains minimum healthy task count.

## How did you secure your AWS environment?
IAM least privilege roles per service. Secrets Manager for all credentials.
KMS encryption for S3 RDS DynamoDB. WAF on ALB for OWASP protection.
VPC private subnets for all services. GuardDuty for threat detection. CloudTrail for audit.

## How did you handle large data volumes?
Hot data in DynamoDB and ElastiCache. Warm data in RDS with read replicas.
Cold data archived to S3 Glacier via lifecycle policies. Athena for ad-hoc queries on S3.

## How did you manage infrastructure changes?
Terraform for all AWS resources. State in S3 with DynamoDB lock.
All changes via PR review with terraform plan output. No manual console changes in production.

## How did you monitor production systems?
CloudWatch metrics and alarms for ECS CPU memory and API error rates.
CloudWatch Log Insights for error query. X-Ray for distributed tracing.
PagerDuty integration via SNS for on-call alerts. Dashboards in CloudWatch and Grafana.

## How did you handle container deployments?
Jenkins builds Docker image pushes to ECR with commit SHA tag.
ECS Service rolling deployment updates tasks 1 at a time with health check gate.
Old tasks drain connections before termination. Zero downtime guaranteed.

