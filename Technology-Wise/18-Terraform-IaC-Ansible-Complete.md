# TERRAFORM & INFRASTRUCTURE AS CODE — COMPLETE Q&A
## Senior Cloud Platform Engineer Level | Production Experience

---

## SECTION 1: TERRAFORM FUNDAMENTALS

---

### Q1: Explain Terraform core concepts — providers, resources, state, and modules.

**A:**

```hcl
# Provider configuration with remote backend
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = { source = "hashicorp/aws"; version = "~> 5.0" }
  }
  backend "s3" {
    bucket         = "ercot-terraform-state"
    key            = "production/infrastructure/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"   # Prevent concurrent applies
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Project     = "RIOO-IS"
    }
  }
}
```

**4 Core Terraform Concepts:**
| Concept | Description |
|---|---|
| **Provider** | Plugin to interact with AWS, K8s, etc. |
| **Resource** | Infrastructure object to create (ec2, rds, etc.) |
| **State** | Terraform's record of what it created (tfstate file) |
| **Module** | Reusable, parameterized group of resources |

---

### Q2: How do you structure Terraform for a large organization?

**A: ERCOT Repository structure:**
```
terraform/
├── modules/                    # Reusable modules (versioned)
│   ├── vpc/
│   ├── eks-cluster/
│   ├── rds-oracle/
│   ├── kafka-msk/
│   └── monitoring/
├── environments/
│   ├── dev/
│   │   ├── main.tf             # Calls modules
│   │   ├── variables.tf
│   │   └── terraform.tfvars    # Dev-specific values
│   ├── staging/
│   └── production/
│       ├── main.tf
│       └── terraform.tfvars
└── global/                     # Account-wide: IAM, Route53, S3 buckets
```

**Reusable EKS Module call:**
```hcl
# environments/production/main.tf
module "eks_cluster" {
  source = "../../modules/eks-cluster"
  cluster_name       = "ercot-prod-cluster"
  cluster_version    = "1.29"
  vpc_id             = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnets
  node_groups = {
    general = {
      instance_type = "m5.2xlarge"
      min_size = 3; max_size = 20; desired_size = 6
    }
  }
}
```

---

### Q3: How do you manage Terraform state? Explain remote state and state locking.

**A:**

```hcl
# S3 Backend with DynamoDB locking
terraform {
  backend "s3" {
    bucket         = "ercot-terraform-state"
    key            = "production/eks/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    kms_key_id     = "arn:aws:kms:us-east-1:123456:key/key-id"
    dynamodb_table = "terraform-state-lock"
  }
}

# DynamoDB lock table (bootstrap)
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-state-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
  server_side_encryption { enabled = true }
}
```

**State commands:**
```bash
terraform state list                       # List all resources
terraform state show aws_eks_cluster.main  # Inspect resource
terraform state mv aws_instance.old aws_instance.new   # Rename
terraform import aws_s3_bucket.existing ercot-data-lake # Import existing
terraform state rm aws_instance.to_remove  # Remove without deleting
terraform force-unlock LOCK_ID             # Unlock stuck state
```

**State best practices (ERCOT):**
- S3 with versioning + KMS encryption + public access blocked
- DynamoDB for pessimistic locking (blocks concurrent applies)
- Never commit `.tfstate` to Git
- Separate state files per environment

---

### Q4: Walk through the Terraform CI/CD pipeline you built.

**A: Jenkins pipeline at ERCOT:**

```groovy
pipeline {
    agent { label 'terraform-runner' }
    stages {
        stage('Validate & Format') {
            steps {
                sh 'terraform validate'
                sh 'terraform fmt -check -recursive'
            }
        }
        stage('Security Scan') {
            steps {
                sh 'tfsec . --severity CRITICAL'      // Block on critical CVEs
                sh 'checkov -d . --framework terraform'  // CIS compliance check
            }
        }
        stage('Plan') {
            steps {
                sh 'terraform plan -var-file=terraform.tfvars -out=tfplan'
                sh 'terraform show -no-color tfplan > tfplan.txt'
                archiveArtifacts 'tfplan.txt'
            }
        }
        stage('Manual Approval - PROD') {
            when { expression { ENVIRONMENT == 'production' } }
            steps { input message: 'Review plan. Approve to apply?' }
        }
        stage('Apply') {
            steps { sh 'terraform apply -auto-approve tfplan' }
        }
    }
}
```

**Quality gates before every apply:**
1. `terraform validate` — syntax check
2. `terraform fmt -check` — style consistency
3. `tfsec` — security vulnerabilities
4. `checkov` — CIS benchmark compliance
5. Plan review + manual approval for production

---

### Q5: Explain for_each vs count. When to use each?

**A:**

```hcl
# count — simple numeric repetition
resource "aws_subnet" "public" {
  count  = 3
  cidr_block = cidrsubnet(var.vpc_cidr, 8, count.index)
}
# Problem: deleting element-1 re-indexes elements 2,3 → terraform destroys/recreates

# for_each — use strings/maps as keys (stable identity)
resource "aws_subnet" "private" {
  for_each = toset(["us-east-1a", "us-east-1b", "us-east-1c"])
  availability_zone = each.key
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, index(tolist(toset(["us-east-1a","us-east-1b","us-east-1c"])), each.key) + 10)
}

# for_each with map — different config per resource
variable "lambda_functions" {
  default = {
    event_processor  = { memory = 1024, timeout = 300 }
    data_validator   = { memory = 512,  timeout = 60  }
    report_generator = { memory = 2048, timeout = 900 }
  }
}

resource "aws_lambda_function" "functions" {
  for_each      = var.lambda_functions
  function_name = "ercot-${each.key}"
  memory_size   = each.value.memory
  timeout       = each.value.timeout
}

# Dynamic blocks — repeated nested blocks within one resource
resource "aws_security_group" "kafka" {
  dynamic "ingress" {
    for_each = [9092, 9093, 9094]
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = [var.vpc_cidr]
    }
  }
}
```

**Rule:** Use `for_each` for anything with stable string identities. Use `count` only for truly interchangeable identical resources.

---

### Q6: How do you handle Terraform drift?

**A:**

```bash
# Detect drift (compare actual vs state)
terraform plan -refresh-only
# Output: "changes to sync state" = drift exists

# Fix drift (update state to match reality, no infra changes)
terraform apply -refresh-only

# Scheduled nightly drift detection at ERCOT:
terraform plan -refresh-only -detailed-exitcode
# Exit 0 = no drift, Exit 2 = drift detected → SNS alert to team
```

**Preventing drift:**
- AWS Config rules: Alert on resources changed outside Terraform
- Service Control Policies: Restrict manual changes in production accounts
- CloudTrail + EventBridge: Alert on RDS/EKS manual modifications
- Process: Emergency manual changes MUST update Terraform within 24h

---

### Q7: Explain Terraform locals and data sources.

**A:**

```hcl
# Data sources — query existing AWS resources
data "aws_vpc" "existing" {
  filter { name = "tag:Name"; values = ["ercot-prod-vpc"] }
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

# Locals — computed values, reduce repetition
locals {
  name_prefix   = "${var.project}-${var.environment}"
  is_production = var.environment == "production"
  account_id    = data.aws_caller_identity.current.account_id
  region        = data.aws_region.current.name

  common_tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
    Project     = var.project
    CostCenter  = var.cost_center
  }

  # Conditional configs
  rds_class   = local.is_production ? "db.r6g.2xlarge" : "db.t3.large"
  rds_multi_az = local.is_production
}

resource "aws_db_instance" "main" {
  identifier     = "${local.name_prefix}-database"
  instance_class = local.rds_class
  multi_az       = local.rds_multi_az
  tags           = local.common_tags
}
```

---

## SECTION 2: ANSIBLE Q&A

---

### Q8: Explain Ansible architecture and core concepts.

**A:**

| Concept | Description |
|---|---|
| **Control Node** | Machine where Ansible runs (Jenkins agent at ERCOT) |
| **Inventory** | List of managed hosts (static file or dynamic AWS plugin) |
| **Playbook** | YAML file defining what tasks to run on which hosts |
| **Role** | Reusable grouping of tasks, handlers, templates, variables |
| **Module** | Building block: `aws_ec2`, `docker_container`, `yum`, etc. |
| **Handler** | Task triggered only when notified (restart on config change) |

**Amazon Robotics results:** 200+ Ansible playbooks → reduced environment provisioning from 4 hours to 15 minutes.

---

### Q9: Show a production Ansible playbook example.

**A:**

```yaml
---
# playbooks/configure-eks-worker.yaml
- name: Configure Kubernetes Worker Node
  hosts: k8s_workers
  become: true
  vars:
    kubernetes_version: "1.29.0"
    
  pre_tasks:
    - name: Validate OS version
      assert:
        that: ansible_distribution == "Amazon"
        fail_msg: "Only Amazon Linux supported"

  tasks:
    - name: Update all packages
      dnf:
        name: "*"
        state: latest

    - name: Load kernel modules for Kubernetes
      modprobe:
        name: "{{ item }}"
        state: present
      loop:
        - overlay
        - br_netfilter

    - name: Configure sysctl for K8s networking
      sysctl:
        name: "{{ item.key }}"
        value: "{{ item.value }}"
        sysctl_file: /etc/sysctl.d/kubernetes.conf
        reload: true
      loop:
        - { key: 'net.bridge.bridge-nf-call-iptables', value: '1' }
        - { key: 'net.ipv4.ip_forward', value: '1' }

    - name: Install containerd and kubelet
      dnf:
        name:
          - "containerd"
          - "kubelet-{{ kubernetes_version }}"
          - "kubectl-{{ kubernetes_version }}"
        state: present

    - name: Configure containerd
      template:
        src: templates/containerd-config.toml.j2
        dest: /etc/containerd/config.toml
      notify: restart containerd

    - name: Enable kubelet
      systemd:
        name: kubelet
        enabled: true
        state: started

    - name: Join Kubernetes cluster
      command: |
        kubeadm join {{ k8s_api_endpoint }}:6443 \
          --token {{ k8s_token }} \
          --discovery-token-ca-cert-hash {{ k8s_ca_hash }}
      register: join_result
      changed_when: "'joined the cluster' in join_result.stdout"

  handlers:
    - name: restart containerd
      systemd:
        name: containerd
        state: restarted
```

---

### Q10: How do you use dynamic AWS inventory with Ansible?

**A:**

```yaml
# inventory/aws_ec2.yaml — dynamic inventory plugin
plugin: aws_ec2
regions:
  - us-east-1
filters:
  tag:ManagedBy: Ansible
  instance-state-name: running
  tag:Environment: "{{ env }}"
groups:
  k8s_workers:  "'kubernetes' in tags.Role"
  kafka_brokers: "'kafka' in tags.Role"
compose:
  ansible_host: private_ip_address
  ansible_user: ec2-user
keyed_groups:
  - key: tags.Environment
    prefix: env
```

```bash
# Execute with dynamic inventory
ansible-playbook \
  -i inventory/aws_ec2.yaml \
  playbooks/configure-eks-worker.yaml \
  --extra-vars "env=production k8s_api_endpoint=10.0.10.100" \
  --check           # Dry run first
  --diff            # Show what changed
  --limit "env_production"   # Run only on production group

# Adhoc commands
ansible k8s_workers -i inventory/aws_ec2.yaml -m ping
ansible kafka_brokers -i inventory/aws_ec2.yaml -m shell -a "df -h"
```

---

### Q11: How do you secure sensitive data in Ansible (Vault)?

**A:**

```bash
# Create encrypted vault file
ansible-vault create vars/prod-secrets.yaml
# ansible-vault encrypt_string 'super_secret_password' --name 'db_password'

# vars/prod-secrets.yaml (encrypted)
# $ANSIBLE_VAULT;1.1;AES256
# 64333535656563...

# Decrypt at runtime
ansible-playbook playbook.yaml \
  --vault-password-file ~/.vault-password   # File with vault password
  # OR: --ask-vault-pass                   # Prompt for password
  # OR: --vault-id prod@/path/to/password  # Named vault IDs
```

**Better approach — use AWS Secrets Manager (no vault files needed):**
```yaml
- name: Get DB password from Secrets Manager
  community.aws.aws_secret:
    name: "ercot/prod/db-credentials"
    region: us-east-1
  register: db_secret

- name: Configure application
  template:
    src: app-config.j2
    dest: /etc/app/config.yaml
  vars:
    db_password: "{{ (db_secret.secret | from_json).password }}"
  no_log: true   # Don't log sensitive values
```

---

*File: 18-Terraform-IaC-Ansible-Complete.md | Created: June 2026 | Role: Sr Cloud Platform Engineer*

