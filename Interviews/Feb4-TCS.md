Q1: Can you explain the changes introduced in Java 8 Futures?
A1: Yes! In Java 8, there were several changes, such as:

Lambda expressions
Stream APIs
Functional interfaces
Default methods in interfaces
Base64 encoding and decoding methods
Optional classes
Collector classes for stream operations
Parallel array streams
Q2: What is the difference between map, filter, and reduce in Java Streams?
A2:

Map: The map operation transforms each element of the stream using a given function.
Filter: The filter operation is used to filter the elements of a stream based on a condition specified by a predicate.
Reduce: The reduce operation is used to aggregate or combine the elements of the stream into a single result, like summing the elements or finding the maximum.
Q3: What is the difference between Comparable and Comparator in Java?
A3:

Comparable: Used when objects of a class need to be compared with each other. The class implements the Comparable interface and overrides the compareTo method.
Comparator: Used when we need to compare objects from different classes or implement custom comparison logic. It uses the compare method to compare two objects.
Q4: What is the difference between Future and CompletableFuture?
A4:

Future: Used for simple asynchronous operations and it blocks when trying to get the result of the task.
CompletableFuture: A better choice for complex asynchronous programming as it provides non-blocking operations, the ability to combine multiple tasks together, and handle task completion via callbacks. You can also manually complete tasks in CompletableFuture, which isn't possible with Future.
Q5: What is manual completion in the context of CompletableFuture?
A5: Manual completion refers to the ability to explicitly complete a task in CompletableFuture. Instead of relying on automatic execution flow, the developer can control when the task is marked as complete. This is useful for situations where the task depends on external conditions or other computations.

Q6: Can you explain what reactive programming is in Java?
A6: Reactive programming in Java refers to asynchronous programming where data streams and propagation of changes are handled. It allows expressing dynamic data streams easily and is based on the concept of handling streams of data and events. This is implemented via the Reactive Streams API, and it enables developers to process and manipulate streams in a functional style, improving code readability and performance.

Q7: How does Java Streams work in a functional style?
A7: Java Streams allow developers to process sequences of elements in a functional style. Instead of using traditional loops, you can use operations like map, filter, and collect to process data in a declarative manner. This approach makes the code more readable and less error-prone, especially with complex operations on large datasets.

Q8: What is thread-local storage in Java?
A8: Thread-local storage is a memory management technique in Java that allows each thread to have its own independent copy of a variable. This prevents data sharing between threads and provides thread safety. The data appears to be global in the system but is actually local to the thread using it, which can help prevent synchronization issues.

