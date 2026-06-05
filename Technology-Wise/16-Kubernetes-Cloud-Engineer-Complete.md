# KUBERNETES — CLOUD ENGINEER COMPLETE Q&A
## Senior Cloud Platform Engineer Level | Production Experience

---

## SECTION 1: KUBERNETES ARCHITECTURE & CORE CONCEPTS

---

### Q1: Explain Kubernetes architecture and its core components.

**A:** Kubernetes has a master-worker architecture:

**Control Plane (Master Node) Components:**
- **kube-apiserver** — Front-end for the Kubernetes control plane; processes REST API requests
- **etcd** — Distributed key-value store; stores all cluster state and configuration data
- **kube-scheduler** — Watches for new pods with no assigned node; selects the best node for pod placement
- **kube-controller-manager** — Runs controller loops: Node Controller, Replication Controller, Endpoints Controller, Service Account Controller
- **cloud-controller-manager** — Interfaces with underlying cloud provider (AWS, GCP, OCI)

**Worker Node Components:**
- **kubelet** — Agent on each node; ensures containers run in pods as specified
- **kube-proxy** — Network proxy maintaining iptables/IPVS rules for service communication
- **Container Runtime** — Docker, containerd, or CRI-O running actual containers

```
Control Plane
┌─────────────────────────────────────────────────┐
│  kube-apiserver ← etcd (cluster state)          │
│  kube-scheduler ← kube-controller-manager       │
│  cloud-controller-manager                        │
└─────────────────────────────────────────────────┘
         │ API calls
Worker Nodes
┌─────────────────────┐  ┌─────────────────────┐
│ kubelet             │  │ kubelet             │
│ kube-proxy          │  │ kube-proxy          │
│ containerd          │  │ containerd          │
│ Pods (containers)   │  │ Pods (containers)   │
└─────────────────────┘  └─────────────────────┘
```

**At ERCOT:** Ran 3-node control plane (HA) with worker nodes spread across 3 AZs ensuring no single point of failure in the Kubernetes cluster managing RIOO-IS microservices.

---

### Q2: What is the difference between a Pod, ReplicaSet, Deployment, and StatefulSet?

**A:**

| Object | Purpose | Use Case |
|---|---|---|
| **Pod** | Smallest deployable unit; wraps one or more containers | Rarely created directly |
| **ReplicaSet** | Ensures desired number of pod replicas always running | Managed by Deployment |
| **Deployment** | Manages ReplicaSets; provides rolling updates and rollback | Stateless applications |
| **StatefulSet** | Like Deployment but with stable network identity, persistent storage | Databases, Kafka, Zookeeper |
| **DaemonSet** | Runs one pod per node | Log agents, monitoring agents |
| **Job/CronJob** | Runs pod to completion / on a schedule | Batch jobs, scheduled tasks |

**Deployment Example (used in Amazon Robotics):**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: warehouse-api
  namespace: logistics
  labels:
    app: warehouse-api
    version: "2.1.0"
    env: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: warehouse-api
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1           # Allow 1 extra pod during update
      maxUnavailable: 0     # Never reduce below desired count
  template:
    metadata:
      labels:
        app: warehouse-api
        version: "2.1.0"
    spec:
      affinity:
        podAntiAffinity:    # Spread pods across AZs
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchLabels:
                app: warehouse-api
            topologyKey: topology.kubernetes.io/zone
      containers:
      - name: warehouse-api
        image: 123456789.dkr.ecr.us-east-1.amazonaws.com/warehouse-api:2.1.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: "250m"
            memory: "512Mi"
          limits:
            cpu: "500m"
            memory: "1Gi"
        env:
        - name: DB_URL
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: url
        - name: KAFKA_BROKERS
          valueFrom:
            configMapKeyRef:
              name: kafka-config
              key: brokers
        livenessProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /actuator/health/readiness
            port: 8080
          initialDelaySeconds: 20
          periodSeconds: 5
          failureThreshold: 3
```

**StatefulSet Example (Kafka/Zookeeper):**
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: kafka
  namespace: kafka-system
spec:
  serviceName: kafka-headless
  replicas: 3
  selector:
    matchLabels:
      app: kafka
  template:
    metadata:
      labels:
        app: kafka
    spec:
      containers:
      - name: kafka
        image: confluentinc/cp-kafka:7.4.0
        ports:
        - containerPort: 9092
        volumeMounts:
        - name: kafka-data
          mountPath: /var/lib/kafka/data
  volumeClaimTemplates:              # Each pod gets its own PVC
  - metadata:
      name: kafka-data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: gp3
      resources:
        requests:
          storage: 100Gi
```

---

### Q3: Explain Kubernetes Services and their types.

**A:** A Service is an abstraction that exposes pods as a network service with a stable IP and DNS name.

```yaml
# ClusterIP — Internal access only (default)
apiVersion: v1
kind: Service
metadata:
  name: warehouse-api-svc
  namespace: logistics
spec:
  type: ClusterIP
  selector:
    app: warehouse-api
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
---
# NodePort — Exposes on each node's IP at a static port
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080   # Range: 30000-32767
---
# LoadBalancer — Creates AWS/cloud load balancer (used in ERCOT)
spec:
  type: LoadBalancer
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
    service.beta.kubernetes.io/aws-load-balancer-internal: "true"
  ports:
  - port: 443
    targetPort: 8080
---
# Headless Service — No ClusterIP, used for StatefulSets
spec:
  clusterIP: None
  selector:
    app: kafka
```

**Service Types Summary:**
| Type | Use Case | When I Used It |
|---|---|---|
| ClusterIP | Microservice-to-microservice | All internal service calls at Amazon Robotics |
| NodePort | Debugging, external access via node | Dev/test environments |
| LoadBalancer | Expose to internet or internal users | ERCOT external APIs, Amazon Robotics public endpoints |
| Headless | StatefulSets (Kafka, databases) | Kafka cluster at Amazon Robotics |
| ExternalName | Map service to external DNS | Database connections to RDS at ERCOT |

---

### Q4: How do you configure Horizontal Pod Autoscaler (HPA) and Cluster Autoscaler?

**A:**

**HPA — scales pods based on metrics:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: warehouse-api-hpa
  namespace: logistics
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: warehouse-api
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70     # Scale up when CPU > 70%
  - type: Resource
    resource:
      name: memory
      target:
        type: AverageValue
        averageValue: 800Mi
  - type: Pods                      # Custom metric: requests per second
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: "1000"
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60    # Wait 60s before scaling up again
      policies:
      - type: Pods
        value: 4
        periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300   # Wait 5min before scaling down
      policies:
      - type: Percent
        value: 25
        periodSeconds: 60
```

**Cluster Autoscaler — scales nodes based on pending pods:**
```yaml
# EKS Cluster Autoscaler configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cluster-autoscaler
  namespace: kube-system
spec:
  template:
    spec:
      containers:
      - name: cluster-autoscaler
        image: k8s.gcr.io/autoscaling/cluster-autoscaler:v1.28.0
        command:
        - ./cluster-autoscaler
        - --v=4
        - --stderrthreshold=info
        - --cloud-provider=aws
        - --skip-nodes-with-local-storage=false
        - --expander=least-waste        # Choose node group that wastes fewest resources
        - --balance-similar-node-groups
        - --scale-down-enabled=true
        - --scale-down-delay-after-add=10m
        - --scale-down-unneeded-time=10m
        - --max-graceful-termination-sec=600
        env:
        - name: AWS_REGION
          value: us-east-1
```

**Production experience (Amazon Robotics):** HPA scaled warehouse-api from 3 to 15 pods during warehouse peak hours (7-9 AM EST), Cluster Autoscaler added 5 nodes automatically to accommodate the extra pods within 3 minutes.

---

### Q5: Explain RBAC in Kubernetes. How do you implement it?

**A:** RBAC (Role-Based Access Control) restricts what actions users/service accounts can perform.

**Key Objects:**
- **Role/ClusterRole** — Defines permissions (what can be done)
- **RoleBinding/ClusterRoleBinding** — Assigns Role to user/group/service account

```yaml
# Role — Namespace-scoped permissions
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer-role
  namespace: logistics
rules:
- apiGroups: ["apps"]
  resources: ["deployments", "replicasets"]
  verbs: ["get", "list", "watch", "create", "update"]
- apiGroups: [""]
  resources: ["pods", "pods/log", "configmaps"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["secrets"]
  verbs: []    # No access to secrets
---
# RoleBinding — Assign role to a user
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developer-binding
  namespace: logistics
subjects:
- kind: User
  name: john.doe@ercot.com
  apiGroup: rbac.authorization.k8s.io
- kind: Group
  name: platform-developers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer-role
  apiGroup: rbac.authorization.k8s.io
---
# ServiceAccount RBAC — for pods accessing K8s API
apiVersion: v1
kind: ServiceAccount
metadata:
  name: warehouse-api-sa
  namespace: logistics
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456:role/warehouse-api-role   # IAM role for pod
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pod-reader-global
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: monitoring-cluster-binding
subjects:
- kind: ServiceAccount
  name: prometheus-sa
  namespace: monitoring
roleRef:
  kind: ClusterRole
  name: pod-reader-global
  apiGroup: rbac.authorization.k8s.io
```

**ERCOT RBAC Model:**
- `platform-admin` ClusterRole — Full cluster access (only 3 people)
- `developer-role` Role — Namespace-scoped, no secret access
- `read-only-role` Role — Viewing only (for support teams)
- `cicd-role` Role — Deploy permissions for Jenkins service account
- Pod service accounts mapped to IAM roles via IRSA (IAM Roles for Service Accounts)

---

### Q6: How do you implement Kubernetes Network Policies?

**A:** Network Policies control pod-to-pod communication at the network level.

```yaml
# Deny all ingress/egress by default (security best practice)
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: logistics
spec:
  podSelector: {}    # Applies to all pods in namespace
  policyTypes:
  - Ingress
  - Egress
---
# Allow specific ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: warehouse-api-network-policy
  namespace: logistics
spec:
  podSelector:
    matchLabels:
      app: warehouse-api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:                    # Allow from ingress-nginx namespace
        matchLabels:
          name: ingress-nginx
    - podSelector:                          # Allow from other services in logistics namespace
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: database
    ports:
    - protocol: TCP
      port: 5432      # PostgreSQL
  - to:
    - namespaceSelector:
        matchLabels:
          name: kafka-system
    ports:
    - protocol: TCP
      port: 9092      # Kafka
  - to: []            # Allow DNS resolution
    ports:
    - protocol: UDP
      port: 53
    - protocol: TCP
      port: 53
```

**Amazon Robotics practice:** Used Calico CNI for network policies. Each microservice namespace had default-deny; allowed traffic only between specific services. This prevented lateral movement in case of container compromise.

---

### Q7: Explain ConfigMaps and Secrets. How do you manage them securely?

**A:**

**ConfigMap — non-sensitive configuration:**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: warehouse-config
  namespace: logistics
data:
  app.properties: |
    kafka.brokers=kafka-0.kafka-headless:9092,kafka-1.kafka-headless:9092
    redis.host=redis-master.cache
    log.level=INFO
    feature.flag.new-sorting=true
  KAFKA_TOPIC: warehouse-events
  MAX_RETRY_COUNT: "3"
```

**Secret — sensitive configuration (Base64 encoded at rest, encrypted in etcd):**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
  namespace: logistics
type: Opaque
data:
  username: d2FyZWhvdXNlX3VzZXI=   # base64 encoded
  password: U3VwZXJTZWNyZXQxMjM=   # base64 encoded
  url: amRiYzpvcmFjbGU6...          # base64 encoded JDBC URL
```

**Using in a Pod:**
```yaml
spec:
  containers:
  - name: app
    envFrom:
    - configMapRef:
        name: warehouse-config     # All configmap keys as env vars
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
    - name: secrets-volume
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: config-volume
    configMap:
      name: warehouse-config
  - name: secrets-volume
    secret:
      secretName: db-credentials
      defaultMode: 0400    # Read-only by owner only
```

**Secure Secrets Management at ERCOT/Amazon:**
```yaml
# Using AWS Secrets Manager with External Secrets Operator
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
  namespace: logistics
spec:
  refreshInterval: 1h           # Refresh from AWS Secrets Manager hourly
  secretStoreRef:
    name: aws-secretsmanager
    kind: ClusterSecretStore
  target:
    name: db-credentials
    creationPolicy: Owner
  data:
  - secretKey: password
    remoteRef:
      key: ercot/prod/db-credentials    # AWS Secrets Manager path
      property: password
  - secretKey: url
    remoteRef:
      key: ercot/prod/db-credentials
      property: connection-url
```

---

### Q8: How do you perform a rolling update and rollback in Kubernetes?

**A:**

```bash
# --- Deployment Update ---
# Update image (triggers rolling update)
kubectl set image deployment/warehouse-api \
  warehouse-api=123456.dkr.ecr.us-east-1.amazonaws.com/warehouse-api:2.2.0 \
  -n logistics

# Check rollout status
kubectl rollout status deployment/warehouse-api -n logistics
# Output: Waiting for deployment "warehouse-api" rollout to finish: 1 out of 3 new replicas have been updated...
# Output: deployment "warehouse-api" successfully rolled out

# View rollout history
kubectl rollout history deployment/warehouse-api -n logistics
# REVISION  CHANGE-CAUSE
# 1         Initial deployment v2.0.0
# 2         Updated to v2.1.0 - added caching
# 3         Updated to v2.2.0 - performance improvements

# --- Rollback ---
# Rollback to previous version
kubectl rollout undo deployment/warehouse-api -n logistics

# Rollback to specific revision
kubectl rollout undo deployment/warehouse-api --to-revision=1 -n logistics

# Pause rollout (if canary testing)
kubectl rollout pause deployment/warehouse-api -n logistics

# Resume rollout
kubectl rollout resume deployment/warehouse-api -n logistics
```

**Amazon Robotics CI/CD pipeline rollback script:**
```bash
#!/bin/bash
# automated-rollback.sh
DEPLOYMENT=$1
NAMESPACE=$2
HEALTH_ENDPOINT=$3

# Check deployment health after update
MAX_WAIT=300  # 5 minutes
INTERVAL=10
ELAPSED=0

while [ $ELAPSED -lt $MAX_WAIT ]; do
  HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $HEALTH_ENDPOINT)
  if [ $HTTP_STATUS -eq 200 ]; then
    echo "Deployment healthy - keeping new version"
    exit 0
  fi
  sleep $INTERVAL
  ELAPSED=$((ELAPSED + INTERVAL))
done

echo "Deployment unhealthy after ${MAX_WAIT}s - rolling back"
kubectl rollout undo deployment/$DEPLOYMENT -n $NAMESPACE
kubectl rollout status deployment/$DEPLOYMENT -n $NAMESPACE
```

---

### Q9: Explain Pod Disruption Budget (PDB) and why it matters.

**A:** PDB prevents voluntary disruptions from taking down too many pods at once, ensuring availability during node maintenance, cluster upgrades, etc.

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: warehouse-api-pdb
  namespace: logistics
spec:
  minAvailable: 2        # At least 2 pods must be available at all times
  # OR: maxUnavailable: 1  # At most 1 pod unavailable at a time
  selector:
    matchLabels:
      app: warehouse-api
```

**When PDB matters:**
- `kubectl drain node-1` — Moves pods off a node; PDB ensures graceful migration
- EKS node group updates — Kubernetes respects PDB before terminating pods
- Cluster upgrades — Control plane upgrades drain nodes; PDB prevents service disruption

**ERCOT practice:** Set `minAvailable: 2` for all production deployments with 3+ replicas. Saved us during EKS node group rolling update — Kubernetes respected PDB and only evicted pods after replacements were healthy.

---

### Q10: How do you implement Kubernetes Ingress and TLS termination?

**A:**

```yaml
# Install NGINX Ingress Controller (via Helm at Amazon Robotics)
# helm install ingress-nginx ingress-nginx/ingress-nginx \
#   --set controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-type"=nlb

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: warehouse-ingress
  namespace: logistics
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/rate-limit: "100"                   # 100 req/sec limit
    nginx.ingress.kubernetes.io/proxy-body-size: "10m"
    nginx.ingress.kubernetes.io/affinity: "cookie"                  # Sticky sessions
    cert-manager.io/cluster-issuer: "letsencrypt-prod"             # Auto TLS via cert-manager
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - warehouse-api.ercot.internal
    - logistics-api.ercot.internal
    secretName: ercot-tls-secret    # Contains TLS cert and key
  rules:
  - host: warehouse-api.ercot.internal
    http:
      paths:
      - path: /api/v1
        pathType: Prefix
        backend:
          service:
            name: warehouse-api-svc
            port:
              number: 80
      - path: /api/v2
        pathType: Prefix
        backend:
          service:
            name: warehouse-api-v2-svc
            port:
              number: 80
  - host: logistics-api.ercot.internal
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: logistics-api-svc
            port:
              number: 80
```

---

### Q11: How do you monitor a Kubernetes cluster? What tools do you use?

**A:**

**Stack used at Amazon Robotics and ERCOT:**
```
Prometheus (metrics collection)
  → Grafana (dashboards & alerting)
  → AlertManager (routing alerts to PagerDuty/Slack)
  → kube-state-metrics (K8s object metrics)
  → node-exporter (node-level metrics)
  → custom application metrics
```

**Prometheus deployment via Helm:**
```bash
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set prometheus.prometheusSpec.retention=15d \
  --set prometheus.prometheusSpec.storageSpec.volumeClaimTemplate.spec.resources.requests.storage=50Gi \
  --set grafana.adminPassword=$GRAFANA_ADMIN_PASSWORD \
  --set alertmanager.config.global.slack_api_url=$SLACK_WEBHOOK
```

**Key Prometheus Queries:**
```promql
# CPU utilization per pod
sum(rate(container_cpu_usage_seconds_total{namespace="logistics"}[5m])) by (pod)
  / sum(kube_pod_container_resource_limits{resource="cpu", namespace="logistics"}) by (pod) * 100

# Memory utilization
sum(container_memory_working_set_bytes{namespace="logistics"}) by (pod)
  / sum(kube_pod_container_resource_limits{resource="memory", namespace="logistics"}) by (pod) * 100

# Pod restart count (alerts when > 3 restarts in 1h)
increase(kube_pod_container_status_restarts_total{namespace="logistics"}[1h]) > 3

# Deployment replicas available vs desired
kube_deployment_status_replicas_available{namespace="logistics"}
  / kube_deployment_spec_replicas{namespace="logistics"} < 0.75

# P99 HTTP response time
histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket{namespace="logistics"}[5m])) by (le, service))
```

**Grafana Dashboard panels I built at ERCOT:**
1. Cluster overview — Node count, pod count, CPU/memory utilization
2. Namespace breakdown — Per-team resource consumption
3. Deployment health — Desired vs available replicas, restart count
4. Network traffic — Bytes in/out per pod
5. Kafka consumer lag — Per consumer group, per topic
6. Business metrics — API request rates, error rates, latency percentiles

---

### Q12: Explain Kubernetes Persistent Volumes (PV), PVC, and StorageClass.

**A:**

```yaml
# StorageClass — defines storage properties (used for dynamic provisioning)
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gp3-encrypted
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  iops: "3000"
  throughput: "125"
  encrypted: "true"
  kmsKeyId: "arn:aws:kms:us-east-1:123456:key/key-id"
reclaimPolicy: Retain       # Keep data even if PVC deleted
volumeBindingMode: WaitForFirstConsumer   # Wait until pod scheduled to provision
allowVolumeExpansion: true
---
# PersistentVolumeClaim — Application requests storage
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: kafka-data-kafka-0
  namespace: kafka-system
spec:
  accessModes:
  - ReadWriteOnce         # RWO: single node mount (EBS)
  # ReadWriteMany (EFS) for shared storage
  storageClassName: gp3-encrypted
  resources:
    requests:
      storage: 100Gi
---
# PersistentVolume — Static provisioning (rarely used with dynamic storage)
apiVersion: v1
kind: PersistentVolume
metadata:
  name: oracle-data-pv
spec:
  capacity:
    storage: 500Gi
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  csi:
    driver: ebs.csi.aws.com
    volumeHandle: vol-0123456789abcdef0   # Existing EBS volume
```

**Storage Access Modes:**
| Mode | Abbreviation | Supported By |
|---|---|---|
| ReadWriteOnce | RWO | EBS, local | Single node read/write |
| ReadOnlyMany | ROX | EFS, NFS | Multiple nodes read-only |
| ReadWriteMany | RWX | EFS, NFS, FSx | Multiple nodes read/write |

---

### Q13: How do you troubleshoot a pod that is in CrashLoopBackOff or Pending state?

**A:**

```bash
# --- Diagnose CrashLoopBackOff ---
# Step 1: Check pod events
kubectl describe pod warehouse-api-7d94f9-xk8j2 -n logistics
# Look for: OOMKilled, Exit Code 1, health check failures, image pull errors

# Step 2: Check container logs (current instance)
kubectl logs warehouse-api-7d94f9-xk8j2 -n logistics

# Step 3: Check previous container logs (before crash)
kubectl logs warehouse-api-7d94f9-xk8j2 -n logistics --previous

# Step 4: Exec into container for debugging (if it's running briefly)
kubectl exec -it warehouse-api-7d94f9-xk8j2 -n logistics -- /bin/sh

# --- Common CrashLoopBackOff Causes ---
# 1. OOMKilled → Increase memory limits
# 2. Exit Code 1 → Application startup failure → Check app logs
# 3. Liveness probe failure → Wrong path/port in probe → Fix probe config
# 4. Missing ConfigMap/Secret → Ensure dependencies exist
# 5. Permission denied → Check security context, PVC permissions

# --- Diagnose Pending Pod ---
kubectl describe pod pending-pod-xyz -n logistics
# Look for: Insufficient cpu, Insufficient memory, node selector mismatch, PVC not bound

# Check node resources
kubectl top nodes
kubectl describe node ip-10-0-1-100.us-east-1.compute.internal | grep -A 10 "Allocated resources"

# Check if PVC is bound
kubectl get pvc -n logistics
# STATUS: Pending → StorageClass issue, or no nodes in correct AZ

# Check taints that might prevent scheduling
kubectl get nodes -o json | jq '.items[].spec.taints'

# --- Fix Examples ---
# OOMKilled - increase memory limit
kubectl set resources deployment/warehouse-api \
  -c warehouse-api \
  --limits=memory=2Gi \
  -n logistics

# Force pod recreation on specific node
kubectl label node ip-10-0-1-100.compute.internal workload=cpu-intensive
# Add nodeSelector to pod spec
```

**Real incident at Amazon Robotics:** Warehouse API pods went CrashLoopBackOff at 6 AM. Checked logs — `OutOfMemoryError: GC overhead limit exceeded`. Root cause: Kafka consumer batching increased message size. Fix: Increased JVM heap size (`-Xmx1g` to `-Xmx2g`) and memory limits. Resolution in 8 minutes.

---

### Q14: What is Helm and how do you use it in production?

**A:** Helm is the package manager for Kubernetes — packages K8s manifests into reusable "Charts."

```bash
# Install a chart
helm install my-app ./charts/warehouse-app \
  --namespace logistics \
  --values ./environments/prod/values.yaml \
  --set image.tag=2.1.0 \
  --set replicaCount=3 \
  --atomic        # Roll back if install fails
  --timeout 5m

# Upgrade a release
helm upgrade my-app ./charts/warehouse-app \
  --namespace logistics \
  --values ./environments/prod/values.yaml \
  --set image.tag=2.2.0 \
  --reuse-values   # Reuse previously set values
  --atomic

# Rollback to previous release
helm rollback my-app 1 -n logistics

# List releases
helm list -n logistics
helm history my-app -n logistics
```

**Helm Chart structure (Amazon Robotics standard):**
```
warehouse-app/
├── Chart.yaml              # Chart metadata
├── values.yaml             # Default values
├── environments/
│   ├── dev/values.yaml     # Dev overrides
│   ├── staging/values.yaml
│   └── prod/values.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── configmap.yaml
    ├── hpa.yaml
    ├── pdb.yaml
    ├── ingress.yaml
    ├── networkpolicy.yaml
    └── NOTES.txt           # Post-install instructions
```

**values.yaml pattern:**
```yaml
# values.yaml
replicaCount: 1
image:
  repository: 123456.dkr.ecr.us-east-1.amazonaws.com/warehouse-api
  tag: latest
  pullPolicy: IfNotPresent
resources:
  requests:
    cpu: 100m
    memory: 256Mi
  limits:
    cpu: 500m
    memory: 1Gi
autoscaling:
  enabled: false
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70

# prod/values.yaml overrides
replicaCount: 3
image:
  tag: "2.1.0"
autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 20
resources:
  limits:
    cpu: "2"
    memory: 4Gi
```

---

## SECTION 2: KUBERNETES OPERATIONS

---

### Q15: How do you perform a Kubernetes cluster upgrade?

**A:**

**EKS Managed Cluster Upgrade (used at ERCOT and Amazon Robotics):**
```bash
# Step 1: Review release notes for breaking changes
# Check: https://kubernetes.io/releases/notes/

# Step 2: Update control plane first
aws eks update-cluster-version \
  --name ercot-prod-cluster \
  --kubernetes-version 1.29 \
  --region us-east-1

# Monitor upgrade
aws eks describe-cluster --name ercot-prod-cluster \
  --query cluster.status

# Step 3: Update managed node groups (one at a time)
aws eks update-nodegroup-version \
  --cluster-name ercot-prod-cluster \
  --nodegroup-name workers-az1 \
  --kubernetes-version 1.29

# Step 4: Update add-ons (CoreDNS, kube-proxy, vpc-cni)
aws eks update-addon \
  --cluster-name ercot-prod-cluster \
  --addon-name kube-proxy \
  --addon-version v1.29.0-eksbuild.1

# Step 5: Verify all pods healthy after upgrade
kubectl get pods -A | grep -v Running | grep -v Completed
kubectl rollout status ds/aws-node -n kube-system   # VPC CNI daemonset
```

**Pre-upgrade checklist:**
1. Review K8s changelog for deprecated API versions
2. Run `kubectl convert` to migrate deprecated YAML manifests
3. Test upgrade in staging cluster first
4. Verify PodDisruptionBudgets are configured
5. Ensure backups of etcd are taken
6. Communicate maintenance window to stakeholders

---

### Q16: How do you handle Kubernetes node failures and draining?

**A:**

```bash
# Cordon a node — prevent new pods from scheduling
kubectl cordon node-ip-10-0-1-100.us-east-1.compute.internal

# Drain a node — evict all pods (respects PDB)
kubectl drain node-ip-10-0-1-100.us-east-1.compute.internal \
  --ignore-daemonsets \           # Skip daemonset pods (they can't be moved)
  --delete-emptydir-data \        # Delete pods with emptyDir volumes
  --grace-period=120 \            # Give 2 minutes for graceful shutdown
  --timeout=300s                  # Fail after 5 minutes

# If PDB is blocking drain (emergency)
kubectl drain ... --disable-eviction=true  # Bypasses PDB (use carefully)

# Uncordon after maintenance
kubectl uncordon node-ip-10-0-1-100.us-east-1.compute.internal

# Replace a failed node (EKS)
# 1. Identify failed node
kubectl get nodes | grep NotReady

# 2. Terminate EC2 instance (Auto Scaling Group launches replacement)
aws ec2 terminate-instances --instance-ids i-0123456789abcdef0

# 3. Monitor replacement node joining cluster
kubectl get nodes --watch
```

---

## SECTION 3: KUBERNETES SECURITY

---

### Q17: How do you secure a Kubernetes cluster in production?

**A:** Layered security approach:

**1. API Server Security:**
```bash
# Use IRSA (IAM Roles for Service Accounts) instead of EC2 instance profiles
eksctl create iamserviceaccount \
  --name warehouse-api-sa \
  --namespace logistics \
  --cluster ercot-prod-cluster \
  --attach-policy-arn arn:aws:iam::123456:policy/warehouse-api-policy \
  --approve

# Enable audit logging
aws eks update-cluster-config \
  --name ercot-prod-cluster \
  --logging '{"clusterLogging":[{"types":["api","audit","authenticator"],"enabled":true}]}'
```

**2. Pod Security Standards:**
```yaml
# Enforce restricted security context
apiVersion: v1
kind: Namespace
metadata:
  name: logistics
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
---
# Pod with restrictive security context
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
    volumeMounts:
    - name: tmp                   # Writable temp directory (since root FS is read-only)
      mountPath: /tmp
  volumes:
  - name: tmp
    emptyDir: {}
```

**3. Container Image Security:**
```yaml
# ECR image scanning + admission webhook
# Only allow images from approved ECR registry
# Enforce image tag (no :latest in production)
# CVE scanning in CI/CD pipeline before push
```

**4. etcd Encryption:**
```yaml
# Enable encryption of secrets at rest in etcd
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
- resources:
  - secrets
  providers:
  - aescbc:
      keys:
      - name: key1
        secret: <base64-encoded-32-byte-key>
  - identity: {}
```

**Security checklist I follow at ERCOT:**
- ✅ IRSA for pod AWS permissions (no static credentials)
- ✅ Network policies with default-deny
- ✅ Pod Security Standards (restricted namespace)
- ✅ Read-only root filesystems for all containers
- ✅ ECR image scanning in CI/CD; block if critical CVEs
- ✅ RBAC with least-privilege roles
- ✅ etcd encryption at rest
- ✅ Audit logging to CloudWatch
- ✅ Secrets via External Secrets Operator from AWS Secrets Manager
- ✅ Regular security scans with kube-bench (CIS benchmark)

---

### Q18: What is the difference between requests and limits in Kubernetes? Why are they important?

**A:**

- **Requests** — Minimum guaranteed resources; used for scheduling decisions
- **Limits** — Maximum resources a container can use; enforced by cgroups

```yaml
resources:
  requests:
    cpu: "250m"         # 0.25 CPU cores guaranteed
    memory: "512Mi"     # 512MB guaranteed
  limits:
    cpu: "1000m"        # 1 CPU core max (throttled if exceeded)
    memory: "1Gi"       # 1GB max (OOMKilled if exceeded)
```

**Quality of Service (QoS) Classes:**
| Class | Condition | Eviction Priority |
|---|---|---|
| **Guaranteed** | requests == limits for all containers | Last to be evicted |
| **Burstable** | requests < limits (or only one set) | Middle priority |
| **BestEffort** | No requests or limits set | First to be evicted (avoid in prod) |

**Production guidelines (Amazon Robotics standard):**
- Always set requests and limits for production workloads
- Never set limits to equal requests for Java apps (JVM needs burst memory for GC)
- Start with CPU limit = 2x request; monitor with VPA recommendations
- Use `LimitRange` to enforce defaults per namespace
- Set memory limits = 1.5x requests for Java, 1.2x for Go/Node.js

```yaml
# LimitRange — enforce resource defaults in namespace
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: logistics
spec:
  limits:
  - default:         # Default limits if not specified
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:  # Default requests if not specified
      cpu: "100m"
      memory: "256Mi"
    max:             # Maximum allowed
      cpu: "4"
      memory: "8Gi"
    min:             # Minimum required
      cpu: "50m"
      memory: "64Mi"
    type: Container
```

---

## SECTION 4: KUBERNETES INTERVIEW RAPID-FIRE

---

### Q19: What happens when you run `kubectl apply -f deployment.yaml`?

**A:**
1. `kubectl` sends HTTP POST/PATCH request to kube-apiserver
2. kube-apiserver authenticates/authorizes the request
3. Admission controllers validate/mutate the request
4. Object stored in etcd
5. kube-controller-manager detects desired state differs from actual (via watch)
6. Deployment controller creates/updates ReplicaSet
7. ReplicaSet controller creates pods
8. kube-scheduler assigns pods to nodes
9. kubelet on selected node pulls image and starts container
10. Container is running and reports status back to kubelet → kube-apiserver → etcd

---

### Q20: What is the difference between `kubectl apply` vs `kubectl create` vs `kubectl replace`?

**A:**
- `kubectl create` — Imperative; fails if object already exists
- `kubectl apply` — Declarative; creates if not exists, updates if exists (stores last-applied-configuration annotation) — **use this in production**
- `kubectl replace` — Replaces entire object; fails if doesn't exist; does NOT apply partial updates
- `kubectl patch` — Applies partial updates using JSON/YAML merge patch

---

### Q21: Explain etcd backup and restore.

**A:**
```bash
# Backup etcd (run on control plane node)
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /backup/etcd-snapshot-$(date +%Y%m%d-%H%M%S).db

# Verify snapshot
ETCDCTL_API=3 etcdctl snapshot status /backup/etcd-snapshot.db

# Restore etcd
ETCDCTL_API=3 etcdctl snapshot restore /backup/etcd-snapshot.db \
  --data-dir=/var/lib/etcd-restored \
  --name master-1 \
  --initial-cluster master-1=https://127.0.0.1:2380 \
  --initial-cluster-token etcd-cluster-new \
  --initial-advertise-peer-urls https://127.0.0.1:2380
```
**For EKS** — AWS manages etcd; backup via automated snapshots; for disaster recovery, recreate cluster and use GitOps to redeploy workloads.

---

*File: 16-Kubernetes-Cloud-Engineer-Complete.md | Created: June 2026 | Role: Sr Cloud Platform Engineer*

