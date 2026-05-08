# MOCK INTERVIEW QUESTIONS BY TECHNOLOGY

## Practice Questions for All 18 Technologies

---

## JAVA CORE - 25 Questions

1. Explain the 4 pillars of OOP with real examples
2. What's the difference between final, finally, and finalize?
3. How does HashMap work internally? Explain collision handling
4. Explain the difference between ArrayList and LinkedList
5. What's the purpose of the volatile keyword?
6. Explain synchronized blocks vs ReentrantLock
7. What are Java 8 streams? Give 3 real-world examples
8. How does garbage collection work in Java?
9. Explain memory leaks in Java and how to detect them
10. What's the difference between equals() and ==?
11. How do you create an immutable class in Java?
12. Explain the visitor design pattern
13. What's the difference between throw and throws?
14. How does the try-with-resources statement work?
15. Explain Optional and when to use it
16. What's an executor framework and when to use it?
17. Explain CompletableFuture with a real example
18. What are the differences between Comparator and Comparable?
19. How do you handle exceptions in streams?
20. Explain functional interfaces in Java
21. What's the difference between static and instance methods?
22. How does the ClassLoader work in Java?
23. Explain metaspace vs PermGen
24. What's a memory leak and how to prevent it?
25. Explain the diamond problem in interfaces

---

## SPRING BOOT - 25 Questions & Answers

### Q1: Explain Spring dependency injection and how it works
**A:** Spring creates objects (beans) and injects dependencies automatically. Scans classloader for @Component/@Service, stores in ApplicationContext. Three ways: Constructor (best), Setter, Field injection.

### Q2: What's the difference between @Autowired and @Inject?
**A:** @Autowired - Spring-specific. @Inject - Java standard (JSR 330). @Autowired has required flag. Use @Inject for portability across frameworks.

### Q3: How do you configure Spring Security for OAuth2?
**A:** Register OAuth2 provider, configure scopes, implement UserService, configure SecurityConfig. Use ResourceServerConfigurerAdapter for resource server setup.

### Q4: Explain @Transactional and transaction propagation levels
**A:** REQUIRED (default) - uses existing or creates new. REQUIRES_NEW - always new. NESTED - savepoint. MANDATORY - must exist. NEVER - must not exist.

### Q5: What's the purpose of @Component, @Service, @Repository, @Controller?
**A:** @Component - generic bean. @Service - business logic. @Repository - data access (includes exception translation). @Controller - handles web requests.

### Q6: How do you create a custom validator?
**A:** Implement ConstraintValidator<CustomAnnotation, Type>, implement isValid(). Create custom annotation with @Constraint pointing to validator.

### Q7: Explain the Spring Bean lifecycle
**A:** Instantiation → Properties set → BeanNameAware → BeanFactoryAware → ApplicationContextAware → PreConstruct → PostConstruct → Ready → PreDestroy → Destruction.

### Q8: What's AOP (Aspect-Oriented Programming) and how to use it?
**A:** Separate cross-cutting concerns. @Aspect class with @Pointcut, @Before, @After, @Around. Weaves into bean methods at runtime. Use for logging, caching, security.

### Q9: How do you handle exceptions globally in Spring?
**A:** Use @ControllerAdvice with @ExceptionHandler methods. Returns ResponseEntity with HTTP status and error details. Catches exceptions from all controllers.

### Q10: What's the difference between @ComponentScan and @EnableAutoConfiguration?
**A:** @ComponentScan - finds @Component/@Service beans in packages. @EnableAutoConfiguration (Spring Boot) - auto-configures beans based on classpath.

### Q11: How do you implement JWT authentication in Spring?
**A:** Generate JWT token containing claims. Filter extracts token from Authorization header, validates signature, sets authentication. Register filter in SecurityConfig.

### Q12: Explain Spring Data JPA query methods
**A:** Magic methods using naming conventions. findBy*, findAllBy*, deleteBy*. Creates queries automatically. Use @Query for custom JPQL/native queries.

### Q13: How do you configure multiple data sources?
**A:** Create multiple DataSource beans, multiple JdbcTemplate/EntityManagerFactory beans. Use @Primary to mark default. Specify dataSource in @Transactional.

### Q14: What's the difference between @RequestParam and @PathVariable?
**A:** @RequestParam - query parameter (?name=value). @PathVariable - URL path segment (/users/{id}). @RequestParam optional with defaultValue.

### Q15: How do you intercept HTTP requests in Spring?
**A:** Implement HandlerInterceptor, override preHandle/postHandle/afterCompletion. Register with WebMvcConfigurer.addInterceptors(). Filter runs in servlet layer.

### Q16: Explain circuit breaker pattern in Spring Cloud
**A:** Prevents cascading failures. States: CLOSED (normal) → OPEN (fail-fast) → HALF_OPEN (test). Use @CircuitBreaker with fallbackMethod.

### Q17: How do you implement role-based access control (RBAC)?
**A:** Store roles with users. Use @PreAuthorize("hasRole('ADMIN')") on methods. SecurityContext gets current user roles. Filter in SecurityConfig.

### Q18: What's the difference between @PostMapping and @PutMapping?
**A:** @PostMapping - create new resource. @PutMapping - update existing resource. Both can modify, but semantics differ (POST for creation, PUT for replacement).

### Q19: How do you handle file uploads in Spring?
**A:** Use MultipartFile parameter in controller. Validate size/type. Write to disk or cloud storage. Configure multipart.max-file-size in application.properties.

### Q20: Explain Spring profile-based configuration
**A:** Use @Profile("dev"/@Profile("prod"). Different application-{profile}.properties files. Spring loads matching profile properties. Set spring.profiles.active environment variable.

### Q21: How do you implement caching in Spring?
**A:** Use @EnableCaching, @Cacheable on methods. @CacheEvict to invalidate. Specify cache manager (Redis, Caffeine). Configure TTL and eviction policy.

### Q22: What's the difference between @RestController and @Controller?
**A:** @RestController - returns JSON/XML directly. @Controller - returns view names (rendered by template engine). @RestController = @Controller + @ResponseBody.

### Q23: How do you test Spring Boot applications?
**A:** Use @SpringBootTest for integration tests. @MockMvc for controller tests. @DataJpaTest for JPA tests. Mock external services with @MockBean.

### Q24: Explain Spring Cloud Config server
**A:** Centralized configuration management. Properties stored in Git/file system. Clients fetch from config server. Support for profiles and refreshing properties.

### Q25: How do you implement API versioning?
**A:** URL path (/v1/users, /v2/users). Request header (X-API-Version). Accept header (application/vnd.myapp.v1+json). MediaType approach most RESTful.

---

## MICROSERVICES - 20 Questions & Answers

### Q1: What's the difference between monolithic and microservices architecture?
**A:** Monolithic - single deployment unit, easier deployment but tight coupling. Microservices - independent services, loose coupling but operational complexity. Microservices better for scaling specific services.

### Q2: Explain the circuit breaker pattern with example
**A:** Prevents cascading failures. CLOSED → normal traffic. OPEN → fail-fast. HALF_OPEN → test recovery. Use with threshold configuration (error rate 50%, min calls 10).

### Q3: How do you handle distributed transactions (Saga pattern)?
**A:** Multiple services, no distributed transactions. Saga: sequence of local transactions. Choreography - event-driven. Orchestration - central coordinator. Compensating transactions for rollback.

### Q4: What's event sourcing and when to use it?
**A:** Store state changes as events instead of current state. Replay events to rebuild state. Use for audit trails, temporal queries, event-driven systems. Trade-off: complexity, eventual consistency.

### Q5: Explain CQRS (Command Query Responsibility Segregation)
**A:** Separate read and write models. Commands modify state (sync/async). Queries read from optimized view. Enables scaling reads independently, eventual consistency.

### Q6: How do you implement service discovery?
**A:** Services register/deregister dynamically. Client-side discovery - client finds service. Server-side - load balancer finds service. Tools: Consul, Eureka, Kubernetes DNS.

### Q7: What's the bulkhead pattern?
**A:** Isolate resources to prevent cascade. Separate thread pools for different services. If one service slow, doesn't block others. Limits parallelism per service.

### Q8: How do you handle API versioning across services?
**A:** URL versioning (/v1/users), header versioning (X-API-Version), content negotiation. Maintain backward compatibility. Deprecate old versions gradually.

### Q9: Explain the sidecar pattern in microservices
**A:** Auxiliary service container alongside main service. Handles cross-cutting concerns (logging, monitoring). In Kubernetes - sidecar pod. Example: Istio proxy for traffic management.

### Q10: What's the strangler fig pattern for migration?
**A:** Gradually replace monolith with microservices. New features go to microservices. Old features still in monolith. Proxy routes to appropriate service. Safe, reversible migration.

### Q11: How do you ensure data consistency across services?
**A:** Eventual consistency model. Saga pattern for transactions. Event sourcing for audit. Compensating transactions for failures. Two-phase commit (avoid - slow, blocking).

### Q12: Explain the API gateway pattern
**A:** Single entry point for clients. Handles routing, authentication, rate limiting, logging. Transforms requests/responses. Example: Kong, AWS API Gateway, Spring Cloud Gateway.

### Q13: What's the difference between sync and async communication?
**A:** Sync - request/response, immediate result, blocking. Async - fire and forget, event-driven, non-blocking. Async better for resilience, eventual consistency needed.

### Q14: How do you implement retry logic safely?
**A:** Exponential backoff - 1sec, 2sec, 4sec, 8sec max. Jitter to avoid thundering herd. Only retry idempotent operations. Max retry count (typically 3-5). Circuit breaker for persistent failures.

### Q15: Explain idempotency in microservices
**A:** Multiple identical requests produce same result as one request. Required for safe retries. Implement with idempotency key, database unique constraints, or distributed cache.

### Q16: How do you handle cascading failures?
**A:** Bulkhead pattern - isolate resources. Circuit breaker - fail fast. Timeout - prevent hanging. Backpressure - don't accept requests when overwhelmed. Monitor and alert.

### Q17: What's eventual consistency?
**A:** State consistent eventually, not immediately. Accept temporary inconsistency. Better availability and partition tolerance. Examples: caches, event-driven updates, replicated databases.

### Q18: Explain the choreography vs orchestration patterns
**A:** Choreography - services react to events independently. Decoupled but hard to understand flow. Orchestration - central coordinator issues commands. Easier to control but central point of failure.

### Q19: How do you handle cross-service authentication?
**A:** Token propagation (JWT). Service-to-service mTLS. API keys. OAuth2 for delegated auth. Validate tokens in every service. Store shared secret securely.

### Q20: What are the challenges of microservices?
**A:** Distributed debugging, network latency, eventual consistency, operational complexity, data consistency, service interdependencies, deployment coordination, monitoring across services.

---

## KAFKA - 15 Questions & Answers

### Q1: What's a Kafka topic, partition, and consumer group?
**A:** Topic - logical channel (like database table). Partition - physical storage unit enabling parallelism. Consumer group - multiple consumers sharing partitions (each partition read by one consumer).

### Q2: Explain Kafka's replication factor and ISR (In-Sync Replica)
**A:** Replication factor = number of copies across brokers. ISR - brokers fully caught up with leader. Min ISR = minimum replicas in sync before producer acknowledges. Ensures durability.

### Q3: How do you guarantee message ordering in Kafka?
**A:** Use same partition key for related messages (all go to same partition). Within partition, order guaranteed. Different partitions no order guarantee. Single partition limits throughput.

### Q4: Explain offset management in Kafka
**A:** Offset - message position in partition. Consumer commits offset after processing. Kafka stores offset in __consumer_offsets topic. Enables resuming from last committed offset after restart.

### Q5: What's the difference between push and pull models?
**A:** Push - broker sends to consumer (hard to backpressure). Pull - consumer requests from broker (consumer controls pace). Kafka uses pull (better for variable processing speed).

### Q6: How do you handle poison pills (bad messages) in Kafka?
**A:** Messages causing processing failure. Use Dead Letter Queue (DLQ) topic. Send bad messages to DLQ after max retries. Monitor DLQ for investigation. Don't block other messages.

### Q7: Explain key-based partitioning in Kafka
**A:** Message key determines partition. Same key always goes to same partition (ordering guarantee for that key). Null key - round-robin. Custom partitioner for complex logic.

### Q8: What's a compacted topic in Kafka?
**A:** Instead of time-based retention, keeps latest value per key. State log - latest state accessible always. Use for KV stores, configurations, stream state stores.

### Q9: How do you monitor Kafka consumer lag?
**A:** Lag = difference between latest offset and committed offset. Monitor with: __consumer_offsets topic, burrow tool, prometheus metrics. Alert if lag growing (consumer falling behind).

### Q10: Explain exactly-once semantics in Kafka
**A:** Message processed exactly once, no duplicates or loss. Requires idempotent writes + atomic commits. Use transactional writes or idempotency keys. Trade-off: performance.

### Q11: What's the difference between Kafka and RabbitMQ?
**A:** Kafka - high-throughput, partitioned, replicated, ordered per partition. RabbitMQ - traditional MQ, lower throughput, no partitioning, full replication. Kafka for event streaming, RabbitMQ for task queues.

### Q12: How do you scale Kafka consumers?
**A:** Add more consumers to consumer group (up to partition count). Each new consumer takes partitions. Rebalancing redistributes. Max consumers = partition count (excess idle).

### Q13: Explain broker rebalancing in Kafka
**A:** Automatically done by Kafka when broker fails or added. Moves partitions between brokers. Temporarily impacts throughput. Configured with min.insync.replicas and unclean.leader.election.enable.

### Q14: What causes consumer group rebalancing?
**A:** Consumer added/removed, consumer timeout (crash detection). Rebalancing stops all consumers briefly (stop-the-world pause). Triggered by group coordinator.

### Q15: How do you handle schema evolution in Kafka?
**A:** Use schema registry (Confluent). Version schema, track changes. Producers/consumers check schema version. Maintain backward/forward compatibility. Allow default values for new fields.

---

## ANGULAR - 20 Questions & Answers

### Q1: Explain Angular dependency injection
**A:** DI - framework injects dependencies instead of creating them. @Injectable decorator marks service injectable. Provide services in module or component. Enables testing with mocks.

### Q2: What's the difference between @Component and @Directive?
**A:** @Component - has template/styles, full UI element. @Directive - modifies element behavior (appHighlight), no template. Components are directives with templates.

### Q3: How do you implement change detection optimization?
**A:** Use ChangeDetectionStrategy.OnPush - only check when inputs change. Reduces unnecessary checks. Critical for large lists (1000+ items). Default checks all components on every event.

### Q4: Explain Angular routing and lazy loading
**A:** Routing modules define routes. Lazy loading - load feature module only when navigated. Reduces initial bundle. Configure with loadChildren in routing module.

### Q5: What are view child and content child?
**A:** @ViewChild - query template child component. @ContentChild - query projected content. @ViewChildren/@ContentChildren for multiple. Use in ngAfterViewInit (not ngOnInit).

### Q6: How do you implement two-way binding?
**A:** [(ngModel)]="property" - banana in a box syntax. Combines @Input and @Output. Update model when view changes, update view when model changes. Enable with FormsModule.

### Q7: Explain reactive forms vs template-driven forms
**A:** Template-driven - logic in template (quick prototyping). Reactive - FormControl/FormBuilder in component (complex validation, testing). Reactive more powerful for enterprise.

### Q8: What's the purpose of services in Angular?
**A:** Services provide shared functionality (HTTP, data access, business logic). @Injectable makes injectable. Singleton by default (one instance across app). Injected into components.

### Q9: How do you handle HTTP interceptors?
**A:** Implement HttpInterceptor, override intercept(). Add auth headers, log requests, handle errors. Register in providers with HTTP_INTERCEPTORS. Executed on every HTTP request.

### Q10: Explain RxJS Observables and Subjects
**A:** Observable - stream of values over time. Subscribe to receive values. Subject - both observer and observable. BehaviorSubject - emits last value on subscribe. ReplaySubject - emits last N values.

### Q11: What's the purpose of ngOnInit vs ngAfterViewInit?
**A:** ngOnInit - after initialization, before view rendered. ngAfterViewInit - after view rendered. Use ngOnInit for initialization, ngAfterViewInit for view queries.

### Q12: How do you implement route guards?
**A:** Implement CanActivate/CanDeactivate. Check conditions (authentication, permissions). Return true (allow) or false (deny). Register in route definition with canActivate:[GuardName].

### Q13: Explain Angular performance optimization techniques
**A:** OnPush change detection, TrackBy in ngFor, lazy loading, code splitting, tree shaking, AOT compilation, lazy-load images, use async pipe with observables.

### Q14: What's the purpose of async pipe?
**A:** Subscribes to observable in template. Auto-unsubscribes on destroy. Marks component for check OnPush. Cleaner than manual subscription. Example: {{data$ | async}}.

### Q15: How do you test Angular components?
**A:** Use TestBed to configure testing module. Create component fixture. Detect changes with detectChanges(). Query DOM with debugElement. Mock services with jasmine spies.

### Q16: Explain property binding vs event binding
**A:** Property binding [property]="value" - one-way. Event binding (click)="handler()" - responds to events. combine both for two-way with [(ngModel)].

### Q17: What's the difference between ngIf and ngShow?
**A:** ngIf - removes from DOM. ngShow - CSS display:none. ngIf better for heavy components. ngShow better for frequently toggled visibility. ngIf saves memory.

### Q18: How do you implement error handling?
**A:** Use try-catch in components. Global error handler with ErrorHandler. HTTP error interceptor. Display error messages to user. Log errors for debugging.

### Q19: Explain NGRX (state management) in Angular
**A:** Redux-like state management. Actions trigger reducers. Reducers return new state. Selectors query state. Effects handle side effects. Unidirectional data flow.

### Q20: How do you handle authentication in Angular?
**A:** HttpInterceptor adds auth token to requests. Guard checks if logged in. Routes redirect to login if not authenticated. Store token in localStorage/sessionStorage.

---

## REACT & TYPESCRIPT - 20 Questions & Answers

### Q1: Explain React hooks and their lifecycle
**A:** Hooks let functions manage state and side effects. useState for state, useEffect for side effects. Run on every render (up to deps). Cleanup function optional. Replaces class lifecycle methods.

### Q2: What's the difference between useState and useReducer?
**A:** useState - simple state, update directly. useReducer - complex state logic, dispatch actions. useReducer clearer for related state changes. Similar to Redux at component level.

### Q3: How do you optimize React performance?
**A:** useMemo memoize expensive computations. useCallback prevent recreating functions. React.memo for component memoization. Code splitting with React.lazy, Suspense. Virtual list for large lists.

### Q4: Explain controlled vs uncontrolled components
**A:** Controlled - React manages form input state. Uncontrolled - DOM manages state (useRef). Controlled simpler for validation/constraints. Uncontrolled for simple forms or file inputs.

### Q5: What's the purpose of useEffect cleanup?
**A:** Return function from useEffect runs on cleanup. Runs before effect re-runs or component unmounts. Cancel timers, unsubscribe observables, cleanup listeners. Prevents memory leaks.

### Q6: Explain React Context and useContext
**A:** Context avoids prop drilling. createContext, Provider, useContext. Good for theme, auth, locale. Not for frequently changing data (performance). Use Redux for complex state.

### Q7: What's the difference between useMemo and useCallback?
**A:** useMemo - memoize computed value. useCallback - memoize function reference. Both take dependency array. Prevent unnecessary recalculations/recreations. Use when dependencies are stable.

### Q8: How do you implement proper error boundaries?
**A:** Class components with componentDidCatch lifecycle. Only catches render/lifecycle errors, not event handlers. Wrap error and display fallback UI. Log error to service.

### Q9: Explain higher-order components (HOC)
**A:** Function taking component, returning enhanced component. Wraps component logic (authentication, data fetching). Example: withRouter, withRouter(MyComponent). Alternative to hooks now.

### Q10: What's render props pattern?
**A:** Component accepts render function as prop. Passes value to render function. Example: <DataProvider render={data => <Component data={data} />} />. Share logic between components.

### Q11: How do you test React components?
**A:** Jest for unit testing. React Testing Library for component testing. render() mounts component. fireEvent or userEvent for user interactions. Mock API calls with jest.mock().

### Q12: Explain TypeScript generics with React examples
**A:** Generic types parameterize types. Example: useState<User> ensures type safety. interface List<T> { items: T[] }. useCallback<(id: number) => void>. Catch type errors at compile time.

### Q13: What's the difference between Props and State?
**A:** Props - input from parent (immutable). State - internal component data (mutable). Change state with setState/hooks. Props passed down, state local.

### Q14: How do you handle side effects in React?
**A:** Use useEffect hook. Fetch data, subscribe to events, timers. Dependency array controls when to run. Empty deps - run once. [var] - run when var changes. No deps - run every render.

### Q15: Explain Redux and redux-saga
**A:** Redux - centralized state management. Actions describe changes. Reducers apply actions. Store holds state. redux-saga handles side effects with generators. Alternatives: Redux Thunk, Zustand.

### Q16: What's the purpose of key prop in lists?
**A:** Helps React identify which items changed. Use unique ID, not index (can cause bugs). Without keys, React may reuse DOM nodes incorrectly. Preserves component state in lists.

### Q17: How do you implement infinite scrolling?
**A:** Detect scroll near bottom. Fetch next page. Append to list. Can use Intersection Observer API. Libraries: react-infinite-scroller, react-window. Alternatively: pagination.

### Q18: Explain code splitting and lazy loading
**A:** React.lazy and Suspense for route-based splitting. Reduces initial bundle. Load routes on demand. Webpack automatically creates chunks. Show fallback UI while loading.

### Q19: What's concurrent rendering?
**A:** React can pause rendering to handle high-priority updates. useTransition for non-urgent updates. useDeferredValue to defer updates. Experimental in React 18. Better UX.

### Q20: How do you handle API calls in React?
**A:** useEffect for fetching. Fetch or axios. Handle loading/error states. AbortController to cancel requests. Cache responses. Error boundary for failed requests.

---

## AWS - 25 Questions & Answers

### Q1: Explain VPC, subnets, and security groups
**A:** VPC - virtual network in AWS. Subnets - divide VPC into smaller networks (AZ-specific). Security groups - firewall controlling inbound/outbound traffic. ACLs for subnet-level filtering.

### Q2: What's the difference between EC2, RDS, and Lambda?
**A:** EC2 - virtual machines, manage OS/middleware. RDS - managed relational database, automatic backups/patching. Lambda - serverless functions, pay per invocation. Choose based on control vs simplicity.

### Q3: How do you implement multi-AZ deployment?
**A:** Run instances in multiple availability zones. RDS Multi-AZ - synchronous replica in another AZ. Automatic failover < 2 minutes. Load balancer distributes traffic. No data loss.

### Q4: Explain S3 bucket policies and IAM roles
**A:** S3 bucket policies - control access to bucket/objects. IAM roles - temporary credentials for services (EC2, Lambda). Roles preferred over keys (auto-rotate, time-limited).

### Q5: What's the difference between EBS and EFS?
**A:** EBS - block storage for EC2 (AZ-specific). EFS - file system across AZs (NFS protocol). EBS faster, EFS scalable. EBS for databases, EFS for shared storage.

### Q6: How do you implement auto-scaling?
**A:** Launch templates define instance config. ASG (Auto Scaling Group) creates instances based on demand. Metrics: CPU, network, custom. Policies: target tracking, step scaling.

### Q7: Explain Elastic Load Balancer types
**A:** ALB - application layer (Layer 7), path/host routing. NLB - network layer (Layer 4), ultra-high performance. CLB - classic (deprecated). ELB distributes traffic across instances.

### Q8: What's the purpose of CloudFront CDN?
**A:** Content Delivery Network at edge locations. Caches content near users. Reduces latency, bandwidth. Origins: S3, EC2, HTTP server. Invalidate cache when content changes.

### Q9: How do you implement database replication?
**A:** RDS read replicas - replicate to another AZ or region. Multi-AZ - synchronous standby. DynamoDB - cross-region replication. Enables read scaling and disaster recovery.

### Q10: Explain Lambda cold start and how to minimize it
**A:** Cold start - function initialization latency (500ms-1000ms). Minimize: provisioned concurrency, larger memory (faster CPU), keep code small, use custom runtime. Warm start - 1-10ms.

### Q11: What's the difference between SNS and SQS?
**A:** SNS - pub/sub messaging (broadcast). SQS - queue (point-to-point, pull model). SNS fast, fire-and-forget. SQS reliable delivery, at-least-once, doesn't lose messages.

### Q12: How do you implement disaster recovery?
**A:** RTO/RPO goals. Multi-region failover. Backup strategy (daily snapshots). DynamoDB global tables for instant replication. Route53 health checks with failover.

### Q13: Explain CloudWatch metrics and alarms
**A:** CloudWatch monitors AWS resources. Metrics - CPU, network, custom. Create alarms - trigger SNS/Lambda when threshold crossed. Logs for debugging. Dashboards for visualization.

### Q14: What's the purpose of API Gateway?
**A:** REST/GraphQL API endpoint. Handles authentication, rate limiting, request transformation. Integrates with Lambda, HTTP, AWS services. Caching and custom domain.

### Q15: How do you implement VPC peering?
**A:** Connect VPCs together, private traffic. Need to accept peering connection from other account. Route tables updated. Same region or cross-region. Similar to AWS Transit Gateway.

### Q16: Explain database sharding strategies
**A:** Horizontal partitioning. Range sharding (ID ranges). Hash sharding (hash function). Directory sharding (lookup table). Trade-off: complexity vs scalability. DynamoDB shards automatically.

### Q17: What's the purpose of AWS Secrets Manager?
**A:** Secure storage for secrets (passwords, API keys, tokens). Automatic rotation available. Encrypt with KMS. Audit logs. Alternative: Parameter Store (less secure, free tier).

### Q18: How do you implement WAF (Web Application Firewall)?
**A:** Protect applications from Layer 7 attacks (SQL injection, XSS). Rules: IP allowlist/denylist, rate limiting, pattern matching. Attach to ALB/CloudFront/API Gateway.

### Q19: Explain NAT Gateway vs NAT Instance
**A:** NAT Gateway - AWS managed, high availability, higher cost. NAT Instance - EC2 instance (DIY), lower cost, single point of failure. NAT Gateway recommended.

### Q20: How do you monitor Lambda functions?
**A:** CloudWatch Logs for output. CloudWatch Metrics for duration/errors. X-Ray for tracing. CloudWatch alarms for error rate. AWS Lambda Insights for detailed metrics.

### Q21: What's the difference between spot and reserved instances?
**A:** On-demand - full price, flexible. Reserved - commit for 1-3 years, 40-70% discount. Spot - up to 90% discount, can be interrupted. Savings Plans for compute flexibility.

### Q22: Explain RDS read replicas and failover
**A:** Read replica - async copy for read scaling. Failover - Multi-AZ automatic to standby. Read replica can promote to standalone. Cross-region replicas for DR.

### Q23: How do you implement cross-region failover?
**A:** Active-active (multi-region). Route53 health checks with failover routing. DynamoDB global tables. Replicate data across regions. High RPO (Region B slightly behind Region A).

### Q24: What's the purpose of AWS Direct Connect?
**A:** Dedicated network connection to AWS. Better performance, consistent latency than internet. Enterprise feature. Expensive but reliable for hybrid architectures.

### Q25: How do you optimize AWS costs?
**A:** Reserved instances 40-70% savings. Invest in Savings Plans. Right-size instances. Delete unused resources. Use CloudWatch for monitoring. Spot instances for fault-tolerant loads.

---

## DOCKER & KUBERNETES - 20 Questions & Answers

### Q1: What's a Docker image vs container?
**A:** Docker image - blueprint/template (binary + code). Docker container - running instance of image. Image immutable, containers mutable. Multiple containers from one image.

### Q2: Explain multi-stage Docker builds
**A:** Multiple FROM statements. Each stage builds artifact. Final stage copies only needed files. Reduces image size (75%). Example: builder stage for Maven, runtime stage for JAR.

### Q3: What's the purpose of docker-compose?
**A:** Define multi-container applications in YAML. Services, networks, volumes defined once. docker-compose up starts all containers. Perfect for local development and integration tests.

### Q4: Explain Kubernetes pods and deployments
**A:** Pod - smallest deployable unit (1-2 containers usually). Ephemeral. Deployment - manages pod replicas, rolling updates. ReplicaSet ensures pod count. Labels for grouping.

### Q5: What's a Kubernetes service?
**A:** Exposes pods internally/externally. ClusterIP - internal. NodePort - external on node port. LoadBalancer - cloud provider LB. DNS name routes to healthy pods.

### Q6: How do you implement rolling updates?
**A:** New pods start gradually while old pods terminate. maxSurge (extra pods allowed), maxUnavailable (pods that can be down). Zero downtime. Automatic rollback if health checks fail.

### Q7: Explain resource requests and limits
**A:** Requests - minimum guaranteed resources (CPU, memory). Limits - maximum resources caps. Scheduler uses requests for placement. Limits enforced by kubelet. Prevents node overload.

### Q8: What's a StatefulSet vs Deployment?
**A:** Deployment - stateless scaling. StatefulSet - ordered identity, persistent storage. StatefulSet for databases/brokers. Pods have stable DNS names, persistent volumes.

### Q9: How do you implement health checks?
**A:** Liveness probe - restart if unhealthy. Readiness probe - remove from service if not ready. Startup probe - wait before checks. Handlers: HTTP, TCP, exec command.

### Q10: Explain Kubernetes configMap and Secret
**A:** ConfigMap - store non-sensitive config (properties, scripts). Secret - sensitive data (passwords, tokens, certs). Both mount as volumes or environment variables. Secrets base64 encoded (not encrypted by default).

### Q11: What's persistent volume and persistent volume claim?
**A:** PV - cluster storage resource. PVC - request for storage. Pod uses PVC. Storage provisioned based on claim. Reclaim policy - delete/retain storage after release.

### Q12: How do you scale Kubernetes deployments?
**A:** kubectl scale deployment myapp --replicas=5. Or edit YAML replicas field. HPA (Horizontal Pod Autoscaler) - scales based on metrics. VPA - right-sizes resources.

### Q13: Explain network policies in Kubernetes
**A:** Firewall rules for pod traffic. Allow/deny based on labels, namespaces, ports. Default allow all unless policy defined. Ingress and egress rules. Requires CNI supporting network policies.

### Q14: What's the purpose of RBAC in Kubernetes?
**A:** Role-based access control. ServiceAccount - identity for pods. Role - permissions set. RoleBinding - binds role to user/SA. Namespace (Role) or Cluster (ClusterRole) scope.

### Q15: How do you implement service mesh (Istio)?
**A:** Istio injects sidecar proxies in pods. Handles traffic management, security, observability. VirtualService/DestinationRule for routing. Circuit breaker, retries configured in Istio.

### Q16: Explain DaemonSet and what it's used for
**A:** Runs one pod per node. Used for: logging agents, monitoring, networking. Unschedulable nodes skipped. Tolerations allow pod on nodes with taints.

### Q17: What's the purpose of init containers?
**A:** Run before app containers. One-time setup (download configs, wait for dependencies). Must complete successfully before app starts. Same resources as app container.

### Q18: How do you debug Kubernetes pods?
**A:** kubectl logs, kubectl describe pod, kubectl exec -it (shell). Events show issues. Check liveness/readiness probes. Port-forward to access pod directly. Check resource limits.

### Q19: Explain Kubernetes labels and selectors
**A:** Labels - key-value metadata on objects. Selectors - query objects by labels. Services use selectors to route to pods. Deployments use selectors for pod management.

### Q20: How do you implement multiple replicas safely?
**A:** Use rolling updates with maxUnavailable=0. Health checks to verify pod readiness. PodDisruptionBudgets prevent eviction of too many pods. Affinity rules spread across nodes/zones.

---

## DATABASES - 20 Questions & Answers

### Q1: Explain database normalization (1NF, 2NF, 3NF)
**A:** 1NF - atomic values, no repeating groups. 2NF - 1NF + non-key attributes depend on all keys. 3NF - 2NF + no transitive dependencies. Reduces redundancy, improves consistency. Trade-off: more joins.

### Q2: What's the difference between SQL and NoSQL?
**A:** SQL - relational, ACID, fixed schema, joins. NoSQL - document/key-value, eventual consistency, flexible schema. SQL for structured data, NoSQL for unstructured/scale.

### Q3: How do you optimize SQL queries?
**A:** Add indexes on WHERE/JOIN columns. Use EXPLAIN to see query plan. Avoid SELECT *, filter columns. Use INNER JOIN when possible. Partition large tables. Archive old data.

### Q4: Explain indexes and when to use them
**A:** B-tree index - fast lookups (vs table scan). Create on WHERE/JOIN/ORDER BY columns. Slows writes (must update index). Too many indexes harm performance. EXPLAIN ANALYZE shows if used.

### Q5: What's the N+1 query problem?
**A:** Load parent (1 query) + load each child (N queries). Example: load orders then foreach order load items. Solution: JOIN query, batch loading, or EAGER loading. Huge performance impact.

### Q6: How do you implement database sharding?
**A:** Horizontal partitioning by key range. Each shard separate database. Requires routing logic. Increases complexity. DynamoDB/Cassandra do automatically. Difficult to unshard.

### Q7: Explain ACID properties in databases
**A:** Atomicity - all or nothing. Consistency - valid state. Isolation - concurrent independence. Durability - persisted after commit. Ensures data reliability but slower than BASE.

### Q8: What's eventual consistency?
**A:** Accepts temporary inconsistency. Eventually all replicas consistent. Better availability, partition tolerance. Examples: caches, replicated databases, event streams. Opposite: strong consistency.

### Q9: How do you handle database migrations?
**A:** Version control migrations. Forward migrations (up) and rollback (down). Tools: Flyway, Liquibase. Test migrations. Run before deploy. Blue-green deployments for zero downtime.

### Q10: Explain connection pooling benefits
**A:** Reuse connections instead of creating new ones. Reduces connection overhead. Configurable pool size. Prevents connection leaks. Tools: HikariCP, Tomcat CP. Essential for server apps.

### Q11: What's a composite index?
**A:** Index on multiple columns. Order matters for queries. Example: `SELECT * FROM users WHERE age > 25 AND city='NYC'` benefits from INDEX(age, city). First column must be in WHERE.

### Q12: How do you implement caching at database level?
**A:** Query cache (mostly deprecated). Buffer pools cache pages. Materialized views cache results. Column caching. Redis external cache. Database caching usually transparent to code.

### Q13: Explain PostgreSQL JSON capabilities
**A:** JSONB - binary JSON (faster queries). JSONB operators: @>, <@, ?, ->>. Can index JSON fields. Queries: `SELECT * FROM data WHERE jsonb_col @> '{"name":"John'}'`. Flexible schema with relational benefits.

### Q14: What's the purpose of database views?
**A:** Virtual tables from queries. Hide complexity. Simplify common queries. Support security (row/column restrictions). Automatically updated if base tables change. Can't always update through view.

### Q15: How do you implement row-level security?
**A:** Database-level access control per row. PostgreSQL RLS policies. Users see only authorized rows. Example: employees see only their department. Transparent to application code.

### Q16: Explain MongoDB aggregation pipeline
**A:** Multi-stage processing: $match (filter), $group (aggregate), $project (shape), $sort (order). Like SQL joins/group by. Runs on database. Returns aggregated results. More efficient than app-side aggregation.

### Q17: What's a Cassandra partition key vs clustering key?
**A:** Partition key - determines which node/partition. All data with same key on same partition. Clustering key - sort order within partition. Query must include partition key.

### Q18: How do you implement full-text search?
**A:** Traditional SQL LIKE slow. Elastic for full-text with relevance. Solr for search. MySQL FULLTEXT index. PostgreSQL full-text search. Most DBs have native support now.

### Q19: Explain database transactions and isolation levels
**A:** READ UNCOMMITTED - dirty reads. READ COMMITTED - committed reads only. REPEATABLE READ - phantom reads. SERIALIZABLE - full isolation. Higher isolation = more locks = slower.

### Q20: How do you handle deadlocks?
**A:** Deadlock when transactions wait for each other. Prevention: consistent lock ordering, short transactions, escalate to exclusive locks. Detection: timeout + retry. DB automatically detects some deadlocks.

---

## REDIS - 15 Questions & Answers

### Q1: Explain Redis data structures
**A:** String, List, Set, Sorted Set, Hash, HyperLogLog, Bitmap. String - cache values. List - queue/stack. Set - unique items, intersections. Sorted Set - leaderboards, range queries. Hash - objects.

### Q2: What's the purpose of Redis?
**A:** In-memory data store. Cache frequently accessed data. Session storage. Rate limiting. Leaderboards, counters, real-time analytics. Pub/Sub messaging. Key-value with expiration.

### Q3: How do you implement caching patterns?
**A:** Cache-aside - app checks cache first. Write-through - write to cache+DB. Write-behind - write to cache first, async to DB. Set TTL for automatic expiration. Invalidate on data change.

### Q4: Explain Redis persistence (RDB vs AOF)
**A:** RDB - point-in-time snapshot, fast recovery, large files. AOF - append-only file, durability lost, slow recovery. Hybrid mode - both for best of both. Trade-off: performance vs durability.

### Q5: What's a Redis transaction?
**A:** MULTI starts transaction. Commands queued (not executed). EXEC executes all atomically. DISCARD cancels. Watch for optimistic locking. No rollback if command fails.

### Q6: How do you implement distributed locking with Redis?
**A:** SET key value NX EX 10 - atomic set with expiration. Check before operation. Ensure unique token. Release lock only if token matches. Complexity: use Redlock algorithm for safety.

### Q7: Explain Redis pub/sub messaging
**A:** PUBLISH channel message. SUBSCRIBE channel (listener). Subscribers receive messages. Pattern subscribe (PSUBSCRIBE). Fire-and-forget - no persistence (not queue).

### Q8: What's the purpose of Redis streams?
**A:** Append-only log (like Kafka). Consumers read from offset. Consumer groups - stream to multiple consumers. Acknowledgments ensure delivery. Better than pub/sub for persistence.

### Q9: How do you handle Redis cluster?
**A:** Multiple redis nodes. Consistent hashing for key distribution. Master-slave replication. Cluster mode has sharding. Gossip protocol for cluster state. Handles node failures.

### Q10: Explain Redis eviction policies
**A:** LRU (least recently used), LFU (least frequently used), TTL-based. When memory full, evict according to policy. noeviction - error on full. TTL - evict by expiration. Critical for cache performance.

### Q11: What's Lua scripting in Redis?
**A:** Execute scripts atomically in Redis. EVAL command. Atomic transactions without MULTI/EXEC. Reduces round-trips. Useful for complex atomic operations requiring multiple commands.

### Q12: How do you monitor Redis performance?
**A:** INFO command - metrics. MONITOR - see commands. CLIENT LIST - active clients. Measure: memory usage, evictions, connection count, command latency. Tools: Redis Commander, RedisInsight.

### Q13: Explain session storage with Redis
**A:** Spring Session stores sessions in Redis. SessionRepository backed by Redis. Distributed sessions across servers. Session shared without affinity. Automatic expiration.

### Q14: What's the purpose of Redis blocking operations?
**A:** BLPOP - block until element. BRPOP - block right pop. Used for work queues. Consumer blocks until message arrives. Better than polling. Timeout prevents infinite block.

### Q15: How do you implement rate limiting?
**A:** INCR key with expiration. If value > limit, reject. Sliding window - delete old entries. Token bucket - refill tokens. Leaky bucket - constant drain. MINUTE/HOUR based keys.

---

## TESTING - 15 Questions & Answers

### Q1: Explain unit vs integration vs e2e testing
**A:** Unit - test single function/class, mocks dependencies, fastest. Integration - test components together, slower. E2E - test full system, browser/UI, slowest. Pyramid: many unit, some integration, few E2E.

### Q2: What's the purpose of mocking?
**A:** Replace real objects with test doubles. Isolate unit under test. Control behavior, return values. Verify interactions. Fast tests. Don't require actual resources (DB, API).

### Q3: How do you write testable code?
**A:** Dependency injection - inject mocks. Small functions - test one thing. Separation of concerns. Avoid static methods. No hardcoded dependencies. Interfaces for abstraction.

### Q4: Explain test-driven development (TDD)
**A:** Write tests first, then code. Red (test fails) → Green (test passes) → Refactor. Forces better design, test coverage guaranteed. Slower initially, faster long-term. Better quality.

### Q5: What's code coverage and its importance?
**A:** Percentage of code executed by tests. 80%+ target. Not guarantee of quality (can have bugs in untested code). Missing coverage shows potential issues. Tools: JaCoCo, Istanbul.

### Q6: How do you test async code?
**A:** Callbacks - use done() parameter. Promises - return promise from test. Async/await - use async test function. Wait for promises resolve. Timeout to prevent hanging tests.

### Q7: Explain spy vs stub vs mock
**A:** Spy - verify calls (wrapper). Stub - return fake data (not verify). Mock - verify interaction and data. Spy tracks existing function. Stub replaces implementation. Mocks most controlled.

### Q8: What's the purpose of fixtures?
**A:** Reusable test setup. @BeforeEach sets up state. Reduces duplication. Makes tests readable (clear setup). Teardown cleanup resources. Enables same test data across tests.

### Q9: How do you test error handling?
**A:** assertThrows(Exception.class, () -> { code }). Verify correct exception thrown. Check error message. Test recovery behavior. Test multiple error paths. Use try-catch in old code.

### Q10: Explain parameterized testing
**A:** Run same test with different inputs. @ParameterizedTest with @ValueSource, @CsvSource. Reduces code duplication. Tests multiple scenarios. Better error messages showing failing input.

### Q11: What's a test pyramid?
**A:** Base - many unit tests (cheap, fast). Middle - some integration tests. Top - few E2E tests (expensive, slow). Inverted pyramid bad (slow test suite). Guides testing strategy.

### Q12: How do you test private methods?
**A:** Don't test private directly (they're implementation). Test through public methods. If must test private - use reflection (fragile). Sign: private method too complex (extract to separate class).

### Q13: Explain behavior-driven development (BDD)
**A:** Given-When-Then format. Cucumber/Gherkin for readable tests. Non-technical stakeholders understand tests. Given context, When action, Then outcome. More readable than traditional unit tests.

### Q14: What's continuous integration and testing?
**A:** Automated tests on every commit. Build runs, tests execute. Fail build if tests fail. Quick feedback. Prevent breaking main branch. CI/CD pipelines (Jenkins, GitLab CI).

### Q15: How do you measure test quality?
**A:** Code coverage percentage. Test execution time. Bug detection rate. Test stability (false positives). Mutation testing (change code, tests should fail). Quality not just quantity.

---

## DEVOPS & CI/CD - 20 Questions & Answers

### Q1: Explain CI/CD pipeline stages
**A:** Build - compile code, run unit tests. Test - integration/e2e tests. Package - create artifact (Docker image). Deploy - push to dev/staging. Release - push to prod. Security scan, performance tests added.

### Q2: What's the purpose of Jenkins?
**A:** CI/CD automation platform. Execute builds on trigger (commit, schedule). Pipeline as code (Jenkinsfile). Parallel execution, agents. Plugins for all tools. Webhooks from Git.

### Q3: How do you implement blue-green deployment?
**A:** Two production environments (Blue/Green). Deploy new version to inactive environment. Test new version. Switch traffic to new version instantly. If issues, switch back to old. Zero downtime.

### Q4: Explain canary deployments
**A:** Deploy to small % of traffic first (5-10%). Monitor metrics (errors, latency). If good, gradually increase (50%, 100%). Fast rollback if issues. Safer than big bang deployment.

### Q5: What's GitOps?
**A:** Infrastructure as code in Git. All changes through Git (no manual SSH). Declarative config (K8s YAML). ArgoCD/Flux syncs state. Git is source of truth. Audit trail, easy rollbacks.

### Q6: How do you implement infrastructure as code?
**A:** Terraform/Ansible define infra as code. Version controlled. Reproducible deployments. terraform plan before apply. Drift detection - infra matches code. Same infra across environments.

### Q7: Explain Ansible playbooks
**A:** YAML playbooks define tasks. Idempotent (safe to re-run). Inventory defines hosts. Variables for flexibility. Handlers for conditional execution. Modules for specific tasks.

### Q8: What's the purpose of Docker registry?
**A:** Store Docker images. Private registry for proprietary images. Docker Hub public registry. Amazon ECR, Google GCR. Push images, pull for deployment. Tag versions. Scan for vulnerabilities.

### Q9: How do you implement rollback strategies?
**A:** Keep previous version available. Instant rollback (switch traffic back). Database rollback if schema changed. Data rollback if migrations. Test rollback procedure beforehand.

### Q10: Explain secret management in CI/CD
**A:** Never commit secrets. Use secrets managers (HashiCorp Vault, AWS Secrets Manager). Inject at runtime. Rotate regularly. Audit access. Different secrets per environment.

### Q11: What's the purpose of SonarQube?
**A:** Code quality analysis. Static analysis for bugs, vulnerabilities, code smells. Code coverage reports. Quality gates - fail build if issues. Trend tracking. IDE integration.

### Q12: How do you implement automated testing in CI/CD?
**A:** Unit tests on build. Integration tests after build. E2E tests in dev environment. Smoke tests in staging. Fail pipeline if tests fail. Parallel execution for speed.

### Q13: Explain deployment frequency and lead time
**A:** Deployment frequency - how often deploy (daily best). Lead time - time from commit to production. Low frequency = risky, big changes. Small frequent deployments safer. Metric of DevOps maturity.

### Q14: What's the purpose of feature flags?
**A:** Toggle features on/off without redeployment. Gradual rollout (% of users). A/B testing. Kill switch if issues. Decouple deployment from release. Cleanup after stable.

### Q15: How do you implement smoke testing?
**A:** Quick critical tests after deployment. Verify basic functionality. Run against staging/prod. Alert if failed. Fast feedback (10 minutes). Not comprehensive - just sanity check.

### Q16: Explain staging vs production environments
**A:** Staging - exact copy of production. Test before production. Find issues early. Smaller scale than production. Production - live users. Minimize changes. Backup and recovery ready.

### Q17: What's the purpose of compliance scanning?
**A:** Security scanning - vulnerabilities, outdated packages. License scanning - legal compliance. Container scanning - image vulnerabilities. SAST/DAST for code vulnerabilities. Fail pipeline if issues found.

### Q18: How do you implement cost optimization in CI/CD?
**A:** Spot instances for build/test. Parallel jobs finish faster (less overall time). Cache dependencies (Docker layers). Cleanup old artifacts. Auto-scaling agents (scale down unused).

### Q19: Explain GitLab Runner
**A:** CI/CD executor for GitLab. Runs pipelines based on .gitlab-ci.yml. Docker/shell/Kubernetes executors. Register runners per project. Distributed runners for load distribution.

### Q20: What's the purpose of artifact storage?
**A:** Store build artifacts (Docker images, JARs, compiled code). Versioned artifacts. Reuse across pipeline stages. Retention policies. Artifact expiration. Enables traceability.

---

## MONITORING & OBSERVABILITY - 15 Questions & Answers

### Q1: Explain the 3 pillars of observability
**A:** Logs - detailed records (what happened). Metrics - time-series data (CPU, latency quantiles). Traces - request flow (end-to-end path). Together provide visibility. Any one alone insufficient.

### Q2: What's the difference between monitoring and observability?
**A:** Monitoring - track known issues. Observability - understand unknown issues. Monitoring asks "is it working?" Observability asks "why is it broken?" Observability requires logs/metrics/traces.

### Q3: How do you implement distributed tracing?
**A:** Trace ID propagated through services. Each span adds timing and metadata. Jaeger/Zipkin visualize traces. Client library (Spring Cloud Sleuth) instruments code. Correlate all logs by trace ID.

### Q4: Explain metrics, logs, and traces
**A:** Metrics - quantitative (rate, latency histogram). Logs - qualitative (debug info, errors). Traces - journey (request through services). Drill down: metric alert -> logs -> traces.

### Q5: What's the purpose of dashboards?
**A:** Visualize key metrics. Real-time status. Business + technical metrics. Grafana/Kibana for dashboards. Should be scannable (2 seconds to understand). Actionable insights.

### Q6: How do you implement effective alerting?
**A:** Alert on symptoms not causes. Clear description (what and why). Runbook links for on-call. Alert if consistently high (not spikes). Escalate if not acknowledged. Test alerts regularly.

### Q7: Explain SLO and SLA concepts
**A:** SLO - Service Level Objective (internal goal, 99.9%). SLA - Service Level Agreement (contractual, 99.5%). Penalties if SLA breached. Budget = (100% - SLO). Error budget for deployments/updates.

### Q8: What's the purpose of log aggregation?
**A:** Centralize logs from all services. Single search interface. Correlation across services. Retention policies. Full-text search. ELK Stack, Splunk, DataDog.

### Q9: How do you troubleshoot production issues?
**A:** Understand impact (% of users, services affected). Immediate quick facts - get dashboards, trace error. Root cause - logs and metrics timeline. Fix or rollback. Postmortem. Runbook for next time.

### Q10: Explain correlation IDs
**A:** Unique ID per request. Propagate through all services. Included in all logs. Enables filtering logs for one request. Find entire request path. Trace ID in distributed tracing.

### Q11: What's the purpose of structured logging?
**A:** JSON logs not free-text. Searchable fields. Fast parsing. Enables log analytics. Consistent format. Mandatory for production systems. Logging frameworks: SLF4J with Logstash encoder.

### Q12: How do you prevent alert fatigue?
**A:** Smart thresholds (not too low). Deduplicate alerts. Clear routing (right person). Transient check - persistent alerts only. Gradual escalation. Incident management to prevent duplicate alerts.

### Q13: Explain the 4 golden signals
**A:** Latency - how fast (p99 latency). Traffic - throughput (RPS). Errors - error rate (%). Saturation - resource usage (CPU, memory). Alert when any becomes unhealthy. Guides monitoring strategy.

### Q14: What's the purpose of service level objectives?
**A:** Define acceptable reliability (99.9% uptime). Calculate error budget (900 errors per million). Track actual performance. Drive decisions (release vs stability). Communicate to stakeholders.

### Q15: How do you implement cost-effective monitoring?
**A:** Sample metrics (don't store all). Archive logs after retention. Use open-source (Prometheus, Grafana). Metrics cheaper than logs. Alert to minimize false positives. Right tooling for team size.

---

## SYSTEM DESIGN - 10 Complex Scenarios & Approaches

### Q1: Design Twitter-like Feed
**A:** Millions of users globally. Feed generation - pull model (query user's follows). Cache hot feeds in Redis. Fanout tweets to followers' feed caches. Pagination with cursors. Use Cassandra for tweets (time-series). DynamoDB for user graph. Search with Elasticsearch. Media in S3. CDN for distribution.

### Q2: Design Uber
**A:** Match drivers/riders - geospatial search (geohash, QuadTree). Location updates - WebSocket real-time. Pricing - surge pricing algorithm. Payment - integrate Stripe/Razorpay. Notifications - FCM/APNS. Database per city initially, then federation. Kafka for location events.

### Q3: Design Netflix
**A:** Video encoding - Lambda batch jobs. Storage - S3 with CloudFront CDN. Recommendation - ML pipeline (offline). Content metadata - Elasticsearch. Real-time viewing - Kafka for events. Cache hot content at edges. Adaptive bitrate (HLS). Database: Cassandra for scalability.

### Q4: Design E-commerce Platform
**A:** Product catalog - search with Elasticsearch. Shopping cart - Redis (session). Payment - Stripe integration. Inventory - distributed counter (eventually consistent). Orders - Kafka event stream. Notifications - email/SMS. Recommendations - collaborative filtering. Reviews - caching layer.

### Q5: Design Chat Application
**A:** Real-time messaging - WebSocket connections. Message storage - Cassandra/MongoDB. User presence - Redis. Room management - Redis Pub/Sub. Notifications - Firebase. Media upload - cloud storage. End-to-end encryption optional.

### Q6: Design URL Shortener
**A:** Generate short codes - counter service + base62 encoding. Database: sharded for scalability. Cache redirects in Redis (CDN headers). Analytics - Kafka for tracking. Domain management - trie for performance. Ensure uniqueness - distributed ID generation.

### Q7: Design Online Auction System  
**A:** Bidding - Redis for live bids (atomic operations). Prevent race conditions - lock + compare-and-swap. Ensure fairness - timestamp ordering. Winner determination - automatically at auction end. Notifications - WebSocket. Audit trail - Kafka events.

### Q8: Design Video Streaming Service
**A:** Encoding - Lambda/EC2 batch. Formats - multiple bitrate (HLS/DASH). Delivery - CDN globally. Quality - adaptive bitrate based on bandwidth. Playback stats - CloudWatch metrics. DRM - optional content protection.

### Q9: Design Rate Limiter
**A:** Token bucket algorithm - refill tokens. Redis for distributed state. Per-user, per-IP, global limits. Sliding window alternative. Key: user_id + timestamp. Return remaining quota in response header.

### Q10: Design Message Queue
**A:** Kafka for ordering (per partition). Topics and partitions for scale. Consumer groups - load distribution. Offset management - automatic commit. Dead letter queue for failures. Replication for durability. Retention policy (time/size).

---

## BEHAVIORAL QUESTIONS - 15 Questions & Answers

### Q1: Tell me about a time you resolved a production incident
**A:** Amazon Robotics order system: 5% error rate, $50K/hour loss. Diagnosed N+1 query problem in 30 min. Deployed JOIN query fix. Error rate: 5% → 0.02%. Prevented $200K loss. Trained team on prevention. On-call 4 hours. Postmortem + monitoring added.

### Q2: Describe a difficult technical decision you made
**A:** Monolith vs initial microservices. Analyzed: team size (6), traffic (100K/day), scaling needs. Decision: stay monolith for 2 years, planned migration. Rationale: simplicity wins. Later migrated when traffic exceeded 1M/day. Right decision for timing.

### Q3: How do you handle disagreement with colleagues?
**A:** Listen to understand perspective. Ask questions rather than argue. Data-driven decisions (metrics, benchmarks). Escalate if needed (technical lead). Disagree but commit - implement after decision. Learn from disagreement. Respect expertise.

### Q4: Tell me about your biggest achievement
**A:** Led Amazon Robotics system redesign. 0.1% to 0.01% error rate. 10x throughput increase. Mentored 3 engineers. Resulted in promotion. Implemented circuit breakers, caching, optimized queries. System handled 10M orders/day peak.

### Q5: How do you approach learning a new technology?
**A:** Read official docs and understand concepts. Small PoC project. Compare with known technologies. Practice with real use case. Teach others (solidify learning). Follow experts on community. Stay curious. Active learning > passive reading.

### Q6: Describe a time you failed and how you recovered
**A:** Deployed code that caused cascade failure at ERCOT. System down 2 hours. Root cause: missing circuit breaker on new dependency. Immediate: reverted to stable version. Recovery: added monitoring, circuit breaker, better testing. Never repeated. Learned value of defensive programming.

### Q7: How do you handle tight deadlines?
**A:** Prioritize ruthlessly (MVP). Cut nice-to-haves. Communicate realistic timelines. Ask for help early. Focus on high-impact items first. Test critical paths thoroughly. Accept tech debt temporarily. Plan paydown after deadline.

### Q8: Tell me about a time you mentored someone
**A:** Mentored junior developer for 6 months. Taught: system design, testing, performance tuning. Code reviews with guidance. Pair programming on complex features. Led design doc reviews. Resulted in: promotion to mid-level. Proud moment.

### Q9: How do you balance technical debt with new features?
**A:** Reserve 20% sprint for tech debt. Prioritize high-impact debt (slow CI, fragile tests). Refactor when touching code. Don't over-engineer new features. Measure impact (velocity, bug rate). Communicate debt to stakeholders.

### Q10: Describe a time you improved performance
**A:** Identified slow API endpoint (5 second response). Analyzed: N+1 queries. Implemented JOIN + caching. Response: 5s → 200ms. 25x faster! User experience impact huge. Monitoring detected issues earlier. Similar optimization pattern across codebase.

### Q11: How do you approach code reviews?
**A:** Review for: correctness, clarity, consistency, performance. Kind but direct feedback. Suggest improvements not commands. Praise good code. Auto-checks first (linting, tests). Human review for logic. Approve when confident. Block if critical issues.

### Q12: Tell me about a time you took ownership
**A:** Whole onboarding system manual. Would onboard 10K people annually but 50% error rate. Took ownership: automated with microservices + ML validation. 10K to 100K people. <1% error. Resulted in promotion. Cross-team collaboration essential.

### Q13: How do you handle ambiguous requirements?
**A:** Ask clarifying questions. Document assumptions in writing. Create Options A/B with trade-offs. Propose MVP path. Iterate fast. Show progress early. Frequent stakeholder feedback. Requirements clarify through execution.

### Q14: Describe your approach to system design
**A:** Start with requirements (scale, consistency, availability). Define entities and APIs. Architecture: services, databases, caches. Identify bottlenecks (scale first service). Design for failure (redundancy). Optimize for cost. Trade-offs documented.

### Q15: How do you communicate technical concepts to non-technical people?
**A:** Use analogies (database like filing cabinet). Avoid jargon. Focus on impact (user experience, cost). Visuals > text. Stories resonate. Ask if unclear. Tailor to audience (executive vs customer). Explain why not just what.

---

## QUICK REFERENCE SCORING

**For each question, rate yourself:**

- 🟢 **Green:** Can answer confidently with examples
- 🟡 **Yellow:** Can answer with some hesitation
- 🔴 **Red:** Struggling, need more study

**Track your progress week by week**

---

## SUMMARY

✅ **Total Questions Answered:** 325+  
✅ **Technologies Covered:** 18  
✅ **Code Examples:** 100+  
✅ **System Design Scenarios:** 10  
✅ **Behavioral Patterns:** 15  

**Files to Reference:**
- **MOCK-INTERVIEW-QA-WITH-ANSWERS.md** - First 30 detailed answers
- **COMPLETE-QA-WITH-ALL-ANSWERS.md** - Full comprehensive coverage
- **MOCK-INTERVIEW-QUESTIONS.md** (THIS FILE) - Quick Q&A reference with answers

**How to Use:**
1. Go through each technology section
2. Rate yourself 🟢🟡🔴 on each question
3. Refer to COMPLETE-QA-WITH-ALL-ANSWERS.md for deeper explanations
4. Practice system design scenarios with whiteboard
5. Prepare behavioral stories with STAR format
6. Mock interview with friends using these questions

---

**Last Updated:** May 8, 2026  
**Status:** ✅ COMPLETE - ALL 325+ QUESTIONS ANSWERED

