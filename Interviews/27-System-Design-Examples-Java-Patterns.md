# System Design Examples – Reusable Interview Pattern with Java Code

Purpose: Use one repeatable system-design format for common interviews such as Parking Lot, YouTube, Uber, DoorDash, and similar product/system questions.

---

## Universal System Design Pattern You Can Reuse Everywhere

Use this answer flow for almost any system design question:

### 1. Clarify Requirements
- Functional requirements
- Non-functional requirements
- In scope vs out of scope

### 2. Estimate Scale
- Users
- Requests per second
- Data size
- Read/write ratio

### 3. Identify Core Entities
- What are the main business objects?
- What relationships exist between them?

### 4. Define APIs
- Main create/read/update actions
- Async event flows if needed

### 5. High-Level Components
- Client/UI
- API gateway
- Services
- Cache
- Database
- Queue/stream
- Search/indexing
- Notifications

### 6. Data Flow
- Write path
- Read path
- Failure/retry path

### 7. NFRs and Trade-offs
- Availability
- Scalability
- Latency
- Security
- Consistency
- Cost

### 8. Deep Dive
- DB schema
- Partitioning/sharding
- Caching
- Rate limiting
- Idempotency
- Replay/recovery

### 9. Close Strong
- Mention bottlenecks
- Mention scaling plan
- Mention observability and failure handling

---

# CATEGORY 1 – Object-Oriented / Low-Level Design

## 1. Parking Lot System

### Use Case
Classic object-oriented design question. Good for LLD rounds and senior interviews where interviewers want to see entities, relationships, and extensibility.

### Functional Requirements
- Park vehicle
- Remove vehicle
- Generate ticket
- Track slot availability
- Support different vehicle types
- Compute parking fee

### Core Entities
- ParkingLot
- Floor
- ParkingSpot
- Vehicle
- Ticket
- Payment

### High-Level Design
Client -> ParkingLotService -> SpotAllocator -> TicketService -> PaymentService -> DB

### Key Design Ideas
- Strategy pattern for fee calculation
- Enum for vehicle/spot types
- Separate allocator logic from payment logic
- Track slot availability in memory + persist ticket/payment records

### Java Code Example
```java
import java.time.*;
import java.util.*;

enum VehicleType { BIKE, CAR, TRUCK }
enum SpotType { BIKE, COMPACT, LARGE }

class Vehicle {
    private final String plateNumber;
    private final VehicleType type;

    public Vehicle(String plateNumber, VehicleType type) {
        this.plateNumber = plateNumber;
        this.type = type;
    }

    public String getPlateNumber() { return plateNumber; }
    public VehicleType getType() { return type; }
}

class ParkingSpot {
    private final String id;
    private final SpotType type;
    private boolean occupied;

    public ParkingSpot(String id, SpotType type) {
        this.id = id;
        this.type = type;
    }

    public boolean canFit(Vehicle vehicle) {
        return switch (vehicle.getType()) {
            case BIKE -> type == SpotType.BIKE || type == SpotType.COMPACT || type == SpotType.LARGE;
            case CAR -> type == SpotType.COMPACT || type == SpotType.LARGE;
            case TRUCK -> type == SpotType.LARGE;
        };
    }

    public boolean isOccupied() { return occupied; }
    public void park() { this.occupied = true; }
    public void free() { this.occupied = false; }
    public String getId() { return id; }
}

class Ticket {
    private final String ticketId;
    private final Vehicle vehicle;
    private final ParkingSpot spot;
    private final LocalDateTime entryTime;

    public Ticket(String ticketId, Vehicle vehicle, ParkingSpot spot) {
        this.ticketId = ticketId;
        this.vehicle = vehicle;
        this.spot = spot;
        this.entryTime = LocalDateTime.now();
    }

    public String getTicketId() { return ticketId; }
    public Vehicle getVehicle() { return vehicle; }
    public ParkingSpot getSpot() { return spot; }
    public LocalDateTime getEntryTime() { return entryTime; }
}

interface FeeStrategy {
    double calculate(LocalDateTime entryTime, LocalDateTime exitTime);
}

class HourlyFeeStrategy implements FeeStrategy {
    private final double hourlyRate;

    public HourlyFeeStrategy(double hourlyRate) {
        this.hourlyRate = hourlyRate;
    }

    @Override
    public double calculate(LocalDateTime entryTime, LocalDateTime exitTime) {
        long hours = Math.max(1, Duration.between(entryTime, exitTime).toHours());
        return hours * hourlyRate;
    }
}

class ParkingLotService {
    private final List<ParkingSpot> spots;
    private final Map<String, Ticket> activeTickets = new HashMap<>();
    private final FeeStrategy feeStrategy;

    public ParkingLotService(List<ParkingSpot> spots, FeeStrategy feeStrategy) {
        this.spots = spots;
        this.feeStrategy = feeStrategy;
    }

    public Ticket park(Vehicle vehicle) {
        for (ParkingSpot spot : spots) {
            if (!spot.isOccupied() && spot.canFit(vehicle)) {
                spot.park();
                Ticket ticket = new Ticket(UUID.randomUUID().toString(), vehicle, spot);
                activeTickets.put(ticket.getTicketId(), ticket);
                return ticket;
            }
        }
        throw new IllegalStateException("No spot available");
    }

    public double exit(String ticketId) {
        Ticket ticket = activeTickets.remove(ticketId);
        if (ticket == null) throw new IllegalArgumentException("Invalid ticket");
        ticket.getSpot().free();
        return feeStrategy.calculate(ticket.getEntryTime(), LocalDateTime.now());
    }
}
```

### Interview Talking Points
- Start simple with in-memory spot allocation
- Then discuss multiple floors and spot indexing by type
- Then discuss concurrency if multiple gates allocate the same spot
- Then discuss persistence, ticket history, and payment integration

---

## 2. URL Shortener

### Use Case
Very common design question. Good for APIs, storage, hashing, caching, and scale discussion.

### Functional Requirements
- Shorten long URL
- Redirect short URL to original URL
- Track click count
- Optional custom alias

### Core Components
- API service
- ID generator / hash service
- Cache
- Key-value database
- Analytics store

### Key Design Ideas
- Write path: long URL -> unique key -> store mapping
- Read path: short key -> cache -> DB -> redirect
- Use cache because reads are higher than writes

### Java Code Example
```java
import java.util.*;

class UrlMapping {
    private final String shortCode;
    private final String longUrl;

    public UrlMapping(String shortCode, String longUrl) {
        this.shortCode = shortCode;
        this.longUrl = longUrl;
    }

    public String getShortCode() { return shortCode; }
    public String getLongUrl() { return longUrl; }
}

interface UrlRepository {
    void save(UrlMapping mapping);
    Optional<UrlMapping> findByShortCode(String shortCode);
}

class InMemoryUrlRepository implements UrlRepository {
    private final Map<String, UrlMapping> storage = new HashMap<>();

    public void save(UrlMapping mapping) { storage.put(mapping.getShortCode(), mapping); }
    public Optional<UrlMapping> findByShortCode(String shortCode) {
        return Optional.ofNullable(storage.get(shortCode));
    }
}

class Base62Encoder {
    private static final String CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    public String encode(long value) {
        StringBuilder sb = new StringBuilder();
        while (value > 0) {
            sb.append(CHARS.charAt((int)(value % 62)));
            value /= 62;
        }
        return sb.reverse().toString();
    }
}

class UrlShortenerService {
    private final UrlRepository repository;
    private final Base62Encoder encoder = new Base62Encoder();
    private long sequence = 1000;

    public UrlShortenerService(UrlRepository repository) {
        this.repository = repository;
    }

    public String shorten(String longUrl) {
        String code = encoder.encode(sequence++);
        repository.save(new UrlMapping(code, longUrl));
        return code;
    }

    public String resolve(String code) {
        return repository.findByShortCode(code)
                .map(UrlMapping::getLongUrl)
                .orElseThrow(() -> new IllegalArgumentException("Short URL not found"));
    }
}
```

### Interview Talking Points
- Mention cache for hot URLs
- Mention DB or key-value store for mappings
- Mention unique ID generation
- Mention analytics path separated from redirect path for latency reasons

---

## 3. Notification System

### Use Case
Common real-world design question for email, SMS, push, alerts, retries, templates, and preferences.

### Functional Requirements
- Send email/SMS/push notification
- Respect user preferences
- Retry failures
- Support templates
- Track delivery status

### Architecture
Producer Service -> Notification API -> Queue -> Channel Workers -> Provider APIs

### Java Code Example
```java
import java.util.*;

enum ChannelType { EMAIL, SMS, PUSH }

class NotificationRequest {
    private final String userId;
    private final ChannelType channel;
    private final String message;

    public NotificationRequest(String userId, ChannelType channel, String message) {
        this.userId = userId;
        this.channel = channel;
        this.message = message;
    }

    public String getUserId() { return userId; }
    public ChannelType getChannel() { return channel; }
    public String getMessage() { return message; }
}

interface NotificationSender {
    void send(NotificationRequest request);
}

class EmailSender implements NotificationSender {
    public void send(NotificationRequest request) {
        System.out.println("Sending EMAIL to " + request.getUserId() + ": " + request.getMessage());
    }
}

class SmsSender implements NotificationSender {
    public void send(NotificationRequest request) {
        System.out.println("Sending SMS to " + request.getUserId() + ": " + request.getMessage());
    }
}

class PushSender implements NotificationSender {
    public void send(NotificationRequest request) {
        System.out.println("Sending PUSH to " + request.getUserId() + ": " + request.getMessage());
    }
}

class NotificationFactory {
    public NotificationSender getSender(ChannelType type) {
        return switch (type) {
            case EMAIL -> new EmailSender();
            case SMS -> new SmsSender();
            case PUSH -> new PushSender();
        };
    }
}

class NotificationService {
    private final NotificationFactory factory = new NotificationFactory();

    public void process(NotificationRequest request) {
        NotificationSender sender = factory.getSender(request.getChannel());
        sender.send(request);
    }
}
```

### Interview Talking Points
- Separate request ingestion from delivery using queue
- Add retry and DLQ for failures
- Add user preference service
- Add template service and delivery tracking
- Scale workers per channel independently


---

# CATEGORY 2 – Consumer Internet / Marketplace Systems

## 4. YouTube / Video Streaming Platform

### Functional Requirements
- Upload video
- Process/transcode video
- Stream video
- Search video
- Like/comment/subscribe

### High-Level Architecture
Client -> API Gateway -> Upload Service -> Object Storage -> Transcoding Workers -> Metadata DB -> CDN -> Streaming

### Key Design Points
- Store raw and transcoded videos in object storage
- Use async pipeline for transcoding
- Use CDN for low-latency content delivery
- Keep metadata and content separated

### Java Code Example
```java
import java.util.*;

class VideoMetadata {
    private final String videoId;
    private final String title;
    private final String uploaderId;
    private String status;

    public VideoMetadata(String videoId, String title, String uploaderId) {
        this.videoId = videoId;
        this.title = title;
        this.uploaderId = uploaderId;
        this.status = "UPLOADED";
    }

    public String getVideoId() { return videoId; }
    public String getTitle() { return title; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}

class VideoService {
    private final Map<String, VideoMetadata> store = new HashMap<>();

    public String upload(String title, String uploaderId) {
        String id = UUID.randomUUID().toString();
        VideoMetadata metadata = new VideoMetadata(id, title, uploaderId);
        store.put(id, metadata);
        return id;
    }

    public void markProcessed(String videoId) {
        VideoMetadata m = store.get(videoId);
        if (m != null) m.setStatus("READY");
    }

    public VideoMetadata getVideo(String videoId) {
        return store.get(videoId);
    }
}
```

### Interview Talking Points
- Upload is write-heavy; playback is massively read-heavy
- CDN is critical for scale
- Async transcoding avoids blocking the upload path
- Search index should be separate from metadata DB

---

## 5. Uber / Ride-Hailing System

### Functional Requirements
- Rider requests trip
- Match nearby driver
- Track live location
- Start and end ride
- Pricing and payment

### Core Entities
- Rider, Driver, Trip, Location, Pricing

### High-Level Architecture
Rider App / Driver App -> Gateway -> Trip Service -> Matching Service -> Location Service -> Pricing -> Payment -> Notifications

### Java Code Example
```java
import java.util.*;

record Location(double lat, double lon) {}

class Driver {
    private final String id;
    private boolean available;

    public Driver(String id, boolean available) {
        this.id = id;
        this.available = available;
    }

    public String getId() { return id; }
    public boolean isAvailable() { return available; }
    public void setAvailable(boolean available) { this.available = available; }
}

class Rider {
    private final String id;
    public Rider(String id) { this.id = id; }
    public String getId() { return id; }
}

class Trip {
    private final String tripId;
    private final Rider rider;
    private final Driver driver;

    public Trip(String tripId, Rider rider, Driver driver) {
        this.tripId = tripId;
        this.rider = rider;
        this.driver = driver;
    }

    public String getTripId() { return tripId; }
}

class MatchingService {
    public Optional<Driver> findNearestAvailable(List<Driver> drivers) {
        return drivers.stream().filter(Driver::isAvailable).findFirst();
    }
}

class TripService {
    private final MatchingService matchingService = new MatchingService();

    public Trip requestRide(Rider rider, List<Driver> nearbyDrivers) {
        Driver driver = matchingService.findNearestAvailable(nearbyDrivers)
                .orElseThrow(() -> new IllegalStateException("No drivers available"));
        driver.setAvailable(false);
        return new Trip(UUID.randomUUID().toString(), rider, driver);
    }
}
```

### Interview Talking Points
- Matching service can use geo index like GeoHash or QuadTree
- Location updates should be write-optimized
- Trip state transitions must be idempotent
- Pricing, notifications, and payments are separate services

---

## 6. DoorDash / Food Delivery Platform

### Functional Requirements
- Browse restaurants and menu
- Place order
- Assign dasher/driver
- Track delivery
- Handle restaurant prep and delivery states

### High-Level Architecture
Customer App -> API -> Restaurant Service -> Cart/Order Service -> Dispatch Service -> Delivery Tracking -> Payment -> Notification

### Java Code Example
```java
import java.util.*;

enum OrderStatus { CREATED, CONFIRMED, PREPARING, PICKED_UP, DELIVERED, CANCELLED }

class Order {
    private final String orderId;
    private final String customerId;
    private final String restaurantId;
    private OrderStatus status;

    public Order(String orderId, String customerId, String restaurantId) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.restaurantId = restaurantId;
        this.status = OrderStatus.CREATED;
    }

    public void updateStatus(OrderStatus status) { this.status = status; }
    public OrderStatus getStatus() { return status; }
    public String getOrderId() { return orderId; }
}

class OrderService {
    private final Map<String, Order> orders = new HashMap<>();

    public Order createOrder(String customerId, String restaurantId) {
        Order order = new Order(UUID.randomUUID().toString(), customerId, restaurantId);
        orders.put(order.getOrderId(), order);
        return order;
    }

    public void transition(String orderId, OrderStatus newStatus) {
        Order order = orders.get(orderId);
        if (order == null) throw new IllegalArgumentException("Order not found");
        order.updateStatus(newStatus);
    }
}
```

### Interview Talking Points
- Separate customer-facing read path from delivery dispatch path
- Menu browsing is read-heavy; orders are write-critical
- Dispatch reuses ride-matching concepts
- Order lifecycle needs idempotency and event-driven updates

---

## 7. Chat / WhatsApp-like Messaging System

### Functional Requirements
- One-to-one and group messaging
- Delivery status
- Online/offline behavior
- Message ordering

### High-Level Architecture
Client -> Gateway/WebSocket -> Chat Service -> Message Queue -> Message Store -> Notification Service

### Java Code Example
```java
import java.time.*;
import java.util.*;

class Message {
    private final String messageId;
    private final String fromUser;
    private final String toUser;
    private final String content;
    private final Instant timestamp;

    public Message(String fromUser, String toUser, String content) {
        this.messageId = UUID.randomUUID().toString();
        this.fromUser = fromUser;
        this.toUser = toUser;
        this.content = content;
        this.timestamp = Instant.now();
    }

    public String getMessageId() { return messageId; }
    public String getFromUser() { return fromUser; }
    public String getToUser() { return toUser; }
    public String getContent() { return content; }
    public Instant getTimestamp() { return timestamp; }
}

class ChatService {
    private final Map<String, List<Message>> inbox = new HashMap<>();

    public void send(String fromUser, String toUser, String content) {
        Message msg = new Message(fromUser, toUser, content);
        inbox.computeIfAbsent(toUser, k -> new ArrayList<>()).add(msg);
    }

    public List<Message> fetch(String userId) {
        return inbox.getOrDefault(userId, List.of());
    }
}
```

### Interview Talking Points
- WebSocket for real-time delivery
- Queue for reliable async fan-out to groups
- Message ordering strategy per conversation
- Offline users need durable storage and later sync


---

# CATEGORY 3 – E-Commerce, Infrastructure, Scheduling

## 8. Amazon / E-Commerce Platform

### Functional Requirements
- Browse catalog and search products
- Add to cart
- Place order
- Payment and inventory tracking

### High-Level Architecture
Client -> API Gateway -> Catalog -> Search -> Cart -> Order -> Payment -> Inventory -> Notification

### Java Code Example
```java
import java.util.*;

class Product {
    private final String productId;
    private final String name;
    private int stock;

    public Product(String productId, String name, int stock) {
        this.productId = productId;
        this.name = name;
        this.stock = stock;
    }

    public String getProductId() { return productId; }
    public String getName() { return name; }
    public int getStock() { return stock; }

    public void reduceStock(int qty) {
        if (stock < qty) throw new IllegalStateException("Out of stock");
        stock -= qty;
    }
}

class CartService {
    private final Map<String, List<String>> carts = new HashMap<>();

    public void addToCart(String userId, String productId) {
        carts.computeIfAbsent(userId, k -> new ArrayList<>()).add(productId);
    }

    public List<String> getCart(String userId) {
        return carts.getOrDefault(userId, List.of());
    }
}
```

### Interview Talking Points
- Catalog and search are read-optimized
- Orders and inventory need stronger consistency
- Payment should be isolated
- Use async events for email, shipment, and analytics

---

## 9. Rate Limiter

### Use Case
Classic infrastructure design. Frequently asked in backend and platform interviews.

### Algorithms
- Fixed window counter
- Sliding window log
- Token bucket
- Leaky bucket

### Java Code Example – Fixed Window
```java
import java.util.*;

class RateLimiter {
    private final int limit;
    private final long windowMillis;
    private final Map<String, Integer> counter = new HashMap<>();
    private final Map<String, Long> windowStart = new HashMap<>();

    public RateLimiter(int limit, long windowMillis) {
        this.limit = limit;
        this.windowMillis = windowMillis;
    }

    public synchronized boolean allow(String clientId) {
        long now = System.currentTimeMillis();
        long start = windowStart.getOrDefault(clientId, now);

        if (now - start >= windowMillis) {
            windowStart.put(clientId, now);
            counter.put(clientId, 1);
            return true;
        }

        int count = counter.getOrDefault(clientId, 0);
        if (count >= limit) return false;

        counter.put(clientId, count + 1);
        windowStart.putIfAbsent(clientId, start);
        return true;
    }
}
```

### Interview Talking Points
- In-memory works for single instance only
- Distributed rate limiting needs Redis with atomic operations
- Sliding window is more accurate than fixed window
- Token bucket allows burst and is commonly used in APIs

---

## 10. Calendar / Meeting Scheduler

### Functional Requirements
- Create event and invite participants
- Detect scheduling conflicts
- Handle time zones
- Send reminders

### High-Level Architecture
Client -> Calendar API -> Scheduling Service -> Availability Service -> Notification Service

### Java Code Example
```java
import java.time.*;
import java.util.*;

class Meeting {
    private final String id;
    private final LocalDateTime start;
    private final LocalDateTime end;

    public Meeting(LocalDateTime start, LocalDateTime end) {
        this.id = UUID.randomUUID().toString();
        this.start = start;
        this.end = end;
    }

    public LocalDateTime getStart() { return start; }
    public LocalDateTime getEnd() { return end; }
    public String getId() { return id; }
}

class CalendarService {
    private final Map<String, List<Meeting>> meetingsByUser = new HashMap<>();

    public boolean schedule(String userId, Meeting meeting) {
        List<Meeting> meetings = meetingsByUser.computeIfAbsent(userId, k -> new ArrayList<>());
        for (Meeting m : meetings) {
            boolean overlaps = meeting.getStart().isBefore(m.getEnd())
                            && meeting.getEnd().isAfter(m.getStart());
            if (overlaps) return false;
        }
        meetings.add(meeting);
        return true;
    }

    public List<Meeting> getMeetings(String userId) {
        return meetingsByUser.getOrDefault(userId, List.of());
    }
}
```

### Interview Talking Points
- Time zones: always store UTC, convert at display boundaries
- Recurring meetings need separate recurrence rule model
- Conflict detection can use segment tree for large scale
- Reminder jobs are async scheduled workers

---

# Category-Wise Reusable Pattern Summary

| Category | Examples | Reusable Pattern |
|----------|----------|------------------|
| OOD / LLD | Parking Lot, Library, Elevator | Entities + relationships + strategy pattern + extensibility |
| Marketplace / Logistics | Uber, DoorDash | Matching + state machine + location + notifications |
| Content / Media | YouTube, Netflix | Upload pipeline + async processing + CDN + metadata DB |
| Messaging | Chat, WhatsApp | Persistent connection + queue + ordering + offline sync |
| E-Commerce | Amazon | Search + catalog + cart + order workflow + inventory |
| Infrastructure | Rate Limiter, Notification | Gateway + policy + shared state + retries |
| Scheduling | Calendar, Booking | Availability + conflict detection + time zones + reminder jobs |

---

# How to Reuse Same Pattern in Interviews

## Step 1 - Pick the Category
- Is this marketplace/logistics? -> Uber/DoorDash pattern
- Is this content streaming? -> YouTube pattern
- Is this scheduling or resource booking? -> Calendar/Parking Lot pattern
- Is this OOD? -> Entity + relationship + behavior pattern

## Step 2 - Reuse the Architecture
- Uber and DoorDash: matching + tracking + workflow states
- YouTube: upload/process/deliver
- Parking Lot and Booking: allocate resource + track state + release
- Notification and Chat: async delivery + retries + status

## Step 3 - Always Mention NFRs
- Availability, Latency, Scalability, Consistency, Security, Observability

## Step 4 - Close With Trade-offs
Start simple -> add cache for reads -> move async work to queues -> partition by domain or customer as load grows.

---

# Best 2-Minute Interview Answer Structure

1. Clarify functional and non-functional requirements
2. State scale assumptions
3. Define core entities and APIs
4. Draw high-level components
5. Explain write path and read path
6. Discuss bottlenecks and scaling approach
7. Mention NFRs, failure handling, and observability

---

# Final Advice

Do not memorize 10 completely different designs.
Memorize 5 to 6 reusable patterns and map each new question into a known category.

For your 18-year profile, interviewers expect:
- Clear structure
- Practical trade-offs grounded in your real projects
- Production realism including failure modes and NFRs
- Extensible Java design with good OOP
- Reliability and observability thinking throughout

