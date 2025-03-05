JSON Web Token (JWT) and OAuth2 Implementation in Spring
Both JWT (JSON Web Token) and OAuth2 are widely used in modern web applications for securing APIs, authenticating users, and enabling Single Sign-On (SSO). Below, I'll explain both concepts and how to implement them in a Spring Boot application.

Overview
1. JSON Web Token (JWT):
JWT is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.
JWTs can be signed using a secret key (HMAC algorithm) or a public/private key pair (RSA, ECDSA).
It is commonly used in stateless authentication, where the server does not need to maintain any session state. Instead, it relies on the token itself to store user information.
Structure of a JWT:
A JWT is composed of three parts:

Header: Contains metadata, such as the algorithm used for signing.
Payload: Contains the claims (data) like user identity, roles, etc.
Signature: Ensures the token's authenticity and integrity.
A JWT is typically represented as:

header.payload.signature


 OAuth2:
OAuth2 is an authorization framework that allows third-party services to exchange user data without exposing user credentials.
It enables authorization via access tokens, and it is commonly used with protocols like OAuth2 Authorization Code Flow, Client Credentials Flow, etc.
Spring Boot Integration
1. JWT Implementation in Spring Boot:
Let's first implement JWT-based authentication in a Spring Boot application.

Step 1: Add Dependencies

In your pom.xml file, include dependencies for Spring Boot, Spring Security, and JWT:

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security</artifactId>
    </dependency>
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt</artifactId>
        <version>0.11.2</version> <!-- Ensure you use the latest version -->
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>

Step 2: Create JWT Utility Class

Create a utility class to generate and validate JWT tokens.

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.util.Date;

public class JwtTokenUtil {
    private String secretKey = "secret"; // Secret key used for signing JWT

    // Generate JWT Token
    public String generateToken(String username) {
        return Jwts.builder()
                .setSubject(username)
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 60)) // 1 hour expiration
                .signWith(SignatureAlgorithm.HS256, secretKey)
                .compact();
    }

    // Validate JWT Token
    public boolean validateToken(String token, String username) {
        return username.equals(getUsernameFromToken(token)) && !isTokenExpired(token);
    }

    // Extract username from the JWT Token
    public String getUsernameFromToken(String token) {
        return getClaimsFromToken(token).getSubject();
    }

    // Extract expiration date from the JWT Token
    private Date getExpirationDateFromToken(String token) {
        return getClaimsFromToken(token).getExpiration();
    }

    // Extract Claims from the JWT Token
    private Claims getClaimsFromToken(String token) {
        return Jwts.parser()
                .setSigningKey(secretKey)
                .parseClaimsJws(token)
                .getBody();
    }

    // Check if the token is expired
    private boolean isTokenExpired(String token) {
        return getExpirationDateFromToken(token).before(new Date());
    }
}

Step 3: Create Authentication Filter

To intercept and validate the JWT in each request:

import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private JwtTokenUtil jwtTokenUtil;

    public JwtAuthenticationFilter(JwtTokenUtil jwtTokenUtil) {
        this.jwtTokenUtil = jwtTokenUtil;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, javax.servlet.FilterChain filterChain)
            throws ServletException, IOException {
        String token = request.getHeader("Authorization");

        if (token != null && token.startsWith("Bearer ")) {
            token = token.substring(7);
            String username = jwtTokenUtil.getUsernameFromToken(token);

            if (username != null && SecurityContextHolder.getContext().getAuthentication() == null) {
                if (jwtTokenUtil.validateToken(token, username)) {
                    Authentication authentication = new UsernamePasswordAuthenticationToken(username, null, new ArrayList<>());
                    SecurityContextHolder.getContext().setAuthentication(authentication);
                }
            }
        }

        filterChain.doFilter(request, response);
    }
}

Step 4: Configure Spring Security

Now configure Spring Security to use the JWT filter:

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    private JwtTokenUtil jwtTokenUtil;

    public SecurityConfig(JwtTokenUtil jwtTokenUtil) {
        this.jwtTokenUtil = jwtTokenUtil;
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
            .authorizeRequests()
            .antMatchers("/authenticate", "/register").permitAll()
            .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(jwtTokenUtil), UsernamePasswordAuthenticationFilter.class);
    }
}

Step 5: Create Authentication Controller

Create an endpoint where users can authenticate and get the JWT token.

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AuthenticationController {

    private JwtTokenUtil jwtTokenUtil;

    public AuthenticationController(JwtTokenUtil jwtTokenUtil) {
        this.jwtTokenUtil = jwtTokenUtil;
    }

    @PostMapping("/authenticate")
    public String createToken(@RequestBody User user) {
        // Validate user and generate JWT token
        return jwtTokenUtil.generateToken(user.getUsername());
    }
}

2. OAuth2 Implementation in Spring Boot:
Spring Security supports OAuth2 out of the box. For OAuth2-based authentication, you would typically use OAuth2 Authorization Code Flow or OAuth2 Client Credentials Flow.

Step 1: Add Dependencies

Add the Spring Security OAuth2 dependencies to your pom.xml:
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-oauth2-client</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.security</groupId>
        <artifactId>spring-security-oauth2-jose</artifactId>
    </dependency>
</dependencies>

Step 2: Configure Application Properties

You need to configure OAuth2 properties like client ID, client secret, and authorization server URLs in application.properties or application.yml.
spring.security.oauth2.client.registration.google.client-id=your-client-id
spring.security.oauth2.client.registration.google.client-secret=your-client-secret
spring.security.oauth2.client.registration.google.scope=profile, email
spring.security.oauth2.client.registration.google.redirect-uri={baseUrl}/login/oauth2/code/{registrationId}
spring.security.oauth2.client.provider.google.authorization-uri=https://accounts.google.com/o/oauth2/auth
spring.security.oauth2.client.provider.google.token-uri=https://oauth2.googleapis.com/token
spring.security.oauth2.client.provider.google.jwk-set-uri=https://www.googleapis.com/oauth2/v3/certs

Step 3: Configure OAuth2 Login

You can enable OAuth2 login in your SecurityConfig:

import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.oauth2Login()
            .defaultSuccessUrl("/home", true)
            .and()
            .authorizeRequests()
            .antMatchers("/login", "/error").permitAll()
            .anyRequest().authenticated();
    }
}

Conclusion
JWT Authentication is useful for stateless authentication where the server does not need to store sessions. JWT tokens carry the user’s identity and roles within the token itself, providing a scalable and secure way to authenticate requests.

OAuth2 Authentication is used for scenarios like third-party authentication (e.g., logging in with Google/Facebook) and provides more flexible and standardized ways of authorization.

By integrating JWT or OAuth2 with Spring Security, you can implement a secure authentication mechanism in your Spring Boot applications.
