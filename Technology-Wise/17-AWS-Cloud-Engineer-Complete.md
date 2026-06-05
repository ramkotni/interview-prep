# AWS CLOUD ENGINEER — COMPLETE Q&A
## Senior Cloud Platform Engineer Level | Production-Grade Answers

---

## SECTION 1: AWS CORE SERVICES

---

### Q1: Explain the AWS Well-Architected Framework and its pillars.

**A:** The AWS Well-Architected Framework provides best practices for building secure, high-performing, resilient, and efficient infrastructure.

**6 Pillars:**

| Pillar | Key Principles | My Implementation |
|---|---|---|
| **Operational Excellence** | IaC, CI/CD, monitoring, runbooks | Jenkins pipelines, Terraform, Grafana dashboards at ERCOT |
| **Security** | Least privilege, encryption, audit logs | IAM IRSA, Secrets Manager, CloudTrail, KMS at Amazon Robotics |
| **Reliability** | Multi-AZ, backups, auto-recovery, DR testing | Active-active multi-AZ, RDS replicas, quarterly DR tests |
| **Performance Efficiency** | Right-sizing, serverless, caching | Fargate rightsizing, Lambda for event processors, ElastiCache |
| **Cost Optimization** | Reserved/spot instances, rightsizing | $500k+ saved at Amazon Robotics via RI + Spot + rightsizing |
| **Sustainability** | Reduce environmental impact | Graviton2 instances (40% better price/performance) |

---

### Q2: Explain VPC design and subnetting. How did you design VPCs in production?

**A:**

**VPC Architecture at ERCOT (Production):**
```
VPC: 10.0.0.0/16
├── Public Subnets (Internet-facing)
│   ├── us-east-1a: 10.0.0.0/24  → ALB, NAT Gateway, Bastion
│   ├── us-east-1b: 10.0.1.0/24  → ALB, NAT Gateway
│   └── us-east-1c: 10.0.2.0/24  → ALB, NAT Gateway
├── Private App Subnets (EKS workers, Lambda, ECS)
│   ├── us-east-1a: 10.0.10.0/24 → Kubernetes worker nodes
│   ├── us-east-1b: 10.0.11.0/24 → Kubernetes worker nodes
│   └── us-east-1c: 10.0.12.0/24 → Kubernetes worker nodes
├── Private Data Subnets (RDS, ElastiCache, MSK)
│   ├── us-east-1a: 10.0.20.0/24 → RDS primary, Kafka broker
│   ├── us-east-1b: 10.0.21.0/24 → RDS replica, Kafka broker
│   └── us-east-1c: 10.0.22.0/24 → RDS replica, Kafka broker
└── VPC Endpoints (private access to AWS services)
    ├── S3 Gateway Endpoint (no NAT for S3 traffic)
    ├── ECR Interface Endpoint (pull Docker images privately)
    ├── Secrets Manager Endpoint (no internet for secrets)
    └── SSM Endpoint (no bastion needed)
```

**Terraform VPC Module (ERCOT):**
```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "ercot-prod-vpc"
  cidr = "10.0.0.0/16"

  azs              = ["us-east-1a", "us-east-1b", "us-east-1c"]
  public_subnets   = ["10.0.0.0/24", "10.0.1.0/24", "10.0.2.0/24"]
  private_subnets  = ["10.0.10.0/24", "10.0.11.0/24", "10.0.12.0/24"]
  database_subnets = ["10.0.20.0/24", "10.0.21.0/24", "10.0.22.0/24"]

  enable_nat_gateway     = true
  single_nat_gateway     = false    # One per AZ for HA (not cost-optimized)
  enable_vpn_gateway     = true     # Site-to-site VPN to on-premises
  enable_dns_hostnames   = true
  enable_dns_support     = true

  # EKS cluster tags (required for EKS to use subnets)
  public_subnet_tags = {
    "kubernetes.io/role/elb" = 1
  }
  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = 1
  }

  # VPC Endpoints for private AWS service access
  enable_s3_endpoint                    = true
  enable_secretsmanager_endpoint        = true
  enable_ecr_api_endpoint               = true
  enable_ecr_dkr_endpoint               = true

  tags = {
    Environment = "production"
    Project     = "RIOO-IS"
  }
}
```

---

### Q3: Explain AWS IAM — roles, policies, IRSA, and cross-account access.

**A:**

**IAM Core Concepts:**
```hcl
# IAM Policy — defines permissions
resource "aws_iam_policy" "warehouse_api_policy" {
  name        = "warehouse-api-policy"
  description = "Permissions for warehouse API microservice"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["s3:GetObject", "s3:PutObject"]
        Resource = "arn:aws:s3:::warehouse-data-bucket/*"
      },
      {
        Effect   = "Allow"
        Action   = ["secretsmanager:GetSecretValue"]
        Resource = "arn:aws:secretsmanager:us-east-1:123456:secret:prod/warehouse/*"
      },
      {
        Effect   = "Allow"
        Action   = ["sns:Publish"]
        Resource = "arn:aws:sns:us-east-1:123456:warehouse-events"
      },
      {
        Effect   = "Deny"
        Action   = ["iam:*", "ec2:*", "rds:*"]    # Explicit deny overrides Allow
        Resource = "*"
        Condition = {
          StringNotEquals = {
            "aws:PrincipalTag/service" = "warehouse-api"
          }
        }
      }
    ]
  })
}

# IAM Role with trust policy for EKS IRSA
resource "aws_iam_role" "warehouse_api_role" {
  name = "warehouse-api-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = {
        Federated = aws_iam_openid_connect_provider.eks.arn
      }
      Action = "sts:AssumeRoleWithWebIdentity"
      Condition = {
        StringEquals = {
          "${replace(data.aws_eks_cluster.cluster.identity[0].oidc[0].issuer, "https://", "")}:sub" = "system:serviceaccount:logistics:warehouse-api-sa"
          "${replace(data.aws_eks_cluster.cluster.identity[0].oidc[0].issuer, "https://", "")}:aud" = "sts.amazonaws.com"
        }
      }
    }]
  })
}
```

**Cross-account access pattern:**
```hcl
# Account A (dev): Role that can be assumed from Account B (prod)
resource "aws_iam_role" "cross_account_role" {
  name = "CrossAccountDeployRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "arn:aws:iam::PROD_ACCOUNT_ID:root" }
      Action    = "sts:AssumeRole"
      Condition = {
        StringEquals = {
          "sts:ExternalId" = var.external_id   # Extra security
        }
        Bool = {
          "aws:MultiFactorAuthPresent" = "true"
        }
      }
    }]
  })
}

# CI/CD pipeline assumes role for deployment
# aws sts assume-role \
#   --role-arn arn:aws:iam::DEV_ACCOUNT:role/CrossAccountDeployRole \
#   --role-session-name "jenkins-deploy-session"
```

**IRSA (IAM Roles for Service Accounts):**
```bash
# Create service account with IAM role annotation (eksctl)
eksctl create iamserviceaccount \
  --name warehouse-api-sa \
  --namespace logistics \
  --cluster ercot-prod-cluster \
  --attach-policy-arn arn:aws:iam::123456:policy/warehouse-api-policy \
  --approve \
  --override-existing-serviceaccounts

# The pod gets AWS credentials injected via OIDC token
# No static keys needed — credentials rotate automatically
```

---

### Q4: Explain AWS RDS — multi-AZ, read replicas, Aurora, and backup strategies.

**A:**

**RDS Multi-AZ vs Read Replicas:**
| Feature | Multi-AZ | Read Replica |
|---|---|---|
| **Purpose** | High availability, automatic failover | Read scaling, reporting, DR |
| **Synchronization** | Synchronous (zero data loss) | Asynchronous (slight lag) |
| **Failover** | Automatic (<2 min DNS update) | Manual promotion |
| **Cross-Region** | Same region only | Supports cross-region |
| **Cost** | 2x instance cost | Additional instance cost |

**RDS Setup (Terraform at Amazon Robotics):**
```hcl
resource "aws_db_instance" "warehouse_db" {
  identifier              = "warehouse-prod-db"
  engine                  = "oracle-ee"
  engine_version          = "19.0.0.0.ru-2023-07.rur-2023-07.r1"
  instance_class          = "db.r6g.2xlarge"
  allocated_storage       = 500
  max_allocated_storage   = 2000     # Enable storage autoscaling
  storage_type            = "gp3"
  storage_encrypted       = true
  kms_key_id              = aws_kms_key.rds.arn

  # Multi-AZ for HA
  multi_az                = true

  # Networking
  db_subnet_group_name    = aws_db_subnet_group.private.name
  vpc_security_group_ids  = [aws_security_group.rds.id]
  publicly_accessible     = false

  # Authentication
  manage_master_user_password = true    # Rotates password in Secrets Manager automatically

  # Backup
  backup_retention_period = 30           # 30 days PITR
  backup_window           = "03:00-04:00"  # Off-peak backup window
  delete_automated_backups = false

  # Maintenance
  maintenance_window           = "Mon:04:00-Mon:05:00"
  auto_minor_version_upgrade   = true
  apply_immediately            = false   # Apply during maintenance window

  # Performance Insights
  performance_insights_enabled          = true
  performance_insights_retention_period = 7    # 7 days (free tier)

  # Enhanced monitoring
  monitoring_interval    = 60            # 60-second granularity
  monitoring_role_arn    = aws_iam_role.rds_monitoring.arn

  # Deletion protection
  deletion_protection    = true

  tags = {
    Environment = "production"
    Backup      = "critical"
  }
}

# Read Replica (for reporting workloads)
resource "aws_db_instance" "warehouse_replica" {
  identifier             = "warehouse-prod-db-replica"
  replicate_source_db    = aws_db_instance.warehouse_db.identifier
  instance_class         = "db.r6g.xlarge"
  storage_encrypted      = true
  publicly_accessible    = false

  performance_insights_enabled = true
}
```

**Aurora Serverless v2 (used at Biogen):**
```hcl
resource "aws_rds_cluster" "aurora_cluster" {
  cluster_identifier      = "supply-chain-aurora"
  engine                  = "aurora-postgresql"
  engine_version          = "15.3"
  engine_mode             = "provisioned"
  database_name           = "supplychain"

  # Serverless v2 scaling
  serverlessv2_scaling_configuration {
    max_capacity = 16.0    # ACUs (Aurora Capacity Units)
    min_capacity = 0.5     # Scale to near-zero when idle
  }

  # Global database for cross-region DR
  global_cluster_identifier = aws_rds_global_cluster.global.id

  backup_retention_period = 35
  deletion_protection     = true
  storage_encrypted       = true
}
```

**Backup Strategy at Amazon Robotics:**
```
Automated: Daily snapshots retained 30 days (PITR enabled)
Manual: Weekly snapshots to separate account for DR
Cross-region: Replicate critical database snapshots to us-west-2
Testing: Monthly restore test in staging account
RTO: 4 hours (restore from snapshot to new RDS instance)
RPO: 1 hour (using PITR — recover to any point in last 35 days)
```

---

### Q5: Explain AWS Lambda — use cases, configuration, and optimization.

**A:**

**Lambda use cases at ERCOT (from resume):**
- Event processors for grid state changes
- Scheduled jobs (data cleanup, reports)
- API integrations (webhook receivers)
- Kafka consumer triggers
- CloudWatch alarm automation

**Lambda Configuration (Terraform):**
```hcl
resource "aws_lambda_function" "event_processor" {
  function_name = "ercot-event-processor"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "java21"
  handler       = "com.ercot.EventProcessor::handleRequest"
  filename      = data.archive_file.lambda_zip.output_path

  # Memory = CPU allocation (1769 MB = 1 vCPU)
  memory_size   = 1024
  timeout       = 300         # 5 minutes max

  # VPC for private resource access
  vpc_config {
    subnet_ids         = module.vpc.private_subnet_ids
    security_group_ids = [aws_security_group.lambda.id]
  }

  # Environment variables (non-sensitive)
  environment {
    variables = {
      KAFKA_TOPIC       = "grid-events"
      LOG_LEVEL         = "INFO"
      ENVIRONMENT       = "production"
    }
  }

  # Secrets from Secrets Manager (referenced in code, NOT here)
  # code: SecretsManager.getSecretValue("ercot/prod/db-credentials")

  # Concurrency
  reserved_concurrent_executions = 100    # Limit to prevent throttling downstream

  # Dead-letter queue for failed invocations
  dead_letter_config {
    target_arn = aws_sqs_queue.dlq.arn
  }

  # X-Ray tracing
  tracing_config {
    mode = "Active"
  }

  layers = [aws_lambda_layer_version.java_utils.arn]
}

# Event source mapping from Kafka (MSK)
resource "aws_lambda_event_source_mapping" "kafka_trigger" {
  event_source_arn  = aws_msk_cluster.kafka.arn
  function_name     = aws_lambda_function.event_processor.arn
  topics            = ["grid-events"]
  starting_position = "TRIM_HORIZON"
  batch_size        = 100
  enabled           = true
}
```

**Lambda Performance Optimization:**
```java
// Java Lambda — reduce cold start
public class EventProcessor implements RequestHandler<KafkaEvent, Void> {
    // Initialize heavyweight objects OUTSIDE handler (reused across invocations)
    private static final AmazonRDS rdsClient = AmazonRDSClientBuilder.standard()
        .withRegion("us-east-1")
        .build();
    private static final KafkaProducer<String, String> producer;
    
    static {
        // Static initializer runs once per container
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, System.getenv("KAFKA_BROKERS"));
        producer = new KafkaProducer<>(props);
    }
    
    @Override
    public Void handleRequest(KafkaEvent event, Context context) {
        // Only business logic here
        event.getRecords().forEach(record -> processRecord(record.getValue()));
        return null;
    }
}
```

**Cold Start Mitigation:**
- Use **Provisioned Concurrency** for latency-critical functions (keeps warm containers ready)
- Minimize deployment package size (Lambda layers for dependencies)
- Use ARM64 (Graviton2) — 34% better price/performance, faster cold starts for Java
- Java 21 with SnapStart — snapshot JVM after initialization → sub-100ms cold starts

---

### Q6: Explain AWS ECS vs EKS vs Fargate. When to use each?

**A:**

| Service | Description | Best For |
|---|---|---|
| **ECS** | AWS-managed container orchestration; simpler than K8s | AWS-native teams, simpler orchestration needs |
| **EKS** | Managed Kubernetes; full K8s API compatibility | Multi-cloud portability, complex orchestration, existing K8s expertise |
| **Fargate** | Serverless container runtime for ECS or EKS | No node management, variable workloads, cost efficiency |
| **EC2 Launch Type** | ECS/EKS on EC2 instances you manage | Maximum control, custom instance types, GPU workloads |

**Amazon Robotics Decision:**
- Used **ECS + Fargate** for stateless microservices (warehouse API, logistics service)
- Used **EKS + Managed Nodes** for Kafka, stateful applications needing persistent storage
- Used **EKS + Fargate** for batch processing jobs (no idle node costs)

**Fargate Task Definition (Terraform):**
```hcl
resource "aws_ecs_task_definition" "warehouse_api" {
  family                   = "warehouse-api"
  network_mode             = "awsvpc"         # Required for Fargate
  requires_compatibilities = ["FARGATE"]
  cpu                      = "1024"           # 1 vCPU
  memory                   = "2048"           # 2 GB

  execution_role_arn = aws_iam_role.ecs_execution_role.arn
  task_role_arn      = aws_iam_role.warehouse_api_role.arn   # Business permissions

  container_definitions = jsonencode([{
    name      = "warehouse-api"
    image     = "${aws_ecr_repository.warehouse_api.repository_url}:${var.image_tag}"
    essential = true
    portMappings = [{
      containerPort = 8080
      hostPort      = 8080
      protocol      = "tcp"
    }]
    environment = [
      { name = "SPRING_PROFILES_ACTIVE", value = "production" }
    ]
    secrets = [
      {
        name      = "DB_PASSWORD"
        valueFrom = "arn:aws:secretsmanager:us-east-1:123456:secret:prod/db:password::"
      }
    ]
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        "awslogs-group"         = "/ecs/warehouse-api"
        "awslogs-region"        = "us-east-1"
        "awslogs-stream-prefix" = "ecs"
      }
    }
    healthCheck = {
      command     = ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"]
      interval    = 30
      timeout     = 5
      retries     = 3
      startPeriod = 60
    }
  }])
}
```

---

### Q7: Explain AWS CloudWatch — metrics, logs, alarms, and dashboards.

**A:**

**CloudWatch Architecture:**
```
Applications → CloudWatch Logs → Log Groups → Metric Filters → Custom Metrics
                                                                      ↓
EC2/RDS/ECS → CloudWatch Metrics ────────────────────────────────→ Alarms
                                                                      ↓
                                                              SNS → PagerDuty/Slack
```

**CloudWatch Setup (Terraform at ERCOT):**
```hcl
# Custom Metric — application-level metric
resource "aws_cloudwatch_metric_alarm" "api_error_rate" {
  alarm_name          = "ercot-api-error-rate-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "3"
  metric_name         = "5xxErrorRate"
  namespace           = "ERCOT/API"
  period              = "60"           # 1-minute periods
  statistic           = "Average"
  threshold           = "1"            # Alert if >1% error rate
  alarm_description   = "API 5xx error rate above 1% for 3 consecutive minutes"
  treat_missing_data  = "notBreaching"

  alarm_actions = [aws_sns_topic.pagerduty_critical.arn]
  ok_actions    = [aws_sns_topic.slack_notifications.arn]

  dimensions = {
    Environment = "production"
    Service     = "rioo-is-api"
  }
}

# Composite alarm — alert only if BOTH conditions are true (reduce noise)
resource "aws_cloudwatch_composite_alarm" "service_degraded" {
  alarm_name = "ercot-service-degraded"
  alarm_rule = "ALARM(${aws_cloudwatch_metric_alarm.api_error_rate.alarm_name}) AND ALARM(${aws_cloudwatch_metric_alarm.api_latency_p99.alarm_name})"
  alarm_actions = [aws_sns_topic.pagerduty_critical.arn]
}

# Log group with retention
resource "aws_cloudwatch_log_group" "app_logs" {
  name              = "/ercot/rioo-is/application"
  retention_in_days = 90
  kms_key_id        = aws_kms_key.logs.arn
}

# Metric filter — extract custom metrics from log lines
resource "aws_cloudwatch_log_metric_filter" "payment_errors" {
  name           = "payment-processing-errors"
  pattern        = "[timestamp, requestId, level=ERROR, message=\"Payment*\"]"
  log_group_name = aws_cloudwatch_log_group.app_logs.name

  metric_transformation {
    name      = "PaymentErrors"
    namespace = "ERCOT/Business"
    value     = "1"
    unit      = "Count"
  }
}
```

**CloudWatch Logs Insights Queries (I use daily at ERCOT):**
```sql
-- Find slow API requests (p99 latency)
fields @timestamp, @message, responseTime, endpoint
| filter responseTime > 1000
| sort responseTime desc
| stats percentile(responseTime, 99) as p99, count(*) as requests by endpoint
| sort p99 desc
| limit 20

-- Error analysis by service
fields @timestamp, level, service, message
| filter level = "ERROR"
| stats count(*) as errors by service, bin(5m)
| sort errors desc

-- Lambda cold starts
fields @timestamp, @message
| filter @message like /Init Duration/
| stats avg(@initDuration), max(@initDuration), count(*) by functionName
```

---

### Q8: Explain AWS S3 — storage classes, lifecycle policies, versioning, and security.

**A:**

```hcl
resource "aws_s3_bucket" "data_lake" {
  bucket = "ercot-data-lake-prod"
}

# Versioning — protect against accidental deletions
resource "aws_s3_bucket_versioning" "data_lake" {
  bucket = aws_s3_bucket.data_lake.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Lifecycle policy — cost optimization
resource "aws_s3_bucket_lifecycle_configuration" "data_lake" {
  bucket = aws_s3_bucket.data_lake.id

  rule {
    id     = "archive-old-data"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"    # 30 days → Infrequent Access (45% cheaper)
    }
    transition {
      days          = 90
      storage_class = "GLACIER"         # 90 days → Glacier (66% cheaper than IA)
    }
    transition {
      days          = 365
      storage_class = "DEEP_ARCHIVE"    # 1 year → Deep Archive (95% cheaper than standard)
    }
    expiration {
      days = 2555                        # Delete after 7 years
    }
    noncurrent_version_expiration {
      noncurrent_days = 30               # Keep old versions 30 days
    }
  }
}

# Encryption at rest
resource "aws_s3_bucket_server_side_encryption_configuration" "data_lake" {
  bucket = aws_s3_bucket.data_lake.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.s3.arn
    }
    bucket_key_enabled = true    # Reduce KMS API calls (cost optimization)
  }
}

# Block all public access
resource "aws_s3_bucket_public_access_block" "data_lake" {
  bucket                  = aws_s3_bucket.data_lake.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Bucket policy — enforce TLS
resource "aws_s3_bucket_policy" "data_lake" {
  bucket = aws_s3_bucket.data_lake.id
  policy = jsonencode({
    Statement = [{
      Effect    = "Deny"
      Principal = "*"
      Action    = "s3:*"
      Resource  = ["${aws_s3_bucket.data_lake.arn}", "${aws_s3_bucket.data_lake.arn}/*"]
      Condition = {
        Bool = { "aws:SecureTransport" = "false" }
      }
    }]
  })
}
```

**S3 Storage Classes:**
| Class | Use Case | Cost (vs Standard) |
|---|---|---|
| Standard | Frequent access | Baseline |
| Standard-IA | Monthly access | ~45% cheaper storage, retrieval fee |
| Glacier Instant | Quarterly access | ~68% cheaper, ms retrieval |
| Glacier | Archival | ~85% cheaper, minutes-hours retrieval |
| Glacier Deep Archive | Regulatory archives | ~95% cheaper, 12-hour retrieval |

---

### Q9: How do you implement auto-scaling in AWS?

**A:**

**EC2 Auto Scaling Group:**
```hcl
resource "aws_autoscaling_group" "web_asg" {
  name                = "ercot-web-asg"
  vpc_zone_identifier = module.vpc.private_subnet_ids
  target_group_arns   = [aws_lb_target_group.web.arn]

  min_size         = 2
  max_size         = 20
  desired_capacity = 3

  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }

  # Warm pool — pre-initialized instances ready to scale
  warm_pool {
    pool_state                  = "Stopped"    # Stopped = lower cost than Running
    min_size                    = 2
    max_group_prepared_capacity = 5
  }

  instance_refresh {
    strategy = "Rolling"
    preferences {
      min_healthy_percentage = 50
    }
  }

  tag {
    key                 = "Name"
    value               = "ercot-web-instance"
    propagate_at_launch = true
  }
}

# Target Tracking scaling policy (recommended)
resource "aws_autoscaling_policy" "cpu_tracking" {
  name                   = "cpu-target-tracking"
  autoscaling_group_name = aws_autoscaling_group.web_asg.name
  policy_type            = "TargetTrackingScaling"

  target_tracking_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ASGAverageCPUUtilization"
    }
    target_value = 70.0         # Keep CPU at 70%
    scale_in_cooldown  = 300    # Wait 5 min before scaling in
    scale_out_cooldown = 60     # Scale out quickly (60s)
  }
}

# Scheduled scaling (predictive) — ERCOT peak usage pattern
resource "aws_autoscaling_schedule" "scale_up_morning" {
  scheduled_action_name  = "morning-peak-scale-up"
  autoscaling_group_name = aws_autoscaling_group.web_asg.name
  recurrence             = "0 6 * * MON-FRI"  # 6 AM weekdays
  min_size               = 5
  max_size               = 20
  desired_capacity       = 10
}

resource "aws_autoscaling_schedule" "scale_down_evening" {
  scheduled_action_name  = "evening-scale-down"
  autoscaling_group_name = aws_autoscaling_group.web_asg.name
  recurrence             = "0 20 * * MON-FRI"  # 8 PM weekdays
  desired_capacity       = 3
}
```

---

### Q10: Explain AWS disaster recovery strategies.

**A:**

**4 DR Strategies (by RTO/RPO/Cost):**

```
RPO                Low ←──────────────────────────────→ High
RTO  Low ↑
         │  Multi-Site     Warm Standby    Pilot Light    Backup/Restore
         │  Active-Active  (scaled down)  (data only)    (snapshots)
    High ↓
         
Cost:     $$$$$          $$$$             $$$              $$
```

| Strategy | RTO | RPO | Cost | Implementation |
|---|---|---|---|---|
| **Backup & Restore** | Hours | Hours | $ | S3 snapshots, RDS automated backups |
| **Pilot Light** | 30-60 min | Minutes | $$ | Core DB replicated, app infra rebuilt |
| **Warm Standby** | 5-15 min | Seconds | $$$ | Scaled-down active copy in DR region |
| **Multi-Site Active-Active** | Seconds | Zero | $$$$ | Full copy in multiple regions, traffic split |

**Amazon Robotics — Warm Standby implementation:**
```hcl
# Primary Region: us-east-1
# DR Region: us-west-2

# Cross-region RDS Read Replica (RPO: ~1 minute)
resource "aws_db_instance" "dr_replica" {
  provider               = aws.us-west-2
  identifier             = "warehouse-db-dr-replica"
  replicate_source_db    = "arn:aws:rds:us-east-1:123456:db:warehouse-prod-db"
  instance_class         = "db.r6g.large"    # Smaller than primary (warm standby)
  storage_encrypted      = true
  publicly_accessible    = false
  skip_final_snapshot    = false

  # Can be promoted to primary in DR event
  # aws rds promote-read-replica --db-instance-identifier warehouse-db-dr-replica
}

# Route 53 health check + failover routing
resource "aws_route53_health_check" "primary" {
  fqdn              = "api.ercot.internal"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/actuator/health"
  failure_threshold = 3
  request_interval  = 10
}

resource "aws_route53_record" "api_primary" {
  zone_id = var.hosted_zone_id
  name    = "api.ercot.internal"
  type    = "A"

  set_identifier = "primary"
  failover_routing_policy {
    type = "PRIMARY"
  }

  health_check_id = aws_route53_health_check.primary.id
  alias {
    name                   = aws_lb.primary.dns_name
    zone_id                = aws_lb.primary.zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "api_secondary" {
  zone_id = var.hosted_zone_id
  name    = "api.ercot.internal"
  type    = "A"

  set_identifier = "secondary"
  failover_routing_policy {
    type = "SECONDARY"
  }

  alias {
    name                   = aws_lb.dr.dns_name
    zone_id                = aws_lb.dr.zone_id
    evaluate_target_health = false
  }
}
```

---

### Q11: Explain AWS MSK (Managed Kafka), including setup and monitoring.

**A:**

```hcl
resource "aws_msk_cluster" "kafka" {
  cluster_name           = "ercot-kafka-prod"
  kafka_version          = "3.5.1"
  number_of_broker_nodes = 3    # One per AZ

  broker_node_group_info {
    instance_type   = "kafka.m5.2xlarge"
    client_subnets  = module.vpc.database_subnet_ids    # Private subnets
    storage_info {
      ebs_storage_info {
        provisioned_throughput {
          enabled           = true
          volume_throughput = 250
        }
        volume_size = 1000    # 1TB per broker
      }
    }
    security_groups = [aws_security_group.kafka.id]
  }

  encryption_info {
    encryption_in_transit {
      client_broker = "TLS"
      in_cluster    = true
    }
    encryption_at_rest_kms_key_arn = aws_kms_key.kafka.arn
  }

  client_authentication {
    sasl {
      iam = true    # IAM authentication — no passwords needed
    }
  }

  configuration_info {
    arn      = aws_msk_configuration.kafka_config.arn
    revision = aws_msk_configuration.kafka_config.latest_revision
  }

  open_monitoring {
    prometheus {
      jmx_exporter {
        enabled_in_broker = true    # JMX metrics for Prometheus scraping
      }
      node_exporter {
        enabled_in_broker = true
      }
    }
  }

  logging_info {
    broker_logs {
      cloudwatch_logs {
        enabled   = true
        log_group = aws_cloudwatch_log_group.kafka_broker.name
      }
      s3 {
        enabled = true
        bucket  = aws_s3_bucket.kafka_logs.bucket
        prefix  = "kafka/broker-logs"
      }
    }
  }
}

# Kafka configuration tuning
resource "aws_msk_configuration" "kafka_config" {
  name          = "ercot-kafka-config"
  kafka_versions = ["3.5.1"]

  server_properties = <<PROPERTIES
auto.create.topics.enable=false
default.replication.factor=3
min.insync.replicas=2
num.partitions=10
log.retention.hours=168
log.segment.bytes=1073741824
compression.type=snappy
PROPERTIES
}
```

**Kafka Monitoring at ERCOT:**
```bash
# Key metrics to monitor
# UnderReplicatedPartitions: > 0 = replication issue (ALERT immediately)
# OfflinePartitionsCount: > 0 = data unavailable (CRITICAL alert)
# Consumer lag per consumer group/topic
# Produce/consume throughput (bytes/sec)
# Request latency (Produce/Fetch P99)
# Disk utilization per broker (alert at 70%)

# Check consumer lag via CLI
kafka-consumer-groups.sh \
  --bootstrap-server kafka-broker:9092 \
  --describe \
  --group warehouse-processor-group
```

---

### Q12: Explain AWS Secrets Manager vs Parameter Store. When to use each?

**A:**

| Feature | Secrets Manager | Parameter Store |
|---|---|---|
| **Automatic rotation** | ✅ Built-in rotation (RDS, Redshift, etc.) | ❌ Manual rotation |
| **Cost** | $0.40/secret/month + API calls | Free (Standard), $0.05/10k requests (Advanced) |
| **Max value size** | 65,536 bytes | 4,096 bytes (Standard), 8,192 bytes (Advanced) |
| **Cross-account** | ✅ Resource-based policies | ✅ With KMS |
| **Versioning** | ✅ Automatic version management | ✅ With parameter history |

**When to use:**
- **Secrets Manager** — Database credentials, API keys (auto-rotation critical), sensitive data
- **Parameter Store** — App config, feature flags, environment-specific settings, non-sensitive data

```python
# Python — retrieve secret from Secrets Manager
import boto3
import json

def get_db_credentials():
    client = boto3.client('secretsmanager', region_name='us-east-1')
    
    response = client.get_secret_value(
        SecretId='ercot/prod/db-credentials'
    )
    
    secret = json.loads(response['SecretString'])
    return secret['username'], secret['password']

# Lambda function — cache secret across invocations
_db_credentials = None

def handler(event, context):
    global _db_credentials
    if _db_credentials is None:         # Only fetch once per container
        _db_credentials = get_db_credentials()
    
    username, password = _db_credentials
    # use credentials...
```

---

### Q13: Explain AWS Cost Optimization strategies you've implemented.

**A:**

**At Amazon Robotics — $500k+ annual savings:**

```
Strategy 1: Reserved Instances
- Identified steady-state workloads (always-running services)
- Purchased 1-year Reserved Instances for production EKS nodes
- Savings: 35% vs On-Demand

Strategy 2: Spot Instances
- Batch processing workloads (data analytics, reports, test environments)
- Used Spot Interruption handler (SIGTERM → graceful shutdown → save state)
- Savings: 70% vs On-Demand

Strategy 3: Fargate Spot
- Non-critical async workers on Fargate Spot
- Added retry logic for Spot interruptions
- Savings: 40-70% vs regular Fargate

Strategy 4: Rightsizing
- Used CloudWatch Container Insights to identify over-provisioned pods
- Reduced CPU/memory limits based on p99 actual utilization
- Average 25% reduction in requested resources
- Savings: 25% of compute costs

Strategy 5: S3 Lifecycle Policies
- Moved logs >30 days to S3-IA, >90 days to Glacier
- Savings: 65% on log storage

Strategy 6: Cost Allocation Tags
- Every resource tagged: Environment, Team, Project, Service
- Teams could see their own costs in Cost Explorer
- Created accountability → teams proactively optimized their workloads
```

**Cost monitoring Terraform:**
```hcl
# AWS Budget with alerts
resource "aws_budgets_budget" "monthly" {
  name         = "ercot-monthly-budget"
  budget_type  = "COST"
  limit_amount = "50000"
  limit_unit   = "USD"
  time_unit    = "MONTHLY"

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 80              # Alert at 80%
    threshold_type             = "PERCENTAGE"
    notification_type          = "ACTUAL"
    subscriber_email_addresses = ["cloud-team@ercot.com"]
  }

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 100             # Alert at forecast 100%
    threshold_type             = "PERCENTAGE"
    notification_type          = "FORECASTED"
    subscriber_email_addresses = ["cloud-team@ercot.com"]
  }
}
```

---

### Q14: Explain AWS Security best practices — GuardDuty, Security Hub, CloudTrail.

**A:**

```hcl
# CloudTrail — audit log of all API calls
resource "aws_cloudtrail" "main" {
  name                          = "ercot-cloudtrail"
  s3_bucket_name                = aws_s3_bucket.cloudtrail.id
  include_global_service_events = true    # IAM, STS, etc.
  is_multi_region_trail         = true    # All regions
  enable_log_file_validation    = true    # Detect tampering

  cloud_watch_logs_group_arn = "${aws_cloudwatch_log_group.cloudtrail.arn}:*"
  cloud_watch_logs_role_arn  = aws_iam_role.cloudtrail_logs.arn

  event_selector {
    read_write_type           = "All"
    include_management_events = true

    data_resource {
      type   = "AWS::S3::Object"
      values = ["arn:aws:s3:::ercot-data-lake-prod/"]   # S3 data events
    }
  }
}

# GuardDuty — threat detection
resource "aws_guardduty_detector" "main" {
  enable = true

  datasources {
    s3_logs {
      enable = true    # Detect malicious S3 activity
    }
    kubernetes {
      audit_logs {
        enable = true  # Detect K8s API anomalies
      }
    }
    malware_protection {
      scan_ec2_instance_with_findings {
        ebs_volumes {
          enable = true  # Auto-scan EBS for malware
        }
      }
    }
  }
}

# Security Hub — aggregate security findings
resource "aws_securityhub_account" "main" {}

resource "aws_securityhub_standards_subscription" "cis" {
  standards_arn = "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.4.0"
}

resource "aws_securityhub_standards_subscription" "aws_best_practices" {
  standards_arn = "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0"
}
```

**Security incident at Amazon Robotics:**
- GuardDuty finding: EC2 instance making unusual DNS queries (cryptocurrency mining malware)
- Response: Isolated instance in 5 minutes via security group modification, terminated and replaced
- Root cause: Developer had opened SSH port to `0.0.0.0/0` in dev environment
- Fix: AWS Config rule automatically detects and alerts on open security groups; Service Control Policy (SCP) prevents SSH from internet in production

---

*File: 17-AWS-Cloud-Engineer-Complete.md | Created: June 2026 | Role: Sr Cloud Platform Engineer*

