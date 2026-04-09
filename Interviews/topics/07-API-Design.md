# API Design Coding Samples (Spring Boot, Senior Style)

This file gives practical code patterns you can discuss in interviews.

## 1) Good REST resource design
- Use nouns: `/api/v1/orders`
- Use correct methods: `POST`, `GET`, `PATCH`, `DELETE`
- Use idempotency for create/update in distributed flows
- Return standard error model with trace/correlation id

## 2) Example: Create order API with idempotency

```java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {

    private final OrderService orderService;

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @PostMapping
    public ResponseEntity<OrderResponse> createOrder(
            @RequestHeader("Idempotency-Key") String idempotencyKey,
            @Valid @RequestBody CreateOrderRequest request) {

        OrderResponse response = orderService.createOrder(idempotencyKey, request);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping("/{orderId}")
    public ResponseEntity<OrderResponse> getOrder(@PathVariable String orderId) {
        return ResponseEntity.ok(orderService.getOrder(orderId));
    }

    @PatchMapping("/{orderId}")
    public ResponseEntity<OrderResponse> updateStatus(
            @PathVariable String orderId,
            @Valid @RequestBody UpdateOrderStatusRequest request) {

        return ResponseEntity.ok(orderService.updateStatus(orderId, request));
    }
}
```

## 3) Service pattern with idempotency guard

```java
@Service
public class OrderService {

    private final OrderRepository orderRepository;
    private final IdempotencyRepository idempotencyRepository;

    public OrderService(OrderRepository orderRepository,
                        IdempotencyRepository idempotencyRepository) {
        this.orderRepository = orderRepository;
        this.idempotencyRepository = idempotencyRepository;
    }

    @Transactional
    public OrderResponse createOrder(String idempotencyKey, CreateOrderRequest request) {
        Optional<IdempotencyRecord> existing = idempotencyRepository.findByKey(idempotencyKey);
        if (existing.isPresent()) {
            return existing.get().getCachedResponse();
        }

        OrderEntity entity = new OrderEntity();
        entity.setCustomerId(request.customerId());
        entity.setStatus("CREATED");
        entity.setTotalAmount(request.totalAmount());

        OrderEntity saved = orderRepository.save(entity);

        OrderResponse response = new OrderResponse(saved.getId(), saved.getStatus(), saved.getTotalAmount());
        idempotencyRepository.save(new IdempotencyRecord(idempotencyKey, response));

        return response;
    }
}
```

## 4) Standard error response model

```java
public record ApiError(
        String code,
        String message,
        String correlationId,
        String timestamp
) {}
```

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiError> handleValidation(MethodArgumentNotValidException ex) {
        ApiError error = new ApiError(
                "VALIDATION_ERROR",
                "Request validation failed",
                MDC.get("correlationId"),
                Instant.now().toString());
        return ResponseEntity.badRequest().body(error);
    }
}
```

## 5) Pagination and filtering example

```java
@GetMapping
public ResponseEntity<Page<OrderResponse>> listOrders(
        @RequestParam(required = false) String status,
        @RequestParam(defaultValue = "0") int page,
        @RequestParam(defaultValue = "20") int size) {

    Page<OrderResponse> result = orderService.listOrders(status, page, size);
    return ResponseEntity.ok(result);
}
```

## 6) Security pattern (method-level)

```java
@PreAuthorize("hasAnyRole('ADMIN','OPS')")
@DeleteMapping("/{orderId}")
public ResponseEntity<Void> cancelOrder(@PathVariable String orderId) {
    orderService.cancel(orderId);
    return ResponseEntity.noContent().build();
}
```

## 7) Interview talking points (must say)
1. "I design APIs for correctness first, then performance."
2. "I include idempotency and versioning from day one."
3. "I standardize error contracts and correlation IDs for supportability."
4. "I test contract compatibility to avoid client breakage."

## 8) Common API anti-patterns
- Verb-style endpoints (`/createOrder`) instead of resources
- No pagination on list endpoints
- Inconsistent error formats
- Missing timeout/retry policies for downstream dependencies
- No backward compatibility plan

## 9) Quick whiteboard prompts
- Design payment initiation API with retries
- Design notification preference API
- Design inventory reservation API with eventual consistency
