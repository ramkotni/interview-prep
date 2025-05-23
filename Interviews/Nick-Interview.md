# Important Questions and Answers for Interview Preparation

## Spring Boot

| **Question**                                           | **Answer**                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is Spring Boot?**                               | Spring Boot is a framework that simplifies the setup and development of Spring-based applications. It offers production-ready features like embedded servers, health checks, and metrics without requiring a lot of configuration.                                                       |
| **What is Lazy Loading in Spring Boot?**               | Lazy loading in Spring Boot is when beans are not loaded until they are requested. This reduces memory usage and startup time, particularly useful for large applications with many beans.                                                                                           |
| **How can you change server configuration in Spring Boot if you don't need Tomcat?** | You can exclude Tomcat and configure an alternative server like Jetty or Undertow by modifying the `pom.xml` or `build.gradle` file, using the following code snippet: `<dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-web</artifactId><exclusions><exclusion><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-tomcat</artifactId></exclusion></exclusions></dependency>` |
| **What is @Qualifier in Spring Boot?**                 | `@Qualifier` is used to resolve ambiguity when multiple beans of the same type are present. It specifies which bean to inject into the class when using `@Autowired`.                                                                                                              |
| **What is @Bean in Spring Boot?**                       | `@Bean` is used to declare a Spring bean in a configuration class. It helps define custom beans, which Spring will manage and add to the application context.                                                                                                                     |
| **What is Spring Boot AutoConfiguration?**              | AutoConfiguration in Spring Boot is a mechanism that automatically configures application beans based on the classpath and the properties in `application.properties`. This allows you to avoid explicit configuration for common use cases.                                           |
| **What is @SpringBootApplication annotation?**          | `@SpringBootApplication` is a convenience annotation that combines `@Configuration`, `@EnableAutoConfiguration`, and `@ComponentScan` in one. It marks the main class of a Spring Boot application and enables auto-configuration and component scanning.                           |
| **What is Actuator in Spring Boot?**                    | Spring Boot Actuator provides production-ready features like health checks, metrics, and application information. It helps monitor and manage applications. The `/actuator` endpoints can expose various metrics like health, environment, etc.                                        |
| **How do you configure logging in Spring Boot?**        | Spring Boot uses `logback` by default for logging. You can configure logging using `application.properties` or `application.yml` with properties like `logging.level`, `logging.file`, or `logging.pattern.console`.                                                              |

---

## Kafka

| **Question**                                           | **Answer**                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is Kafka?**                                      | Apache Kafka is a distributed streaming platform that is used for building real-time data pipelines and streaming applications. It allows for fault-tolerant, high-throughput messaging between systems.                                                                          |
| **What is the difference between Kafka and RabbitMQ?**   | Kafka is designed for high throughput, fault tolerance, and stream processing, whereas RabbitMQ is more of a message broker designed for message queuing with a focus on message delivery guarantees. Kafka is more suited for real-time analytics and data pipelines.                 |
| **What is Offset in Kafka?**                           | The offset in Kafka is a unique identifier for each message within a partition. Kafka consumers use offsets to track their position in a partition, ensuring that they can resume reading from the correct point in case of a failure.                                                 |
| **What is Zookeeper in Kafka?**                         | Zookeeper is a distributed coordination service used by Kafka to manage metadata, broker configurations, topic partitions, and leader elections. It ensures high availability and consistency within Kafka clusters.                                                             |
| **Why is Replication required in Kafka?**              | Replication ensures fault tolerance in Kafka. By replicating data across multiple brokers, Kafka guarantees that if a broker fails, another broker with a replica of the data will take over, ensuring no data loss and high availability.                                           |
| **What is Kafka Producer and Consumer?**                | A **Kafka Producer** sends messages to Kafka topics, while a **Kafka Consumer** reads messages from Kafka topics. Producers and consumers are the key components that interact with Kafka to provide message-driven applications.                                               |
| **What is a Kafka Broker?**                             | A Kafka broker is a server that stores messages, receives and sends data to clients (producers/consumers), and ensures data durability and availability by managing topic partitions and replicas.                                                                                     |
| **What is a Kafka Topic?**                              | A Kafka topic is a category to which messages are sent. Producers write to topics, and consumers read from topics. Topics can be partitioned for parallel processing.                                                                                                              |
| **What is the role of Consumer Group in Kafka?**        | A Kafka consumer group consists of multiple consumers that divide the load of reading messages from topics. Each consumer in the group reads from a different partition to parallelize the work. Consumer groups help Kafka scale horizontally.                                       |

# Kafka - Leader and Follower

## Question: What is the role of Leader and Follower in Kafka?

### **Answer:**

In Kafka, **Leader** and **Follower** refer to the roles assigned to the replicas of a Kafka **Partition**. Each partition has one leader and one or more followers, and their roles are crucial for data replication, availability, and fault tolerance.

### **Leader:**
- **Role**: The leader is the Kafka broker responsible for handling all **reads** and **writes** for a specific partition.
- **Responsibilities**:
  - The leader is the **only broker** that allows **producers** to write data to the partition.
  - It serves data when **consumers** request messages from that partition.
  - The leader coordinates the replication process to ensure all **follower replicas** are synchronized with it.
  - It keeps track of the latest offset (position) of the partition and responds with the correct data to consumers.

### **Follower:**
- **Role**: Followers are Kafka brokers that replicate data from the leader to ensure **fault tolerance** and **data availability**.
- **Responsibilities**:
  - Followers do not handle read or write requests directly. They simply replicate data from the leader.
  - They periodically fetch the latest data from the leader to maintain an up-to-date copy of the partition.
  - If the leader fails, one of the followers is elected to become the new leader through a process called **leader election**.
  - Followers must stay in sync with the leader to ensure data consistency. If a follower falls too far behind, it might be removed from replication.

### **How Leader and Follower Work Together:**
1. **Replication**: Each Kafka partition can have multiple replicas. One replica is the leader, and the rest are followers. The leader handles all write operations and serves as the point of contact for consumers.
2. **Fault Tolerance**: If the leader broker fails, one of the followers automatically takes over as the new leader. This ensures that Kafka remains available with minimal downtime.
3. **Consistency**: Kafka ensures that once a message is written to the partition, it is replicated to the followers. As long as the majority of replicas (including the leader) have the message, it is considered committed and available to consumers.

### Example Scenario:
- Imagine a Kafka topic with one partition (`p1`), and this partition is replicated across three brokers.
  - Broker 1 holds the **leader** replica.
  - Broker 2 and Broker 3 hold the **follower** replicas.
- Producers send messages to Broker 1 (the **leader**).
- Consumers can read from Broker 1 (the **leader**). If Broker 1 goes down, either Broker 2 or Broker 3 (the **followers**) will take over as the new leader, and consumers can still read data from them.

### **Why is this Important?**
- **Leader**: Ensures data consistency and coordinates the replication process.
- **Follower**: Ensures high availability and fault tolerance. If the leader fails, one of the followers can take over, minimizing downtime.




---

## Kubernetes

| **Question**                                           | **Answer**                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is Kubernetes?**                                | Kubernetes is an open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications across clusters of hosts.                                                                                                 |
| **What is the difference between a Pod and a Container?** | A **Pod** is a group of one or more containers sharing the same storage and network resources. A **Container** is an isolated environment for running an application, while Pods are used to manage and scale containers in a Kubernetes environment.                              |
| **What is the command to see all the pods?**            | `kubectl get pods` shows all the pods in the current namespace. To see all pods across all namespaces, use `kubectl get pods --all-namespaces`.                                                                                                                                     |
| **Which environment is used for Kubernetes?**          | Kubernetes can run in various environments such as on-premise data centers, public cloud platforms (AWS, GCP, Azure), or local development environments like Minikube.                                                                                                            |
| **Explain about Docker and Kubernetes**                | **Docker** is a tool for packaging and running applications in containers, providing isolation. **Kubernetes** is an orchestration platform that automates the deployment, scaling, and management of Docker containers in a distributed environment.                           |
| **What is a Kubernetes Deployment?**                   | A **Deployment** in Kubernetes provides declarative updates to applications. It allows you to define the desired state for Pods and automatically manages changes such as scaling, rolling updates, and rollback.                                                               |
| **What is the role of a Kubernetes Service?**          | A **Kubernetes Service** exposes a set of Pods as a network service, providing load balancing and stable networking to access Pods, even if their IP addresses change.                                                                                                            |
| **What is Kubernetes ConfigMap?**                      | A **ConfigMap** in Kubernetes is used to store configuration data, such as environment variables or command-line arguments, which can be used by Pods in your application.                                                                                                           |
| **What is Kubernetes Ingress?**                        | **Ingress** is an API object in Kubernetes that manages external access to services, typically HTTP. It allows you to define rules to route traffic from outside the cluster to specific services.                                                                                  |

---

## Docker

| **Question**                                           | **Answer**                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is Docker?**                                     | Docker is an open-source platform for automating the deployment of applications inside lightweight, portable containers. Docker helps in packaging an application with all its dependencies into a standardized unit.                                                              |
| **What is Docker Compose?**                             | Docker Compose is a tool for defining and running multi-container Docker applications. Using a `docker-compose.yml` file, you can define the services, networks, and volumes needed for your app and start them with a single command.                                                |
| **What is Dockerfile?**                                 | A **Dockerfile** is a text document that contains all the instructions to build a Docker image. It defines the environment and instructions to install dependencies, copy files, and run commands in the container.                                                                  |
| **What is a Docker Image?**                             | A Docker **image** is a lightweight, stand-alone, and executable package that includes everything needed to run an application, such as code, libraries, environment variables, and runtime.                                                                                       |
| **What is Docker Hub?**                                 | **Docker Hub** is a cloud-based registry for sharing Docker images. It allows developers to upload and download container images for easy reuse. It can be used to pull official images or push custom images.                                                                 |
| **What is the Docker Registry?**                        | The Docker **Registry** is a service where Docker images are stored and can be pulled for use. Docker Hub is the default public registry, but you can set up your own private registry.                                                                                            |
| **What is Docker Networking?**                          | Docker Networking enables communication between Docker containers. By default, containers are isolated from each other, but they can be connected via networks to communicate. There are several network modes, including bridge, host, and overlay.                                |
| **What is the difference between a Docker container and a Docker image?** | A **Docker image** is a read-only template that contains a set of instructions to create a Docker container, while a **Docker container** is a running instance of an image with its own unique environment.                                                                  |

---

## React

| **Question**                                           | **Answer**                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What is React?**                                      | React is a JavaScript library for building user interfaces. It allows developers to create reusable UI components and manage the state of the application efficiently through its virtual DOM.                                                                                       |
| **What is JSX?**                                        | **JSX (JavaScript XML)** is a syntax extension for JavaScript that allows you to write HTML elements and components in JavaScript. JSX is compiled to JavaScript before execution.                                                                                                  |
| **What is the difference between Props and State in React?** | **Props** are immutable and are passed from a parent component to a child component, while **State** is mutable and used to manage dynamic data within a component. State is local to a component, whereas props are passed down from parent to child. |
| **What is the purpose of React's Virtual DOM?**        | The **Virtual DOM** is an in-memory representation of the actual DOM elements. React uses it to optimize UI rendering by first making changes to the virtual DOM and then updating the actual DOM only if necessary, improving performance.                                      |
| **What is React Lifecycle?**                            | React **Lifecycle** refers to the series of methods that are invoked during a component's lifespan (from creation to removal). These include methods like `componentDidMount`, `componentWillUnmount`, and `shouldComponentUpdate`.                                                |
| **What is the use of `useEffect` hook in React?**       | `useEffect` is a React hook that allows you to perform side effects in function components, such as fetching data or subscribing to a service. It runs after every render by default but can be configured to run conditionally.                                                   |
| **What is React Router?**                               | **React Router** is a library used to handle navigation in a React application. It allows for the creation of dynamic routes and navigation between different views or pages in a single-page application (SPA).                                                                |
| **What is the difference between controlled and uncontrolled components in React?** | A **controlled component** is one whose form element values (e.g., input) are controlled by React state, while an **uncontrolled component** maintains its own internal state. Controlled components are typically preferred for their better control and predictability. |

---

This expanded collection of questions and answers covers the most common and important concepts for each technology stack, ensuring you're well-prepared for an interview.
