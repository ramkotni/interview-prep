Here is an example of a simple JWT implementation in Java using the io.jsonwebtoken library (jjwt).
Explanation:
Dependencies: Add the jjwt dependency to your pom.xml if you're using Maven.
JWT Utility Class: This class provides methods to generate and validate JWT tokens.
Key Features:
Generate a JWT token with claims.
Validate and parse a JWT token.
Maven Dependency:
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-api</artifactId>
    <version>0.11.5</version>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-impl</artifactId>
    <version>0.11.5</version>
    <scope>runtime</scope>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-jackson</artifactId>
    <version>0.11.5</version>
    <scope>runtime</scope>
</dependency>

JWT Utility class
import io.jsonwebtoken.*;
import io.jsonwebtoken.security.Keys;

import java.security.Key;
import java.util.Date;
import java.util.Map;

public class JwtUtil {

    private static final String SECRET_KEY = "your-256-bit-secret-your-256-bit-secret"; // Use a secure key
    private static final Key KEY = Keys.hmacShaKeyFor(SECRET_KEY.getBytes());
    private static final long EXPIRATION_TIME = 3600000; // 1 hour in milliseconds

    // Generate a JWT token
    public static String generateToken(String subject, Map<String, Object> claims) {
        return Jwts.builder()
                .setClaims(claims)
                .setSubject(subject)
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + EXPIRATION_TIME))
                .signWith(KEY, SignatureAlgorithm.HS256)
                .compact();
    }

    // Validate and parse a JWT token
    public static Claims validateToken(String token) {
        try {
            return Jwts.parserBuilder()
                    .setSigningKey(KEY)
                    .build()
                    .parseClaimsJws(token)
                    .getBody();
        } catch (JwtException e) {
            throw new RuntimeException("Invalid JWT token", e);
        }
    }
}

import java.util.HashMap;
import java.util.Map;

public class JwtExample {
    public static void main(String[] args) {
        // Generate a token
        Map<String, Object> claims = new HashMap<>();
        claims.put("role", "admin");
        String token = JwtUtil.generateToken("user123", claims);
        System.out.println("Generated Token: " + token);

        // Validate and parse the token
        try {
            Claims parsedClaims = JwtUtil.validateToken(token);
            System.out.println("Subject: " + parsedClaims.getSubject());
            System.out.println("Role: " + parsedClaims.get("role"));
        } catch (RuntimeException e) {
            System.err.println("Token validation failed: " + e.getMessage());
        }
    }
}

This example demonstrates how to generate and validate JWT tokens securely. Replace the SECRET_KEY with a strong, randomly generated key.

Steps to Implement JWT and OAuth2
1. Implementing JWT
JWT (JSON Web Token) is used for stateless authentication. Below are the steps:


Add Dependencies: Add a library like jjwt for JWT handling in your project.


<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-api</artifactId>
    <version>0.11.5</version>
</dependency>
Generate JWT Token: Create a utility class to generate and validate tokens.


import io.jsonwebtoken.*;
import io.jsonwebtoken.security.Keys;
import java.security.Key;
import java.util.Date;

public class JwtUtil {
    private static final String SECRET_KEY = "your-256-bit-secret";
    private static final Key KEY = Keys.hmacShaKeyFor(SECRET_KEY.getBytes());
    private static final long EXPIRATION_TIME = 3600000; // 1 hour

    public static String generateToken(String subject) {
        return Jwts.builder()
                .setSubject(subject)
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + EXPIRATION_TIME))
                .signWith(KEY, SignatureAlgorithm.HS256)
                .compact();
    }

    public static Claims validateToken(String token) {
        return Jwts.parserBuilder()
                .setSigningKey(KEY)
                .build()
                .parseClaimsJws(token)
                .getBody();
    }
}
Use JWT in Authentication:


Generate a token after successful login.
Validate the token in API requests.
<hr></hr>
2. Implementing OAuth2
OAuth2 is used for delegated access to resources. Below are the steps:


Add Dependencies: Use Spring Security for OAuth2 implementation.


<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-client</artifactId>
</dependency>
Configure OAuth2 Client: Add client details in application.yml.


spring:
  security:
    oauth2:
      client:
        registration:
          google:
            client-id: your-client-id
            client-secret: your-client-secret
            scope: profile, email
            redirect-uri: "{baseUrl}/login/oauth2/code/{registrationId}"
            authorization-grant-type: authorization_code
        provider:
          google:
            authorization-uri: https://accounts.google.com/o/oauth2/v2/auth
            token-uri: https://oauth2.googleapis.com/token
            user-info-uri: https://www.googleapis.com/oauth2/v3/userinfo
Enable OAuth2 Login: Configure Spring Security to enable OAuth2 login.


import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.oauth2.config.annotation.web.configuration.EnableOAuth2Client;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableOAuth2Client
public class SecurityConfig {
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .anyRequest().authenticated()
            )
            .oauth2Login();
        return http.build();
    }
}
Protect APIs: Use @PreAuthorize or @RolesAllowed annotations to secure endpoints.


@RestController
public class SecureController {
    @GetMapping("/secure-data")
    @PreAuthorize("hasAuthority('SCOPE_profile')")
    public String getSecureData() {
        return "Secure Data";
    }
}
These steps will help you implement JWT for stateless authentication and OAuth2 for delegated access.
