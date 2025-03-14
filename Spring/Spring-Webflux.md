Spring WebFlux Hello World Example

The Spring Web Flux provides different applications to developers to develop asynchronous, non-blocking web applications by using Mono, Flux, and other classes. In this article, we will be learning to write a basic Hello World program in Spring WenFlux.

Project Creation:
Open STS (Spring Tool Suite) and then select New Project.
After that, we will be redirected to a project creation screen, in Select Project Category like maven or gradle, choose any (Here we will be using Gradle).
Then provide the project name, package name, and other details.
Then select dependencies.
Now click on finish.

Project Dependencies:
In this project, we have used below dependencies and the project category is gradle.

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-webflux'
    developmentOnly 'org.springframework.boot:spring-boot-devtools'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testImplementation 'io.projectreactor:reactor-test'
}

Hello World Program in Spring WebFlux
Here, we have provided a basic example for printing Hello World by using @RestController.

For this, in main package, we have created one Java class named as HelloWorldController.
After that, we have created one @GetMapping end point with name hello.
The @GetMapping is used for creating API End points.
While open with browser, this return output as Hello, World!.

package com.app;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

@RestController
public class HelloWorldController {

    @GetMapping("/hello")
    public Mono<String> hello() {
        return Mono.just("Hello, World!");    //prints Hello, World!
    }
}

package com.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloWorldApplication {
    // Main Method
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}


Spring WebFlux Hello World Example
Last Updated : 28 Feb, 2024
The Spring Web Flux provides different applications to developers to develop asynchronous, non-blocking web applications by using Mono, Flux, and other classes. In this article, we will be learning to write a basic Hello World program in Spring WenFlux.

Project Creation:
Open STS (Spring Tool Suite) and then select New Project.
After that, we will be redirected to a project creation screen, in Select Project Category like maven or gradle, choose any (Here we will be using Gradle).
Then provide the project name, package name, and other details.
Then select dependencies.
Now click on finish.
Project Folder Structure:
Project Structure
Project Dependencies:
In this project, we have used below dependencies and the project category is gradle.

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-webflux'
    developmentOnly 'org.springframework.boot:spring-boot-devtools'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testImplementation 'io.projectreactor:reactor-test'
}
Hello World Program in Spring WebFlux
Here, we have provided a basic example for printing Hello World by using @RestController.

For this, in main package, we have created one Java class named as HelloWorldController.
After that, we have created one @GetMapping end point with name hello.
The @GetMapping is used for creating API End points.
While open with browser, this return output as Hello, World!.
HelloWorldController class:

package com.app;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

@RestController
public class HelloWorldController {

    @GetMapping("/hello")
    public Mono<String> hello() {
        return Mono.just("Hello, World!");    //prints Hello, World!
    }
}
Main Class:

This is a main class of the project.


package com.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloWorldApplication {
    // Main Method
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}
After successfully running this project as Spring Boot App, open any browser then type below API End Point URL:

http://localhost:8080/hello

Explanation of the above Program:
First, we have created one class in main package of project.
The class name is HelloWorldController.
After this, we have created one Get Mapping by using @GetMapping with parameter /hello.
Next, we run this project as Spring Boot Application.
After running, open browser then type the Get mapping URL that is provided in the above.
Once hit that API end point, we got the expected output that is visible in the output screen.

Event loop in Spring WebFlux

Spring WebFlux is a version of the Spring Framework that supports reactive programming, allowing for non-blocking, asynchronous code execution. At the core of its framework, the event loop model is designed to efficiently handle multiple simultaneous requests.

For example, if there are multiple event loops, each event loop group is assigned a socket channel, and each event loop is controlled by an event loop group. The event loop model of Spring WebFlux allows for the efficient handling of many concurrent requests with fewer threads, making it suitable for applications that require high scalability and responsiveness. This simple example shows the basics which has to create a non-blocking REST endpoint using Spring WebFlux.

Spring WebFlux is a version of the Spring Framework that supports reactive programming, allowing for non-blocking, asynchronous code execution. At the core of its framework, the event loop model is designed to efficiently handle multiple simultaneous requests.

For example, if there are multiple event loops, each event loop group is assigned a socket channel, and each event loop is controlled by an event loop group. The event loop model of Spring WebFlux allows for the efficient handling of many concurrent requests with fewer threads, making it suitable for applications that require high scalability and responsiveness. This simple example shows the basics which has to create a non-blocking REST endpoint using Spring WebFlux.

<dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-webflux</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>io.projectreactor</groupId>
            <artifactId>reactor-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

Step 1: Main Class File
Once project is created, automatically Spring framework creates this class with main function and spring application execution starts from here only.

ProjectApplication.java:
package com.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ProjectApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjectApplication.class, args);
    }

}
Step 2: Create Controller
We created a RestController class by using @RestController annotation with name EventHandler in main package of project. This class is used for define the API endpoints as well as defining the required business logic in this class. Below we provide that handler code.

EventHandler.java:
package com.app;

import java.time.Duration;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/api/")
public class EventHandler {

    @GetMapping("/welcome")
    public Mono<String> sayHello() {
        return Mono.just("Hello, Welcome to GeeksForGeeks!").delayElement(Duration.ofSeconds(3));
    }

    @GetMapping("/data")
    public Flux<String> getData() {
        return Flux.just("One", "Two", "Three", "Four").delayElements(Duration.ofSeconds(1));
    }
}

In the above class, we created two different types of APIs for checking event loop functionality in the Handler class.
First, we create a method named called sayHello(). This method returns String type of Mono object.
After this, we created one more method called getData() in the same way, this method is able to return the result in the form of flux of events.
Step 3: Run the Project
Once project development is completed, run the project as Spring Boot App or we can run this project by using Maven commends. Here, we run this project as Spring Boot App. This Project running on 8080 port number with Netty server by default.

Step 4: Test the API
Now test API endpoint. Here, we use Postman tool for API testing.

welcome API:

This API is GET Mapping.

http://localhost:8080/api/welcome

data API:

This API is GET Mapping.

http://localhost:8080/api/data

Event Loop in Action
Handling Requests: When a request hits the API endpoints, it is received by a Netty server which dispatches the request to one of the event loops in its EventLoopGroup.
Scheduling Delays: For the mono, the call to delayElement(Duration.ofSeconds(1)) does not block the event loop. Instead, it schedules a task to complete the Mono after 1 second. The event loop is free to handle other requests during this time.
Processing Flux: The Flux uses delayElements(Duration.ofSeconds(1)). Each element is emitted with a 1-second delay. The event loop schedules these emissions without blocking the thread.
Non-blocking Completion: Once the delay period is over, the event loop handles the completion of the Mono or the next element of the Flux. It invokes the registered callbacks, such as sending the response back to the client.

