Implementing OAuth2 with Spring Security: A Step-by-Step Guide

OAuth is an authorization framework that creates a permissions policy and enables applications to have limited access to user accounts on HTTP services such as Facebook, GitHub, and Google. It works by allowing the users to authorize third-party applications to access their data without sharing their credentials. This article will guide you through implementing OAuth2 in the Spring Boot application using Security and enabling secure login and access to the user data via OAuth2 providers.

What is OAuth2?
OAuth2 (Open Authorization 2.0) is the authorization framework that allows the applications to obtain limited access to user accounts on HTTP services such as Facebook, GitHub, or Google without exposing the user credentials. OAuth2 provides a way for users to access their resources without sharing passwords with third-party applications.

Key Components:
Resource Owner: The user who authorizes the application to access their account.
Client: The application requesting the access to their users accounts.
Authorization Server: The server that authenticates the user and issues the access tokens to the client.
Resource Server: The server that hosts the protected resources and accept the access tokens for the access of the application.
OAuth2 Authorization Flows

OAuth2 defines the several authorization flows the accommodate the different cases:

Authorization Code Grant: The common flow then the suitable for the server side applications. It involves the authorization code exchanges of the application.
Implicit Grant: It is used for the client side applications where the access token is directly returned without the authorization code exchange.
Resource Owner Password Credentials Grant: It is suitable for the trusted applications where the client can directly ask the resources owner for their credentials.
Client Credentials Grant: It is used when the client needs to access its own resources rather than those of the resource owner of the application.
Prerequisites:
Good knowledge of the Spring Boot and Spring Security.
JDK and Intellij Idea installed in your local system.
Google Console Account for OAuth2 provider.
Maven for building dependency management.
Implementing OAuth2 with Spring Security
Step 1: Create a New Spring Boot Project

Create a new Spring Boot Project using IntelliJ Idea and on creating the project, choose the below options:

Project Name: oauth2-spring-security
Language: Java
Type: Maven
Packaging: Jar

Step 2: Add the Dependencies
Add the following dependencies into the Spring project.

Spring Security, OAuth2 Client, Thymeleaf, Spring Web, Spring Boot Dev Tools, Lombok

Step 3: Configure the Application Properties
Open the application.properties file and add the google OAuth configuration code into the project.

spring.application.name=oauth2-spring-security
spring.security.oauth2.client.registration.google.client-id=xxxxxxxxxx-p1io24vn17sdm658fl6ndtio65h17if9.apps.googleusercontent.com
spring.security.oauth2.client.registration.google.client-secret=xxxxxxx-HG1PQCUF1oxbMo0fYd3tc0kulswJ
spring.security.oauth2.client.registration.google.redirect-uri=http://localhost:8080/login/oauth2/code/{registrationId}
spring.security.oauth2.client.registration.google.scope=profile, email

Step 4: Create the User Class
This class represents a user in the application.

Go to src > main > java > oauth2springsecurity > model > User and put the below code.

package com.gfg.oauth2springsecurity.model;

import lombok.Data;

@Data
public class User {
    private String name;
    private String email;

    // Getters and Setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}

This class defines the User model with name and email attributes. It uses Lombok annotations for boilerplate code reduction.

Step 5: Create the UserService Class
This service class is responsible for creating User objects from OAuth2User data.

Go to src > main > java > oauth2springsecurity > service > UserService and put the below code.

package com.gfg.oauth2springsecurity.service;

import com.gfg.oauth2springsecurity.model.User;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    public User createUser(OAuth2User oAuth2User) {
        User user = new User();
        // Set user attributes from OAuth2User
        user.setName(oAuth2User.getAttribute("name"));
        user.setEmail(oAuth2User.getAttribute("email"));
        return user;
    }
}

The UserService class converts OAuth2User data to User objects. It extracts the user's name and email from the OAuth2 user attributes.

Step 6: Create the SecurityConfig Class
This class configures Spring Security for OAuth2 login.

Go to src > main > java > oauth2springsecurity > config > SecurityConfig and put the below code.

package com.gfg.oauth2springsecurity.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                // Authorize requests
                .authorizeRequests(authorizeRequests ->
                        authorizeRequests
                                .requestMatchers("/", "/login").permitAll()
                                .anyRequest().authenticated()
                )
                // Configure OAuth2 login
                .oauth2Login(oauth2Login ->
                        oauth2Login
                                .loginPage("/login")
                                .defaultSuccessUrl("/home", true)
                );
        return http.build();
    }
}

The SecurityConfig class sets up the security filter chain. It configures endpoint authorization and defines the OAuth2 login settings.

Step 7: Create the HomeController Class
This controller handles the login and home page requests.

Go to src > main > java > oauth2springsecurity > controller > HomeController and put the below code.

package com.gfg.oauth2springsecurity.controller;

import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/home")
    public String home(@AuthenticationPrincipal OAuth2User principal, Model model) {
        // Add user name to the model
        model.addAttribute("name", principal.getAttribute("name"));
        return "home";
    }

    @GetMapping("/login")
    public String login() {
        return "login";
    }
}

The HomeController handles requests for the login and home pages. It uses the @AuthenticationPrincipal annotation to access the authenticated user's details.

Step 8: Main Class
No changes are required in the main class.

package com.gfg.oauth2springsecurity;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Oauth2SpringSecurityApplication {

    public static void main(String[] args) {
        SpringApplication.run(Oauth2SpringSecurityApplication.class, args);
    }

}

The main class starts the Spring Boot application. No additional configuration is needed here for OAuth2.

Resource files
Step 9: Create the Login HTML File
This HTML file contains the structure and styles for the login page. It includes a button to initiate the OAuth2 login with Google.

Go to src > main > resources > templates > login.html and put the below HTML code.

<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Login</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .navbar {
            background-color: #81c784; /* Light Green */
        }
        .navbar-brand {
            color: white !important;
        }
        .container {
            margin-top: 100px;
        }
        .card {
            border: none;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .card-header {
            background-color: #81c784; /* Light Green */
            color: white;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }
        .btn-custom {
            background-color: #81c784; /* Light Green */
            color: white;
            border-radius: 5px;
        }
        .btn-custom:hover {
            background-color: #66bb6a; /* Darker Green */
            color: white;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg">
    <a class="navbar-brand" href="#">My App</a>
</nav>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header text-center">
                    Login with OAuth2
                </div>
                <div class="card-body text-center">
                    <p class="card-text">Please login using one of the following options:</p>
                    <a class="btn btn-custom" href="/oauth2/authorization/google">Login with Google</a>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
Step 10: Create the Home HTML File
This HTML file displays the home page after successful login.

Go to src > main > resources > templates > home.html and put the below HTML code.

<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Home</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .navbar {
            background-color: #81c784; /* Light Green */
        }
        .navbar-brand, .nav-link {
            color: white !important;
        }
        .container {
            margin-top: 50px;
        }
        .card {
            border: none;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .card-header {
            background-color: #81c784; /* Light Green */
            color: white;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg">
    <a class="navbar-brand" href="#">My App</a>
    <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="/logout">Logout</a>
            </li>
        </ul>
    </div>
</nav>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">
                    Welcome, <span th:text="${name}"></span>!
                </div>
                <div class="card-body">
                    <p class="card-text">You are now logged in using OAuth2.</p>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

This HTML file defines the structure and styling for the home page. It uses Thymeleaf to dynamically display the authenticated user's name.

pom.xml

<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.3.1</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.gfg</groupId>
    <artifactId>oauth2-spring-security</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>oauth2-spring-security</name>
    <description>oauth2-spring-security</description>
    <url/>
    <licenses>
        <license/>
    </licenses>
    <developers>
        <developer/>
    </developers>
    <scm>
        <connection/>
        <developerConnection/>
        <tag/>
        <url/>
    </scm>
    <properties>
        <java.version>17</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-oauth2-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.thymeleaf.extras</groupId>
            <artifactId>thymeleaf-extras-springsecurity6</artifactId>
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
            <groupId>org.springframework.security</groupId>
            <artifactId>spring-security-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>


Step 11: Run the application
Now run the application and it will start at port 8080.

Step 12: Testing the Application
To test the OAuth2 login, navigate to the following URLs in your web browser:

Login Page:
http://localhost:8080/login

You will see the login page, followed by the Google OAuth2 authentication process. Upon successful login, you will be redirected to the home page with a personalized welcome message.

Benefits of using OAuth2
Security: OAuth2 allows the application to access user data without exposing user credentials.
User Experience: Users can grant and invoke the access to their data without sharing passwords.
Scalability: OAuth2 supports multiple authorization flows, making it adaptable to the various application architectures and use cases.
Interoperability: OAuth2 can be widely adapted and enabling the seamless integration with many services and platforms.
