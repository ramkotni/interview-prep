# SPRING BOOT - INTERVIEW Q&A FORMAT
# Microservices, REST APIs, Security | 18 Years Experience

---

## Q1: Explain Spring Boot architecture - Components and flow.

**A:**

**Spring Boot** = Opinionated framework for building standalone, production-ready applications with minimal configuration.

### Core Components

```java
// 1. Main Application Class
@SpringBootApplication  // Combines @Configuration + @EnableAutoConfiguration + @ComponentScan
public class GridApplicationServer {
    public static void main(String[] args) {
        SpringApplication.run(GridApplicationServer.class, args);
    }
}

// 2. Controller - REST Endpoint
@RestController
@RequestMapping("/api/grid")
public class GridController {

    @Autowired  // Dependency Injection
    private GridService gridService;

    @GetMapping("/{regionId}")
    public ResponseEntity<GridData> getGridData(@PathVariable String regionId) {
        GridData data = gridService.fetchGridData(regionId);
        return ResponseEntity.ok(data);  // 200 OK with data
    }

    @PostMapping
    public ResponseEntity<GridData> createGrid(@RequestBody GridData data) {
        GridData saved = gridService.saveGridData(data);
        return ResponseEntity.status(201).body(saved);  // 201 Created
    }
}

// 3. Service - Business Logic
@Service
public class GridService {

    @Autowired
    private GridRepository gridRepository;

    public GridData fetchGridData(String regionId) {
        return gridRepository.findByRegion(regionId)
            .orElseThrow(() -> new ResourceNotFoundException("Region not found"));
    }

    public GridData saveGridData(GridData data) {
        return gridRepository.save(data);
    }
}

// 4. Repository - Database Access
@Repository
public interface GridRepository extends JpaRepository<GridData, Long> {
    Optional<GridData> findByRegion(String region);
    List<GridData> findByStatusAndRegion(String status, String region);
}

// 5. Entity - Database Model
@Entity
@Table(name = "grid_data")
public class GridData {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String region;

    @Column(nullable = false)
    private Double frequency;

    @Enumerated(EnumType.STRING)
    private GridStatus status;

    @Temporal(TemporalType.TIMESTAMP)
    private LocalDateTime timestamp;

    // Getters, setters, constructors...
}
```

### Request Flow

```
HTTP Request (POST /api/grid with {"region":"TX","frequency":60.0})
    ↓
Dispatcher Servlet (Spring's front controller)
    ↓
Controller.createGrid(GridData data)  // @PostMapping
    ↓
Service.saveGridData(data)           // Business logic
    ↓
Repository.save(data)                // JPA: INSERT INTO grid_data
    ↓
Database saves record
    ↓
Repository returns saved entity (with generated ID)
    ↓
Service returns saved GridData
    ↓
Controller returns ResponseEntity<GridData>
    ↓
Response converted to JSON (Jackson library)
    ↓
HTTP 201 Created with JSON body
    ↓
Client receives response
```

---

## Q2: Explain Spring Boot auto-configuration and when it's disabled.

**A:**

**Auto-configuration** = Spring Boot automatically configures beans based on classpath dependencies.

### How Auto-Configuration Works

```java
// @SpringBootApplication enables auto-configuration
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);  // Triggers auto-config
    }
}

// Spring searches META-INF/spring.factories for enabled configurations
// Example configurations auto-enabled:
// - DataSourceAutoConfiguration (if JPA on classpath)
// - WebMvcAutoConfiguration (if Spring Web on classpath)
// - KafkaAutoConfiguration (if Spring Kafka on classpath)
```

### Common Auto-Configurations

```yaml
# application.yml - Spring Boot reads these for auto-config
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/grid_db
    username: root
    password: secret

  jpa:
    hibernate:
      ddl-auto: update  # Auto-config: Create/update schema
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQL8Dialect

  kafka:
    bootstrap-servers: localhost:9092  # Auto-config: Kafka connection

  redis:
    host: localhost
    port: 6379  # Auto-config: Redis connection
```

### Disable Auto-Configuration

```java
// 1. Disable specific auto-config
@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
public class GridApplication {  // No database auto-config
    public static void main(String[] args) {
        SpringApplication.run(GridApplication.class, args);
    }
}

// 2. Disable all auto-config (manual config everything)
@SpringBootApplication(exclude = {})  // Or
@EnableAutoConfiguration(exclude = {DataSourceAutoConfiguration.class})
public class GridApplication {
}

// 3. Property-based (application.yml)
spring:
  autoconfigure:
    exclude:
      - org.springframework.boot.autoconfigure.data.DataSourceAutoConfiguration
      - org.springframework.boot.autoconfigure.kafka.KafkaAutoConfiguration
```

### Real ERCOT Example: Custom DataSource Config

```java
@Configuration
@EnableAutoConfiguration(exclude = DataSourceAutoConfiguration.class)
public class CustomDataSourceConfig {

    @Bean
    public DataSource dataSource() {
        // Custom DataSource (ERCOT: replicate to backup every write)
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:mysql://grid-db-primary:3306/grid");
        config.setUsername("grid_user");
        config.setPassword("secret");
        config.setMaximumPoolSize(20);
        config.setMinimumIdle(5);
        config.setConnectionTimeout(10000);

        return new HikariDataSource(config);
    }

    @Bean
    public JdbcTemplate jdbcTemplate(DataSource dataSource) {
        return new JdbcTemplate(dataSource);
    }
}
```

---

## Q3: Spring Security - Authentication & Authorization with JWT.

**A:**

**Spring Security** = Framework for authentication (who you are) and authorization (what you can do).

### JWT Flow (ERCOT: Role-based access)

```java
// 1. Login Endpoint - Generate JWT
@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private JwtTokenProvider jwtTokenProvider;

    @PostMapping("/login")
    public ResponseEntity<LoginResponse> login(@RequestBody LoginRequest request) {
        try {
            // Authenticate user
            Authentication auth = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                    request.getUsername(),
                    request.getPassword()
                )
            );

            // Generate JWT token
            String token = jwtTokenProvider.generateToken(auth);

            return ResponseEntity.ok(new LoginResponse(token, "JWT token generated"));
        } catch (BadCredentialsException e) {
            return ResponseEntity.status(401).body(new LoginResponse("", "Invalid credentials"));
        }
    }
}

// 2. JWT Token Provider - Create and validate tokens
@Component
public class JwtTokenProvider {

    @Value("${jwt.secret:mySecretKeyForGridOperations}")
    private String jwtSecret;

    @Value("${jwt.expiration:86400000}")  // 24 hours
    private long jwtExpirationMs;

    public String generateToken(Authentication auth) {
        UserPrincipal userPrincipal = (UserPrincipal) auth.getPrincipal();

        return Jwts.builder()
            .setSubject(userPrincipal.getUsername())
            .claim("roles", userPrincipal.getAuthorities())
            .setIssuedAt(new Date())
            .setExpiration(new Date(System.currentTimeMillis() + jwtExpirationMs))
            .signWith(SignatureAlgorithm.HS512, jwtSecret)
            .compact();
    }

    public String getUsernameFromJWT(String token) {
        return Jwts.parser()
            .setSigningKey(jwtSecret)
            .parseClaimsJws(token)
            .getBody()
            .getSubject();
    }

    public boolean validateToken(String token) {
        try {
            Jwts.parser().setSigningKey(jwtSecret).parseClaimsJws(token);
            return true;
        } catch (JwtException | IllegalArgumentException e) {
            return false;
        }
    }
}

// 3. JWT Filter - Intercept requests, validate token
@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    @Autowired
    private JwtTokenProvider jwtTokenProvider;

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                   HttpServletResponse response,
                                   FilterChain filterChain) throws ServletException, IOException {
        try {
            String jwt = getJwtFromRequest(request);

            if (jwt != null && jwtTokenProvider.validateToken(jwt)) {
                String username = jwtTokenProvider.getUsernameFromJWT(jwt);

                // Load user details and set authentication
                UserDetails userDetails = loadUserDetails(username);
                UsernamePasswordAuthenticationToken authentication =
                    new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());

                SecurityContextHolder.getContext().setAuthentication(authentication);
            }
        } catch (Exception e) {
            logger.error("Could not set user authentication", e);
        }

        filterChain.doFilter(request, response);
    }

    private String getJwtFromRequest(HttpServletRequest request) {
        String bearerToken = request.getHeader("Authorization");
        if (bearerToken != null && bearerToken.startsWith("Bearer ")) {
            return bearerToken.substring(7);
        }
        return null;
    }
}

// 4. Security Configuration
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private JwtAuthenticationFilter jwtAuthenticationFilter;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
            .authorizeRequests()
                .antMatchers("/auth/**").permitAll()        // Public endpoints
                .antMatchers("/api/grid/**").hasRole("GRID_OPERATOR")  // Requires role
                .antMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class);
    }
}

// 5. Controller with role-based access
@RestController
@RequestMapping("/api/grid")
public class GridController {

    @GetMapping("/{regionId}")
    public GridData getGridData(@PathVariable String regionId) {
        // Accessible to GRID_OPERATOR role
        return gridService.fetchGridData(regionId);
    }

    @PostMapping
    @PreAuthorize("hasRole('ADMIN')")  // Only ADMIN can create
    public GridData createGrid(@RequestBody GridData data) {
        return gridService.saveGridData(data);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")  // Only ADMIN can delete
    public ResponseEntity<?> deleteGrid(@PathVariable Long id) {
        gridService.deleteGridData(id);
        return ResponseEntity.ok("Deleted");
    }
}
```

### Real Usage Flow at ERCOT

```
1. User logs in: POST /auth/login {"username":"operator1","password":"secret"}
   Response: {"token":"eyJhbGciOiJIUzUxMiJ9..."}

2. User calls protected endpoint with JWT:
   GET /api/grid/TX
   Header: Authorization: Bearer eyJhbGciOiJIUzUxMiJ9...

3. JwtAuthenticationFilter intercepts:
   - Extracts token from header
   - Validates token (signature, expiration)
   - Extracts username from token
   - Sets authentication in SecurityContext
   - Request proceeds to controller

4. Controller checks authority:
   - User has GRID_OPERATOR role
   - Request allowed, returns grid data

5. If user tries unauthorized action (DELETE without ADMIN):
   - Spring Security throws AccessDeniedException
   - Returns 403 Forbidden
```

---

## Q4: REST APIs - HTTP status codes and error handling.

**A:**

**REST APIs** = Use HTTP methods (GET, POST, PUT, DELETE) and status codes to communicate.

### HTTP Status Codes

```
2xx - Success
  200 OK - Request succeeded
  201 Created - Resource created
  204 No Content - Success but no content to return

3xx - Redirect
  301 Moved Permanently - Resource moved
  304 Not Modified - Cached response valid

4xx - Client Error
  400 Bad Request - Invalid input
  401 Unauthorized - Authentication required
  403 Forbidden - Authenticated but no permission
  404 Not Found - Resource doesn't exist
  409 Conflict - Resource conflict (duplicate, etc)

5xx - Server Error
  500 Internal Server Error - Server bug
  503 Service Unavailable - Server overloaded/maintenance
```

### Spring Boot REST Examples

```java
@RestController
@RequestMapping("/api/grid")
public class GridController {

    // GET - Retrieve all
    @GetMapping
    public ResponseEntity<List<GridData>> getAllGrids() {
        List<GridData> grids = gridService.getAllGrids();
        return ResponseEntity.ok(grids);  // 200 OK
    }

    // GET by ID - With not found handling
    @GetMapping("/{id}")
    public ResponseEntity<GridData> getGrid(@PathVariable Long id) {
        return gridService.getGridById(id)
            .map(ResponseEntity::ok)             // 200 OK
            .orElse(ResponseEntity.notFound().build());  // 404
    }

    // POST - Create new
    @PostMapping
    public ResponseEntity<GridData> createGrid(@RequestBody @Valid GridData data) {
        GridData saved = gridService.saveGridData(data);
        return ResponseEntity.status(HttpStatus.CREATED).body(saved);  // 201
    }

    // PUT - Update existing
    @PutMapping("/{id}")
    public ResponseEntity<GridData> updateGrid(@PathVariable Long id,
                                               @RequestBody @Valid GridData data) {
        return gridService.updateGridData(id, data)
            .map(ResponseEntity::ok)             // 200 OK
            .orElse(ResponseEntity.notFound().build());  // 404
    }

    // DELETE - Remove resource
    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteGrid(@PathVariable Long id) {
        gridService.deleteGridData(id);
        return ResponseEntity.noContent().build();  // 204 No Content
    }
}
```

### Error Handling

```java
// Global Exception Handler
@RestControllerAdvice
public class GlobalExceptionHandler {

    // ResourceNotFoundException - 404
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleResourceNotFound(ResourceNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            "NOT_FOUND",
            ex.getMessage(),
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }

    // Validation errors - 400
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationException(MethodArgumentNotValidException ex) {
        String message = ex.getBindingResult().getFieldError().getDefaultMessage();
        ErrorResponse error = new ErrorResponse("VALIDATION_ERROR", message, LocalDateTime.now());
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
    }

    // Conflict errors - 409
    @ExceptionHandler(DataIntegrityViolationException.class)
    public ResponseEntity<ErrorResponse> handleConflict(DataIntegrityViolationException ex) {
        ErrorResponse error = new ErrorResponse("CONFLICT", "Resource already exists", LocalDateTime.now());
        return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
    }

    // Generic error - 500
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericException(Exception ex) {
        ErrorResponse error = new ErrorResponse(
            "INTERNAL_ERROR",
            "An unexpected error occurred",
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}

// Error Response DTO
@Data
public class ErrorResponse {
    private String errorCode;
    private String message;
    private LocalDateTime timestamp;

    public ErrorResponse(String errorCode, String message, LocalDateTime timestamp) {
        this.errorCode = errorCode;
        this.message = message;
        this.timestamp = timestamp;
    }
}
```

---

[Continue with Q5-Q10...]
