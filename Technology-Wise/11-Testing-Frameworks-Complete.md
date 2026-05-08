# TESTING FRAMEWORKS - COMPREHENSIVE INTERVIEW Q&A

## JUnit, Mockito, TestNG, AssertJ

---

## Q1: JUnit 5 Fundamentals

**A:** Testing framework for Java applications.

### Basic Test Structure:
```java
@DisplayName("Calculator Tests")
class CalculatorTest {
    
    private Calculator calculator;
    
    @BeforeEach  // Runs before each test
    void setUp() {
        calculator = new Calculator();
    }
    
    @Test
    @DisplayName("Should add two positive numbers")
    void testAddPositiveNumbers() {
        // Arrange
        int a = 5, b = 3;
        
        // Act
        int result = calculator.add(a, b);
        
        // Assert
        assertEquals(8, result, "5 + 3 should equal 8");
    }
    
    @Test
    void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calculator.divide(10, 0);
        });
    }
    
    @AfterEach  // Runs after each test
    void tearDown() {
        calculator = null;
    }
    
    @BeforeAll  // Runs once before all tests (static)
    static void setupOnce() {
        System.out.println("Starting test suite");
    }
    
    @AfterAll  // Runs once after all tests (static)
    static void cleanupOnce() {
        System.out.println("Finished test suite");
    }
}
```

### Parameterized Tests:
```java
@ParameterizedTest
@ValueSource(ints = { 1, 3, 5, -3, 15, Integer.MAX_VALUE })
void testOddNumbers(int number) {
    assertTrue(isOdd(number));
}

@ParameterizedTest
@CsvSource({
    "0,    0",
    "1,    1",
    "2,    1",
    "3,    2",
    "5,    5"
})
void testFibonacci(int n, int expected) {
    assertEquals(expected, fibonacci(n));
}

@ParameterizedTest
@MethodSource("provideStringsForIsBlank")
void isBlank_ShouldReturnTrueForNullOrBlankStrings(String input, boolean expected) {
    assertEquals(expected, isBlank(input));
}

static Stream<Arguments> provideStringsForIsBlank() {
    return Stream.of(
        Arguments.of(null, true),
        Arguments.of("", true),
        Arguments.of("  ", true),
        Arguments.of("not blank", false)
    );
}
```

### Test Lifecycle:
```java
@TestInstance(Lifecycle.PER_CLASS)  // Create instance once for all tests
class TestLifecycleExample {
    
    private int counter = 0;
    
    @Test
    @Order(1)  // Run first
    void test1() {
        counter++;
    }
    
    @Test
    @Order(2)  // Run second
    void test2() {
        assertEquals(1, counter);  // counter persists from test1
    }
}
```

---

## Q2: Mockito - Mocking Framework

**A:** Mock dependencies for unit testing.

### Basic Mocking:
```java
public class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }
    
    @Test
    void testGetUserById() {
        // Arrange - Mock the repository
        User mockUser = new User(1L, "John", "john@example.com");
        when(userRepository.findById(1L))
            .thenReturn(Optional.of(mockUser));
        
        // Act
        User result = userService.getUserById(1L);
        
        // Assert
        assertNotNull(result);
        assertEquals("John", result.getName());
        
        // Verify the mock was called
        verify(userRepository, times(1)).findById(1L);
        verify(userRepository, never()).save(any());
    }
    
    @Test
    void testCreateUser() {
        // Arrange
        User newUser = new User(null, "Jane", "jane@example.com");
        User savedUser = new User(2L, "Jane", "jane@example.com");
        
        when(userRepository.save(newUser))
            .thenReturn(savedUser);
        
        // Act
        User result = userService.createUser(newUser);
        
        // Assert
        assertEquals(2L, result.getId());
        verify(userRepository).save(newUser);
    }
    
    @Test
    void testUserNotFound() {
        when(userRepository.findById(999L))
            .thenReturn(Optional.empty());
        
        assertThrows(UserNotFoundException.class, () -> {
            userService.getUserById(999L);
        });
    }
}
```

### Spy (Partial Mocking):
```java
@Test
void testWithSpy() {
    // Create real object but mock specific methods
    UserService spyService = spy(new UserService(userRepository));
    
    // Mock one method
    when(spyService.methodA())
        .thenReturn("mocked");
    
    // Other methods work normally
    String result2 = spyService.methodB();  // Real implementation
}
```

### ArgumentCaptor (Capture Arguments):
```java
@Test
void testArgumentCaptor() {
    ArgumentCaptor<User> userCaptor = ArgumentCaptor.forClass(User.class);
    
    userService.createUser(new User(null, "John", "john@example.com"));
    
    verify(userRepository).save(userCaptor.capture());
    
    User capturedUser = userCaptor.getValue();
    assertEquals("john@example.com", capturedUser.getEmail());
}
```

---

## Q3: Integration Testing with Spring

**A:** Test Spring components together.

### Spring Boot Test Configuration:
```java
@SpringBootTest  // Load entire Spring context
class UserControllerIntegrationTest {
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Autowired
    private UserRepository userRepository;
    
    @BeforeEach
    void setUp() {
        userRepository.deleteAll();
    }
    
    @Test
    void testCreateUser() {
        // Arrange
        CreateUserRequest request = new CreateUserRequest();
        request.setName("John");
        request.setEmail("john@example.com");
        
        // Act
        ResponseEntity<UserDTO> response = restTemplate.postForEntity(
            "/api/users",
            request,
            UserDTO.class
        );
        
        // Assert
        assertEquals(HttpStatus.CREATED, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals("John", response.getBody().getName());
        
        // Verify database
        assertEquals(1, userRepository.count());
    }
    
    @Test
    void testGetUserById() {
        // Arrange
        User user = new User();
        user.setName("Jane");
        user.setEmail("jane@example.com");
        User saved = userRepository.save(user);
        
        // Act
        ResponseEntity<UserDTO> response = restTemplate.getForEntity(
            "/api/users/" + saved.getId(),
            UserDTO.class
        );
        
        // Assert
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals("Jane", response.getBody().getName());
    }
}
```

### Test Slice (Test Only Specific Layer):
```java
@WebMvcTest(UserController.class)  // Only loads web layer
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void testGetUser() throws Exception {
        User mockUser = new User(1L, "John", "john@example.com");
        when(userService.getUserById(1L))
            .thenReturn(mockUser);
        
        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.name").value("John"));
        
        verify(userService).getUserById(1L);
    }
}
```

### Repository Testing:
```java
@DataJpaTest  // Only loads JPA components
class UserRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void testFindByEmail() {
        User user = new User();
        user.setName("John");
        user.setEmail("john@example.com");
        entityManager.persistAndFlush(user);
        
        Optional<User> found = userRepository.findByEmail("john@example.com");
        
        assertTrue(found.isPresent());
        assertEquals("John", found.get().getName());
    }
}
```

---

## Q4: Assertion Libraries

**A:** Make assertions more readable with AssertJ.

### AssertJ Fluent Assertions:
```java
@Test
void testAssertJ() {
    User user = new User(1L, "John", "john@example.com");
    
    // Fluent, readable assertions
    assertThat(user)
        .isNotNull()
        .hasFieldOrPropertyWithValue("name", "John")
        .hasFieldOrPropertyWithValue("email", "john@example.com");
    
    List<User> users = Arrays.asList(
        new User(1L, "John", "john@example.com"),
        new User(2L, "Jane", "jane@example.com")
    );
    
    assertThat(users)
        .hasSize(2)
        .extracting(User::getName)
        .contains("John", "Jane");
    
    String email = "john@example.com";
    assertThat(email)
        .startsWith("john")
        .endsWith(".com")
        .contains("@");
}
```

---

## Q5: Test Coverage

**A:** Measure code coverage with JaCoCo.

### JaCoCo Maven Configuration:
```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.8</version>
    <executions>
        <execution>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>

<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <!-- Fail build if coverage below 80% -->
        <forkMode>once</forkMode>
    </configuration>
</plugin>
```

### Generate Report:
```bash
mvn clean test
# Report: target/site/jacoco/index.html
```

---

## Q6: Common Testing Scenarios

### Testing Exceptions:
```java
@Test
void testExceptionMessage() {
    assertThatThrownBy(() -> userService.getUserById(999L))
        .isInstanceOf(UserNotFoundException.class)
        .hasMessage("User not found: 999");
}

@Test
void testMultipleExceptions() {
    assertThatCode(() -> {
        userService.createUser(null);
    }).hasStackTraceContaining("NullPointerException");
}
```

### Testing Collections:
```java
@Test
void testListOperations() {
    List<String> fruits = Arrays.asList("apple", "banana", "cherry");
    
    assertThat(fruits)
        .isNotEmpty()
        .hasSize(3)
        .contains("apple", "banana")
        .doesNotContain("orange")
        .allMatch(f -> f.length() > 0)
        .anyMatch(f -> f.startsWith("b"));
}
```

### Testing Async Operations:
```java
@Test
void testAsyncOperation() throws InterruptedException {
    // Test async code with CompletableFuture
    CompletableFuture<User> future = userService.getUserAsync(1L);
    
    User result = future.join();  // Wait for completion
    assertThat(result).isNotNull();
}
```

---

## Q7: Test Best Practices

✅ **Test Organization:**
- One test class per production class
- Test names describe what they test
- Use meaningful variable names
- Follow AAA pattern (Arrange-Act-Assert)

✅ **Test Focus:**
- Test one thing per test
- Mock external dependencies
- Don't test external libraries
- Focus on behavior, not implementation

✅ **Performance:**
- Keep tests fast
- Avoid databases in unit tests
- Use mocks for slow operations
- Run fast tests frequently

✅ **Coverage Goals:**
- Aim for 80%+ coverage
- Don't aim for 100% (diminishing returns)
- Focus on critical paths
- Coverage doesn't mean quality

---

**Last Updated:** May 8, 2026


