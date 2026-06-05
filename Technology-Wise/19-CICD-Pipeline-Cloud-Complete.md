# CI/CD PIPELINES — CLOUD ENGINEER COMPLETE Q&A
## Jenkins, GitLab CI/CD, Deployment Strategies | Production Experience

---

## SECTION 1: CI/CD FUNDAMENTALS

---

### Q1: Explain CI/CD pipeline design for a large engineering organization.

**A:** CI/CD = Continuous Integration (merge often, build/test automatically) + Continuous Delivery (always deployable) + Continuous Deployment (auto-deploy to production).

**Pipeline Architecture at Amazon Robotics (200+ weekly deployments):**
```
Developer Push → GitLab/GitHub → Webhook → Jenkins
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    │                         │                         │
              Stage 1: Build           Stage 2: Test           Stage 3: Security
              - Compile code           - Unit tests             - SonarQube
              - Run linting            - Integration tests      - OWASP scan
              - Build Docker image     - Contract tests         - ECR scan
                    │                         │                         │
                    └─────────────────────────┘─────────────────────────┘
                                              │
                                     Stage 4: Artifact
                                     - Push to ECR
                                     - Sign artifact
                                     - Version tagging
                                              │
                              ┌───────────────┴───────────────┐
                              │                               │
                        Dev Deploy                    Staging Deploy
                        (auto)                        (auto after dev)
                              │                               │
                              └───────────────┬───────────────┘
                                              │
                                    Manual Approval Gate
                                              │
                                    Production Deploy
                                    (canary 5% → 100%)
```

---

### Q2: Show a complete Jenkins pipeline for a microservice.

**A:**

```groovy
// Jenkinsfile — Warehouse API deployment pipeline
pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: maven
    image: maven:3.9-eclipse-temurin-21
    command: ['sleep', '99d']
  - name: docker
    image: docker:24-dind
    securityContext:
      privileged: true
  - name: kubectl
    image: bitnami/kubectl:1.29
    command: ['sleep', '99d']
"""
        }
    }

    parameters {
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'production'])
        string(name: 'IMAGE_TAG', defaultValue: 'latest')
    }

    environment {
        APP_NAME       = 'warehouse-api'
        ECR_REGISTRY   = '123456789.dkr.ecr.us-east-1.amazonaws.com'
        SONAR_HOST     = 'https://sonar.ercot.internal'
        GIT_COMMIT_SHORT = "${GIT_COMMIT.take(8)}"
        IMAGE_TAG      = "${BUILD_NUMBER}-${GIT_COMMIT_SHORT}"
    }

    stages {

        stage('Code Quality') {
            steps {
                container('maven') {
                    sh 'mvn checkstyle:check'
                    sh 'mvn pmd:check'
                }
            }
        }

        stage('Unit Tests') {
            steps {
                container('maven') {
                    sh 'mvn test -Dtest.profile=unit'
                }
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                    jacoco execPattern: 'target/jacoco.exec',
                           classPattern: 'target/classes',
                           minimumInstructionCoverage: '80'   // Fail if coverage < 80%
                }
            }
        }

        stage('Integration Tests') {
            steps {
                container('maven') {
                    sh 'mvn test -Dtest.profile=integration'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                container('maven') {
                    withSonarQubeEnv('SonarQube') {
                        sh '''
                            mvn sonar:sonar \
                              -Dsonar.projectKey=${APP_NAME} \
                              -Dsonar.host.url=${SONAR_HOST} \
                              -Dsonar.login=${SONAR_TOKEN}
                        '''
                    }
                }
            }
        }

        stage('SonarQube Quality Gate') {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true   // Fail if quality gate fails
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                container('docker') {
                    sh 'mvn package -DskipTests'
                    sh """
                        docker build \
                          --build-arg APP_VERSION=${IMAGE_TAG} \
                          --build-arg BUILD_DATE=\$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
                          -t ${ECR_REGISTRY}/${APP_NAME}:${IMAGE_TAG} \
                          -t ${ECR_REGISTRY}/${APP_NAME}:latest \
                          .
                    """
                }
            }
        }

        stage('Security Scan - Container') {
            steps {
                container('docker') {
                    // Trivy container vulnerability scan
                    sh """
                        trivy image \
                          --severity CRITICAL,HIGH \
                          --exit-code 1 \         // Fail pipeline if CRITICAL vulns
                          --format table \
                          ${ECR_REGISTRY}/${APP_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                container('maven') {
                    sh '''
                        mvn dependency-check:check \
                          -DfailBuildOnCVSS=7 \    // Fail if CVSS >= 7
                          -DsuppressionFile=owasp-suppressions.xml
                    '''
                }
            }
            post {
                always {
                    publishHTML([
                        reportDir: 'target',
                        reportFiles: 'dependency-check-report.html',
                        reportName: 'OWASP Dependency Report'
                    ])
                }
            }
        }

        stage('Push to ECR') {
            steps {
                container('docker') {
                    withAWS(credentials: 'aws-ecr-credentials', region: 'us-east-1') {
                        sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_REGISTRY}'
                        sh 'docker push ${ECR_REGISTRY}/${APP_NAME}:${IMAGE_TAG}'
                        sh 'docker push ${ECR_REGISTRY}/${APP_NAME}:latest'
                    }
                }
            }
        }

        stage('Deploy to Dev') {
            when { expression { params.DEPLOY_ENV in ['dev', 'staging', 'production'] } }
            steps {
                container('kubectl') {
                    sh """
                        kubectl set image deployment/${APP_NAME} \
                          ${APP_NAME}=${ECR_REGISTRY}/${APP_NAME}:${IMAGE_TAG} \
                          -n dev
                        kubectl rollout status deployment/${APP_NAME} -n dev --timeout=5m
                    """
                }
            }
        }

        stage('Smoke Tests - Dev') {
            steps {
                sh 'newman run tests/smoke-tests.json --env-var baseUrl=https://warehouse-api.dev.ercot.internal'
            }
        }

        stage('Deploy to Staging') {
            when { expression { params.DEPLOY_ENV in ['staging', 'production'] } }
            steps {
                container('kubectl') {
                    sh """
                        kubectl set image deployment/${APP_NAME} \
                          ${APP_NAME}=${ECR_REGISTRY}/${APP_NAME}:${IMAGE_TAG} \
                          -n staging
                        kubectl rollout status deployment/${APP_NAME} -n staging --timeout=5m
                    """
                }
            }
        }

        stage('Performance Tests - Staging') {
            when { expression { params.DEPLOY_ENV in ['staging', 'production'] } }
            steps {
                sh '''
                    k6 run \
                      --vus 100 \
                      --duration 5m \
                      --threshold "http_req_duration{p99}<500" \    // P99 < 500ms
                      tests/performance/load-test.js
                '''
            }
        }

        stage('Manual Approval - Production') {
            when { expression { params.DEPLOY_ENV == 'production' } }
            steps {
                timeout(time: 4, unit: 'HOURS') {
                    input message: "Deploy ${APP_NAME}:${IMAGE_TAG} to PRODUCTION?",
                          submitter: 'platform-leads,engineering-managers'
                }
            }
        }

        stage('Canary Deploy - Production') {
            when { expression { params.DEPLOY_ENV == 'production' } }
            steps {
                // Step 1: Deploy canary (5% traffic)
                sh """
                    kubectl apply -f k8s/canary-deployment.yaml \
                      --set image.tag=${IMAGE_TAG} \
                      -n production
                """

                // Step 2: Monitor for 10 minutes
                sh 'sleep 600'

                // Step 3: Check error rate during canary
                sh '''
                    ERROR_RATE=$(kubectl exec -n monitoring deployment/prometheus -- \
                      promtool query instant http://localhost:9090 \
                      "rate(http_requests_total{job=\"warehouse-api\",status=~\"5..\"}[5m])")
                    if [ $(echo "$ERROR_RATE > 0.01" | bc) -eq 1 ]; then
                        echo "Error rate too high during canary! Rolling back."
                        kubectl rollout undo deployment/warehouse-api-canary -n production
                        exit 1
                    fi
                '''

                // Step 4: Full rollout
                container('kubectl') {
                    sh """
                        kubectl set image deployment/${APP_NAME} \
                          ${APP_NAME}=${ECR_REGISTRY}/${APP_NAME}:${IMAGE_TAG} \
                          -n production
                        kubectl rollout status deployment/${APP_NAME} -n production --timeout=10m
                    """
                }
            }
        }
    }

    post {
        success {
            slackSend channel: '#deployments',
                      color: 'good',
                      message: "✅ ${APP_NAME}:${IMAGE_TAG} deployed to ${params.DEPLOY_ENV} by ${BUILD_USER}"
        }
        failure {
            slackSend channel: '#deployments',
                      color: 'danger',
                      message: "❌ ${APP_NAME} deployment FAILED. Check: ${BUILD_URL}"
            // Auto-rollback on production failure
            script {
                if (params.DEPLOY_ENV == 'production') {
                    sh 'kubectl rollout undo deployment/${APP_NAME} -n production'
                }
            }
        }
    }
}
```

---

### Q3: Explain deployment strategies — Blue-Green, Canary, Rolling Update, Recreate.

**A:**

| Strategy | Zero Downtime | Rollback Speed | Traffic Control | Risk | Use Case |
|---|---|---|---|---|---|
| **Recreate** | ❌ | Fast | None | High | Dev/test only |
| **Rolling Update** | ✅ | Slow (re-roll) | None | Medium | Standard K8s default |
| **Blue-Green** | ✅ | Instant (switch) | None | Low | Critical systems, instant rollback |
| **Canary** | ✅ | Fast | Percentage | Lowest | Risk mitigation, A/B testing |
| **Shadow** | ✅ | N/A | Mirrored | None | Testing new version with prod traffic |

**Blue-Green Deployment:**
```yaml
# Blue environment (current production)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: warehouse-api-blue
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: warehouse-api
      version: blue
  template:
    metadata:
      labels:
        app: warehouse-api
        version: blue
    spec:
      containers:
      - name: warehouse-api
        image: warehouse-api:v1.0.0
---
# Green environment (new version)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: warehouse-api-green
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: warehouse-api
      version: green
  template:
    metadata:
      labels:
        app: warehouse-api
        version: green
    spec:
      containers:
      - name: warehouse-api
        image: warehouse-api:v2.0.0
---
# Service — switch traffic by changing selector
apiVersion: v1
kind: Service
metadata:
  name: warehouse-api-svc
spec:
  selector:
    app: warehouse-api
    version: blue    # Change to "green" to switch traffic instantly
  ports:
  - port: 80
    targetPort: 8080
```

```bash
# Switch traffic from blue to green
kubectl patch service warehouse-api-svc \
  -p '{"spec":{"selector":{"version":"green"}}}' \
  -n production

# If issues: instant rollback to blue
kubectl patch service warehouse-api-svc \
  -p '{"spec":{"selector":{"version":"blue"}}}' \
  -n production
```

**Canary with NGINX Ingress:**
```yaml
# Stable deployment (95% traffic)
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: warehouse-api-stable
  annotations:
    nginx.ingress.kubernetes.io/canary: "false"
spec:
  rules:
  - host: warehouse-api.ercot.internal
    http:
      paths:
      - path: /
        backend:
          service:
            name: warehouse-api-stable-svc
            port:
              number: 80
---
# Canary deployment (5% traffic initially)
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: warehouse-api-canary
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "5"    # 5% of traffic
spec:
  rules:
  - host: warehouse-api.ercot.internal
    http:
      paths:
      - path: /
        backend:
          service:
            name: warehouse-api-canary-svc
            port:
              number: 80
```

```bash
# Gradually increase canary weight
kubectl annotate ingress warehouse-api-canary \
  nginx.ingress.kubernetes.io/canary-weight="25" \
  --overwrite -n production

kubectl annotate ingress warehouse-api-canary \
  nginx.ingress.kubernetes.io/canary-weight="50" \
  --overwrite -n production

# Full rollout — promote canary to stable
kubectl annotate ingress warehouse-api-canary \
  nginx.ingress.kubernetes.io/canary-weight="100" \
  --overwrite -n production
```

**Amazon Robotics result:** Implemented canary releases → reduced failed deployments by 90%.

---

### Q4: How do you implement GitLab CI/CD? Show a complete pipeline.

**A:**

```yaml
# .gitlab-ci.yml
stages:
  - validate
  - test
  - security
  - build
  - deploy-dev
  - deploy-staging
  - deploy-production

variables:
  DOCKER_TLS_CERTDIR: "/certs"
  ECR_REGISTRY: "123456789.dkr.ecr.us-east-1.amazonaws.com"
  APP_NAME: "warehouse-api"

# ─── Validate ───────────────────────────────────────────────
code-format-check:
  stage: validate
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn checkstyle:check
    - mvn fmt:check
  only:
    - merge_requests
    - main

# ─── Tests ──────────────────────────────────────────────────
unit-tests:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn test -Dtest.profile=unit
  coverage: '/Total.*?([0-9]{1,3})%/'     # Extract coverage from logs
  artifacts:
    reports:
      junit: target/surefire-reports/*.xml
      coverage_report:
        coverage_format: jacoco
        path: target/site/jacoco/jacoco.xml
  only:
    - merge_requests
    - main

integration-tests:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  services:
    - name: postgres:15                      # Spin up dependencies
      alias: postgres
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/testdb
  script:
    - mvn test -Dtest.profile=integration
  only:
    - merge_requests
    - main

# ─── Security ───────────────────────────────────────────────
owasp-dependency-check:
  stage: security
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn dependency-check:check -DfailBuildOnCVSS=8
  artifacts:
    paths:
      - target/dependency-check-report.html
    when: always
  only:
    - main

# ─── Build ──────────────────────────────────────────────────
docker-build-push:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - apk add --no-cache aws-cli
    - aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_REGISTRY
  script:
    - mvn package -DskipTests
    - docker build -t $ECR_REGISTRY/$APP_NAME:$CI_COMMIT_SHORT_SHA .
    # Trivy scan
    - trivy image --severity CRITICAL --exit-code 1 $ECR_REGISTRY/$APP_NAME:$CI_COMMIT_SHORT_SHA
    - docker push $ECR_REGISTRY/$APP_NAME:$CI_COMMIT_SHORT_SHA
  only:
    - main

# ─── Deploy Dev ─────────────────────────────────────────────
deploy-dev:
  stage: deploy-dev
  image: bitnami/kubectl:1.29
  environment:
    name: development
    url: https://warehouse-api.dev.ercot.internal
  script:
    - kubectl set image deployment/$APP_NAME $APP_NAME=$ECR_REGISTRY/$APP_NAME:$CI_COMMIT_SHORT_SHA -n dev
    - kubectl rollout status deployment/$APP_NAME -n dev --timeout=5m
  only:
    - main

# ─── Deploy Staging ─────────────────────────────────────────
deploy-staging:
  stage: deploy-staging
  image: bitnami/kubectl:1.29
  environment:
    name: staging
    url: https://warehouse-api.staging.ercot.internal
  script:
    - kubectl set image deployment/$APP_NAME $APP_NAME=$ECR_REGISTRY/$APP_NAME:$CI_COMMIT_SHORT_SHA -n staging
    - kubectl rollout status deployment/$APP_NAME -n staging --timeout=5m
  only:
    - main
  needs: ["deploy-dev"]

# ─── Deploy Production ──────────────────────────────────────
deploy-production:
  stage: deploy-production
  image: bitnami/kubectl:1.29
  environment:
    name: production
    url: https://warehouse-api.ercot.internal
  when: manual                                  # Requires manual trigger
  script:
    # Canary: 10% traffic for 10 minutes
    - kubectl annotate ingress $APP_NAME-canary nginx.ingress.kubernetes.io/canary-weight=10 --overwrite -n production
    - sleep 600
    - ./scripts/check-error-rate.sh
    # Full rollout
    - kubectl set image deployment/$APP_NAME $APP_NAME=$ECR_REGISTRY/$APP_NAME:$CI_COMMIT_SHORT_SHA -n production
    - kubectl rollout status deployment/$APP_NAME -n production --timeout=10m
  only:
    - main
  needs: ["deploy-staging"]
  allow_failure: false
```

---

### Q5: How do you implement GitOps with ArgoCD?

**A:**

**GitOps principle:** Git is the single source of truth for infrastructure state. No manual `kubectl apply` — ArgoCD syncs K8s state to match Git repo.

```yaml
# ArgoCD Application manifest
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: warehouse-api
  namespace: argocd
spec:
  project: logistics-team

  source:
    repoURL: https://gitlab.ercot.internal/platform/k8s-manifests
    targetRevision: main
    path: logistics/warehouse-api

  destination:
    server: https://kubernetes.default.svc
    namespace: logistics

  syncPolicy:
    automated:
      prune: true      # Delete K8s resources removed from Git
      selfHeal: true   # Revert manual kubectl changes automatically
    syncOptions:
    - CreateNamespace=true
    - PrunePropagationPolicy=foreground
    - ApplyOutOfSyncOnly=true

  # Notify on sync
  notifications:
    annotations:
      notifications.argoproj.io/subscribe.on-sync-succeeded.slack: "deployments"
      notifications.argoproj.io/subscribe.on-sync-failed.slack: "alerts"
```

**GitOps workflow:**
```bash
# Developer workflow: Update image tag in Git
# 1. CI pipeline builds and pushes Docker image
# 2. CI pipeline updates image tag in manifests repo
git clone https://gitlab.ercot.internal/platform/k8s-manifests
sed -i "s|image: warehouse-api:.*|image: warehouse-api:${NEW_TAG}|" \
  logistics/warehouse-api/deployment.yaml
git commit -am "chore: update warehouse-api to ${NEW_TAG}"
git push origin main

# 3. ArgoCD detects change and syncs to Kubernetes automatically
# 4. ArgoCD notifies Slack channel of successful deployment
```

---

### Q6: Explain how you implement automated rollback.

**A:**

```bash
#!/bin/bash
# automated-rollback.sh — runs after every production deployment

DEPLOYMENT=$1
NAMESPACE=$2
HEALTH_CHECK_URL=$3
WAIT_MINUTES=${4:-10}

echo "Monitoring deployment ${DEPLOYMENT} for ${WAIT_MINUTES} minutes..."

END_TIME=$(($(date +%s) + WAIT_MINUTES * 60))

while [ $(date +%s) -lt $END_TIME ]; do
  # Check 1: Pod restarts
  RESTARTS=$(kubectl get pods -n $NAMESPACE -l app=$DEPLOYMENT \
    -o jsonpath='{.items[*].status.containerStatuses[0].restartCount}')
  if echo "$RESTARTS" | grep -qE '[3-9]|[1-9][0-9]'; then
    echo "Too many pod restarts: $RESTARTS"
    rollback
    exit 1
  fi

  # Check 2: Deployment available replicas
  DESIRED=$(kubectl get deployment $DEPLOYMENT -n $NAMESPACE -o jsonpath='{.spec.replicas}')
  AVAILABLE=$(kubectl get deployment $DEPLOYMENT -n $NAMESPACE -o jsonpath='{.status.availableReplicas}')
  if [ "$AVAILABLE" -lt "$DESIRED" ]; then
    echo "Deployment degraded: $AVAILABLE/$DESIRED replicas available"
    # Wait a bit more before deciding
    sleep 30
    AVAILABLE=$(kubectl get deployment $DEPLOYMENT -n $NAMESPACE -o jsonpath='{.status.availableReplicas}')
    if [ "$AVAILABLE" -lt "$DESIRED" ]; then
      rollback
      exit 1
    fi
  fi

  # Check 3: HTTP health
  HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 $HEALTH_CHECK_URL)
  if [ "$HTTP_STATUS" != "200" ]; then
    echo "Health check failed: HTTP $HTTP_STATUS"
    rollback
    exit 1
  fi

  sleep 30
done

echo "Deployment validated successfully after ${WAIT_MINUTES} minutes"

rollback() {
  echo "ROLLING BACK deployment ${DEPLOYMENT}"
  kubectl rollout undo deployment/$DEPLOYMENT -n $NAMESPACE
  kubectl rollout status deployment/$DEPLOYMENT -n $NAMESPACE --timeout=5m

  # Alert team
  aws sns publish \
    --topic-arn arn:aws:sns:us-east-1:123456:deployment-alerts \
    --message "AUTO-ROLLBACK: ${DEPLOYMENT} rolled back in ${NAMESPACE}. Reason: $1"
}
```

---

### Q7: How do you secure CI/CD pipelines?

**A:**

**Security controls implemented at ERCOT/Amazon Robotics:**

```groovy
// 1. Never use hardcoded credentials — use IAM roles or Jenkins credentials
withCredentials([aws(credentialsId: 'aws-ecr-prod', region: 'us-east-1')]) {
    sh 'aws ecr get-login-password | docker login ...'
}

// 2. Pin Docker image versions (no :latest in pipelines)
image: maven:3.9.6-eclipse-temurin-21    // Not maven:latest

// 3. Scan before push — not after
sh 'trivy image --exit-code 1 --severity CRITICAL myapp:${TAG}'
// Push only if scan passes

// 4. Artifact signing — verify integrity
sh 'cosign sign --key cosign.key ${ECR_REGISTRY}/myapp:${TAG}'

// 5. Least-privilege Jenkins service account
// Jenkins SA only has: ECR push, K8s deploy to specific namespace
// No admin access

// 6. Separate pipelines per environment
// Dev pipeline: auto-run, no approval
// Staging pipeline: auto-run after dev success
// Production pipeline: manual approval from team leads

// 7. Secret scanning in code
sh 'gitleaks detect --source . --verbose'    // Detect hardcoded secrets
sh 'truffleHog git file://.'                 // Scan git history
```

**Secret management flow:**
```
Secrets Manager → Jenkins Plugin → Build → K8s Secret
                                        (never in Dockerfile)
                                        (never in env logs)
                                        (never in git)
```

---

### Q8: Explain how you measure CI/CD pipeline performance (DORA metrics).

**A:**

**DORA (DevOps Research and Assessment) 4 Key Metrics:**

| Metric | Description | Target (Elite) | Amazon Robotics Result |
|---|---|---|---|
| **Deployment Frequency** | How often you deploy to prod | Multiple per day | 200+ per week |
| **Lead Time for Changes** | Commit to production time | < 1 hour | < 4 hours |
| **Change Failure Rate** | % deployments causing incidents | < 5% | < 2% (canary) |
| **MTTR** | Time to restore after failure | < 1 hour | 25 minutes |

```python
# DORA metrics calculation from Jenkins data
import requests
from datetime import datetime, timedelta

JENKINS_URL = "https://jenkins.ercot.internal"
TOKEN = "jenkins-api-token"

def get_deployment_frequency(pipeline_name, days=30):
    """Count production deployments in last N days"""
    builds = requests.get(
        f"{JENKINS_URL}/job/{pipeline_name}/api/json?tree=builds[number,timestamp,result,duration]",
        auth=('admin', TOKEN)
    ).json()['builds']
    
    cutoff = datetime.now() - timedelta(days=days)
    prod_builds = [
        b for b in builds
        if datetime.fromtimestamp(b['timestamp']/1000) > cutoff
        and b['result'] == 'SUCCESS'
    ]
    
    return len(prod_builds) / days  # Deployments per day

# Publish to CloudWatch custom metrics
import boto3
cw = boto3.client('cloudwatch')
cw.put_metric_data(
    Namespace='ERCOT/DORA',
    MetricData=[{
        'MetricName': 'DeploymentFrequency',
        'Value': get_deployment_frequency('warehouse-api-pipeline'),
        'Unit': 'Count'
    }]
)
```

---

*File: 19-CICD-Pipeline-Cloud-Complete.md | Created: June 2026 | Role: Sr Cloud Platform Engineer*

