# Top 100 Frequently Asked Q&A – Java Full Stack Engineer (18 Years)

Generated from Interviews/16-FullStack-Interview-QA.md.
This file is a curated set of the most interview-relevant 100 questions for senior Java full stack / lead roles.

## Coverage

- Leadership and Behavioral
- Core Java and Concurrency
- Spring Boot, REST, and Security
- JPA, Database, and Resilience
- Microservices and Integration Patterns
- Angular and Frontend
- Cloud, AWS, and DevOps
- System Design and NFRs

---

## Leadership and Behavioral (10)

1. Q: Tell me about yourself.
   A: I have 18 years in Java full-stack engineering, with strong backend focus on Spring Boot microservices, Angular frontend, cloud delivery, and production reliability.
   Example: I worked on compliance-heavy ERCOT workflows and high-throughput Amazon-style event systems.


2. Q: What is your biggest strength?
   A: End-to-end ownership from design to production stabilization.
   Example: I design API contracts, implement services, support deployment, and handle incident RCA.


3. Q: Why senior role now?
   A: I bring hands-on technical depth plus architecture and incident leadership.
   Example: I can reduce both delivery risk and production failure rate.


4. Q: How do you prioritize work?
   A: Business impact first, then production risk, dependencies, and deadlines.
   Example: Sev-1 reliability fix comes before non-critical UI enhancement.


5. Q: How do you handle conflict in a team?
   A: I align everyone on facts, options, trade-offs, and measurable outcomes.
   Example: For architecture disagreements, I compare latency, cost, and maintainability.


6. Q: Leadership style?
   A: Hands-on, transparent, and outcome-focused.
   Example: I unblock dependencies quickly and keep decision ownership clear.


7. Q: How do you mentor engineers?
   A: Through design reviews, pair programming, and gradual ownership transfer.
   Example: Junior dev starts with bug fixes, then owns a feature module.


8. Q: How do you communicate with non-technical stakeholders?
   A: I use risk, timeline, cost, and customer impact language.
   Example: “This delay affects release by 2 days and risks billing accuracy.”


9. Q: How do you handle scope change mid-sprint?
   A: Re-estimate impact, re-prioritize, and align trade-offs with stakeholders.
   Example: Move nice-to-have stories to next sprint.


10. Q: What is release success?
    A: Stable production and expected business outcome with healthy SLOs.
    Example: No Sev-1 incidents and target throughput met post-release.


---

## Core Java and Concurrency (20)

21. Q: Why Java for enterprise?
    A: Stability, mature ecosystem, strong tooling, and JVM performance.
    Example: Long-lived financial/compliance systems run reliably on Java stacks.


22. Q: Encapsulation in practical terms?
    A: Hide internal state, expose controlled behavior.
    Example: `Account.deposit()` validates rules before updating balance.


23. Q: Abstraction vs encapsulation?
    A: Abstraction hides complexity; encapsulation protects state.
    Example: Interface abstracts payment; private fields encapsulate card data.


24. Q: Inheritance vs composition?
    A: Prefer composition for flexibility and lower coupling.
    Example: `OrderService` uses `PricingStrategy` instead of deep class hierarchy.


25. Q: Polymorphism use case?
    A: One interface, multiple implementations.
    Example: `NotificationService` -> Email/SMS/Push implementations.


26. Q: ArrayList vs LinkedList?
    A: ArrayList faster for random access; LinkedList better for frequent middle inserts/deletes.
    Example: API response lists usually prefer ArrayList.


27. Q: HashMap vs TreeMap?
    A: HashMap unordered O(1) average; TreeMap sorted O(log n).
    Example: TreeMap useful for range lookups.


28. Q: HashMap vs ConcurrentHashMap?
    A: HashMap is not thread-safe; ConcurrentHashMap handles concurrent operations safely.
    Example: Shared in-memory counters in multi-thread service.


29. Q: HashMap vs Hashtable?
    A: Hashtable is legacy synchronized and less preferred.
    Example: Use ConcurrentHashMap for modern concurrent map usage.


30. Q: equals/hashCode contract?
    A: Equal objects must produce same hashCode.
    Example: Otherwise duplicates appear in HashSet unexpectedly.


31. Q: Why String immutable?
    A: Security, caching, thread safety.
    Example: Safe as map key and in auth token processing.


32. Q: What is String pool?
    A: JVM stores string literals to reuse memory.
    Example: Same literal points to shared instance.


33. Q: Comparable vs Comparator?
    A: Comparable defines natural order; Comparator defines external/custom order.
    Example: Sort Employee by salary descending with Comparator.


34. Q: What is Optional?
    A: Wrapper to represent potential absence of value.
    Example: `Optional<User>` for repository lookup.


35. Q: Checked vs unchecked exceptions?
    A: Checked must be handled/declared; unchecked are runtime errors.
    Example: IOException checked, IllegalArgumentException unchecked.


41. Q: What is record in Java?
    A: Compact immutable data carrier.
    Example: `record UserDto(Long id, String name) {}`


42. Q: What is Java Memory Model?
    A: Rules for visibility and ordering between threads.
    Example: volatile ensures updated value visibility.


43. Q: volatile vs synchronized?
    A: volatile for visibility only; synchronized for atomicity + visibility.
    Example: Counter increment needs synchronized/atomic, not only volatile.


44. Q: Deadlock?
    A: Two or more threads wait forever on each other’s locks.
    Example: Lock order mismatch A->B and B->A.


45. Q: Deadlock prevention?
    A: Consistent lock order, lock timeout, smaller critical sections.
    Example: Lock resources by sorted ID.


---

## Spring Boot, REST, and Security (15)

61. Q: Why Spring Boot?
    A: Fast bootstrap and production-ready features.
    Example: Actuator endpoints for health and metrics.


62. Q: @Controller vs @RestController?
    A: @RestController returns body directly for APIs.
    Example: JSON endpoints for Angular clients.


63. Q: Constructor injection advantage?
    A: Explicit dependencies and better testability.
    Example: Easy mocking in unit tests.


64. Q: Bean scopes?
    A: singleton, prototype, request, session.
    Example: Stateless service usually singleton.


65. Q: What is Spring Actuator?
    A: Operational endpoints for monitoring and health.
    Example: `/actuator/health` for readiness checks.


66. Q: Global exception handling pattern?
    A: `@ControllerAdvice` with standardized error model.
    Example: errorCode + message + correlationId.


67. Q: Input validation?
    A: Bean validation annotations plus centralized handling.
    Example: `@NotBlank`, `@Size` for request DTO.


68. Q: DTO vs entity?
    A: DTO for API contract; entity for persistence model.
    Example: Keep DB fields hidden from public API.


69. Q: Idempotency in REST?
    A: Repeated request should produce same final state.
    Example: Payment create API with idempotency key.


70. Q: PUT vs PATCH?
    A: PUT full replacement; PATCH partial update.
    Example: PATCH `/user/123` to update email only.


71. Q: API versioning approach?
    A: Backward compatibility + deprecation timeline.
    Example: `/api/v1/orders` and `/api/v2/orders`.


72. Q: Pagination best practice?
    A: Cursor/offset + metadata response.
    Example: `nextCursor` for large datasets.


73. Q: CORS handling?
    A: Configure backend to allow trusted origins/methods.
    Example: Permit Angular app origin only.


74. Q: JWT flow?
    A: Authenticate user, issue token, validate on each request.
    Example: Bearer token checked by filter.


75. Q: OAuth2 role?
    A: Standard authorization framework often issuing JWT tokens.
    Example: External identity provider integration.


---

## Data Access, JPA, and Resilience (10)

81. Q: N+1 query issue?
    A: Excessive child queries from lazy loading patterns.
    Example: Fetch join prevents per-row extra query.


82. Q: JPA fetch strategy?
    A: Choose lazy by default, optimize with targeted eager/fetch joins.
    Example: Use projection for list endpoints.


83. Q: @Transactional pitfalls?
    A: Long transaction scope causes lock contention and latency.
    Example: Avoid external HTTP calls inside transaction.


84. Q: Flyway/Liquibase why?
    A: Versioned schema changes in CI/CD.
    Example: Track DB migration history per release.


85. Q: Retry policy best practice?
    A: Retry transient errors only, with exponential backoff and jitter.
    Example: Don’t retry business validation errors.


86. Q: Circuit breaker purpose?
    A: Fail fast on unhealthy dependency to protect system.
    Example: Open breaker after repeated timeout failures.


87. Q: Bulkhead pattern?
    A: Isolate resources per dependency to limit blast radius.
    Example: Separate thread pool for external payment provider.


88. Q: Timeout strategy?
    A: Dependency-specific timeout budget tied to SLO.
    Example: 200 ms for cache, 2s for third-party API max.


89. Q: Rate limiting use case?
    A: Protect service from abuse or spikes.
    Example: Token bucket per client key.


90. Q: Correlation ID usage?
    A: Trace one request across microservices and logs.
    Example: Propagate `X-Correlation-Id` header end-to-end.


---

## Microservices and Integration Patterns (10)

91. Q: Service discovery?
    A: Dynamic endpoint resolution in distributed runtime.
    Example: Consumer discovers healthy service instances.


92. Q: API gateway value?
    A: Centralized routing, auth, throttling, and policies.
    Example: Single entry point for all frontend calls.


93. Q: Monolith vs microservices decision?
    A: Choose based on domain complexity, scale, and team boundaries.
    Example: Start modular monolith for early stage products.


94. Q: Strangler migration pattern?
    A: Gradually replace monolith modules with services.
    Example: Route one endpoint group to new service first.


95. Q: Saga pattern?
    A: Manage distributed transactions with compensating actions.
    Example: Cancel inventory reservation if payment fails.


96. Q: Orchestration vs choreography?
    A: Orchestration uses central coordinator; choreography uses events between services.
    Example: Order workflow orchestrator service.


97. Q: Eventual consistency?
    A: Data converges over time across services.
    Example: Analytics dashboard updates shortly after order creation.


98. Q: Outbox pattern?
    A: Persist event and business data atomically.
    Example: Order row + outbox row in same DB transaction.


99. Q: Contract testing purpose?
    A: Detect breaking API/provider changes early.
    Example: Consumer-driven contract in CI.


100. Q: Idempotent consumer?
     A: Handles duplicate messages safely.
     Example: Use event ID dedup table.


---

## Angular and Frontend (15)

111. Q: Why Angular in enterprise?
     A: Structured framework with DI, modules, and strong conventions.
     Example: Easier onboarding across large teams.


112. Q: Component vs service responsibilities?
     A: Component handles UI; service handles business/API logic.
     Example: Product page uses ProductService for data.


113. Q: constructor vs ngOnInit?
     A: constructor for DI; ngOnInit for runtime initialization.
     Example: API fetch in ngOnInit.


114. Q: Important lifecycle hooks?
     A: OnInit, OnChanges, AfterViewInit, OnDestroy.
     Example: Unsubscribe in OnDestroy.


115. Q: Reactive forms benefit?
     A: Better control for complex validations and dynamic forms.
     Example: Multi-step onboarding with conditional fields.


116. Q: Template forms vs reactive forms?
     A: Template forms simpler; reactive forms scalable for enterprise complexity.
     Example: Choose reactive for large compliance forms.


117. Q: HTTP interceptor use?
     A: Add tokens, centralize error handling/logging.
     Example: Attach Bearer token automatically.


118. Q: Route guards use case?
     A: Block unauthorized route access.
     Example: Admin-only pages protected by role guard.


119. Q: switchMap vs mergeMap?
     A: switchMap cancels stale requests; mergeMap keeps parallel requests.
     Example: Search box uses switchMap.


120. Q: concatMap use case?
     A: Preserve order of async operations.
     Example: Sequential update API calls.


121. Q: debounceTime use case?
     A: Reduce request flood from rapid input.
     Example: 300ms delay for search query calls.


122. Q: Angular memory leak causes?
     A: Unsubscribed streams and long-lived references.
     Example: Event subscription not cleaned on component destroy.


123. Q: Memory leak prevention?
     A: async pipe or takeUntil pattern.
     Example: Subject-based destroy notifier.


124. Q: OnPush strategy benefit?
     A: Reduced change detection overhead and better performance.
     Example: Dashboard with many widgets.


125. Q: trackBy in ngFor?
     A: Avoid full DOM rerender for list changes.
     Example: Table row updates by ID.


---

## Cloud, AWS, and DevOps (10)

141. Q: EC2 vs ECS vs EKS?
     A: EC2 gives max control, ECS simplifies container ops, EKS provides Kubernetes ecosystem.
     Example: ECS for moderate complexity microservices.


142. Q: Why S3?
     A: Durable, scalable object storage for files and logs.
     Example: Store report exports and audit files.


143. Q: IAM best practice?
     A: Least privilege, role-based access, and regular review.
     Example: Separate role per service.


144. Q: CloudWatch usage?
     A: Collect metrics, logs, and alarms.
     Example: Alert on 5xx error rate spikes.


145. Q: Autoscaling strategy?
     A: Scale on meaningful signals like CPU, queue depth, latency.
     Example: Scale Kafka consumers by lag threshold.


146. Q: Infrastructure as Code value?
     A: Repeatable, versioned, auditable environment provisioning.
     Example: Terraform for dev/stage/prod parity.


147. Q: Docker benefit?
     A: Consistent runtime packaging across environments.
     Example: Same image runs in test and prod.


148. Q: Kubernetes value?
     A: Orchestration, autoscaling, self-healing, rolling deployment.
     Example: Auto-restart unhealthy pods.


149. Q: CI/CD key stages?
     A: Build, test, security, quality gate, deploy, verify.
     Example: Fail pipeline if integration tests fail.


150. Q: Artifact repository role?
     A: Store immutable build artifacts for traceability.
     Example: Promote same artifact from stage to production.


---

## System Design and NFRs (10)

191. Q: How do you start system design interview?
     A: Clarify scope and NFRs first, then components, APIs, data, scaling, and failures.
     Example: Ask for traffic, peak RPS, latency targets, compliance constraints.


192. Q: Top NFRs you prioritize?
     A: Availability, latency, throughput, security, compliance, operability.
     Example: Compliance-heavy systems prioritize traceability over raw speed.


193. Q: High availability strategy?
     A: Multi-instance stateless services, health checks, failover.
     Example: Load balancer routes only to healthy instances.


194. Q: Resilience strategy?
     A: Timeout, retry budget, circuit breaker, bulkhead, fallback.
     Example: External API outage does not crash whole user flow.


195. Q: Observability strategy?
     A: Correlated logs, metrics, traces, and SLO-based alerts.
     Example: Trace pinpoints slow dependency causing p95 spike.


196. Q: ERCOT one-minute answer?
     A: Secure workflow platform with role-based Angular UI, Spring Boot APIs, Oracle transactions, and full auditability of every transition.
     Example: Compliance reporting driven from immutable audit data.


197. Q: Amazon one-minute answer?
     A: Kafka-based event-driven services designed for burst traffic, low latency, and safe failure handling.
     Example: Consumer scaling + partition fixes reduced lag under peak load.


198. Q: Biogen/Dell one-minute answer?
     A: Biogen focused on regulated integrity and traceability; Dell focused on PLM integration consistency across ERP/MES.
     Example: Reconciliation/replay controls improved downstream data quality.


199. Q: Tough incident STAR short answer?
     A: During peak load latency spike, I stabilized via fallback/timeout controls, fixed query bottlenecks, then added preventive load-test gates and alerts.
     Example: Error rate dropped and SLA recovered in same incident window.


200. Q: Final interview closing statement?
     A: I’m a hands-on senior full-stack engineer who can design, build, and stabilize business-critical systems with strong NFR ownership and measurable outcomes.
     Example: I can contribute immediately as Lead/Staff in both architecture and delivery execution.


