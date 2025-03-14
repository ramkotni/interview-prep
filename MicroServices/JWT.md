Spring Boot 3.0 – JWT Authentication with Spring Security using MySQL Database

Spring Boot 3.0 has come with many changes in Spring Security . In this article, we’ll learn how to implement JWT authentication and authorization in a Spring Boot 3.0 application using Spring Security 6 with MySQL Database.

Demo Project
Step 1: Create a New Spring Boot Project in Spring Initializr

To create a new Spring Boot project, please refer to How to Create a Spring Boot Project in Spring Initializr and Run it in IntelliJ IDEA . For this project choose the following things

Project: Maven
Language: Java
Packaging: Jar
Java: 17
Please choose the following dependencies while creating the project.

Spring Web
Spring Security
MySQL Driver
Spring Data JPA
Lombok
Additionally, we have added dependencies for JWT also. Below are the dependencies

<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-api</artifactId>
    <version>0.11.5</version>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-impl</artifactId>
    <version>0.11.5</version>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-jackson</artifactId>
    <version>0.11.5</version>
</dependency>

complete pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.0.8</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <groupId>com.gfg</groupId>
    <artifactId>springboot3-security</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springboot3-security</name>
    <description>Demo project for Spring Boot 3 Security</description>

    <properties>
        <java.version>17</java.version>
        <jjwt.version>0.11.5</jjwt.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <scope>runtime</scope>
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
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-api</artifactId>
            <version>${jjwt.version}</version>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-impl</artifactId>
            <version>${jjwt.version}</version>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-jackson</artifactId>
            <version>${jjwt.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.0.8</version> <!-- Specify the version explicitly -->
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

Step 2: Create a UserController

Go to the src > main > java > controller and create a class UserController and put the below code. In this, we have created a simple REST API in our controller class.

import com.ey.springboot3security.entity.AuthRequest;
import com.ey.springboot3security.entity.UserInfo;
import com.ey.springboot3security.service.JwtService;
import com.ey.springboot3security.service.UserInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
public class UserController {

    @Autowired
    private UserInfoService service;

    @Autowired
    private JwtService jwtService;

    @Autowired
    private AuthenticationManager authenticationManager;

    @GetMapping("/welcome")
    public String welcome() {
        return "Welcome this endpoint is not secure";
    }

    @PostMapping("/addNewUser")
    public String addNewUser(@RequestBody UserInfo userInfo) {
        return service.addUser(userInfo);
    }

    @GetMapping("/user/userProfile")
    @PreAuthorize("hasAuthority('ROLE_USER')")
    public String userProfile() {
        return "Welcome to User Profile";
    }

    @GetMapping("/admin/adminProfile")
    @PreAuthorize("hasAuthority('ROLE_ADMIN')")
    public String adminProfile() {
        return "Welcome to Admin Profile";
    }

    @PostMapping("/generateToken")
    public String authenticateAndGetToken(@RequestBody AuthRequest authRequest) {
        Authentication authentication = authenticationManager.authenticate(
            new UsernamePasswordAuthenticationToken(authRequest.getUsername(), authRequest.getPassword())
        );
        if (authentication.isAuthenticated()) {
            return jwtService.generateToken(authRequest.getUsername());
        } else {
            throw new UsernameNotFoundException("Invalid user request!");
        }
    }
}

Step 3: Create a SecurityConfig Class

Go to the src > main > java > config and create a class SecurityConfig and put the below code. This is the new changes brought in Spring Boot 3.0.

import com.ey.springboot3security.filter.JwtAuthFilter;
import com.ey.springboot3security.service.UserInfoService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {

    @Bean
    public UserDetailsService userDetailsService() {
        return new UserInfoService();
    }

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http, JwtAuthFilter jwtAuthFilter) throws Exception {
        http
                .csrf(csrf -> csrf.disable())
                .authorizeHttpRequests(auth -> auth
                        .requestMatchers("/auth/welcome", "/auth/addNewUser", "/auth/generateToken").permitAll()
                        .requestMatchers("/auth/user/**").hasAuthority("ROLE_USER")
                        .requestMatchers("/auth/admin/**").hasAuthority("ROLE_ADMIN")
                        .anyRequest().authenticated())
                .sessionManagement(sess -> sess.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                .authenticationProvider(authenticationProvider())
                .addFilterBefore(jwtAuthFilter, UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationProvider authenticationProvider() {
        DaoAuthenticationProvider authenticationProvider = new DaoAuthenticationProvider();
        authenticationProvider.setUserDetailsService(userDetailsService());
        authenticationProvider.setPasswordEncoder(passwordEncoder());
        return authenticationProvider;
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }

    @Bean
    public JwtAuthFilter jwtAuthFilter(UserDetailsService userDetailsService, JwtService jwtService) {
        return new JwtAuthFilter(userDetailsService, jwtService);
    }
}

Step 4: Create Entity Classes

Go to the src > main > java > entity and create a class UserInfo and put the below code.

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
public class UserInfo {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String name;
    private String email;
    private String password;
    private String roles;

}

Similarly, create a class AuthRequest and put the below code.
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class AuthRequest {

    private String username;
    private String password;

}

Step 5: Create Filter Class

Go to the src > main > java > filter and create a class JwtAuthFilter and put the below code.

import com.ey.springboot3security.service.JwtService;
import com.ey.springboot3security.service.UserInfoService;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

@Component
public class JwtAuthFilter extends OncePerRequestFilter {

    private final UserDetailsService userDetailsService;
    private final JwtService jwtService;

    @Autowired
    public JwtAuthFilter(UserDetailsService userDetailsService, JwtService jwtService) {
        this.userDetailsService = userDetailsService;
        this.jwtService = jwtService;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        String authHeader = request.getHeader("Authorization");
        String token = null;
        String username = null;

        if (authHeader != null && authHeader.startsWith("Bearer ")) {
            token = authHeader.substring(7);
            username = jwtService.extractUsername(token);
        }

        if (username != null && SecurityContextHolder.getContext().getAuthentication() == null) {
            UserDetails userDetails = userDetailsService.loadUserByUsername(username);
            if (jwtService.validateToken(token, userDetails)) {
                UsernamePasswordAuthenticationToken authToken = new UsernamePasswordAuthenticationToken(
                        userDetails,
                        null,
                        userDetails.getAuthorities());
                authToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(authToken);
            }
        }
        filterChain.doFilter(request, response);
    }
}

Step 6: Create a Repository Interface

Go to the src > main > java > repository and create an interface UserInfoRepository and put the below code.

import com.ey.springboot3security.entity.UserInfo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserInfoRepository extends JpaRepository<UserInfo, Integer> {
    Optional<UserInfo> findByEmail(String email); // Use 'email' if that is the correct field for login
}

Step 7: Create Service Classes

Go to the src > main > java > service and create a class JwtService and put the below code.

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;

import java.security.Key;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

@Component
public class JwtService {

    public static final String SECRET = "5367566859703373367639792F423F452848284D6251655468576D5A71347437";

    public String generateToken(String email) { // Use email as username
        Map<String, Object> claims = new HashMap<>();
        return createToken(claims, email);
    }

    private String createToken(Map<String, Object> claims, String email) {
        return Jwts.builder()
                .setClaims(claims)
                .setSubject(email)
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 30))
                .signWith(getSignKey(), SignatureAlgorithm.HS256)
                .compact();
    }

    private Key getSignKey() {
        byte[] keyBytes = Decoders.BASE64.decode(SECRET);
        return Keys.hmacShaKeyFor(keyBytes);
    }

    public String extractUsername(String token) {
        return extractClaim(token, Claims::getSubject);
    }

    public Date extractExpiration(String token) {
        return extractClaim(token, Claims::getExpiration);
    }

    public <T> T extractClaim(String token, Function<Claims, T> claimsResolver) {
        final Claims claims = extractAllClaims(token);
        return claimsResolver.apply(claims);
    }

    private Claims extractAllClaims(String token) {
        return Jwts.parserBuilder()
                .setSigningKey(getSignKey())
                .build()
                .parseClaimsJws(token)
                .getBody();
    }

    private Boolean isTokenExpired(String token) {
        return extractExpiration(token).before(new Date());
    }

    public Boolean validateToken(String token, UserDetails userDetails) {
        final String username = extractUsername(token);
        return (username.equals(userDetails.getUsername()) && !isTokenExpired(token));
    }
}

Similarly, create a class UserInfoDetails and put the below code.

import com.ey.springboot3security.entity.UserInfo;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

public class UserInfoDetails implements UserDetails {

    private String username; // Changed from 'name' to 'email' for clarity
    private String password;
    private List<GrantedAuthority> authorities;

    public UserInfoDetails(UserInfo userInfo) {
        this.username = userInfo.getEmail(); // Use email as username
        this.password = userInfo.getPassword();
        this.authorities = List.of(userInfo.getRoles().split(","))
                .stream()
                .map(SimpleGrantedAuthority::new)
                .collect(Collectors.toList());
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return authorities;
    }

    @Override
    public String getUsername() {
        return username;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }
}

Similarly, create a class UserInfoService and put the below code.

import com.ey.springboot3security.entity.UserInfo;
import com.ey.springboot3security.repository.UserInfoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UserInfoService implements UserDetailsService {

    @Autowired
    private UserInfoRepository repository;

    @Autowired
    private PasswordEncoder encoder;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        Optional<UserInfo> userDetail = repository.findByEmail(username); // Assuming 'email' is used as username

        // Converting UserInfo to UserDetails
        return userDetail.map(UserInfoDetails::new)
                .orElseThrow(() -> new UsernameNotFoundException("User not found: " + username));
    }

    public String addUser(UserInfo userInfo) {
        // Encode password before saving the user
        userInfo.setPassword(encoder.encode(userInfo.getPassword()));
        repository.save(userInfo);
        return "User Added Successfully";
    }
}

Step 8: Make the following changes in the application.properties file

spring.main.allow-circular-references=true
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url = jdbc:mysql://localhost:3306/university
spring.datasource.username = root
spring.datasource.password = 143@Arpilu
spring.jpa.hibernate.ddl-auto = update
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQLDialect
spring.jpa.hibernate.naming.physical-strategy=org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl

Test the Application
Now run your application and test it out. Hit the following URL

http://localhost:8080/auth/addNewUser
It will add the user to the database.

Now, hit the following URL to generate the token.

http://localhost:8080/auth/generateToken
It will generate the token.

Now using this take we can access our endpoint according to the ROLE. Hit the following URL and put the Bearer token.

http://localhost:8080/auth/user/userProfile
Refer to the screenshot below.

JSON Web Token (JWT)

In today’s digital world, web security and data protection on servers are critical concerns. JSON Web Tokens (JWT) provide a secure way to authenticate users, validate identities, and ensure safe communication between clients and servers, preventing unauthorized access.

What is a JWT Token?
A JSON Web Token (JWT) is a standard (RFC 7519) for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using these two algorithms

HMAC (Hash-based Message Authentication Code)
RSA or ECDSA (Asymmetric cryptographic algorithms)
JWTs are primarily used for authentication and secure data exchange in web applications and APIs.

How JWT token works?
User Logs In: The client (browser) sends login credentials to the server.
Server Generates JWT: If credentials are valid, the server creates a JWT containing user data and signs it with a secret key.
Token Sent to Client: The JWT is sent back to the client and stored (usually in localStorage or a cookie).
Client Sends Token in Requests: For protected routes, the client includes the JWT in the Authorization header (Bearer Token).
Server Verifies and Responds: The server verifies the token, extracts user info, and processes the request if valid.
JWT Structure
A JWT consists of three parts, separated by dots (.)

Header. Payload. Signature
Header: Contains metadata about the token, such as the algorithm used for signing.
Payload: Stores the claims, i.e., data being transmitted.
Signature: Ensures the token’s integrity and authenticity.
1. Header
The header contains metadata about the token, including the signing algorithm and token type here metadata means data about data.

{
    "alg": "HS256",
    "typ": "JWT"
}
alg: Algorithm used for signing (e.g., HS256, RS256).
typ: Token type, always “JWT”.
Base64Url Encoded Header

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
2. Payload
The payload contains the information about the user also called as a claim and some additional information including the timestamp at which it was issued and the expiry time of the token.

{
    "userId": 123,
    "role": "admin",
    "exp": 1672531199
}
Common claim types:

iss (Issuer): Identifies who issued the token.
sub (Subject): Represents the user or entity the token is about.
aud (Audience): Specifies the intended recipient.
exp (Expiration): Defines when the token expires.
iat (Issued At): Timestamp when the token was created.
nbf (Not Before): Specifies when the token becomes valid.
Base64Url Encoded Payload

eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNzA4MzQ1MTIzLCJleHAiOjE3MDgzNTUxMjN9
3. Signature
The signature ensures token integrity and is generated using the header, payload, and a secret key. In this example we will use HS256 algorithm to implement the Signature part

HMACSHA256(
    base64UrlEncode(header) + "." + base64UrlEncode(payload),
    secret
)
The signature after using the secret_key

SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
4. Final JWT token
After all these steps the final JWT token is generated by joining the Header, Payload and Signature via a dot. It looks like as it is shown below.

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNzA4MzQ1MTIzLCJleHAiOjE3MDgzNTUxMjN9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c


Security Considerations
Use HTTPS: Prevent man-in-the-middle attacks by transmitting JWTs over HTTPS.
Set Expiration Time: Prevent long-lived tokens that can be exploited.
Use Secure Storage: Store JWTs securely (e.g., HttpOnly cookies instead of local storage).
Verify Signature: Always validate the token’s signature before trusting its content.
Implementing JWT in a web application
1. Code to create a JSON web token
This code generates a JWT (JSON Web Token) using the jsonwebtoken library in Node.js. The token contains user data and is signed with a secret key for security.

Command to install jsonwebtoken library in NodeJS

npm install jsonwebtoken



const jwt = require('jsonwebtoken');
const secretKey = 'abcde12345';

const token = jwt.sign({
  id: 1,
  username: 'GFG'
}, secretKey, { expiresIn: '1h' });

console.log(token);
Output

Screenshot-2025-02-21-094110
Code to create a JSON web token



Importing JWT Library: The jsonwebtoken module is required to create and verify tokens.
Defining Secret Key: A secret key (abcde12345) is used to sign the token securely.
Creating JWT: The jwt.sign() method generates a token with user details (id, username) and an expiration time of 1 hour.
Logging the Token: The generated JWT is printed to the console for use in authentication.
2. Code to verify a JSON web token
This code verifies a JWT using the jsonwebtoken library in Node.js. It checks if the token is valid and extracts the payload if authentication succeeds.


jwt.verify(token, 'abcde12345', (err, decoded) => {
    if (err) {
      console.log('Token is invalid');
    } else {
      console.log('Decoded Token:', decoded);
    }
  });
Output

Screenshot-2025-02-21-100424
Code to verify a JSON web token

Verifying the Token: The jwt.verify() method checks if the provided token is valid using the secret key.
Handling Errors: If verification fails, an error (err) occurs, and “Token is invalid” is logged.
Decoding Token Data: If valid, the decoded object contains the original user details.
Logging the Decoded Data: The decoded payload is printed to the console, showing user details from the token.
Advantages of using JSON Web Token
Stateless Authentication: No need to store user sessions on the server; JWT contains all necessary data.
Compact & Fast: Being small in size, JWT is efficiently transmitted in HTTP headers, making it ideal for APIs.
Secure & Tamper-Proof: JWTs are signed using a secret key or public/private key pair, ensuring integrity.
Cross-Platform Support: Can be used with any technology (JavaScript, Python, Java, etc.) for authentication.
Built-in Expiry: Tokens can have an expiration time (expiresIn), reducing the risk of long-term access misuse.
Conclusion
JSON Web Tokens (JWT) provide a secure, fast, and stateless way to handle authentication. They are widely used in APIs, web apps, and mobile apps due to their compact size, cross-platform support, and built-in security features. By leveraging JWT, developers can ensure safe and efficient user authentication without storing sessions on the server.

JSON Web Token (JWT) -FAQs
What is a JSON Web Token (JWT)?
A JWT is a compact, URL-safe way to represent claims (statements) between parties as a JSON object, commonly used for authentication and authorization.


How does JWT authentication work?
The client receives a JWT after successful login and includes it in subsequent requests (usually in the Authorization header), allowing the server to verify the client’s identity.


What is the structure of a JWT?
A JWT consists of three parts: a header (describing the algorithm), a payload (containing claims), and a signature (ensuring integrity), all Base64URL encoded and separated by dots.


What is the purpose of the JWT signature?
The signature, generated using a secret key, ensures that the JWT hasn’t been tampered with; only someone with the key can create a valid signature.


Where should JWTs be stored in HTTP requests?
JWTs should be stored in the Authorization header using the Bearer scheme (e.g., Authorization: Bearer <token>).



