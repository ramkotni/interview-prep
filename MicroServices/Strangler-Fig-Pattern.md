Strangler Fig Pattern

This pattern incrementally replaces a legacy system with a microservices architecture. The new system gradually takes over the functionality of the old system until the legacy system is entirely replaced.

Migrating a monolithic insurance application to a microservices architecture. The strangler fig pattern allows the new microservices to take over functionalities one by one, reducing the risk and complexity associated with a big-bang migration.

Strangler Pattern in Micro-services | System Design
Last Updated : 29 Aug, 2023
The Strangler pattern is an architectural approach employed during the migration from a monolithic application to a microservices-based architecture. It derives its name from the way a vine slowly strangles a tree, gradually replacing its growth. Similarly, the Strangler pattern involves replacing parts of a monolithic application with microservices over time.

In order to implement strangler pattern, we need to follow 3 steps that are as follows:

Transform
Co-exists
Eliminate

Use Cases for the Strangler Pattern:
The Strangler pattern is primarily used when migrating from a monolithic architecture to microservices. It proves beneficial in scenarios where complete system rewrites pose significant risks and disruptions. This pattern is particularly suitable for legacy systems with complex codebases that are challenging to refactor entirely.

Features of the Strangler Pattern:
The Strangler pattern offers several essential features:

Gradual Migration: This pattern enables a step-by-step migration from a monolithic application to microservices. It allows organizations to replace specific functionality or modules incrementally.
Coexistence: During the migration process, the monolithic application and microservices coexist, ensuring uninterrupted system functionality.
Strangling Behavior: The Strangler pattern gradually replaces components or modules of the monolithic application with microservices, leading to the eventual replacement of the legacy system.
Implementation of Strangler Pattern:
Consider an e-commerce application with a monolithic architecture. To migrate the order management functionality to microservices using the Strangler pattern, follow these implementation steps:

Identify the order management functionality within the monolithic application.
Create an order management microservice.
Configure the API gateway to route order management requests to the microservice.
Migrate specific functionalities from the monolithic application to the microservice.
Repeat steps 1-4 until the monolithic application is fully replaced.

Use Cases for the Strangler Pattern:
The Strangler pattern is primarily used when migrating from a monolithic architecture to microservices. It proves beneficial in scenarios where complete system rewrites pose significant risks and disruptions. This pattern is particularly suitable for legacy systems with complex codebases that are challenging to refactor entirely.

Features of the Strangler Pattern:
The Strangler pattern offers several essential features:

Gradual Migration: This pattern enables a step-by-step migration from a monolithic application to microservices. It allows organizations to replace specific functionality or modules incrementally.
Coexistence: During the migration process, the monolithic application and microservices coexist, ensuring uninterrupted system functionality.
Strangling Behavior: The Strangler pattern gradually replaces components or modules of the monolithic application with microservices, leading to the eventual replacement of the legacy system.
Implementation of Strangler Pattern:
Consider an e-commerce application with a monolithic architecture. To migrate the order management functionality to microservices using the Strangler pattern, follow these implementation steps:

Identify the order management functionality within the monolithic application.
Create an order management microservice.
Configure the API gateway to route order management requests to the microservice.
Migrate specific functionalities from the monolithic application to the microservice.
Repeat steps 1-4 until the monolithic application is fully replaced.


