# DOCKER & KUBERNETES - COMPREHENSIVE INTERVIEW Q&A

## Expert Level Q&A | Production Experience

---

## Q1: Docker Fundamentals

**A:** Docker containerizes applications for consistent deployment.

### Dockerfile Example (Multi-stage Build):
```dockerfile
# Stage 1: Build
FROM maven:3.8-openjdk-17 AS builder
WORKDIR /build
COPY . .
RUN mvn clean package -DskipTests

# Stage 2: Runtime
FROM openjdk:17-jdk-slim
WORKDIR /app

# Copy jar from builder
COPY --from=builder /build/target/app.jar app.jar

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

# Environment
ENV JAVA_OPTS="-Xms256m -Xmx512m -XX:+UseG1GC"

# Expose port
EXPOSE 8080

# Run
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

### Build and Run:
```bash
# Build image
docker build -t myapp:1.0 -f Dockerfile .

# Run container
docker run -d \
  --name myapp-container \
  -p 8080:8080 \
  -e DB_URL=jdbc:mysql://db-host:3306/mydb \
  -e JAVA_OPTS="-Xms256m -Xmx512m" \
  myapp:1.0

# View logs
docker logs -f myapp-container

# Execute command in container
docker exec -it myapp-container bash
```

### Docker Compose (Multiple Services):
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - DB_URL=jdbc:mysql://mysql:3306/mydb
      - JAVA_OPTS=-Xms256m -Xmx512m
    depends_on:
      - mysql
    networks:
      - mynetwork

  mysql:
    image: mysql:8.0
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=root123
      - MYSQL_DATABASE=mydb
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - mynetwork

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - mynetwork

volumes:
  mysql-data:
  redis-data:

networks:
  mynetwork:
    driver: bridge
```

### Container Registry:
```bash
# Login to registry
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag myapp:1.0 123456.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0

# Push to registry
docker push 123456.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0

# Pull image
docker pull 123456.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0
```

---

## Q2: Kubernetes Fundamentals

**A:** Orchestrates containers across clusters.

### Core Concepts:

**Pod:** Smallest unit, contains 1+ containers
**Deployment:** Manages pod replicas
**Service:** Exposes pods to network
**ConfigMap:** Environment configuration
**Secret:** Sensitive data (encrypted)
**PersistentVolume:** Storage across pods

### Deployment Manifest:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0    # Zero-downtime deployment
  
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: myregistry/my-app:1.0
        imagePullPolicy: IfNotPresent
        
        ports:
        - containerPort: 8080
          name: http
        - containerPort: 9090
          name: metrics
        
        env:
        - name: JAVA_OPTS
          value: "-Xms256m -Xmx512m"
        - name: DB_URL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: db_url
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: db_password
        
        # Health checks
        livenessProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        
        readinessProbe:
          httpGet:
            path: /actuator/health/readiness
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
          failureThreshold: 3
        
        # Resource limits
        resources:
          requests:
            cpu: 250m
            memory: 512Mi
          limits:
            cpu: 500m
            memory: 1Gi
        
        volumeMounts:
        - name: logs
          mountPath: /var/log/app
      
      volumes:
      - name: logs
        emptyDir: {}

---
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
  namespace: production
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  db_url: "jdbc:mysql://mysql-svc:3306/mydb"
  app_env: "production"

---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
stringData:
  db_password: "SecurePassword123"
  api_key: "secret-api-key"
```

### kubectl Commands:
```bash
# Check deployments
kubectl get deployments -n production
kubectl get pods -n production
kubectl get services -n production

# View pod logs
kubectl logs -f deployment/my-app -n production

# Scale deployment
kubectl scale deployment my-app --replicas=5 -n production

# Update image
kubectl set image deployment/my-app \
  my-app=myregistry/my-app:2.0 \
  -n production

# Check rollout
kubectl rollout status deployment/my-app -n production

# Rollback if needed
kubectl rollout undo deployment/my-app -n production

# Port forward for testing
kubectl port-forward svc/my-app-service 8080:80 -n production

# Execute in pod
kubectl exec -it pod/my-app-xyz -- bash

# Check resource usage
kubectl top nodes
kubectl top pods -n production

# Debug pod
kubectl describe pod pod-name -n production
kubectl logs pod-name -n production --previous  # Previous restart
```

---

## Q3: Kubernetes Best Practices

✅ **High Availability:**
- Multi-replica deployments
- Pod Disruption Budgets
- Anti-affinity rules for spread

✅ **Resource Management:**
- Set requests and limits
- Use namespaces to isolate workloads
- Configure resource quotas

✅ **Security:**
- Network policies
- RBAC (Role-Based Access Control)
- Pod security policies
- Secrets encryption

✅ **Monitoring:**
- Prometheus for metrics
- Liveness/readiness probes
- Resource monitoring
- Log aggregation

---

## Q4: Service Mesh (Optional, Advanced)

**Istio** adds traffic management, security, and observability:

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: my-app
spec:
  hosts:
  - my-app
  http:
  - match:
    - uri:
        prefix: "/v2"
    route:
    - destination:
        host: my-app
        subset: v2
  - route:
    - destination:
        host: my-app
        subset: v1
---
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: my-app
spec:
  host: my-app
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 100
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
```

---

**Last Updated:** May 8, 2026


