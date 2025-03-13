API Gateway Pattern

An API Gateway acts as a single entry point for all clients, routing requests to the appropriate microservices. It can handle cross-cutting concerns such as authentication, logging, rate limiting, and load balancing.

A large e-commerce platform where multiple clients (web, mobile, third-party) need to interact with various services (catalog, user management, orders). The API Gateway simplifies client communication by providing a unified interface and handling complexities like security and routing.

An API Gateway acts as a single entry point for all clients, routing requests to the appropriate microservices. It can handle cross-cutting concerns such as authentication, logging, rate limiting, and load balancing.

A large e-commerce platform where multiple clients (web, mobile, third-party) need to interact with various services (catalog, user management, orders). The API Gateway simplifies client communication by providing a unified interface and handling complexities like security and routing.

Advantages of API gateway pattern –

It encloses the whole internal structure of web applications. 
It never calls a particular service. For example, client interaction with API gateway.
It helps in the simplification of code of the client-side.
Disadvantages of API gateway pattern – 

It is an important component for every web application means the web application services will be shown only if the API is up-to-date means updated.
It becomes very important for each process for being lightweight because otherwise their time complexity will get increased because their developer has to wait in the process of updating API. 

What is API Gateway | System Design?
Last Updated : 26 Nov, 2024
An API Gateway is a key component in system design, particularly in microservices architectures and modern web applications. It serves as a centralized entry point for managing and routing requests from clients to the appropriate microservices or backend services within a system.
Table of Content

What is an API Gateway?
How does API Gateway work?
How differently API Gateway works with Microservices and Monolith Architecture?
API Gateway with Microservices Example
API Gateway with Monolith Example
Best practices for implementing API Gateway
Benefits of using an API Gateway
Challenges of using an API Gateway
Popular API Gateway Solution
What is an API Gateway?
One service that serves as a reverse proxy between clients and backend services is the API Gateway. After receiving incoming client requests, it manages a number of responsibilities, including rate limitation, routing, and authentication, before forwarding the requests to the appropriate backend services.


By offering a consistent interface and hiding the complexity of the underlying architecture, it acts as a single point of entry for clients to access a variety of services.

In the above diagram:

User will send the request from mobile or web application.
API Gateway will determine which request is coming.
Authentication means the user need to proof there identity to the server or client, by providing there User_Id and Password. For example: Login or Signup page.
SSL full form Secure Socket Layer, it is used to establish an encrypted link between a server and a client.
It provides the ability to perform protocol translation, where incoming requests are translated from one channel to another.
When requests are aggregated, a request received by an API gateway will trigger requests to different endpoints, and return response to the client.

The primary purpose of an API Gateway is to simplify the client’s interaction with the underlying services, enhance security, and provide various features for managing and monitoring API traffic.


How does API Gateway work?
Let us see how API Gateway works:

Step 1: Routing
The API Gateway initially analyzes a request sent by a client to identify which service or microservice should handle it. The URL path, HTTP method, or headers are just some of the criteria that might be used to determine this routing.
Step 2: Protocol translation
Incoming requests can be converted between protocols via the API Gateway. For instance, it can receive client HTTP queries and translate them into WebSocket or gRPC requests for backend services.
Step 3: Request aggregation
To complete a single request, a client may occasionally need to retrieve information from several providers. To increase efficiency and cut down on round trips, the API Gateway can combine these calls into a single call.
Step 4: Authentication and authorization
Incoming request permission and authentication can be managed by the API Gateway. It can confirm the client’s authentication and determine whether they are authorized to access the resources they have requested.
Step 5: Rate limiting and throttling
The API Gateway can include rate-limiting and throttling rules to guard against misuse and guarantee balanced resource use. It may restrict how many queries a client may submit in a given amount of time.
Step 6: Load balancing
The API Gateway can distribute incoming requests across multiple instances of a service to ensure high availability and scalability.
Step 7: Caching
To improve performance, the API Gateway can cache responses from backend services and serve them directly to clients for subsequent identical requests.
Step 8: Monitoring and logging
Incoming request metrics and logs can be gathered by the API Gateway, which offers information on system performance and usage.
How differently API Gateway works with Microservices and Monolith Architecture?
The way an API Gateway works with microservices differs from how it works with a monolithic architecture in several key aspects:

| **Aspect**                 | **Monolithic Architecture**                                                                                             | **Microservices Architecture**                                                                                                     |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| **Request routing**         | In a monolithic architecture, the API Gateway typically routes requests to different parts of the monolith based on the request URL or other criteria. | In a microservices architecture, the API Gateway routes requests to different microservices based on the request URL or other criteria, acting as a “front door” to the microservices ecosystem. |
| **Service discovery**       | In a monolithic architecture, service discovery is not typically a concern, as all parts of the application are contained within the same codebase. | In a microservices architecture, the API Gateway may need to use service discovery mechanisms to dynamically locate and route requests to the appropriate microservices. |
| **Authentication and authorization** | In both architectures, the API Gateway can handle authentication and authorization. However, in a microservices architecture, there may be more complex authorization scenarios, as requests may need to be authorized by multiple microservices. | In both architectures, the API Gateway can handle authentication and authorization. However, in a microservices architecture, there may be more complex authorization scenarios, as requests may need to be authorized by multiple microservices. |
| **Load balancing**          | In both architectures, the API Gateway can perform load balancing. | However, in a microservices architecture, load balancing may be more complex, as requests may need to be load balanced across multiple instances of multiple microservices. |
| **Fault tolerance**         | In both architectures, the API Gateway can provide fault tolerance by retrying failed requests and routing requests to healthy instances of services. | However, fault tolerance may be more critical in a microservices architecture, where the failure of a single microservice should not bring down the entire system. |

API Gateway with Microservices Example
Example Scenario:


Let’s consider a hypothetical e-commerce system with microservices. The system has services for user management, product catalog, shopping cart, and order processing. Clients interact with the system through a web application.

Explanation of the above diagram
The web application communicates with the API Gateway.
The API Gateway routes requests to the appropriate microservices (e.g., user-related requests to the Users service).
It handles authentication, rate limiting, caching, and other functions.
Error responses are also standardized by the API Gateway.
API Gateway with Monolith Example
Example Scenario:


Consider a traditional e-commerce monolithic application. The API Gateway can still serve as a central entry point and manage authentication, request transformation, caching, and other features.

Explanation of the above the diagram
The web application communicates with the API Gateway.
The API Gateway simplifies client interactions and provides security and caching and other features.
It also manages API versioning and error handling.
Best practices for implementing API Gateway
Below are the best practices for API Gateway:

Security: To prevent abuse, utilize SSL/TLS for encryption, implement strong authentication and authorization methods, and use IP whitelisting and rate limiting.
Performance Optimization: Reduce latency and speed up response times by utilizing caching, request/response compression, and effective routing.
Scalability: Design for horizontal scalability, use load balancing, and monitor performance metrics to scale resources as needed.
Monitoring and Logging: Use monitoring tools to track performance indicators, interface with logging and monitoring systems for centralized management, and implement extensive logging.
Error Handling: Implement robust error handling mechanisms and use standardized error codes and messages for consistency.
Versioning and Documentation: Maintain backward compatibility and manage changes with versioning. Also, keep documentation updated so developers can learn how to use the API.
Benefits of using an API Gateway
Centralized Entry Point
Clients (such as web or mobile applications) usually need to communicate with many endpoints in order to access various functionality in complex systems that include multiple microservices or backend services.
Routing and Load Balancing
API Gateways analyze incoming requests and determine which backend service should handle them based on various factors such as the request’s URL, headers, or even the content of the request.
Additionally, they can distribute incoming requests evenly across multiple instances of the same service to ensure load balancing.
Authentication and Authorization
Only authorized users or apps can access the services behind the gateway due to their ability to enforce authentication.
Usually, tools like JWTs, OAuth tokens, and API keys are used for this. Additionally, they manage authorization by determining whether the application or user that has been authenticated has the required rights to access particular resources.
Request and Response Transformation
API Gateways can transform requests and responses as they pass through.
For example, they can convert data formats (e.g., from JSON to XML or vice versa) to ensure compatibility between different parts of the system.
Challenges of using an API Gateway
API Gateways can introduce several challenges, especially in complex environments or when not properly configured. Some common challenges include:

Performance bottlenecks: When managing a high volume of requests, API gateways may become a performance bottleneck or a single point of failure. To make sure they can support the load, careful configuration and design are needed.
Increased latency: Requests may experience increased latency if an API gateway is introduced, particularly if complicated routing, authentication, or other processes must be carried out. This problem can be reduced by using caching and optimizing the Gateway’s configuration.
Complexity: Managing and configuring an API Gateway can be complex, especially in environments with a large number of services and endpoints. Proper documentation and automation tools can help reduce this complexity.
Security risks: Security flaws including incorrect permission, authentication, or the disclosure of private data can be brought about by improperly designed API gateways. To reduce these threats, regular security assessments and updates are crucial.
Scalability challenges: It can be difficult to scale an API gateway, particularly in dynamic environments with varying demand. To guarantee scalability, load balancing and horizontal scaling techniques are important.
Popular API Gateway Solution
Below are some API Gateway Solution:

Amazon API Gateway: It is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. It supports RESTful APIs as well as WebSocket APIs for real-time communication.
Apigee: It now part of Google Cloud, is a platform that enables organizations to design, secure, deploy, monitor, and scale APIs. It offers features like API analytics, API monetization, and developer portal management.
Kong: It is an open-source API Gateway and microservices management layer. It is built on top of Nginx and provides features like request routing, authentication, rate limiting, and logging.
Microsoft Azure API Management: It is a fully managed service that helps organizations publish, secure, and manage APIs. It offers features like API gateway functionality, developer portal management, and API versioning.
Conclusion
An API Gateway is a central component in system design that helps manage and optimize the communication between clients and backend services. It simplifies client interactions, enhances security, and provides various features for controlling and monitoring API traffic, making it an essential part of modern distributed systems and microservices architectures.


