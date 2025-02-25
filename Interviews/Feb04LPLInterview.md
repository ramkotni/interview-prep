1. What is MongoDB journaling?
Answer:
Journaling in MongoDB refers to the process that provides a consistent view of data on disk and allows MongoDB to recover from the last checkpoint. If MongoDB exits unexpectedly between checkpoints, journaling is required to recover information that occurred after the last checkpoint. It creates a journal record for each client-initiated write operation, including any internal write operations like document updates that may also modify associated indexes.

2. Why does MongoDB create a single journal record for both update operations and index modifications?
Answer:
MongoDB creates a single journal record for both the update operation and index modifications to ensure consistency and atomicity. When a document is updated in a collection, the index might need to be modified as well. By combining these operations into a single journal record, MongoDB ensures that both updates and index changes are logged together, helping in recovery in case of a failure.

3. What is the role of the G1 Garbage Collector in Java 17?
Answer:
The G1 Garbage Collector (G1GC) in Java 17 has received several performance enhancements, such as improved memory usage by removing duplicate strings and better performance when dealing with large objects. Additionally, there has been a speed-up in parallel full GC processes, which significantly enhances the application's performance.

4. What are functional interfaces in Java, and what are the different types?
Answer:
Functional interfaces in Java are interfaces with a single abstract method. They support lambda expressions and are used primarily for functional programming. The four common types of functional interfaces are:

Predicate: Accepts input and returns a boolean (true or false).
Consumer: Accepts an argument but does not return a value.
Supplier: Does not accept any arguments but returns a value.
Function: Takes an argument and returns a result.
5. How does Java handle Optional to avoid null pointer exceptions?
Answer:
Java Optional is used to handle potential null values in a way that avoids NullPointerExceptions. Methods like orElse provide default values when the value is absent, while ifPresent executes code only if the value is present. The equals method checks equality between Optional objects.

6. What is the difference between fail-fast and fail-safe iterators in Java?
Answer:
A fail-fast iterator immediately throws a ConcurrentModificationException if the collection structure is modified while iterating. In contrast, a fail-safe iterator does not throw any exception and can safely handle concurrent modifications during iteration.

7. How to handle concurrent modification in Java collections?
Answer:
To handle concurrent modifications, Java provides thread-safe collections, like ConcurrentHashMap. This allows multiple threads to read and write data concurrently. For complex operations, you may need to use methods like compute to ensure data consistency when updating key-value pairs.

8. What is the difference between submit and execute in Executor Services?
Answer:
The execute method from the Executor interface simply executes a given Runnable task without returning a result. On the other hand, the submit method returns a Future object that represents the result of the submitted task. This allows the checking of completion, waiting for results, or retrieving the result of the task.

9. How do you transition from a monolithic to a microservices architecture?
Answer:
The process involves breaking down a monolithic application into smaller, independent services. Key steps include evaluating the current system, identifying modular components, refactoring the code, splitting databases, and designing communication between services. The architecture must be thoroughly tested, and performance should be monitored during migration.

10. What is the Circuit Breaker design pattern?
Answer:
The Circuit Breaker pattern is used for fault tolerance in microservices. It helps prevent failures from propagating between services. The pattern operates in three states:

Closed: The service works normally.
Open: The service is not functioning, and requests are blocked.
Half-Open: The service is intermittently tested to see if it is recovering.
11. What is Load Balancing in microservices?
Answer:
Load balancing in microservices distributes traffic across multiple instances of a service to ensure that no single server is overloaded. It improves scalability, fault tolerance, and responsiveness by evenly distributing traffic and rerouting it in case of server failure. There are two types: server-side and client-side load balancing.

12. How does the Two-Phase Commit Protocol work in a distributed system?
Answer:
The Two-Phase Commit Protocol ensures consistency across distributed systems. It has two phases:

Prepare Phase: Participants vote to commit or roll back.
Commit Phase: The coordinator instructs all participants to either commit or roll back based on the votes. It ensures data consistency even across distributed systems.
13. What is JWT in microservices authentication?
Answer:
JWT (JSON Web Token) is used for authentication and authorization in microservices. It is a compact, URL-safe token that is used to verify the identity of the user and to ensure secure communication between services.

14. How does caching work in Spring JPA?
Answer:
In Spring JPA, caching is implemented using annotations like @Cacheable. This annotation is applied to methods to cache the results of expensive operations. Caching helps improve performance by avoiding redundant database queries.

15. What is the significance of @ManyToOne and @OneToMany annotations in JPA?
Answer:
In JPA, the @ManyToOne annotation represents the "many" side of a relationship, while the @OneToMany represents the "one" side. For example, a Student entity could be associated with a Department entity. The @ManyToOne is used on the Student entity, and the @OneToMany is used on the Department entity.

16. How is localization handled in React?
Answer:
Localization in React can be achieved using libraries such as i18n. React doesn't have built-in localization features, but using i18n libraries helps translate UI elements into different languages for better accessibility and internationalization.

17. What is useState vs useRef in React?
Answer:
In React, useState is used to manage state values that trigger a re-render when updated, while useRef is used for storing mutable values that persist across renders without triggering re-renders.

18. What is a custom hook in React?
Answer:
A custom hook in React is a reusable function that encapsulates logic and can be shared across components. Custom hooks are prefixed with use and help improve code reusability. An example is useLocalStorage, which interacts with the browser's local storage.

19. What is useMemo vs React.memo?
Answer:

React.memo is a higher-order component that prevents unnecessary re-renders of a functional component if the props haven't changed.
useMemo is a hook that memoizes the result of a function and only recomputes it when its dependencies change. It is useful for expensive calculations or operations that are not needed on every render.
20. What is Redux in React?
Answer:
Redux is a state management library in React that helps manage the state of an application globally. It allows for consistent and predictable state updates, especially for larger and more complex applications.

21. How do you handle resetting state in Redux?
Answer:
Resetting state in Redux can be done by modifying the root reducer to handle a global reset action or by resetting individual slices using Redux Toolkit. The state can be reset to its initial value using action dispatching.

22. What is the purpose of using @Cacheable in Spring?
Answer:
The @Cacheable annotation in Spring is used to cache the result of a method, improving performance by storing previously computed values. It avoids repetitive expensive computations or database queries by fetching the result from the cache if available.
