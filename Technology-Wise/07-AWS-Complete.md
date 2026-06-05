# AWS SERVICES — COMPLETE Q&A
## Comprehensive coverage of all AWS services | Interview Level

---

## SECTION 1: AWS CORE SERVICES - Q&A

---

### Q1: What are the main AWS services used in production? Categorize them.

**A:**

**Compute Services:**
- EC2 — Virtual machines (on-demand, reserved, spot instances)
- Lambda — Serverless functions (event-driven)
- ECS — Container orchestration on EC2
- EKS — Managed Kubernetes clusters
- Fargate — Serverless container runtime
- Batch — Large-scale batch processing
- App Runner — Modern applications

**Storage Services:**
- S3 — Object storage (scalable, durable)
- EBS — Block storage for EC2
- EFS — Elastic File System (shared)
- Glacier — Long-term archival storage
- FSx — Fully managed file systems

**Database Services:**
- RDS — Relational databases (MySQL, PostgreSQL, Oracle)
- Aurora — High-performance MySQL/PostgreSQL
- DynamoDB — NoSQL key-value store
- Redshift — Data warehouse for analytics
- ElastiCache — In-memory cache (Redis, Memcached)

**Networking:**
- VPC — Virtual Private Cloud
- Route 53 — DNS service with health checks
- CloudFront — CDN for content delivery
- API Gateway — Managed API service
- ALB / NLB — Load balancers
- VPN — Virtual Private Network
- PrivateLink — Private connectivity

**Application Services:**
- SQS — Message queue (async)
- SNS — Publish/Subscribe notifications
- Kinesis — Real-time data streaming
- EventBridge — Event routing
- Step Functions — Serverless workflows

**Security & Compliance:**
- IAM — Identity and Access Management
- Secrets Manager — Secrets with auto-rotation
- Parameter Store — Configuration storage
- AWS Config — Compliance monitoring
- GuardDuty — Threat detection
- CloudTrail — API call logging
- WAF — Web Application Firewall

**DevOps:**
- CodePipeline — CI/CD orchestration
- CodeBuild — Managed build service
- CodeDeploy — Automated deployment
- CloudFormation — IaC (declarative)

**Monitoring:**
- CloudWatch — Metrics, logs, alarms
- X-Ray — Distributed tracing
- CloudWatch Logs — Centralized logging

---

### Q2: Explain AWS IAM in detail — components, policies, roles, best practices.

**A:**

**IAM Core Concepts:**
- **Users** — Individual accounts (avoid for services, use roles)
- **Groups** — Collection of users
- **Roles** — Identity assumed by EC2/Lambda/users
- **Policies** — JSON files defining permissions
- **Permissions** — Allow/Deny specific actions on resources

**IAM Policy Structure:**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3Read",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ],
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "10.0.0.0/8"
        }
      }
    },
    {
      "Sid": "DenyS3Delete",
      "Effect": "Deny",
      "Action": "s3:DeleteObject",
      "Resource": "*"
    }
  ]
}
```

**IAM Best Practices (Production):**
- ✅ Use roles instead of users for EC2/Lambda
- ✅ IRSA (IAM Roles for Service Accounts) for Kubernetes pods
- ✅ MFA for human users
- ✅ Resource-level permissions (not just service-level)
- ✅ Temporary credentials via STS (auto-rotate)
- ✅ Cross-account access via assume role
- ✅ Regular access reviews (quarterly)
- ✅ Least-privilege principle (deny by default)

**Real Example (Amazon Robotics):**
```
Lambda Function → IAM Role = warehouse-api-role
  Permissions:
    - S3 GetObject on s3://warehouse-data-prod/*
    - RDS ConnectDB on warehouse-prod-db only
    - Secrets GetSecretValue on arn:*:warehouse-prod-*
    - Everything else: DENIED
    
Credentials auto-rotate every hour (STS temporary credentials)
CloudTrail logs every action this role takes
```

---

### Q3: Explain S3 in production — storage classes, lifecycle, versioning, security.

**A:**

**Storage Classes (cost vs retrieval time):**

| Class | Cost vs Standard | Retrieval Speed | Min Duration | Use |
|---|---|---|---|---|
| Standard | 100% | Instant | None | Hot data |
| Intelligent-Tiering | 100% → 45% | Auto-optimizes | None | Unknown access |
| Standard-IA | 45% cheaper | Minutes | 30 days | Backup/archives |
| Glacier Instant | 68% cheaper | Minutes | 90 days | Quarterly access |
| Glacier Flexible | 85% cheaper | Hours-Days | 90 days | Archival |
| Deep Archive | 95% cheaper | 12+ hours | 180 days | Legal hold |

**Lifecycle Policy (automatic cost optimization):**
```yaml
Transitions:
  Day 0:   New object → Standard
  Day 30:  → Standard-IA (lower cost, slight retrieval fee)
  Day 90:  → Glacier (cheaper long-term)
  Day 365: → Deep Archive (cheapest)
  Day 2555: Delete (keep 7 years for compliance)
```

**S3 Security Layers:**
- Encryption at rest (SSE-KMS, not SSE-S3)
- Versioning (protect against deletion)
- Block Public Access (prevents accidental exposure)
- Bucket policies + IAM (least privilege)
- MFA Delete (require 2nd factor for permanent delete)
- Access logging (who accessed what)
- Server access logs (HTTP logs)
- CloudTrail (all API calls)
- Presigned URLs (temporary access for others)

---

### Q4: Explain RDS in production—Multi-AZ, read replicas, backups, and failover.

**A:**

**Multi-AZ (High Availability):**
- Primary in AZ-a + Standby in AZ-b
- Synchronous replication (zero data loss)
- Automatic failover <2 min if primary fails
- DNS updated, traffic redirected
- Cost: 2x (both instances running)

**Read Replicas (Scale reads):**
- Async replication (sligh lag)
- Can be in different region
- Separate endpoint (application specifies)
- Can be promoted to standalone
- No automatic failover (manual promotion)

**Backup & Restore (Disaster Recovery):**
```
Automated:
  - Daily backup window: 02:00-03:00 UTC
  - Retention: 35 days (PITR to any second)
  - Stored in S3 (managed by AWS)
  
Manual:
  - Weekly snapshots for long-term
  - Cross-region copy for DR
  
Testing:
  - Monthly restore test in staging
  - Verify data integrity
  - Test application compatibility
```

**Failure Scenarios:**

| Scenario | Impact | Recovery | RTO |
|---|---|---|---|
| Primary EC2 fails | Brief interruption | Auto-failover to Standby | <2 min |
| Network issue | Connection timeout | Check security groups/routes | <5 min |
| Data corruption | Data loss | Restore from backup (specific time) | Hours |
| Entire AZ down | Brief interruption | DNS + failover | <2 min |

---

### Q5: Explain Lambda — use cases, cold starts, optimization, pricing.

**A:**

**Common Use Cases:**
- Event-driven (S3, DynamoDB streams)
- REST API (via API Gateway)
- Scheduled tasks (CloudWatch Events)
- Async workers (SQS/SNS messages)
- Data pipeline (ETL)
- Image processing
- Webhook receivers

**Cold Starts (latency overhead first invocation):**
```
Cold Start Timeline:
  1. Container allocated → Network setup (50ms)
  2. Runtime loaded → JVM/Python importer (500-3000ms depends on runtime)
  3. Handler code executed → Client code runs (varies)
  
Runtime Cold Start Times:
  - Go: ~50ms (fastest)
  - Node.js: ~100-300ms
  - Python: ~100-300ms
  - Java: ~1-3 seconds (slowest)
  - C#: ~500-1000ms
```

**Optimization Strategies:**
```
1. Use ARM64 (Graviton2)
   - 34% better price/performance
   - Faster cold starts
   
2. Java SnapStart
   - Sub-100ms cold starts
   - Snapshot after initialization
   
3. Provisioned Concurrency
   - Keep N containers warm
   - Eliminate cold starts (cost: pre-pay)
   
4. Minimize package
   - Use Lambda layers (shared, cached)
   - Remove unused dependencies
   
5. Optimize code
   - Init outside handler (reused across invocations)
   - Lazy load modules
   - Use connection pooling
```

---

### Q6: Explain VPC — subnets, routing, security groups, NACL.

**A:**

**VPC Layers (Defense in Depth):**
```
Internet → Route Tables (which subnet?)
         → NACLs (stateless, both directions)
         → Security Groups (stateful, instance-level)
         → EC2 Instance
```

**Security Groups vs NACL:**

| Feature | Security Group | NACL |
|---|---|---|
| Scope | Instance | Subnet |
| Default | Deny all inbound | Allow all |
| Stateful | Yes (return traffic auto-allowed) | No (explicit rules) |
| Layer | Instance-level (fine control) | Subnet-level (general control) |

**Production VPC Design (3 AZs):**
```
VPC: 10.0.0.0/16
├── Public Subnets (ALB, NAT)
│   ├── AZ-a: 10.0.0.0/24
│   ├── AZ-b: 10.0.1.0/24
│   └── AZ-c: 10.0.2.0/24
├── Private Subnets (EKS, EC2)
│   ├── AZ-a: 10.0.10.0/24
│   ├── AZ-b: 10.0.11.0/24
│   └── AZ-c: 10.0.12.0/24
├── Database Subnets (RDS)
│   ├── AZ-a: 10.0.20.0/24
│   ├── AZ-b: 10.0.21.0/24
│   └── AZ-c: 10.0.22.0/24
└── VPC Endpoints (private)
    ├── S3 Gateway
    ├── SecretsManager Interface
    ├── ECR Interface
    └── Systems Manager Interface
```

---

### Q7: Explain CloudWatch — metrics, logs, alarms, dashboards.

**A:**

**CloudWatch Metrics (numeric data over time):**
- Default AWS metrics (CPU%, connections, requests)
- Custom metrics (business, application-specific)
- Resolution: 1-minute (standard) or 1-second (high-precision)

**CloudWatch Logs:**
- Centralized log aggregation
- Log groups (${application-name}, ${environment})
- Log streams (container, instance, function)
- Log Insights (SQL-like queries)

**CloudWatch Alarms (3 states):**
```
OK              → Metric within threshold
ALARM           → Metric exceeded → Trigger action
INSUFFICIENT    → Not enough data
```

**Alarm Actions:**
- SNS (email, Slack, PagerDuty)
- Auto Scaling (scale up/down)
- Lambda (custom automation)
- EC2 action (reboot, terminate)

**Example Queries:**
```sql
# Error rate
fields @message, @timestamp
| filter @message like /ERROR/
| stats count() as error_count by bin(5m)

# Slow requests (P99)
fields @duration
| filter ispresent(@duration)
| stats pct(@duration, 99) as p99_latency
```

---

### Q8: Explain Auto Scaling — policies, lifecycle hooks, scaling strategies.

**A:**

**Scaling Policy Types:**

| Type | Complexity | Use |
|---|---|---|
| Target Tracking | Simple | "Keep CPU at 70%" |
| Step Scaling | Medium | Scale aggressively at >80% |
| Simple Scaling | Basic | Add N instances on threshold |
| Scheduled | Predictable | 9 AM traffic spike |

**Lifecycle Hooks (Graceful Shutdown):**
```
EC2 Lifecycle:

Launch → (running) → Terminate
         ↓
      Lifecycle Hook
      (pause here)
      
Use Case: Drain traffic before removing
  - Pod marked "not ready" in Kubernetes
  - Existing connections drain gracefully
  - New connections routed elsewhere
  - After timeout, forcefully terminate
```

---

### Q9: Explain cost optimization strategies at scale.

**A:**

**Savings Mechanisms (ROI order):**

```
1. Right-sizing (25% savings)
   → CloudWatch metrics identify over-provisioning
   → Downsize t3.2xlarge → t3.large
   
2. Reserved Instances (33% 1-yr, 55% 3-yr)
   → Steady-state workloads
   → Break-even: 4-6 months prepayment
   
3. Spot Instances (70% savings)
   → Non-critical workloads, accept 2-min interruption
   → Batch jobs, test environments
   
4. S3 Lifecycle (65% on logs)
   → 30d: Standard → Standard-IA
   → 90d: Standard-IA → Glacier
   → Saves $50k+ annually
   
5. Unused cleanup ($30-100k)
   → Delete unused EBS volumes
   → Remove old snapshots (>90 days)
   → Terminate stopped instances
   → Release Elastic IPs
```

---

### Q10: Explain AWS security best practices across all layers.

**A:**

**Multi-layer Security:**

```
Layer 1: Prevention
  - IAM least-privilege
  - Security groups (needed ports only)
  - VPC (network segmentation)
  - WAF (block injection attacks)

Layer 2: Detection
  - CloudTrail (all API calls)
  - GuardDuty (ML threat detection)
  - Config (compliance: "is this encrypted?")
  - Security Hub (aggregate findings)

Layer 3: Response
  - Automated remediation
  - Incident runbooks
  - Forensic analysis
```

**Encryption Best Practices:**
```
At Rest:
  - S3: SSE-KMS (not default SSE-S3)
  - RDS: KMS encryption enabled
  - EBS: Encrypted volumes
  - Secrets: KMS encrypted
  
In Transit:
  - TLS 1.2+ (no HTTP)
  - mTLS between services
  - VPN for hybrid

Key Management:
  - AWS KMS: manages key encryption keys
  - Secrets Manager: auto-rotate credentials
  - Annual key rotation
  - Audit who accessed which key
```

---

*File: 07-AWS-Complete.md | Created June 2026 | Sr Cloud Platform Engineer*

