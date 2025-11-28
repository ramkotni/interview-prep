1. Dockerize the Application
a. Dockerize Spring Boot (Backend)

Create a Dockerfile in the Spring Boot project:

# Build stage
FROM maven:3.9.2-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Run stage
FROM eclipse-temurin:17-jdk
WORKDIR /app
COPY --from=build /app/target/demo-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]


Build image:

docker build -t task-backend:1.0 .


Run container locally:

docker run -p 8080:8080 task-backend:1.0

b. Dockerize Angular (Frontend)

Create a Dockerfile in the Angular project:

# Build stage
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build --prod

# Serve stage
FROM nginx:alpine
COPY --from=build /app/dist/task-app /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


Build image:

docker build -t task-frontend:1.0 .


Run container locally:

docker run -p 4200:80 task-frontend:1.0

c. Kafka using Docker

Use Docker Compose for Kafka & Zookeeper:

version: '3.8'
services:
  zookeeper:
    image: wurstmeister/zookeeper:3.4.6
    ports:
      - "2181:2181"

  kafka:
    image: wurstmeister/kafka:2.13-2.7.0
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: localhost
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181


Start with:

docker-compose up -d

2. Kubernetes Deployment
a. Create Kubernetes manifests
Backend Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: task-backend:1.0
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: backend-service
spec:
  selector:
    app: backend
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
  type: ClusterIP

Frontend Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: task-frontend:1.0
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  selector:
    app: frontend
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer

Kafka Deployment (optional for K8s)

Usually use Strimzi operator for Kafka in Kubernetes for production.

For simple dev setup, you can deploy the Docker Compose Kafka using K8s pods & services.

b. Apply manifests
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml


Check pods:

kubectl get pods


Check services:

kubectl get svc

3. Summary Flow of Deployment Task
Step	Action
Dockerize Backend	Create Dockerfile, build & run Spring Boot image
Dockerize Frontend	Create Dockerfile, build Angular, serve via Nginx
Kafka	Run Kafka & Zookeeper via Docker Compose or K8s
Kubernetes Deployment	Create Deployment + Service YAMLs for backend & frontend
Apply & Verify	kubectl apply -f ..., check pods & services
Access App	Frontend via LoadBalancer IP/NodePort → REST API calls backend → Kafka events handled by consumer

✅ Key points to explain in interview

Docker allows packaging each component independently.

Kubernetes enables scaling (replicas) and service discovery.

Backend communicates with Kafka cluster for event-driven architecture.

Frontend communicates with backend via Service URL.

Shows real-world microservices deployment workflow.
