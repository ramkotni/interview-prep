# DISASTER RECOVERY & CLOUD PROCEDURES — COMPLETE Q&A
## Senior Cloud Platform Engineer | Production Experience
---
## SECTION 1: DISASTER RECOVERY
### Q1: Explain RTO, RPO, and AWS DR strategies.
**A:**
- **RTO (Recovery Time Objective)** — Max acceptable downtime. How fast must system recover?
- **RPO (Recovery Point Objective)** — Max acceptable data loss. How much data can you lose?
| Strategy | RTO | RPO | Cost | How |
|---|---|---|---|---|
| **Backup & Restore** | 4-8 hrs | 24 hrs | $ | RDS snapshots, S3 backups |
| **Pilot Light** | 30-60 min | 15 min | $$ | DB replica in DR region, app rebuilt |
| **Warm Standby** | 5-15 min | 1 min | $$$ | Scaled-down active env in DR region |
| **Multi-Site Active-Active** | Seconds | Zero | $$$$ | Full active copy, Route 53 failover |
**ERCOT:** Warm Standby — RTO 4hrs, RPO 1hr
**Amazon Robotics:** Multi-AZ Active-Active — RTO <30sec, RPO Zero
---
### Q2: How do you implement multi-AZ architecture?
**A:**
```hcl
# Spread EKS pods across AZs
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - topologyKey: topology.kubernetes.io/zone
      labelSelector:
        matchLabels:
          app: warehouse-api
# RDS Multi-AZ (automatic failover <2 min)
resource "aws_db_instance" "main" {
  multi_az = true
  backup_retention_period = 35
}
# Route 53 health check failover
resource "aws_route53_health_check" "primary" {
  fqdn              = "api.ercot.internal"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/actuator/health"
  failure_threshold = 3
  request_interval  = 10
}
```
---
### Q3: How do you test DR procedures?
**A: Quarterly DR exercises at ERCOT:**
```bash
#!/bin/bash
# Quarterly DR Simulation
# Step 1: Force Route 53 failover
aws route53 update-health-check --health-check-id $HC_ID --disabled
# Step 2: Measure failover time
START=$(date +%s)
while ! curl -s https://api-dr.ercot.internal/health | grep -q UP; do sleep 5; done
echo "Failover complete in $(($(date +%s)-START)) seconds"
# Step 3: Promote RDS read replica
aws rds promote-read-replica --db-instance-identifier warehouse-db-dr-replica --region us-west-2
aws rds wait db-instance-available --db-instance-identifier warehouse-db-dr-replica --region us-west-2
# Step 4: Run smoke tests against DR
newman run smoke-tests.json --env-var baseUrl=https://api-dr.ercot.internal
# Step 5: Document results vs RTO/RPO targets
```
**Incident Response Process:**
```
T+0:  Alert fires (CloudWatch/Grafana) → PagerDuty on-call
T+2:  Acknowledge, open Slack #incident channel
T+5:  Assess: check dashboards, recent deploys
T+10: Escalate if P0/P1 (page additional engineers)
T+25: Identify root cause and apply fix (rollback/failover/restart)
T+45: Confirm resolution, notify stakeholders
T+24h: Write RCA, 5-why analysis, preventive action items
```
---
### Q4: Explain backup strategies for RDS, S3, and Kubernetes.
**A:**
```hcl
# RDS — automated PITR + cross-region replication
resource "aws_db_instance" "main" {
  backup_retention_period = 35     # 35-day PITR
  backup_window = "02:00-03:00"    # Off-peak
}
# Restore to point in time
# aws rds restore-db-instance-to-point-in-time \
#   --source-db-instance-identifier warehouse-prod-db \
#   --target-db-instance-identifier warehouse-restored \
#   --restore-time 2026-06-01T10:00:00Z
# S3 Cross-Region Replication
resource "aws_s3_bucket_replication_configuration" "data_lake" {
  rule {
    destination {
      bucket        = aws_s3_bucket.data_lake_dr.arn
      storage_class = "STANDARD_IA"
    }
    status = "Enabled"
  }
}
```
```bash
# Kubernetes PV backup with Velero
velero install --provider aws --bucket ercot-k8s-backups --backup-location-config region=us-east-1
velero schedule create daily-backup \
  --schedule="0 2 * * *" \
  --include-namespaces logistics,kafka-system \
  --ttl 720h
# Restore namespace
velero restore create --from-backup daily-backup-20260601 --include-namespaces logistics
```
---
## SECTION 2: CLOUD INFRASTRUCTURE PROCEDURES
---
### Q5: Walk through how you onboard a new application to the cloud platform.
**A: ERCOT Onboarding Checklist:**
```
Week 1 — Architecture Review:
  □ Define SLO/SLI (availability, latency targets)
  □ Identify dependencies (DB, Kafka topics, external APIs)
  □ Choose container strategy (EKS vs ECS, Fargate vs EC2)
  □ Security classification (data sensitivity, encryption needs)
Week 1-2 — Infrastructure (Terraform):
  □ VPC resources: security groups, IAM roles, IRSA
  □ ECR repository with image lifecycle policies
  □ RDS/Aurora database or schema in shared cluster
  □ Kafka topics with replication factor/retention config
  □ AWS Secrets Manager paths for all credentials
  □ CloudWatch log groups
Week 2 — CI/CD Pipeline:
  □ Jenkins/GitLab pipeline (test → security scan → build → deploy)
  □ ECR push credentials configured
  □ Dev/Staging/Prod deployment stages
  □ Automated rollback on deployment failure
Week 2-3 — Observability:
  □ Prometheus annotations on deployment
  □ Health endpoints (/actuator/health/liveness, /readiness)
  □ Grafana dashboard (CPU, memory, HTTP rate, error rate, latency)
  □ CloudWatch alarms with PagerDuty routing
Week 3-4 — Production Readiness:
  □ Runbook written and tested
  □ DR failover tested
  □ Load test at 2x expected peak traffic
  □ On-call rotation updated
```
---
### Q6: How do you implement cost optimization?
**A: Amazon Robotics — $500k+ annual savings:**
| Strategy | Mechanism | Savings |
|---|---|---|
| **Reserved Instances** | 1-yr RI for steady production nodes | 35% |
| **Spot Instances** | Batch/test workloads on Spot | 70% |
| **Fargate Spot** | Async workers on Fargate Spot | 50% |
| **Rightsizing** | CloudWatch metrics → downsize over-provisioned | 25% |
| **S3 Lifecycle** | Logs: Standard→IA→Glacier→DeepArchive | 65% |
| **Unused Cleanup** | Auto-stop dev nights/weekends; delete old snapshots | $30k |
```python
# Automated cleanup — runs weekly
import boto3
from datetime import datetime, timezone, timedelta
def cleanup_old_snapshots(days_to_keep=90):
    ec2 = boto3.client('ec2')
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_to_keep)
    for snap in snapshots:
        if snap['StartTime'] < cutoff and 'KEEP' not in snap.get('Description',''):
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
def stop_dev_instances_weekends():
    if datetime.now().weekday() != 5: return   # Only Saturday
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Environment', 'Values': ['dev', 'staging']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    ids = [i['InstanceId'] for r in instances['Reservations'] for i in r['Instances']]
    if ids:
        ec2.stop_instances(InstanceIds=ids)
```
---
### Q7: Explain Oracle Cloud Infrastructure (OCI) vs AWS.
**A:**
| Feature | AWS | OCI |
|---|---|---|
| **Compute** | EC2 | OCI Compute (VM/Bare Metal) |
| **Container** | EKS, Fargate | OKE (Oracle Kubernetes Engine) |
| **Database** | RDS, Aurora | Oracle DB Cloud, Autonomous DB |
| **Object Storage** | S3 | OCI Object Storage |
| **Networking** | VPC, Security Groups | VCN, Security Lists, NSGs |
| **Serverless** | Lambda | OCI Functions |
| **Monitoring** | CloudWatch | OCI Monitoring, Logging |
| **IaC** | Terraform, CloudFormation | Terraform, OCI Resource Manager |
**OCI advantages for Oracle workloads:**
- Oracle Exadata Cloud — highest IOPS for Oracle DB
- Oracle Autonomous Database — self-managing, auto-patching
- Oracle RAC support (not available in AWS)
- No extra Oracle licensing fees when running Oracle DB on OCI
- Predictable pricing (egress costs ~10x cheaper than AWS)
**OCI Terraform example:**
```hcl
provider "oci" {
  region = "us-ashburn-1"
  auth   = "InstancePrincipal"
}
resource "oci_core_instance" "app_server" {
  availability_domain = data.oci_identity_availability_domains.ads.availability_domains[0].name
  compartment_id      = var.compartment_id
  shape               = "VM.Standard.E4.Flex"
  shape_config {
    ocpus         = 4
    memory_in_gbs = 16
  }
  source_details {
    source_type = "image"
    source_id   = var.oracle_linux_image_id
  }
  create_vnic_details {
    subnet_id        = oci_core_subnet.app_subnet.id
    assign_public_ip = false
  }
}
```
---
### Q8: How do you implement cloud security? Explain WAF, GuardDuty, Security Hub.
**A:**
**Security Layers at ERCOT/Amazon Robotics:**
```
Layer 1 — Identity: IAM least-privilege, IRSA, MFA, quarterly access reviews
Layer 2 — Network: Private subnets, Security Groups, WAF, AWS Shield, PrivateLink
Layer 3 — Data: KMS encryption (EBS/RDS/S3/Kafka), Secrets Manager auto-rotation
Layer 4 — Detection: CloudTrail (all API calls), GuardDuty (ML threat detection),
                     Security Hub (CIS benchmark), Config (compliance rules)
Layer 5 — Container: ECR scanning, cosign signing, Pod Security Standards,
                     read-only root filesystems, network policies
```
```hcl
# GuardDuty — threat detection
resource "aws_guardduty_detector" "main" {
  enable = true
  datasources {
    s3_logs { enable = true }
    kubernetes { audit_logs { enable = true } }
    malware_protection { scan_ec2_instance_with_findings { ebs_volumes { enable = true } } }
  }
}
# Security Hub — aggregate findings + CIS compliance
resource "aws_securityhub_account" "main" {}
resource "aws_securityhub_standards_subscription" "cis" {
  standards_arn = "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.4.0"
}
# WAF — protect public APIs
resource "aws_wafv2_web_acl" "api_protection" {
  name  = "ercot-api-waf"
  scope = "REGIONAL"
  rule {
    name     = "rate-limit"
    priority = 1
    action { block {} }
    statement {
      rate_based_statement {
        limit              = 2000   # 2000 req per 5-min window per IP
        aggregate_key_type = "IP"
      }
    }
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "RateLimitRule"
      sampled_requests_enabled   = true
    }
  }
}
```
---
### Q9: How do you monitor and improve platform reliability using SLOs and SLIs?
**A:**
**SRE Practice at Amazon Robotics:**
```
SLO (Service Level Objective) — commitment to users:
  "99.9% of API requests will succeed"
  "99% of API requests will complete in <500ms"
SLI (Service Level Indicator) — the metric you measure:
  "Ratio of successful requests to total requests in 5-minute window"
  "P99 response time measured at load balancer"
Error Budget:
  SLO 99.9% → 0.1% error budget = 43.8 minutes downtime/month
  If error budget < 10% remaining: freeze non-critical releases
  If error budget exhausted: full release freeze, focus on reliability
```
**Prometheus SLO queries:**
```promql
# Availability SLI
sum(rate(http_requests_total{status!~"5.."}[5m]))
  / sum(rate(http_requests_total[5m]))
# Latency SLI — % of requests under 500ms
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[5m]))
  / sum(rate(http_request_duration_seconds_count[5m]))
# Error budget remaining (over 30 days)
1 - (
  (1 - sum(rate(http_requests_total{status!~"5.."}[30d])) / sum(rate(http_requests_total[30d])))
  / (1 - 0.999)   # SLO threshold 99.9%
)
```
---
### Q10: Explain Kafka in cloud — MSK setup, topic design, DR.
**A:**
**MSK (Amazon Managed Kafka) Setup:**
```hcl
resource "aws_msk_cluster" "kafka" {
  cluster_name           = "ercot-kafka-prod"
  kafka_version          = "3.5.1"
  number_of_broker_nodes = 3
  broker_node_group_info {
    instance_type = "kafka.m5.2xlarge"
    client_subnets = module.vpc.database_subnet_ids
    storage_info {
      ebs_storage_info { volume_size = 1000 }
    }
  }
  encryption_info {
    encryption_in_transit { client_broker = "TLS" }
    encryption_at_rest_kms_key_arn = aws_kms_key.kafka.arn
  }
  client_authentication { sasl { iam = true } }
}
```
**Topic Design Best Practices:**
```bash
# Create topic with proper replication
kafka-topics.sh --bootstrap-server $BROKERS \
  --create \
  --topic warehouse-events \
  --partitions 12 \            # partitions = max parallelism for consumers
  --replication-factor 3 \     # 3 replicas across 3 AZs
  --config min.insync.replicas=2 \  # Need 2 replicas to acknowledge write
  --config retention.ms=604800000 \ # 7 days retention
  --config compression.type=snappy  # 40% size reduction
# Monitor consumer lag
kafka-consumer-groups.sh \
  --bootstrap-server $BROKERS \
  --describe --group warehouse-processor-group
# LAG > 10000 = alert (consumer falling behind)
```
**Key metrics to alert on:**
- `UnderReplicatedPartitions > 0` → CRITICAL: replication failing
- `OfflinePartitionsCount > 0` → CRITICAL: data unavailable
- Consumer lag per group > threshold → WARNING: consumer struggling
- Disk utilization > 70% → WARNING: plan capacity expansion
---
*File: 20-Disaster-Recovery-Cloud-Procedures.md | Created: June 2026 | Role: Sr Cloud Platform Engineer*
