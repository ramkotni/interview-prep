Java and Spring Framework
Q: What are the key features introduced in Java 8?
A: Key features include:


Lambda expressions
Stream API
Functional interfaces
Default and static methods in interfaces
Optional class
New Date and Time API
Method references
Q: Explain the difference between @Component, @Service, @Repository, and @Controller in Spring.
A: All are stereotypes in Spring:


@Component: Generic stereotype for any Spring-managed component.
@Service: Specialization of @Component for service layer logic.
@Repository: Specialization of @Component for DAO (Data Access Object) layer, with exception translation.
@Controller: Specialization of @Component for handling web requests in MVC.
Q: How does Spring Boot simplify application development?
A: Spring Boot simplifies development by:


Providing auto-configuration
Embedding servers like Tomcat/Jetty
Offering starter dependencies
Simplifying configuration with application.properties or application.yml
Q: What is the difference between @RestController and @Controller in Spring?
A: @RestController is a combination of @Controller and @ResponseBody, used for RESTful web services. @Controller is used for traditional MVC applications.


<hr></hr>
Microservices and REST API
Q: What are the key principles of microservices architecture?
A: Key principles include:


Decentralized governance
Independent deployment
Scalability
Loose coupling
Domain-driven design
Resilience and fault tolerance
Q: How do you handle inter-service communication in microservices?
A: Common approaches include:


Synchronous communication using REST or gRPC
Asynchronous communication using message brokers like RabbitMQ or Kafka
Q: What is the purpose of API Gateway in microservices?
A: API Gateway acts as a single entry point for clients, handling:


Request routing
Load balancing
Authentication and authorization
Rate limiting
Protocol translation
<hr></hr>
ORM Frameworks
Q: What is the difference between JPA and Hibernate?
A: JPA is a specification for ORM, while Hibernate is an implementation of JPA. Hibernate provides additional features like caching, custom SQL, and more.


Q: How does Hibernate manage caching?
A: Hibernate supports:


First-level cache (session-level, enabled by default)
Second-level cache (shared across sessions, requires configuration with providers like Ehcache)
<hr></hr>
Docker and Kubernetes
Q: What is the difference between Docker and Kubernetes?
A: Docker is a containerization platform, while Kubernetes is an orchestration tool for managing containers at scale.


Q: How do you scale applications in Kubernetes?
A: Applications can be scaled using:


Horizontal Pod Autoscaler (HPA)
Manually increasing the number of replicas in a deployment
<hr></hr>
UI Frameworks
Q: What are the key differences between Angular and React?
A:


Angular is a full-fledged framework, while React is a library.
Angular uses TypeScript, while React uses JavaScript/JSX.
Angular has two-way data binding, while React uses one-way data binding.
Q: How does Angular handle dependency injection?
A: Angular uses a hierarchical dependency injection system with providers defined in modules, components, or services.


<hr></hr>
AWS and Cloud
Q: What are the key AWS services you have worked with?
A: Common services include:


EC2 for compute
S3 for storage
IAM for access control
Lambda for serverless computing
Q: How do you secure AWS resources?
A: By:


Using IAM roles and policies
Enabling encryption (e.g., S3 bucket encryption)
Setting up VPCs and security groups
Enabling CloudTrail for auditing
<hr></hr>
DevOps
Q: How does Jenkins fit into a CI/CD pipeline?
A: Jenkins automates build, test, and deployment processes, integrating with tools like Git, Maven, and Docker.


Q: What is the purpose of an artifact repository like Artifactory?
A: It stores build artifacts (e.g., JARs, WARs) for versioning and reuse in deployments.


<hr></hr>
Additional Topics
Q: What is OAuth, and how does it work?
A: OAuth is an authorization framework that allows third-party applications to access resources on behalf of a user without sharing credentials. It uses access tokens for secure communication.


Q: What is the ELK stack, and how is it used?
A: ELK stands for Elasticsearch, Logstash, and Kibana. It is used for log aggregation, analysis, and visualization.


Q: How do you implement message queues in a distributed system?
A: By using tools like RabbitMQ or Kafka to decouple services, ensure asynchronous communication, and handle message persistence.


<hr></hr>
Soft Skills
Q: How do you handle learning new technologies?
A: By:


Exploring official documentation
Practicing hands-on projects
Participating in online courses or communities
Q: How do you ensure collaboration in a team?
A: By:
Communicating effectively
Participating in code reviews
Sharing knowledge and mentoring juniors
