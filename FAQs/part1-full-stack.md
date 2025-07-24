Starting with Java 8 Features (Sample: Q1–Q10)
Java 8 Features
Q1: What is a lambda expression in Java 8?
A: A lambda expression is a shorthand notation for implementing a functional interface using an anonymous function.
Example:

java
Copy
Edit
List<String> names = Arrays.asList("Tom", "Jerry", "Spike");
names.forEach(name -> System.out.println(name));
Q2: What is the Stream API in Java 8?
A: It allows functional-style operations on collections like filtering, mapping, and reducing.
Example:

java
Copy
Edit
List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
List<Integer> squares = numbers.stream().map(n -> n * n).collect(Collectors.toList());
Q3: What are Functional Interfaces?
A: An interface with a single abstract method (SAM), used in lambda expressions.
Example: Runnable, Callable, or custom like:

java
Copy
Edit
@FunctionalInterface
interface MyFunc {
    void execute();
}
Q4: Explain the default method in interfaces.
A: Java 8 allows interfaces to have default methods with implementation.

java
Copy
Edit
interface Vehicle {
    default void start() { System.out.println("Starting..."); }
}
Q5: What is Optional in Java 8?
A: A container object which may or may not contain a non-null value, helping avoid null pointer exceptions.

java
Copy
Edit
Optional<String> name = Optional.ofNullable("Tom");
name.ifPresent(System.out::println);
Q6: What is the difference between map() and flatMap() in streams?
A: map() transforms each element, flatMap() flattens nested structures.

Q7: What are method references?
A: Shorter syntax for calling methods using :: operator.

java
Copy
Edit
List<String> list = Arrays.asList("A", "B");
list.forEach(System.out::println);
Q8: How is Collectors.groupingBy() used?
A: It groups elements by a classifier function.

java
Copy
Edit
Map<String, List<Employee>> grouped = 
  employees.stream().collect(Collectors.groupingBy(Employee::getDepartment));
Q9: What is the purpose of Predicate interface?
A: Represents a boolean-valued function.

java
Copy
Edit
Predicate<Integer> isEven = x -> x % 2 == 0;
Q10: What is Function<T, R> in Java 8?
A: A functional interface that accepts one argument and returns a result.

java
Copy
Edit
Function<String, Integer> length = s -> s.length();


✅ Spring Boot Questions (Q11–Q50)
Q11: What is Spring Boot?
A: Spring Boot simplifies the development of Spring-based applications by providing auto-configuration, embedded servers (like Tomcat), and opinionated defaults.

Q12: What is @SpringBootApplication?
A: A convenience annotation that combines:

@Configuration

@EnableAutoConfiguration

@ComponentScan

java
Copy
Edit
@SpringBootApplication
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
Q13: How does auto-configuration work in Spring Boot?
A: Spring Boot uses @EnableAutoConfiguration to automatically configure your application based on the dependencies present in the classpath.

Q14: What is application.properties or application.yml used for?
A: To externalize configuration such as server port, DB credentials, logging, etc.

properties
Copy
Edit
server.port=8081
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
Q15: What is the purpose of @RestController?
A: Combines @Controller and @ResponseBody, simplifying RESTful services.

java
Copy
Edit
@RestController
public class ProductController {
    @GetMapping("/products")
    public List<Product> getAll() { return productService.findAll(); }
}
Q16: What is the difference between @Component, @Service, and @Repository?
A:

@Component: Generic stereotype.

@Service: Marks a business service.

@Repository: Marks DAO layer and adds exception translation.

Q17: What is Spring Boot DevTools?
A: A module that enables hot reloading, live reload, and improved development productivity.

Q18: How do you create a REST API in Spring Boot?
A: Using @RestController, HTTP annotations (@GetMapping, @PostMapping), and a service/repo layer.

Q19: What is Spring Data JPA?
A: A module to simplify database access using JpaRepository, automatic query generation, and paging/sorting.

Q20: How do you connect to a database in Spring Boot?
A: Use starter dependencies like spring-boot-starter-data-jpa, configure application.properties, and use @Entity, @Repository.

Q21: What is H2 database and when is it used?
A: In-memory database useful for dev/testing with minimal setup.

Q22: How do you handle exceptions in Spring Boot?
A: Using @ControllerAdvice and @ExceptionHandler.

java
Copy
Edit
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(NotFoundException.class)
    public ResponseEntity<String> handle() {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Not Found");
    }
}
Q23: How to enable CORS in Spring Boot?
A: Globally via WebMvcConfigurer, or per controller using @CrossOrigin.

Q24: How do you secure Spring Boot REST APIs?
A: Use spring-boot-starter-security, configure WebSecurityConfigurerAdapter, and enable OAuth2/JWT as needed.

Q25: What are Spring Boot Starters?
A: Predefined dependency descriptors to simplify adding libraries (e.g., spring-boot-starter-web, spring-boot-starter-data-jpa).

Q26: What is Actuator in Spring Boot?
A: Adds production-ready features such as health checks, metrics, and application info at endpoints like /actuator/health.

Q27: How to create custom actuator endpoints?
A:

java
Copy
Edit
@Component
@Endpoint(id = "custom")
public class CustomEndpoint {
    @ReadOperation
    public String custom() {
        return "custom value";
    }
}
Q28: How do you use profiles in Spring Boot?
A: Use @Profile annotation and separate config files like application-dev.properties.

Q29: What is the difference between @RequestParam and @PathVariable?
A:

@RequestParam is for query params (?id=5)

@PathVariable is for URL segments (/users/5)

Q30: How do you log in Spring Boot?
A: Using SLF4J with implementations like Logback. Configurable in application.properties.

Q31: How do you validate request payload in Spring Boot?
A: Use @Valid or @Validated with validation annotations like @NotBlank, @Size.

Q32: What is CommandLineRunner?
A: Used to run code after the Spring Boot application context is loaded.

Q33: How do you schedule tasks in Spring Boot?
A: Use @EnableScheduling and @Scheduled.

Q34: How to consume REST APIs in Spring Boot?
A: Use RestTemplate or WebClient.

Q35: What’s the difference between RestTemplate and WebClient?
A:

RestTemplate: Synchronous HTTP client (deprecated in future).

WebClient: Asynchronous and reactive client.

Q36: How to return JSON responses?
A: By default, Spring Boot uses Jackson for JSON conversion. Use @RestController.

Q37: How do you upload/download files in Spring Boot?
A: Use MultipartFile in controller and write byte streams.

Q38: What is the use of spring-boot-devtools?
A: Provides automatic restart, livereload, and improved experience during development.

Q39: How do you paginate results in Spring Boot?
A: Use Pageable and Page<T> from Spring Data JPA.

Q40: What is EntityManager?
A: Interface from JPA used for interacting with persistence context.

Q41: Difference between CrudRepository and JpaRepository?
A:

CrudRepository: Basic CRUD operations.

JpaRepository: Adds pagination, sorting, and more JPA features.

Q42: What is Spring Boot initializer?
A: A web-based tool at start.spring.io to generate Spring Boot projects.

Q43: How do you unit test Spring Boot apps?
A: Use @SpringBootTest, @WebMvcTest, @DataJpaTest, and frameworks like JUnit5 and Mockito.

Q44: How to implement custom exception in Spring Boot?
A: Create custom class extending RuntimeException and handle with @ControllerAdvice.

Q45: How do you version REST APIs?
A: Use URI versioning (/v1/products), request header, or content negotiation.

Q46: How to shutdown Spring Boot app gracefully?
A: Use /actuator/shutdown (with settings enabled) or add @PreDestroy.

Q47: What is a bean lifecycle in Spring?
A: Bean instantiation → Property setting → @PostConstruct → usage → @PreDestroy.

Q48: How do you expose metrics in Spring Boot?
A: Use Actuator endpoints like /actuator/metrics or integrate with Prometheus.

Q49: How to load initial data on startup?
A: Use data.sql or CommandLineRunner.

Q50: How do you create a custom starter in Spring Boot?
A: Build a library with auto-configuration class and expose a spring.factories entry.

 Angular Questions (Q51–Q90)
Covering concepts, features, structure, and examples relevant for full-stack interviews.

Q51: What is Angular?
A: Angular is a TypeScript-based open-source framework for building dynamic, single-page web applications (SPAs), developed by Google.

Q52: What are components in Angular?
A: A component controls a part of the UI and consists of a .ts (class), .html (template), and .css/.scss (styles) file.

ts
Copy
Edit
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html'
})
export class HeaderComponent {}
Q53: What is a module in Angular?
A: A module (NgModule) organizes related components, services, and pipes. AppModule is the root module.

Q54: What is data binding?
A: It's the connection between the component logic and the view. Types:

Interpolation ({{}})

Property binding ([src])

Event binding ((click))

Two-way binding ([(ngModel)])

Q55: What is a directive?
A: A directive modifies the DOM.

Structural: *ngIf, *ngFor

Attribute: ngClass, ngStyle

Q56: What is a service in Angular?
A: A service contains business logic or reusable code, and is injectable using @Injectable().

ts
Copy
Edit
@Injectable({ providedIn: 'root' })
export class ProductService {}
Q57: What is dependency injection (DI)?
A: Angular's mechanism to provide components or services into constructors to reduce coupling.

Q58: What is routing in Angular?
A: Enables navigation between views or components using Angular Router.
Example:

ts
Copy
Edit
const routes: Routes = [
  { path: 'home', component: HomeComponent },
];
Q59: What is lazy loading?
A: Loading modules/components on demand to improve performance.

Q60: What is the lifecycle of an Angular component?
A: Key hooks:

ngOnInit()

ngOnChanges()

ngAfterViewInit()

ngOnDestroy()

Q61: What is two-way binding?
A: It synchronizes the model and the view using [(ngModel)]. Requires FormsModule.

Q62: What is Reactive Forms vs Template-Driven Forms?
A:

Reactive: Model-driven, powerful, testable

Template: Simpler, uses directives in HTML

Q63: How do you make HTTP requests in Angular?
A: Using HttpClient from @angular/common/http.

ts
Copy
Edit
constructor(private http: HttpClient) {}
getData() { return this.http.get('/api/data'); }
Q64: What are pipes in Angular?
A: Used to transform output in templates.
Example: {{ amount | currency:'USD' }}

Custom pipe:

ts
Copy
Edit
@Pipe({name: 'capitalize'})
export class CapitalizePipe implements PipeTransform {
  transform(value: string): string {
    return value.charAt(0).toUpperCase() + value.slice(1);
  }
}
Q65: What is a resolver?
A: Pre-fetches data before route activation.

Q66: How do you implement route guards?
A: Using CanActivate, CanDeactivate, etc.

ts
Copy
Edit
@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(): boolean {
    return true; // add logic
  }
}
Q67: What is state management in Angular?
A: Managing component state using services or libraries like NgRx, Akita, or BehaviorSubject.

Q68: What is the Angular CLI?
A: Command-line tool to generate, build, serve, test, and scaffold Angular applications.

Q69: What is NgRx?
A: A state management library using Redux pattern + RxJS.

Q70: What is difference between Subject and BehaviorSubject in RxJS?
A:

Subject: Emits only after subscription

BehaviorSubject: Holds and emits last value to new subscribers

Q71: What is async pipe?
A: Auto-subscribes to an Observable and updates the template.

html
Copy
Edit
<div *ngIf="data$ | async as data">{{ data.name }}</div>
Q72: How do you handle errors in Angular HTTP calls?
A: Use catchError with RxJS.

Q73: What is Change Detection?
A: Angular's mechanism to track and update changes in the view.

Q74: What are ngOnChanges and ngOnInit?
A:

ngOnChanges: Responds to input changes

ngOnInit: Runs after component init

Q75: What are observables?
A: A stream of data over time used with HTTP, events, and reactive programming.

Q76: Difference between Promise and Observable?
A:

Promise: One-time async result

Observable: Stream of multiple values, cancellable

Q77: What is Ahead-of-Time (AOT) compilation?
A: Pre-compiles Angular HTML/TS during build to improve performance.

Q78: How do you optimize performance in Angular apps?
A:

Lazy loading

trackBy in *ngFor

Detach change detection

Minify, AOT

Q79: How do you write unit tests in Angular?
A: Using Jasmine + Karma. Components are tested with TestBed.

Q80: How do you test services?
A: Use TestBed with mocks or spies using Jasmine.

Q81: What is a shared module?
A: A reusable module with common components, directives, and pipes imported in other modules.

Q82: What are standalone components (Angular 14+)?
A: Components that don’t require an NgModule.

Q83: What is a dynamic component loader?
A: Creating components at runtime using ComponentFactoryResolver.

Q84: What is the difference between ViewChild and ContentChild?
A:

ViewChild: Access child from same component

ContentChild: Access projected content

Q85: What is Angular Universal?
A: Server-side rendering for Angular apps, improves SEO and load time.

Q86: What are signals in Angular (v17+)?
A: A reactive primitive like useState to track state changes.

Q87: What is NgZone?
A: Angular’s wrapper around JS execution context, triggering change detection.

Q88: How to deploy Angular to production?
A: Run ng build --prod and deploy dist/ folder to web server or cloud.

Q89: How do you pass data between components?
A: Parent to child: @Input
Child to parent: @Output with EventEmitter

Q90: What is SSR and how is it implemented?
A: Server-side rendering using Angular Universal. Improves load time and SEO.

System Design Questions (Q91–Q120)
Detailed answers with explanations, examples, and Java-related references.

Q91: What is system design and why is it important in full-stack development?

A:
System design is the process of defining the architecture, components, modules, data flow, and interfaces for a system to meet specified requirements. As a Java Full Stack Developer, it's critical to:

Ensure scalability: the system handles increasing load.

Design for reliability: resilient to failure.

Enable maintainability: well-structured modules and services.

Support high performance: through caching, indexing, and optimal code.

A full-stack developer may not architect every component but must understand how backend (Spring Boot), frontend (Angular), database, caching (Redis), and cloud infrastructure (AWS, GCP) interact in the system.

Q92: How would you design a scalable e-commerce application?

A:
Start with the high-level modules:

Frontend: Angular (modular components: product list, cart, checkout)

Backend: Java Spring Boot (microservices: Product Service, Order Service, User Service)

Database: PostgreSQL for transactional data, MongoDB for product catalog

Authentication: JWT + OAuth2

Caching: Redis for product and cart caching

Message Queue: Kafka or RabbitMQ for order processing

API Gateway: Spring Cloud Gateway or AWS API Gateway

Load Balancer: NGINX or AWS ALB

Deployment: Dockerized containers on Kubernetes or AWS ECS

Use microservices so individual parts can scale independently, e.g., Order Service can scale during sales without affecting others.

Q93: What is the difference between monolithic and microservice architecture?

A:

Aspect	Monolith	Microservices
Structure	Single codebase	Multiple independent services
Deployment	Single unit	Multiple deployments
Scalability	Scales as a whole	Scales independently
Fault isolation	Poor	High
DevOps	Simple	Complex CI/CD required

In Java: Monolith = One Spring Boot app
Microservice = Multiple Spring Boot apps, each handling one business responsibility

Q94: How do you handle inter-service communication in microservices?

A:

RESTful HTTP APIs — for synchronous calls

Kafka / RabbitMQ — for asynchronous events

gRPC — for high-performance binary communication

Use Feign clients or WebClient in Spring Boot for internal HTTP calls.

Q95: What is eventual consistency and where would you apply it?

A:
Eventual consistency is a model where data is not immediately consistent across systems but becomes consistent over time.

Use case:
In an e-commerce app, when an order is placed:

Order Service updates order DB immediately

Inventory Service updates later via Kafka event

This prevents tight coupling and scales better than strong consistency.

Q96: How do you manage configuration in microservices?

A:
Use centralized config management:

Spring Cloud Config Server to host shared configurations

Environment-specific YAML/properties

Use vault or AWS Secrets Manager for credentials

Q97: How do you handle service discovery?

A:
Use a service registry like:

Eureka (Netflix OSS)

Consul

Kubernetes DNS

Each service registers itself and fetches others by name.

Q98: What is an API Gateway and why is it used?

A:
An API Gateway routes client requests to appropriate services, handles:

Authentication

Logging

Rate limiting

Request transformation

Examples:

Spring Cloud Gateway

AWS API Gateway

Kong

Q99: How do you ensure high availability?

A:

Stateless services deployed across multiple nodes

Load balancer (NGINX, ALB) routes traffic

Health checks for failover

Multi-region deployment for disaster recovery

Q100: What are key considerations for designing a database schema?

A:

Normalization to reduce redundancy

Indexes for performance

Referential integrity using foreign keys

Partitioning and sharding for scalability

Use NoSQL (MongoDB) for unstructured data like product descriptions

Q101: What is CAP theorem?

A:
CAP = Consistency, Availability, Partition Tolerance.
You can choose at most 2.

Type	Description
Consistency	All clients see same data
Availability	System is always responsive
Partition Tolerance	Works even when network fails

Example: MongoDB favors AP, while traditional RDBMS favors CA.

Q102: How do you design a rate limiter?

A:
Use Token Bucket or Leaky Bucket algorithm.
In Java, tools like:

Bucket4j

Redis-based counters (Atomic)

Used in API Gateway to throttle abusive clients.

Q103: How do you design a logging and monitoring strategy?

A:

Structured logs (JSON) using SLF4J or Log4j

Centralized log storage: ELK stack (Elasticsearch, Logstash, Kibana)

Monitoring: Prometheus + Grafana for metrics, alerts

Q104: What is CQRS pattern?

A:
Command Query Responsibility Segregation:

Split write (commands) and read (queries) into different models.

Improves scalability and performance, especially in event-driven systems.

Q105: How would you handle transactional integrity in microservices?

A:

SAGA Pattern: Split transaction into local ones with compensating logic.

Eventual consistency

Orchestration or choreography for managing workflows

Q106: How do you design a secure full-stack application?

A:

Backend: Spring Security, OAuth2, HTTPS

Frontend: JWT stored in HttpOnly cookie, Angular route guards

Secure headers, input validation, CORS config, CSRF protection

Q107: What are best practices for REST API design?

A:

Use nouns for resources: /users, /orders

HTTP methods: GET, POST, PUT, DELETE

Status codes: 200, 201, 400, 401, 404, 500

Versioning: /api/v1/users

Pagination and filtering

Q108: How do you handle file uploads in a scalable app?

A:

Use cloud storage: AWS S3, GCP Storage

Backend stores metadata in DB

Use presigned URLs to reduce backend load

Q109: How to scale an Angular frontend?

A:

AOT compilation, lazy loading

Tree shaking to remove unused code

Use CDN for static content

Code splitting and gzip compression

Q110: How to scale a Spring Boot backend?

A:

Stateless microservices behind a load balancer

Use Redis caching

Optimize DB access (indexes, connection pool)

Async processing via Kafka or @Async

Deploy on Kubernetes for auto-scaling

Design Patterns Questions (Q121–Q150)
Detailed explanations, code examples, and system design relevance.

Q121: What are design patterns?
A:
Design patterns are reusable solutions to commonly occurring problems in software design. They're not code but templates to solve design issues across languages. For full stack Java developers, these patterns ensure:

Clean architecture

Reusability

Scalability

Maintainability

Q122: What is the Singleton Pattern?
A:
Ensures a class has only one instance and provides a global point of access.

Use Case: Logging, DB connections, config manager.

java
Copy
Edit
public class Singleton {
    private static Singleton instance = new Singleton();
    private Singleton() {}
    public static Singleton getInstance() {
        return instance;
    }
}
Q123: Explain the Factory Pattern with an example.
A:
Provides an interface for creating objects but lets subclasses alter the type of objects.

Use Case: Create objects without exposing instantiation logic.

java
Copy
Edit
interface Shape {
    void draw();
}
class Circle implements Shape {
    public void draw() { System.out.println("Drawing Circle"); }
}
class ShapeFactory {
    public static Shape getShape(String type) {
        return switch (type) {
            case "circle" -> new Circle();
            default -> throw new IllegalArgumentException();
        };
    }
}
Q124: What is the Builder Pattern?
A:
Used to construct complex objects step-by-step.

Use Case: Creating immutable objects with multiple optional fields (e.g., DTOs).

java
Copy
Edit
class User {
    private final String name;
    private final int age;

    public static class Builder {
        private String name;
        private int age;

        public Builder setName(String name) { this.name = name; return this; }
        public Builder setAge(int age) { this.age = age; return this; }
        public User build() { return new User(this); }
    }

    private User(Builder builder) {
        this.name = builder.name;
        this.age = builder.age;
    }
}
Q125: What is the Strategy Pattern?
A:
Enables selecting an algorithm at runtime.

Use Case: Payment processor with different strategies (PayPal, Stripe).

java
Copy
Edit
interface PaymentStrategy {
    void pay(int amount);
}
class PayPal implements PaymentStrategy {
    public void pay(int amount) { System.out.println("Paying with PayPal: " + amount); }
}
class Context {
    private PaymentStrategy strategy;
    public Context(PaymentStrategy strategy) { this.strategy = strategy; }
    public void execute(int amount) { strategy.pay(amount); }
}
Q126: What is the Observer Pattern?
A:
Defines one-to-many dependency between objects. When one object changes, all dependents are notified.

Use Case: Event publishing (like Angular EventEmitter, Kafka).

Q127: What is the Proxy Pattern?
A:
Provides a surrogate or placeholder for another object to control access.

Use Case: Security proxies, caching, lazy loading.

Q128: What is the Decorator Pattern?
A:
Adds responsibilities to objects dynamically.

Use Case: Add logging, security, validation without changing core logic.

java
Copy
Edit
interface Notifier {
    void send(String message);
}
class EmailNotifier implements Notifier {
    public void send(String message) { System.out.println("Email: " + message); }
}
class SMSDecorator implements Notifier {
    private Notifier notifier;
    public SMSDecorator(Notifier notifier) { this.notifier = notifier; }
    public void send(String message) {
        notifier.send(message);
        System.out.println("SMS: " + message);
    }
}
Q129: What is the MVC Pattern?
A:
Model-View-Controller separates application logic:

Model = Data (Spring entities)

View = UI (Angular templates)

Controller = Logic (Spring REST controllers)

Q130: What is the Repository Pattern?
A:
Abstracts data layer logic, separating persistence from business logic. In Spring Boot, JpaRepository is an example.

java
Copy
Edit
public interface ProductRepository extends JpaRepository<Product, Long> {}
Q131: What is Dependency Injection (DI) and how is it implemented in Spring?
A:
DI is a design pattern where objects get their dependencies from an external source.

Spring Example:

java
Copy
Edit
@Service
public class OrderService {
    private final OrderRepository repo;
    public OrderService(OrderRepository repo) { this.repo = repo; }
}
Spring handles injecting OrderRepository automatically.

Q132: What is the Command Pattern?
A:
Encapsulates a request as an object.

Use Case: Undo operations, job queue processing.

Q133: How is the Chain of Responsibility used?
A:
Allows a request to be passed through a chain of handlers.

Use Case: Logging, authentication filters.

Q134: Difference between Template and Strategy Patterns?
A:

Template	Strategy
Inheritance	Composition
Defines skeleton	Defines interchangeable algorithm

Q135: How to implement caching using Decorator pattern?
A:
Wrap actual service inside a caching layer.

java
Copy
Edit
class CachedProductService implements ProductService {
    private final ProductService delegate;
    private final Map<Long, Product> cache = new HashMap<>();
    public Product getProduct(Long id) {
        return cache.computeIfAbsent(id, delegate::getProduct);
    }
}

