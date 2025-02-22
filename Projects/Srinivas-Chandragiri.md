| **#** | **Question** | **Answer** |
|-------|--------------|------------|
| 1 | How can you orchestrate the invocation of two services (Service A and Service B) in a Spring Boot application? | You can orchestrate the invocation of Service A and Service B using asynchronous methods such as `@Async` or `CompletableFuture` for non-blocking operations. If one service fails to respond, you could use circuit breakers (with Resilience4j or Hystrix) and implement fallback methods to ensure the process continues. |
| 2 | When performing performance testing on services (Service A and Service B), how would you handle scenarios where one of the services fails to respond? | In performance testing, simulate service failures using tools like JMeter or load testing frameworks. Utilize a circuit breaker pattern to ensure the failure of one service does not affect others. Implement retries and timeouts with proper exception handling to maintain system resilience. |
| 3 | Discuss the concepts of authentication and authorization in the context of a Spring Boot application. How would you implement and manage these security aspects to control access and ensure data integrity? | Authentication verifies the user’s identity, and authorization determines their access level. In Spring Boot, implement authentication using Spring Security with JWT (JSON Web Token) to manage sessions, and use roles and permissions for authorization. |
| 4 | Explain how `CompletableFuture` is utilized for asynchronous programming in a Spring Boot environment. | `CompletableFuture` allows non-blocking execution by running tasks asynchronously. Example: ```java CompletableFuture.supplyAsync(() -> serviceA.call()).thenAccept(result -> serviceB.call(result));This helps in executing Service A and B in parallel without blocking the main thread. |
| 5 | Is it possible to configure and use two databases in a Spring Boot application? | Yes, it is possible by using multiple DataSource configurations. Define two @Primary and @Bean annotations for each database, and configure JpaRepositories for each. Challenges include managing transactions and ensuring data consistency between databases. | 
| 6 | Share your experience with the features introduced in Java 8 through Java 11. | Java 8 introduced lambda expressions, streams, and the Optional class, enabling functional programming. Java 9 introduced modules, Java 10 improved garbage collection, and Java 11 included long-term support (LTS) and additional enhancements. These features are used in Spring Boot for better performance and code readability. | 
| 7 | Introduction | In my previous roles, I’ve worked as a Full Stack Developer focusing on Spring Boot applications and microservices architecture. I’ve been responsible for both back-end development and deploying solutions in cloud environments. | 
| 8 | Project Architecture | The architecture primarily followed a microservices approach with Spring Boot and Spring Cloud. We used RESTful APIs for communication and deployed services in AWS with Kubernetes for orchestration. | 
| 9 | Spring Security with JWT Token | Spring Security with JWT ensures secure communication between client and server. JWT is used for token-based authentication where tokens are generated after user login and sent with each request for validation. | 
| 10 | Auto Scaling - Horizontal vs Vertical Scaling - AWS | Horizontal scaling adds more instances, while vertical scaling increases the resources (CPU, RAM) of an instance. AWS provides both options, where Elastic Load Balancers (ELB) can be used for horizontal scaling and EC2 instance types for vertical scaling. | 
| 11 | Explain code snippet | The code checks if vehicleDetails.getHeadUnit() is non-null and if it matches specific conditions (MobilePlatformCode and Channel). If these checks pass, a BusinessValidationException is thrown to prevent invalid data submission. | 
| 12 | Sorting program input A: [4,7,3], B: [6,9,2] output A: [2,3,4], B: [6,7,9] | You can sort the arrays by using Java's built-in Arrays.sort() method for both arrays A and B. Example:java CopyArrays.sort(A);Arrays.sort(B);``` |
| 13 | What is multithreading? How to achieve it? | Multithreading is a concept where multiple threads execute concurrently to perform tasks. You can achieve it by extending the `Thread` class or implementing the `Runnable` interface in Java. |
| 14 | In Spring Boot, is it possible to skip DB connection on application startup? | Yes, by configuring the `spring.datasource.initialize=false` property in `application.properties`, you can skip the database connection during startup. |
| 15 | Things to take care of while accessing the production database | Ensure proper database connection pooling, transaction management, and error handling. Implement data backups, logging, and monitoring to avoid performance bottlenecks and data loss. |
| 16 | Tools for logging and monitoring | Tools like Logback, SLF4J, and Spring Boot Actuator are widely used for logging. For monitoring, Prometheus, Grafana, and ELK Stack (Elasticsearch, Logstash, Kibana) are useful. |
| 17 | Which version of Java have you worked with? | I have worked with Java 8, Java 11, and Java 17. Each version provides improvements in functional programming features, garbage collection, and performance. |
| 18 | Have you worked on NoSQL database like MongoDB? | Yes, I have worked with MongoDB in a microservices-based application. We used it for flexible schema design and high availability in distributed systems. |
| 19 | Roles and responsibilities in the last one month to one year span | I have been responsible for developing REST APIs, integrating external services, performing code reviews, and deploying applications to AWS using CI/CD pipelines. |
| 20 | Java - which version have you used? and what do you like about it? | I have used Java 8, 11, and 17. I appreciate Java 8 for its support of lambda expressions and streams, which make the code more concise and readable. |
| 21 | You have created your web application and you are just starting out - how will you take it to production? | First, I would ensure that the application is fully tested. Then, I’d configure CI/CD pipelines using Jenkins or GitHub Actions, and deploy to a cloud environment like AWS using services such as EC2 and RDS. |
| 22 | If I don't want to use EC2 AWS, what are other trendy options these days? | Alternatives to EC2 include containerized services like AWS Fargate, Google Cloud Run, or Kubernetes (with Amazon EKS or Google GKE) for more efficient orchestration and scalability. |
| 23 | SOLID principle | SOLID is a set of design principles that improve code maintainability. The principles are:
 1. **Single Responsibility Principle**
 2. **Open/Closed Principle**
 3. **Liskov Substitution Principle**
 4. **Interface Segregation Principle**
 5. **Dependency Inversion Principle** |
| 24 | How did you implement Payment Gateways? | I implemented payment gateways using APIs like Stripe and PayPal. I ensured secure transactions by using HTTPS, token-based authentication, and handling payment responses asynchronously. |
| 25 | What is the difference between Queue and Topic? | A Queue is a point-to-point messaging model where one producer sends a message to one consumer. A Topic is a publish-subscribe model where messages are sent to multiple consumers. |
| 26 | Heard about AWS SQS and SNS? | Yes, AWS SQS (Simple Queue Service) is used for decoupling services through message queuing. AWS SNS (Simple Notification Service) is used for push notifications and message broadcasting to multiple subscribers. |
| 27 | Why should we select you? | I bring a strong combination of technical skills in Java, Spring Boot, and AWS. I’m also a problem-solver who thrives in collaborative environments and is always focused on delivering quality solutions. |
| 28 | Disadvantage of microservices | Microservices can introduce complexity in terms of managing multiple services, data consistency, and inter-service communication. Additionally, they require infrastructure management and efficient monitoring tools. |
| 29 | Have you used event-driven architecture? | Yes, I’ve worked with event-driven architecture using Kafka and RabbitMQ, where services communicate through events to achieve loose coupling and better scalability. |
| 30 | Have you developed REST API contracts? | Yes, I’ve developed API contracts using OpenAPI (Swagger) and Postman for API documentation. These tools help define and communicate the expected request and response structures for REST APIs. |

| **#** | **Question** | **Answer** |
|-------|--------------|------------|
| 31 | Have you consumed API endpoints? When you ask for API endpoints, what all things would you ask for? | When consuming an API, I would ask for the API documentation (e.g., OpenAPI), expected request and response formats, authentication methods, rate limits, error handling, and any versioning information. |
| 32 | How did you receive third-party communication-related metadata? | Third-party communication metadata can be received via HTTP headers (e.g., Authorization, Content-Type, X-Request-ID) or through the body of the request, depending on the API specifications. I often use Spring’s `@RequestHeader` to access these headers. |
| 33 | Types of Java stream methods. | Java Stream API has several methods like `filter()`, `map()`, `reduce()`, `collect()`, `forEach()`, `flatMap()`, and `sorted()`. These methods help in processing collections in a functional style. |
| 34 | Map vs FlatMap and orElse vs OrElseGet | 
    - **Map**: Transforms each element of a stream.
    - **FlatMap**: Flattens multiple streams into a single stream.
    - **orElse**: Returns a default value if the value is null.
    - **orElseGet**: Returns a default value from a supplier function if the value is null. |
| 35 | Java 8 Features (Functional Interface and Stream) | Java 8 introduced functional interfaces and the Stream API. A functional interface is an interface with a single abstract method. Streams enable functional programming with operations like `map`, `filter`, and `reduce` for processing collections. |
| 36 | Volatile keyword | The `volatile` keyword in Java ensures that a variable's value is always fetched from the main memory and not from the CPU cache. It's commonly used in multi-threading environments to prevent thread-local caching of variables. |
| 37 | ACID properties in transaction | ACID stands for Atomicity, Consistency, Isolation, and Durability. These properties ensure that database transactions are processed reliably. |
| 38 | Commit vs push and fetch vs pull | 
    - **Commit**: Saves changes to the local repository.
    - **Push**: Uploads local changes to a remote repository.
    - **Fetch**: Downloads changes from the remote repository to your local machine but doesn’t merge them.
    - **Pull**: Fetches and automatically merges changes from the remote repository to your local branch. |
| 39 | What all ways to create Singleton Object | Singleton objects can be created in Java using:
    - Static block
    - Enum
    - Bill Pugh Singleton Design (using a static inner class)
    - Lazy initialization |
| 40 | Different types of bean scope and detailed explanation | In Spring, beans have different scopes: 
    - **Singleton** (default): One shared instance per Spring container.
    - **Prototype**: A new instance for every request.
    - **Request**: One instance per HTTP request.
    - **Session**: One instance per HTTP session.
    - **Application**: One instance for the entire application. |
| 41 | == vs === in JavaScript | 
    - `==`: Compares values for equality after type coercion.
    - `===`: Compares values and their types without type coercion. |
| 42 | Crud vs JPA repository | 
    - **CRUD Repository**: Basic operations (Create, Read, Update, Delete) for entities.
    - **JPA Repository**: Extends `CrudRepository` and provides additional methods like batch processing, flushing, and pagination. |
| 43 | JWT token | JWT (JSON Web Token) is a compact and self-contained way to securely transmit information between parties. It's widely used in Spring Boot for authentication and authorization, where the server generates a JWT token and sends it to the client, which includes it in the Authorization header for subsequent requests. |
| 44 | REST API coding and integration testing | REST API coding involves defining endpoints in controllers and using annotations like `@GetMapping`, `@PostMapping`, etc. For integration testing, you can use tools like `@SpringBootTest` and `@WebMvcTest` in Spring to mock services and test APIs. |
| 45 | Types of Data binding in Angular | Angular has two types of data binding:
    - **One-way data binding**: From the component to the view or vice versa (e.g., `{{ data }}`, `[(ngModel)]`).
    - **Two-way data binding**: Allows both the component and view to communicate (e.g., `[(ngModel)]`). |
| 46 | Parent child component communication | In Angular, parent-child communication happens through:
    - **Input**: The parent component passes data to the child using the `@Input` decorator.
    - **Output**: The child component communicates back to the parent using the `@Output` decorator and an EventEmitter. |
| 47 | What is the usage of pipes in Angular? | Pipes in Angular transform data in the template. They are useful for formatting values such as dates, currencies, or numbers without changing the original data. Examples: `date`, `currency`, `uppercase`, etc. |
| 48 | Promises vs Observables | 
    - **Promises**: Handle asynchronous operations and are single-valued.
    - **Observables**: Handle asynchronous operations and allow multiple values over time, supporting operators like `map`, `filter`, and `mergeMap`. |
| 49 | Core Java - Difference between StringBuffer and StringBuilder | 
    - **StringBuffer**: Thread-safe but slower due to synchronization.
    - **StringBuilder**: Not thread-safe but faster than StringBuffer. |
| 50 | SOLID Principle | The SOLID principles are a set of five principles that improve code readability, maintainability, and scalability. They include:
    1. **Single Responsibility Principle**
    2. **Open/Closed Principle**
    3. **Liskov Substitution Principle**
    4. **Interface Segregation Principle**
    5. **Dependency Inversion Principle** |
| 51 | Design Patterns - Difference between Factory Design Pattern and Prototype Design Pattern | 
    - **Factory Pattern**: Provides an interface for creating objects but allows subclasses to alter the type of objects that will be created.
    - **Prototype Pattern**: Creates objects by cloning an existing object rather than creating a new one. |
| 52 | Given a program for Stream API and ask for output | A typical Stream API program might look like:
    ```java
    List<Integer> list = Arrays.asList(4, 7, 1, 2);
    list.stream().filter(x -> x > 2).sorted().forEach(System.out::println);
    ```
    Output: `4, 7` |
| 53 | Functional Interface and Lambda Expression | A **Functional Interface** is an interface with a single abstract method. **Lambda expressions** are used to provide a clear and concise way to represent a method using an expression. Example:
    ```java
    FunctionalInterface greet = (name) -> System.out.println("Hello " + name);
    greet.sayHello("John");
    ``` |
| 54 | Multithreading - Different ways of implementation | Multithreading can be implemented by:
    - Extending the `Thread` class
    - Implementing the `Runnable` interface
    - Using the `ExecutorService` framework for thread pooling. |
| 55 | Synchronization and Executor Framework | **Synchronization** ensures that only one thread can access a critical section of code at a time. **Executor Framework** simplifies thread management by providing pool-based execution models. |
| 56 | How garbage collector works internally | The garbage collector in Java works by identifying and reclaiming memory used by unreachable objects. It uses algorithms like Mark-and-Sweep, Generational GC, and others to clean the heap space. |
| 57 | Exception Handling - How to create a Custom Exception Handling | Custom exceptions can be created by extending the `Exception` class. They allow more specific error messages and handling of custom situations:
    ```java
    public class CustomException extends Exception {
        public CustomException(String message) {
            super(message);
        }
    }
    ```
| 58 | Spring Framework - Difference between @Component, @Service and @Repository tags | 
    - `@Component`: General-purpose annotation for any Spring-managed bean.
    - `@Service`: A specialization of `@Component` for service-layer beans.
    - `@Repository`: A specialization of `@Component` for DAO/repository beans that interact with the database. |
| 59 | Transaction mechanism in Spring Framework | Spring provides declarative transaction management using annotations like `@Transactional`. It allows you to manage transactions across methods and ensures rollback on failure. |
| 60 | Difference between Eager and Lazy Loading | 
    - **Eager Loading**: Loads the associated entities immediately with the parent entity.
    - **Lazy Loading**: Loads associated entities only when they are accessed. |
| 61 | Transient keyword | The `transient` keyword in Java marks a field to be excluded from serialization, meaning it won't be persisted when the object is serialized. |
| 62 | Difference between Isolation and Propagation | 
    - **Isolation**: Defines the visibility of one transaction's changes to others (e.g., `READ_COMMITTED`, `SERIALIZABLE`).
    - **Propagation**: Defines how transactions behave when they are called from another transaction (e.g., `REQUIRED`, `REQUIRES_NEW`). |
| 63 | Maven Lifecycle | Maven has a build lifecycle that includes phases like `compile`, `test`, `package`, `install`, and `deploy`. Each phase executes a set of goals. |
| 64 | Profiles in Maven | Profiles in Maven allow you to customize the build configuration for different environments (e.g., development, production). Profiles can be
| **#** | **Question** | **Answer** |
|-------|--------------|------------|
| 65 | Git - Difference between Branch and Pull | 
    - **Branch**: A branch in Git is a pointer to a snapshot of your changes. It's used to work on different versions of your project independently.
    - **Pull**: `git pull` fetches changes from a remote repository and merges them into your current branch. |
| 66 | Git - Difference between Pull and Fetch | 
    - **Fetch**: `git fetch` retrieves changes from the remote repository without merging them. It updates your local copy of the remote branches.
    - **Pull**: `git pull` fetches changes and immediately merges them into your current branch. |
| 67 | Git - Why used tags in Git | Tags are used to mark specific points in history (like releases) and are useful for versioning. Unlike branches, tags do not change. |
| 68 | Angular - Difference between one-way and two-way binding | 
    - **One-way binding**: Data flows in one direction, either from the component to the view (`{{ data }}`) or from the view to the component (`[value]="data"`).
    - **Two-way binding**: Data flows in both directions between the component and the view, typically achieved with `[(ngModel)]`. |
| 69 | Angular - How parent and child relationship works in Angular components | In Angular:
    - **Parent to Child**: The parent component passes data to the child using `@Input` property binding.
    - **Child to Parent**: The child component communicates with the parent using `@Output` and EventEmitter. |
| 70 | Angular - Lazy routing in Angular | Lazy loading in Angular allows modules to be loaded only when the user navigates to the route associated with the module. This improves the application’s initial loading time. |
| 71 | Angular - Difference between Observer and Behavior in Angular | 
    - **Observer**: The observer listens to changes from an observable, typically using the `subscribe()` method.
    - **BehaviorSubject**: A type of observable that stores the latest value and emits it to new subscribers immediately. |
| 72 | Agile Manifesto | The **Agile Manifesto** emphasizes individuals and interactions, working software, customer collaboration, and responding to change over rigid processes and tools. |
| 73 | How to estimate work in Agile | Work in Agile can be estimated using techniques like story points, t-shirt sizing, or ideal hours. These estimates help in planning sprints and determining workload capacity. |
| 74 | How you can handle work when you have dependency on other person who is on unexpected leave | I would communicate the issue early with the team and manager, potentially adjust deadlines, and take proactive steps to identify temporary solutions or workarounds. |
| 75 | What is User Story and What is Ceremony | 
    - **User Story**: A short description of a feature or functionality from an end user's perspective, often written in the format: "As a [user], I want to [action] so that [reason]."
    - **Ceremony**: Agile ceremonies refer to key meetings, such as Sprint Planning, Daily Standup, Sprint Review, and Sprint Retrospective. |
| 76 | What is AWS CDN | AWS CloudFront is Amazon’s content delivery network (CDN) service that distributes content to users with low latency by using a network of global edge locations. |
| 77 | What is lambda expression in AWS | AWS Lambda allows you to run code in response to events without provisioning or managing servers. Lambda expressions refer to the event-driven, serverless code that executes on the AWS infrastructure. |
| 78 | How can you orchestrate the invocation of two services (Service A and Service B) in a Spring Boot application? | To orchestrate the invocation of two services in Spring Boot, I would use a service layer where the calls to both services (A and B) are made sequentially or concurrently, depending on the requirement. For concurrent calls, I would use `CompletableFuture` or `@Async`. |
| 79 | Describe the approach you would take to ensure that the operation proceeds even if one of the services does not provide a response. | To handle failure scenarios, I would implement **circuit breaker patterns** using libraries like Resilience4j or Hystrix. Additionally, I would use **fallback methods** to ensure that the application doesn't fail completely if one of the services doesn't respond. |
| 80 | When performing performance testing on services (Service A and Service B), how would you handle scenarios where one of the services fails to respond? | In performance testing, I would simulate service failures using **timeout settings** and **circuit breakers**. Additionally, I would configure load balancing and retry strategies to gracefully handle failures without impacting the overall system performance. |
| 81 | Discuss the concepts of authentication and authorization in the context of a Spring Boot application. | **Authentication** is the process of verifying the identity of a user (e.g., using JWT tokens), and **Authorization** determines the resources a user can access based on their roles or permissions. In Spring Boot, I would use Spring Security to manage both authentication and authorization. |
| 82 | Explain how CompletableFuture is utilized for asynchronous programming in a Spring Boot environment. | `CompletableFuture` is used to perform asynchronous operations in Spring Boot. It allows non-blocking operations like API calls to run concurrently and return a result once complete, improving performance. Example:
    ```java
    CompletableFuture.supplyAsync(() -> someService.getData())
        .thenApply(data -> process(data));
    ``` |
| 83 | Is it possible to configure and use two databases in a Spring Boot application? | Yes, Spring Boot allows configuring multiple data sources using the `@Primary` annotation and separate `DataSource`, `EntityManagerFactory`, and `TransactionManager` beans. Each data source can be connected to a different database. |
| 84 | Share your experience with the features introduced in Java 8 through Java 11. | Java 8 introduced lambda expressions, the Stream API, `Optional`, and `java.time`. Java 9 added modules, Java 10 introduced local-variable type inference (`var`), and Java 11 brought new methods to the `String` class and improvements in garbage collection. |
| 85 | Introduction to Spring Security with JWT Token | Spring Security with JWT (JSON Web Tokens) provides a mechanism for securing APIs by issuing a token after successful authentication. The token is sent with each request to verify the user's identity. JWTs are stateless and self-contained. |
| 86 | Auto Scaling - Horizontal vs Vertical Scaling - AWS | 
    - **Horizontal Scaling**: Adding more instances to distribute the load. It's the preferred approach in cloud environments for scalability and availability.
    - **Vertical Scaling**: Increasing the resources (CPU, RAM) of a single instance. While simpler, it has limitations for very high loads. |
| 87 | Explain code snippet - return Optional.ofNullable(vehicleDetails.getHeadUnit())... | This code checks if `vehicleDetails.getHeadUnit()` is not null, then checks if the `mobilePlatformCode` of the head unit matches `MM24`. If both conditions are met, it verifies that the `X_CHANNEL` header is `ONEAPP`, and throws an exception if true. |
| 88 | Sorting program input A:[4,7,3] , B:[6,9,2] output A:[2,3,4], B:[6,7,9] | Sorting the arrays `A` and `B` using Java’s `Arrays.sort()` method would result in:
    - `A = [2, 3, 4]`
    - `B = [6, 7, 9]` |
| 89 | What is multithreading? And how to achieve it? | Multithreading is a programming concept that allows multiple threads to run concurrently, enabling parallel processing. In Java, you can achieve multithreading by extending the `Thread` class or implementing the `Runnable` interface. |
| 90 | In Spring Boot, is it possible to skip DB connection on application startup? | Yes, you can skip DB connection during startup by either configuring the `DataSource` as `@Primary` and conditionally enabling/disabling it using Spring profiles or by using `spring.autoconfigure.exclude` to exclude specific auto-configurations. |
| 91 | Things to take care while accessing production database | When accessing a production database, ensure that you:
    - Use read-only transactions where possible.
    - Have proper backup and recovery procedures in place.
    - Ensure proper access control and security (encryption, VPN, etc.).
    - Monitor database performance and set up alerts for high load or slow queries. |
| 92 | Tools for logging and monitoring | Common tools for logging and monitoring include:
    - **Logging**: Logback, Log4j, SLF4J.
    - **Monitoring**: Prometheus, Grafana, ELK stack (Elasticsearch, Logstash, Kibana), Spring Actuator, and New Relic. |
| 93 | Which version of Java have you worked? | I have worked with Java 8, 9, 10, 11, and 17. Java 8 was my starting point, and I've used features like Lambdas, Streams, and `Optional` extensively. |
| 94 | Have you worked on NoSQL database like MongoDB? | Yes, I have worked with MongoDB for storing unstructured data, especially when I needed scalability and flexibility in schema design. I have used it with Spring Data MongoDB for seamless integration. |
| 95 | Intro - Roles and responsibilities in last one month to last one year span. | Over the last year, I have been involved in designing and developing microservices, implementing security using JWT tokens, optimizing database queries, and ensuring high availability and scalability of applications. |
| 96 | Java - Which version have you used? And what do you like about it? | I have worked primarily with Java 8, 11, and 17. I appreciate the functional programming features introduced in Java 8, such as Lambdas and Streams, as well as the improvements in Java 11, like new methods in the `String` class and better garbage collection. |
| 97 | You have created your web application and you are just starting out - how will you take it to production? | To take my web application to production, I would ensure proper security measures, CI/CD pipelines for automated deployments, load balancing, database scaling, proper logging and monitoring, and backup strategies. |
| 98 | If I don’t want to use EC2 AWS, then what are other trendy options these days? | Other popular AWS services include **AWS Lambda** (serverless computing), **Elastic Beanstalk** (Platform as a Service), or even using **Docker** containers with **Amazon ECS** for orchestration. |
| 99 | SOLID Principle | **SOLID** is an acronym for five principles of object-oriented design that aim to make software easier to maintain and extend. They are:
    1. **Single Responsibility Principle**
    2. **Open/Closed Principle**
    3. **Liskov Substitution Principle**
    4. **Interface Segregation Principle**
    5. **Dependency Inversion Principle** |
| 100 | Design Patterns - Difference between Factory Design Pattern and Prototype Design Pattern | 
    - **Factory Pattern**: Creates objects based on certain conditions or parameters.
    - **Prototype Pattern**: Creates new objects by cloning an existing prototype object. |



