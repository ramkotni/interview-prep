Q2: What design patterns are mentioned in the conversation?
A2: The design patterns mentioned include the Singleton Design Pattern, Observable Design Pattern, Factory Design Pattern, and Decorator Design Pattern.

Q3: How do you implement the Singleton Design Pattern in Java?
A3: To implement the Singleton Design Pattern, you need a private constructor and a static instance of the class. Use a static method to get the instance and ensure global access. To make it thread-safe, synchronization should be applied.

Q4: What are the two types of Saga Design Pattern in microservices?
A4: The two types of Saga Design Pattern are Choreography and Orchestration. Choreography is a decentralized event-driven model, while Orchestration is a centralized model for managing distributed transactions.

Q5: Can you explain the difference between Choreography and Orchestration?
A5: In Choreography, each service communicates directly with others, forming a decentralized system. In Orchestration, a central system coordinates the communication between services.

Q6: How do you inject a distributed cache in a service?
A6: You can inject a distributed cache by using the @Qualifier annotation. If you are using a default cache, the @Primary annotation can be used, but for distributed caches, you should specify a different cache using @Qualifier.

Q7: How can you ensure that the most recently accessed element is moved to the end in a LinkedHashMap?
A7: You can ensure this by setting the accessOrder parameter to true when constructing the LinkedHashMap. This ensures that the most recently accessed element is moved to the end.

Q8: What happens when the cache exceeds its capacity in a LinkedHashMap-based cache implementation?
A8: When the cache exceeds its capacity, the least recently used entry is removed to make space for new elements. This is controlled by the removeEldestEntry method.

Q9: What is the time complexity for GET and PUT operations in a LinkedHashMap?
A9: The time complexity for both GET and PUT operations in a LinkedHashMap is O(1), which is efficient due to the underlying hash table structure.

Q10: How do you balance parentheses using a stack?
A10: To balance parentheses, you can use a stack. Push opening parentheses onto the stack and pop them when a closing parenthesis is encountered. If the stack is empty or the parentheses don't match, it's unbalanced.

Q11: What approach can be used to implement a stack in balancing parentheses?
A11: A stack-based approach, which works on the principle of Last In, First Out (LIFO), is the best approach for balancing parentheses.






