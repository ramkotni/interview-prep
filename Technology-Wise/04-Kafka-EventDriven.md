# KAFKA - EVENT-DRIVEN ARCHITECTURE
# Message Streaming, Producers, Consumers | 18 Years Experience

---

## Q1: What is Kafka? Why use for ERCOT?

**A:**

**Kafka** = Distributed message broker for real-time event streaming.

### Key Concepts

```
Topic: Grid_Updates (collection of events)
  ├─ Partition 0: [Event1, Event2, Event3, ...]
  ├─ Partition 1: [Event4, Event5, Event6, ...]
  └─ Partition 2: [Event7, Event8, Event9, ...]

Producer: Grid Service publishes events to Kafka
Consumer: Notification Service, Analytics Service read events

Offset: Position in partition (event 0, 1, 2...)
Broker: Kafka server that holds topics
```

### Why Kafka for ERCOT (10K+ events/sec)

```java
// Problem with traditional REST:
// Every time grid updates, call notification service
// → Network overhead
// → If notification service down → grid service fails
// → Tight coupling

GridService {
    updateGrid() {
        save to DB
        restTemplate.post("http://notifier/notify")  // Blocks!
        restTemplate.post("http://analytics/record") // Blocks!
    }
}

// Solution with Kafka:
// Grid service publishes event async
// Multiple consumers process independently

GridService {
    updateGrid() {
        save to DB
        kafkaTemplate.send("grid-updates", event)  // Returns immediately!
    }
}

NotificationService listens: onGridUpdate() → send email
AnalyticsService listens: onGridUpdate() → update metrics
AuditService listens: onGridUpdate() → log change

Benefits:
✓ Grid service doesn't wait (Kafka returns immediately)
✓ Services decoupled (don't know about each other)
✓ If notifier down → events stay in Kafka (not lost)
✓ Scale independently (add more consumer instances)
✓ Fault tolerance (events replicated across brokers)
```

---

## Q2: Kafka Producer - How to publish events.

**A:**

```java
// 1. Add Kafka Dependency to pom.xml
// <dependency>
//   <groupId>org.springframework.kafka</groupId>
//   <artifactId>spring-kafka</artifactId>
// </dependency>

// 2. Configure Kafka in application.yml
import org.springframework.kafka.core.KafkaTemplate;

spring:
  kafka:
    bootstrap-servers: localhost:9092
    producer:
      key-serializer: org.apache.kafka.common.serialization.StringSerializer
      value-serializer: org.springframework.kafka.support.serializer.JsonSerializer
      acks: all  # Wait for all replicas to confirm

// 3. Define Event (POJO)
@Data
@AllArgsConstructor
public class GridUpdateEvent {
    private String regionId;
    private Double frequency;
    private Double load;
    private LocalDateTime timestamp;
    private String source;
}

// 4. Create Producer
@Service
public class GridEventProducer {

    @Autowired
    private KafkaTemplate<String, GridUpdateEvent> kafkaTemplate;

    private static final String TOPIC = "grid-updates";

    public void publishGridUpdate(String regionId, Double frequency, Double load) {
        GridUpdateEvent event = new GridUpdateEvent(
            regionId,
            frequency,
            load,
            LocalDateTime.now(),
            "GridService"
        );

        // Send event (async - returns immediately)
        kafkaTemplate.send(TOPIC, regionId, event)  // Key: regionId
            .addCallback(
                result -> logger.info("Published event for region {}", regionId),
                ex -> logger.error("Failed to publish event", ex)
            );
    }
}

// 5. Use Producer in Service
@Service
public class GridService {

    @Autowired
    private GridEventProducer eventProducer;

    @Autowired
    private GridRepository gridRepository;

    public void updateGridFrequency(String regionId, Double frequency) {
        // Update database
        GridData grid = gridRepository.findByRegion(regionId)
            .orElseThrow(() -> new NotFoundException("Region not found"));
        grid.setFrequency(frequency);
        grid.setTimestamp(LocalDateTime.now());
        gridRepository.save(grid);

        // Publish event to Kafka
        eventProducer.publishGridUpdate(regionId, frequency, grid.getLoad());

        // Return immediately
        return grid;
    }
}

// Real ERCOT Data Flow:
GridService.updateGridFrequency("TX", 60.0)
    ↓
1. Save to database (sync)
2. Publish to Kafka "grid-updates" topic (async, returns immediately)
    ├─ Kafka broker receives
    ├─ Replicates to broker-2 (in case broker-1 fails)
    └─ Acknowledges to producer
3. Return 200 OK to client (took ~10ms total)

Meanwhile, consumers listen async:
NotificationService consumes event → sends alert email
AnalyticsService consumes event → updates dashboard
AuditService consumes event → logs to database
(All happen independently, don't block grid service)
```

---

## Q3: Kafka Consumer - Processing events.

**A:**

```java
// 1. Configure Kafka Consumer in application.yml
spring:
  kafka:
    bootstrap-servers: localhost:9092
    consumer:
      group-id: notification-service-group
      key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value-deserializer: org.springframework.kafka.support.serializer.JsonDeserializer
      properties:
        spring:
          json:
            trusted:
              packages: com.ercot.events
      auto-offset-reset: earliest  # Start from beginning if no offset
      enable-auto-commit: false  # Manual commit for reliability

// 2. Create Listener (Consumer)
@Component
public class GridUpdateListener {

    @Autowired
    private NotificationService notificationService;

    @KafkaListener(
        topics = "grid-updates",
        groupId = "notification-service-group",
        containerFactory = "kafkaListenerContainerFactory"
    )
    public void onGridUpdate(GridUpdateEvent event,
                            @Header(KafkaHeaders.RECEIVED_PARTITION_ID) int partition,
                            @Header(KafkaHeaders.OFFSET) long offset) {
        try {
            logger.info("Received event for region {} at offset {}", event.getRegionId(), offset);

            // Process event
            if (event.getFrequency() < 59.5) {
                // Low frequency alert
                notificationService.sendAlert(
                    event.getRegionId(),
                    "Low frequency: " + event.getFrequency() + " Hz"
                );
            }

            if (event.getLoad() > 95) {
                // High load alert
                notificationService.sendAlert(
                    event.getRegionId(),
                    "High load: " + event.getLoad() + "%"
                );
            }

        } catch (Exception e) {
            logger.error("Error processing grid event", e);
            // DO NOT commit offset - message will be retried
        }
    }
}

// 3. Multiple Consumers (same group, different threads)
@Component
public class AnalyticsListener {

    @KafkaListener(
        topics = "grid-updates",
        groupId = "analytics-service-group"  // Different group
    )
    public void onGridUpdate(GridUpdateEvent event) {
        // Update analytics/metrics
        metricsService.recordFrequency(event.getRegionId(), event.getFrequency());
        metricsService.recordLoad(event.getRegionId(), event.getLoad());
    }
}

// 4. Error Handling - Retry and Dead Letter Queue
@Component
public class GridUpdateErrorHandler {

    @Bean
    public ConsumerAwareListenerErrorHandler consumerAwareListenerErrorHandler() {
        return (thrownException, data, consumer) -> {
            logger.error("Error consuming message: {}", data, thrownException);
            // Send to dead letter queue for investigation
            return null;
        };
    }
}

// Real ERCOT Flow:
Kafka Topic: grid-updates (3 partitions)
  Partition 0: [Event1, Event2, Event3]
  Partition 1: [Event4, Event5, Event6]
  Partition 2: [Event7, Event8, Event9]

Consumer Group: notification-service-group
  Instance 1: Reads Partition 0
  Instance 2: Reads Partition 1
  Instance 3: Reads Partition 2

If Instance 1 crashes:
  Instance 2 takes over Partition 0
  Rebalancing: offset committed before reassignment

If Instance 2 has error:
  Offset NOT committed
  Message redelivered after retry timeout
  Eventually sent to dead letter queue if max retries reached
```

---

[File continues with Q4-Q10...]
