parking system 


enums 

enum slotstatus{ EMPTY,OCCUPIED;}
enum Vechicletype{car;}




interface 

interface parkingEventListener{
   void onavilablilitychanged(int avialable)
}


inetrface AllocationStrategy{
    optional<parkingslot> findavilableslot(list<parkingslot> slots);
	}
	
	core class  car , indicator, parking slot, ticket,nearstestfirststrategy implemts AllocationStrategy,displayboard implemnts parkingEventListener
	different class 
	
	
	parkinglot(thread-safe,singleresponsibility:mange slots and notify)
	
	gates (entry/exit orchestration+message
	
	
	flow :
	
	entrygate.admits checks the quick status ; calls parkinglot.park(car).
	parkinglot finds a freeslot via AllocationStrategy
	parking slot.occupy(car) sets indicator --> occupied
	parkinglot decremnets avilable counts creates ticket notifies displayboard
	displayboard print avilableslots :n or parking full if zero.
	
	
	exit (carelaeve)
	exitgate.realease(ticketid) class parkinglot.unpark(ticketid)
	parkingslot.vaccet() sets indicator-----> empty
	parkingslot increments avilable count notifies displayboad
	displayboard shows updated avilablity 
================
Enums
enum SlotStatus {
    EMPTY, OCCUPIED;
}

enum VehicleType {
    CAR;
}

interaces:

interface ParkingEventListener {
    void onAvailabilityChanged(int available);
}

import java.util.List;
import java.util.Optional;

interface AllocationStrategy {
    Optional<ParkingSlot> findAvailableSlot(List<ParkingSlot> slots);
}

Core classes - Vehicle 
class Car {
    private final String licensePlate;

    public Car(String licensePlate) {
        this.licensePlate = licensePlate;
    }

    public String getLicensePlate() {
        return licensePlate;
    }
}

class Indicator {
    private SlotStatus status = SlotStatus.EMPTY;

    public void setStatus(SlotStatus status) {
        this.status = status;
    }

    public SlotStatus getStatus() {
        return status;
    }
}

class ParkingSlot {
    private final int id;
    private final Indicator indicator = new Indicator();
    private Car parkedCar;

    public ParkingSlot(int id) {
        this.id = id;
    }

    public boolean isAvailable() {
        return indicator.getStatus() == SlotStatus.EMPTY;
    }

    public void occupy(Car car) {
        this.parkedCar = car;
        indicator.setStatus(SlotStatus.OCCUPIED);
    }

    public void vacate() {
        this.parkedCar = null;
        indicator.setStatus(SlotStatus.EMPTY);
    }

    public int getId() {
        return id;
    }
}


class Ticket {
    private final int ticketId;
    private final ParkingSlot slot;
    private final Car car;

    public Ticket(int ticketId, ParkingSlot slot, Car car) {
        this.ticketId = ticketId;
        this.slot = slot;
        this.car = car;
    }

    public int getTicketId() { return ticketId; }
    public ParkingSlot getSlot() { return slot; }
    public Car getCar() { return car; }
}

class NearestFirstStrategy implements AllocationStrategy {
    @Override
    public Optional<ParkingSlot> findAvailableSlot(List<ParkingSlot> slots) {
        return slots.stream().filter(ParkingSlot::isAvailable).findFirst();
    }
}

class DisplayBoard implements ParkingEventListener {
    @Override
    public void onAvailabilityChanged(int available) {
        if (available > 0) {
            System.out.println("Available slots: " + available);
        } else {
            System.out.println("Parking Full!");
        }
    }
}

import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

class ParkingLot {
    private final List<ParkingSlot> slots;
    private final AllocationStrategy strategy;
    private final List<ParkingEventListener> listeners = new ArrayList<>();
    private final Map<Integer, Ticket> activeTickets = new HashMap<>();
    private final AtomicInteger availableCount;
    private final AtomicInteger ticketCounter = new AtomicInteger(1);

    public ParkingLot(int capacity, AllocationStrategy strategy) {
        this.slots = new ArrayList<>();
        for (int i = 1; i <= capacity; i++) {
            slots.add(new ParkingSlot(i));
        }
        this.strategy = strategy;
        this.availableCount = new AtomicInteger(capacity);
    }

    public synchronized Ticket park(Car car) {
        Optional<ParkingSlot> slotOpt = strategy.findAvailableSlot(slots);
        if (slotOpt.isEmpty()) {
            System.out.println("No slot available for car: " + car.getLicensePlate());
            return null;
        }

        ParkingSlot slot = slotOpt.get();
        slot.occupy(car);
        int ticketId = ticketCounter.getAndIncrement();
        Ticket ticket = new Ticket(ticketId, slot, car);
        activeTickets.put(ticketId, ticket);

        int updated = availableCount.decrementAndGet();
        notifyListeners(updated);

        return ticket;
    }

    public synchronized void unpark(int ticketId) {
        Ticket ticket = activeTickets.remove(ticketId);
        if (ticket != null) {
            ticket.getSlot().vacate();
            int updated = availableCount.incrementAndGet();
            notifyListeners(updated);
        } else {
            System.out.println("Invalid ticket ID: " + ticketId);
        }
    }

    public void addListener(ParkingEventListener listener) {
        listeners.add(listener);
    }

    private void notifyListeners(int available) {
        for (ParkingEventListener listener : listeners) {
            listener.onAvailabilityChanged(available);
        }
    }
}


class EntryGate {
    private final ParkingLot parkingLot;

    public EntryGate(ParkingLot parkingLot) {
        this.parkingLot = parkingLot;
    }

    public Ticket admit(Car car) {
        System.out.println("Car entering: " + car.getLicensePlate());
        return parkingLot.park(car);
    }
}


class ExitGate {
    private final ParkingLot parkingLot;

    public ExitGate(ParkingLot parkingLot) {
        this.parkingLot = parkingLot;
    }

    public void release(int ticketId) {
        System.out.println("Car exiting with ticket: " + ticketId);
        parkingLot.unpark(ticketId);
    }
}


public class ParkingSystemDemo {
    public static void main(String[] args) {
        ParkingLot parkingLot = new ParkingLot(2, new NearestFirstStrategy());
        DisplayBoard displayBoard = new DisplayBoard();
        parkingLot.addListener(displayBoard);

        EntryGate entryGate = new EntryGate(parkingLot);
        ExitGate exitGate = new ExitGate(parkingLot);

        Car car1 = new Car("KA-01");
        Car car2 = new Car("KA-02");
        Car car3 = new Car("KA-03");

        Ticket t1 = entryGate.admit(car1);
        Ticket t2 = entryGate.admit(car2);
        Ticket t3 = entryGate.admit(car3);  // should show parking full

        exitGate.release(t1.getTicketId());
        Ticket t4 = entryGate.admit(car3);  // now slot is free
    }
}


Single Responsibility Principle (each class has a clear role).

Thread-safety (synchronized in ParkingLot).

Observer pattern (ParkingLot → DisplayBoard).

Strategy pattern (AllocationStrategy).

==========================

Q&A Format

Q1: What was your role as a Senior Java Developer in the project?
A1: During the project, as a Senior Java Developer, I was responsible for requirement analysis and design. I collaborated with business analysts and product owners to understand requirements, participated in sprint planning, and provided technical estimations. I designed scalable, modular, and maintainable solutions using Java, Spring Boot, and Microservices.
In development, I wrote clean, efficient, well-documented code, implemented REST APIs, database integration, and third-party service integration. I used Java 8 features (like Futures) for better readability and performance, conducted code reviews, and participated in knowledge-sharing sessions.

Q2: Can you explain caching and hashing in system design?
A2:

Caching is used to quickly retrieve frequently accessed data to improve performance.

Hashing converts input data into fixed-size values using hash functions. It is widely used in distributed systems for load balancing, fast lookups, and ensuring uniform load distribution.

In our project, we implemented caching using Redis. We integrated it at the service layer of our Spring Boot applications using @EnableCaching, @Cacheable, and @CachePut annotations.

Q3: What is the difference between @Cacheable and @CachePut in Spring Boot caching?
A3:

@Cacheable: Stores the result of a method execution in the cache. Subsequent calls with the same parameters return the cached result, improving performance.

@CachePut: Ensures the method is always executed and its result is stored/updated in the cache, keeping data fresh.

Q4: What is a circular dependency in Spring, and how do you resolve it?
A4: A circular dependency occurs when two or more beans depend on each other (e.g., Bean A needs Bean B, and Bean B needs Bean A). This leads to an endless loop during context initialization.

Solutions:

Use setter injection instead of constructor injection, so Spring can create the beans first and inject later.

Use @Lazy annotation on one of the beans so it is only initialized when actually needed.

Q5: What are stereotype annotations in Spring?
A5:

@Component: Generic annotation for beans.

@Service: Used for service layer classes (business logic).

@Repository: Used for DAO classes (database access).

@Controller: Used for Spring MVC controllers (handle HTTP requests).

These annotations streamline bean management by allowing Spring to auto-detect and configure beans.

Q6: How do you design Spring Boot layers?
A6: Typically, I structure applications into layers:

Controller Layer: Handles HTTP requests.

Service Layer: Contains business logic.

Repository Layer: Handles database persistence.

For example, if a client requires id, name, and location in the product API response, I would expose a GET /products/{id} endpoint using @GetMapping, handle headers like Accept: application/vnd.client1+json, and return data via DTOs.

Q7: What is the difference between returning DTO vs ResponseEntity in Spring REST APIs?
A7:

Returning DTO directly: Spring serializes the DTO into JSON, but you can’t control status codes or headers (always 200 unless exception).

Returning ResponseEntity: Provides full control over response body, headers, and HTTP status codes (200, 201, 404, etc.), which is more flexible and preferred for production-grade REST APIs.

Q8: How do you handle exceptions in Spring Boot REST APIs?
A8: We use @ControllerAdvice with @ExceptionHandler to build Global Exception Handlers.
For example:

Define custom exceptions like CustomerNotFoundException.

Handle them in a centralized exception handler.

Return appropriate error messages and HTTP status codes (404, 500, etc.).

Q9: What are the key features of Java 17?
A9:

Sealed classes/interfaces → control inheritance.

Pattern matching for switch.

Strict floating-point semantics.

API improvements (Foreign function & memory API, Vector API, Context-specific deserialization filters).

We used sealed classes in our project to restrict inheritance and enforce strict design rules.

Q10: Explain intermediate vs terminal operations in Java Streams.
A10:

Intermediate operations (lazy): Transform a stream into another stream. Examples: map, flatMap, filter, distinct, sorted, limit.

Terminal operations (eager): Produce a result or side effect. Examples: forEach, collect, count, reduce, findFirst.

Difference between map and flatMap:

map: Transforms each element into a single element.

flatMap: Transforms each element into a stream, then flattens into one combined stream.

Q11: What is the use of @PreAuthorize in Spring Security?
A11:
@PreAuthorize is used for method-level security. It ensures that only users with specific roles/permissions (e.g., ROLE_ADMIN) can access certain methods. It works along with @EnableMethodSecurity.

Q12: How do you use AOP in your project?
A12: I used Aspect-Oriented Programming (AOP) for:

Logging,

Transaction management,

Security checks,

Monitoring cross-cutting concerns.

Q13: What database design considerations do you follow for high-volume systems?
A13:

Normalization & Denormalization (normalize for integrity, denormalize for performance).

Indexing on frequently used columns.

Partitioning & Sharding for scalability.

Caching frequently accessed data.

Replication for availability.

Optimizing queries and using connection pools to manage DB connections efficiently.

Q14: Can you explain your Parking System design?
A14:
We designed a Parking System with the following:

Enums: SlotStatus (EMPTY/OCCUPIED), VehicleType.

Interfaces: ParkingEventListener, AllocationStrategy.

Core Classes: Car, Indicator, ParkingSlot, Ticket.

Strategy Pattern: NearestFirstStrategy for slot allocation.

Observer Pattern: DisplayBoard listens to slot availability changes.

Thread-Safe ParkingLot: Manages slots, tickets, notifies listeners.

Gates: EntryGate (admit cars) and ExitGate (release cars).

Flow:

EntryGate.admit(car) → calls ParkingLot.park(car).

ParkingLot finds a free slot (via AllocationStrategy).

ParkingSlot.occupy(car) → updates Indicator.

ParkingLot decrements available count, creates Ticket, notifies DisplayBoard.

DisplayBoard shows "Available Slots: N" or "Full".

On exit: ExitGate.release(ticketId) → calls ParkingLot.unpark(ticketId) → slot vacated, count updated, DisplayBoard notified.

