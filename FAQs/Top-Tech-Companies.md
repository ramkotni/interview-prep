Here's a structured markdown file (.md) format for interview questions and answers for Java Full Stack Developer roles across top tech companies:

markdown
Copy
Edit
# Top Tech Companies - Interview Questions and Answers for Java Full Stack Developer Role

---

## 1. **Google**

### **Common Interview Questions:**

1. **What is the difference between `==` and `.equals()` in Java?**
   - `==` compares the memory address of two objects, while `.equals()` compares the actual content of the objects. The `.equals()` method should be overridden to provide meaningful equality checks, such as comparing the fields of an object.

2. **Explain the concept of "Dependency Injection" in Spring.**
   - Dependency Injection (DI) is a design pattern used to implement Inversion of Control (IoC), where the Spring framework provides the objects that a class needs instead of the class creating them. DI can be achieved via Constructor Injection, Setter Injection, or Field Injection.

3. **Describe the Spring Boot architecture.**
   - Spring Boot is a framework for building Java-based web applications quickly. It simplifies configuration by using sensible defaults and auto-configuration. It integrates well with Spring Framework, allowing developers to focus on business logic rather than boilerplate code.

4. **How does garbage collection work in Java?**
   - Java's garbage collector automatically manages memory. It removes objects that are no longer referenced by the program, thus freeing memory. The process involves several stages: marking, sweeping, and compacting.

### **Technical Challenge:**
- **Problem:** Given a list of numbers, find the two numbers that add up to a specific target.
- **Solution:** Write a function using HashMap to store differences and retrieve matching numbers.

---

## 2. **Amazon**

### **Common Interview Questions:**

1. **What is the difference between `ArrayList` and `LinkedList` in Java?**
   - `ArrayList` is backed by a dynamic array, which provides fast random access but slower insertions and deletions (due to shifting elements). `LinkedList`, on the other hand, is a doubly linked list with slower random access but faster insertions and deletions.

2. **Explain how Spring Security works.**
   - Spring Security provides authentication and authorization mechanisms for Java applications. It works by intercepting HTTP requests, determining if the user is authenticated, and checking for required roles or permissions.

3. **What are RESTful services, and how do they differ from SOAP?**
   - RESTful services are based on stateless communication and standard HTTP methods (GET, POST, PUT, DELETE). SOAP (Simple Object Access Protocol) is an XML-based protocol that has more overhead and requires specific processing for request/response formats.

4. **How do you handle exceptions in Spring Boot?**
   - Spring Boot provides `@ControllerAdvice` for global exception handling and `@ExceptionHandler` for handling exceptions in a specific controller. `@ResponseStatus` can also be used to return specific HTTP status codes.

### **Technical Challenge:**
- **Problem:** Implement an algorithm to find the kth largest element in an unsorted array.
- **Solution:** Use a priority queue (min-heap) to maintain the top k largest elements.

---

## 3. **Facebook (Meta)**

### **Common Interview Questions:**

1. **What is the purpose of `final` keyword in Java?**
   - The `final` keyword in Java can be used to define constants, prevent method overriding, or prevent inheritance of a class. A `final` class cannot be subclassed, a `final` method cannot be overridden, and a `final` variable cannot be reassigned.

2. **How do you optimize SQL queries in Java?**
   - Indexing is one of the primary ways to optimize SQL queries. Other strategies include query rewriting for better performance, avoiding SELECT *, using prepared statements to prevent SQL injection, and limiting the use of joins.

3. **Explain the difference between `HashMap` and `TreeMap` in Java.**
   - `HashMap` is an unordered collection that allows fast access to data using a hash table, while `TreeMap` stores keys in a sorted order (natural ordering or using a comparator) and offers slower performance than `HashMap`.

4. **What are microservices and how does Spring Boot support them?**
   - Microservices are an architectural style where an application is composed of loosely coupled, independently deployable services. Spring Boot simplifies the creation of microservices by providing auto-configurations, embedded servers, and easy integration with Spring Cloud for service discovery, circuit breakers, and distributed tracing.

### **Technical Challenge:**
- **Problem:** Implement a cache using a Least Recently Used (LRU) strategy.
- **Solution:** Use a LinkedHashMap with access order enabled to maintain the LRU order and evict the least recently accessed elements when the cache reaches a certain size.

---

## 4. **Microsoft**

### **Common Interview Questions:**

1. **What is the use of the `synchronized` keyword in Java?**
   - The `synchronized` keyword is used to control access to a method or block of code to ensure that only one thread can execute it at a time, thus preventing data inconsistency in multi-threaded environments.

2. **Explain the lifecycle of a Spring Bean.**
   - The lifecycle of a Spring Bean includes instantiation, dependency injection, initialization (post-processors), and destruction. You can control the bean's lifecycle using annotations like `@PostConstruct` and `@PreDestroy`, or via `InitializingBean` and `DisposableBean` interfaces.

3. **How would you handle versioning in REST APIs?**
   - Versioning can be handled in REST APIs using URL path parameters (e.g., `/api/v1/resource`), request headers (e.g., `Accept-Version`), or query parameters (e.g., `/api/resource?version=1`).

4. **What is the difference between `public`, `protected`, and `private` access modifiers in Java?**
   - `public`: The member is accessible from any class.<br>
   - `protected`: The member is accessible within the same package or subclasses.<br>
   - `private`: The member is accessible only within the same class.

### **Technical Challenge:**
- **Problem:** Create a Java application that reads and writes data from/to a MongoDB database.
- **Solution:** Use Spring Boot with Spring Data MongoDB to create CRUD operations and interact with MongoDB using repositories.

---

## 5. **Netflix**

### **Common Interview Questions:**

1. **What is Spring Boot's "auto-configuration"?**
   - Auto-configuration is a feature of Spring Boot that automatically configures your application based on the libraries on the classpath. For example, if Spring Boot detects that you have a specific database library, it will automatically configure the necessary beans for database connection.

2. **Explain the use of the `@RequestMapping` annotation in Spring MVC.**
   - The `@RequestMapping` annotation is used to map HTTP requests to handler methods of MVC and REST controllers. It can be used with different HTTP methods (GET, POST, PUT, DELETE) to handle various types of requests.

3. **What are design patterns you have used in Spring Boot?**
   - Common design patterns used in Spring Boot include Singleton, Factory, Observer (used in Spring events), and Proxy (used in AOP for logging, transactions, etc.).

4. **What is the difference between `@Entity` and `@Table` in JPA?**
   - `@Entity` is used to define a class as a JPA entity, which corresponds to a table in the database. `@Table` is used to specify the name of the table in the database if it is different from the entity's class name.

### **Technical Challenge:**
- **Problem:** Implement pagination in a Spring Boot REST API with MongoDB.
- **Solution:** Use `Pageable` and `Page` interfaces in Spring Data MongoDB to implement pagination.

---

## Conclusion

These are some of the most common interview questions for Java Full Stack Developer roles across top tech companies. To prepare effectively, focus on understanding core concepts of Java, Spring Boot, database interactions (like MongoDB and SQL), and REST APIs. Additionally, be ready to solve algorithmic problems to demonstrate your problem-solving skills.

This markdown file provides structured interview questions and answers for Java Full Stack Developer roles at top tech companies like Google, Amazon, Facebook, Microsoft, and Netflix. It includes both conceptual questions and technical challenges that candidates may encounter during interviews.