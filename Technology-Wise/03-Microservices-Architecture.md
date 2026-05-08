# MICROSERVICES ARCHITECTURE - INTERVIEW Q&A
# Service Design, Communication, Patterns | 18 Years Experience

---

## Q1: Explain Microservices Architecture - Benefits and challenges.

**A:**

**Microservices** = Small, independent, deployable services that communicate over network.

### Benefits at Amazon Robotics

```
Scalability: Scale only robot-tracking service when load increases
            Robot Service: 5 instances
            Warehouse Service: 2 instances
            Notification Service: 1 instance

Deployment: Deploy robot service separately (no need to release entire system)
            Robot service update: 5 minutes
            Other services: unaffected

Technology Freedom: Different teams can choose tech stack
            Robot Service: Java + Spring Boot
            Analytics: Python + Django
            Mobile: Node.js

Resilience: One service down doesn't crash entire system
            Notification service down → warehouse still operates
            (Send notifications to queue, retry later)
```

### Challenges at ERCOT

```
Complexity: Distributed debugging is hard
            Issue: Grid data missing
            Root cause: Grid service → Notification service → Kafka → Message lost?
            Debugging time: 4 hours (vs 20 minutes in monolith)

Network Latency: More round trips
            Monolith: Grid service calls frequency service (in-process): <1ms
            Microservices: Grid service calls frequency service (network): 10-50ms

Data Consistency: Each service has its own database
            Update frequency in grid DB and notify other services
            What if notification service fails after grid service updates?
            Distributed transaction problem → use Saga pattern

Deployment Complexity: Deploy multiple services coordinated
            Deploy grid service → deploy frequency service → deploy notifier
            One fails → entire deployment fails
            Need orchestration: Kubernetes, Docker Compose
```

### Architecture Example - ERCOT

```
┌─────────────────────────────────────────────────┐
│  API Gateway (auth, rate limiting, routing)     │
└─────────────────────────────────────────────────┘
            │        │         │         │
            ↓        ↓         ↓         ↓
        ┌───────┬──────────┬────────┬──────────┐
        │ Grid  │Frequency │Forecast│Notifier  │
        │Service│ Service  │Service │Service   │
        └───────┴──────────┴────────┴──────────┘
         Spring │Spring    │Python  │Spring
         Boot   │Boot      │Django  │Boot
            │       │        │        │
            ↓       ↓        ↓        ↓
        ┌───────┬──────────┬────────┬──────────┐
        │Grid   │Frequency │Weather │Audit     │
        │DB     │DB        │DB      │DB        │
        │MySQL  │Oracle    │Mongo   │Postgres  │
        └───────┴──────────┴────────┴──────────┘

        Services communicate via:
        - REST APIs (synchronous)
        - Kafka (async events)
```

---

## Q2: API Gateway - Why needed? What does it do?

**A:**

**API Gateway** = Single entry point for all client requests. Sits between clients and microservices.

### Responsibilities

```java
// API Gateway implementation with Spring Cloud Gateway
@Configuration
public class GatewayRoute Configuration {

    @Bean
    public RouteLocator routes(RouteLocatorBuilder builder) {
        return builder.routes()
            // Route 1: /grid/* → Grid Service
            .route("gridRoute", r -> r
                .path("/grid/**")
                .filters(f -> f.stripPrefix(1))
                .uri("http://grid-service:8080"))

            // Route 2: /frequency/* → Frequency Service
            .route("frequencyRoute", r -> r
                .path("/frequency/**")
                .filters(f -> f.stripPrefix(1))
                .uri("http://frequency-service:8080"))

            .build();
    }
}

// What gateway does:

// 1. AUTHENTICATION - Validate JWT before forwarding
@Component
public class JwtAuthenticationGatewayFilter {
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        String path = exchange.getRequest().getURI().getPath();

        // Public endpoints - no auth needed
        if (path.startsWith("/auth/") || path.startsWith("/health")) {
            return chain.filter(exchange);
        }

        // Protected endpoints - validate JWT
        String token = exchange.getRequest().getHeaders().getFirst("Authorization");
        if (token == null || !jwtValidator.isValid(token)) {
            return handleAuthError(exchange);  // 401 Unauthorized
        }

        return chain.filter(exchange);
    }
}

// 2. RATE LIMITING - Prevent abuse
@Configuration
public class RateLimitingGatewayFilter {

    @Bean
    public GatewayFilter rateLimitFilter() {
        return (exchange, chain) -> {
            String clientId = exchange.getRequest().getHeaderValues("X-Client-Id")
                .stream().findFirst().orElse("unknown");

            // Allow 100 requests per minute per client
            if (rateLimiter.allowRequest(clientId)) {
                return chain.filter(exchange);
            } else {
                exchange.getResponse().setStatusCode(HttpStatus.TOO_MANY_REQUESTS);
                return exchange.getResponse().writeWith(Mono.empty());
            }
        };
    }
}

// 3. REQUEST LOGGING - Track all requests
//POST /grid/update 200 OK 45ms
//GET /frequency/TX 200 OK 23ms
//POST /forecast 400 Bad Request 5ms (validation error)

// 4. LOAD BALANCING - Distribute across service instances
//Request for /grid/data
//  → check health of grid-service instances
//  → grid-service-1: healthy (5% load)
//  → grid-service-2: healthy (8% load)
//  → Forward to grid-service-1 (least loaded)

// 5. CIRCUIT BREAKING - Prevent cascading failures
//Frequency service down → too many timeout errors
//Circuit breaker OPENS → stop sending requests
//Return 503 Service Unavailable with fallback
//After 30 seconds → try again (HALF_OPEN state)
//If success → CLOSE circuit, resume normal operation
```

### Real Event Flow

```
Client Request: POST /api/grid/update
    │
    ├─ API Gateway receives request
    │  ├─ Extract JWT token from Authorization header
    │  ├─ Validate JWT (exp, signature, roles)
    │  ├─ Get client ID from header
    │  ├─ Check rate limit: 45/100 requests allowed ✓
    │  ├─ Route to Grid Service
    │  └─ Log: "POST /api/grid/update from client X at timestamp"
    │
    ├─ Load Balancer chooses instance
    │  ├─ Check health: grid-service-1 (5% load), grid-service-2 (12% load)
    │  └─ Route to grid-service-1 (least loaded)
    │
    ├─ Grid Service processes
    │  ├─ Validate input
    │  ├─ Update database
    │  ├─ Publish event to Kafka
    │  └─ Return 201 Created
    │
    └─ Response goes back through Gateway
       ├─ Add response headers (X-Response-Time: 45ms)
       ├─ Log response: "POST /api/grid/update 201 Created 45ms"
       └─ Send to client
```

---

## Q3: Service-to-Service Communication - Sync vs Async.

**A:**

### Synchronous (REST, gRPC) - Immediate response

```java
// Grid Service calls Frequency Service synchronously
@Service
public class GridService {

    @Autowired
    private RestTemplate restTemplate;  // Synchronous HTTP client

    public void updateGridWithFrequency(String region) {
        // 1. Grid Service calls Frequency Service
        ResponseEntity<FrequencyData> response = restTemplate.getForEntity(
            "http://frequency-service/api/frequency/" + region,
            FrequencyData.class
        );

        // Blocks here until response received (or timeout)
        FrequencyData frequency = response.getBody();

        // 2. Update grid with frequency
        GridData grid = new GridData(region, frequency.getValue());
        gridRepository.save(grid);

        // 3. Return to client
        return grid;
    }
}

// When to use: GET endpoints, user expects immediate response
// Advantage: Simple, guaranteed delivery
// Disadvantage: Slow if downstream service is slow
```

### Asynchronous (Kafka, RabbitMQ) - Event-driven

```java
// Grid Service publishes event, doesn't wait for response
@Service
public class GridService {

    @Autowired
    private KafkaTemplate<String, GridEvent> kafkaTemplate;

    public void updateGridAsync(String region, Double frequency) {
        // 1. Update grid database
        GridData grid = new GridData(region, frequency);
        gridRepository.save(grid);

        // 2. Publish event to Kafka (fire and forget)
        GridEvent event = new GridEvent(region, frequency, LocalDateTime.now());
        kafkaTemplate.send("grid-updates-topic", event);  // Returns immediately

        // 3. Return to client immediately
        return grid;
        // Note: Frequency service will consume event later
    }
}

// Frequency Service listens to events (asynchronously)
@Component
public class FrequencyServiceListener {

    @KafkaListener(topics = "grid-updates-topic", groupId = "frequency-group")
    public void onGridUpdate(GridEvent event) {
        // Called when event is published
        logger.info("Grid updated for region: {}", event.getRegion());

        // Process event: update frequency calculations, metrics, etc
        updateFrequencyCalculations(event.getRegion());
    }
}

// When to use: Notifications, analytics, loosely coupled updates
// Advantage: Fast, decoupled (don't depend on downstream), scalable
// Disadvantage: Eventual consistency, harder to debug
```

### Comparison Table

| Aspect | Synchronous | Asynchronous |
|--------|------------|--------------|
| Response time | Immediate | Delayed |
| Coupling | Tight (depends on service) | Loose (fire and forget) |
| Reliability | Direct (timeout = failure) | Queued (retry guarantees) |
| Complexity | Simple | Complex (eventual consistency) |
| Throughput | Limited by slowest service | High (batch processed) |
| Use case | GET, immediate response | Notifications, analytics |

### Real ERCOT Use Case

```
Synchronous - User dashboard:
1. User opens dashboard
2. UI calls: GET /api/grid/TX
3. API Gateway → Grid Service (immediate response expected)
4. Grid Service needs frequency: calls Frequency Service (sync REST)
5. Frequency Service returns: 60.0 Hz
6. Grid Service returns to API Gateway
7. API Gateway returns to user UI
8. Total time: ~100ms
Expected behavior: Fast, immediate updates on dashboard

Asynchronous - Audit logging:
1. User updates grid frequency
2. Grid Service saves to DB
3. Grid Service publishes event: "FrequencyUpdated" → Kafka
4. API returns 201 Created immediately
5. Audit Service listens for events (consuming from Kafka)
6. Audit Service logs the change
7. Incident Service listens for anomalies
8. Both services process at their own pace
Total time: 201 response after 10ms, processing continues async
Expected behavior: Fast API response, background processing
```

---

[File continues with Q4-Q10...]
