Q1: What technologies have you worked with?

A1: Yes, I have worked with Docker, Kubernetes, and Amazon Robotics. These are part of the microservices architecture I have worked on.

Q2: Can you explain the concept of microservices?

A2: Microservices refer to a service-oriented architecture where applications are built as independent, small services that can be deployed and scaled independently. The benefits of microservices include single responsibility, loose coupling, asynchronous communication, data ownership, scalability, failure design, security, and logging. These benefits help create resilient and maintainable systems.

Q3: What are the core principles of designing microservices?

A3: The core principles of microservices are:

Single Responsibility Principle: Each microservice should have one well-defined purpose, making it easier to understand, deploy, and maintain.
Loose Coupling: Microservices should have minimal dependencies on each other, allowing independent development, deployment, and scaling.
Asynchronous Communication: Microservices communicate asynchronously to ensure better scalability and decoupling.
Data Ownership: Each service should own and manage its own data.
Scalability: Microservices should be scalable independently based on demand.
Q4: How do you ensure the security of microservices?

A4: We implement security in microservices by focusing on security by design. We use access and identity tokens for secure service-to-service communication and implement defense in depth with encryption, API gateway, container security, and robust logging. We also implement least privilege access, centralized identity management, and multi-layer security controls throughout the development lifecycle.

Q5: How does the API Gateway handle authentication and authorization?

A5: The API Gateway acts as the entry point for all incoming requests. It authenticates requests before forwarding them to the respective microservices. We use OAuth 2.0 for authentication and JWT for validating the token, ensuring that it contains user-specific information, permissions, and rules. If the token is valid, the request is forwarded to the appropriate microservice; otherwise, access is denied.

Q6: How do you manage microservices with Spring Boot?

A6: In Spring Boot, we create separate microservices for various functionalities, such as security services, which connect to the API Gateway. We use Spring Boot's @ControllerAdvice for exception handling, and for database connections, we use MongoDB repositories for NoSQL data and JPA repositories for relational databases.

Q7: Can you explain how Kafka is used for messaging between microservices?

A7: Kafka is used for asynchronous messaging between microservices. We configure Kafka Producer in one service to publish messages to a Kafka topic and Kafka Consumer in another service to consume these messages. The Kafka template simplifies interaction with Kafka topics, and we handle failures using retry policies or dead letter queues for unprocessable messages.

Q8: How do you handle failures in microservices communication?

A8: We handle failures through several mechanisms:

Retry Mechanism: We use Spring Retry or Kafka's built-in retry mechanism to handle temporary failures.
Dead Letter Queues (DLQ): Messages that fail to process are redirected to a DLQ for manual intervention or automatic reprocessing.
Logging and Monitoring: We use tools like ELK stack, Prometheus, and Grafana to monitor and track Kafka messages and system failures.
Q9: What is the process for handling service failures and auto-recovery in microservices?

A9: For service failures and auto-recovery, we use:

Failure Detection: We use service check mechanisms to detect failure.
Auto Restart: If a service crashes, we use system configurations (like Docker or Kubernetes auto-restart policies) to automatically restart the service.
Q10: How do you manage microservices in Docker and Kubernetes?

A10: To deploy microservices with Docker, we use Dockerfiles to set up the application environment and deploy it within containers. For Kubernetes, we use kubectl commands to deploy microservices, create Kubernetes deployment and service YAML files, and connect to AWS ECR for container image storage. We use horizontal pod auto-scaling to handle increased traffic by scaling pods based on CPU and memory usage.

Q11: How do you manage microservices on Amazon EKS (Elastic Kubernetes Service)?

A11: To deploy microservices on Amazon EKS, we authenticate Docker with ECR, build and push Docker images, and use kubectl to create an EKS cluster. We then apply Kubernetes manifests (like deployment and service YAML files) to deploy the services and access them via load balancers. We verify the deployment using kubectl get pods and kubectl get services.

Q12: How do you handle replication and scaling in Kubernetes?

A12: Kubernetes provides auto-scaling through the Horizontal Pod Autoscaler (HPA), which automatically scales the number of pods based on CPU and memory usage. The scaling happens automatically when there is an increase in traffic or load on the application.
