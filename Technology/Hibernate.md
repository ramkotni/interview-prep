Hibernate is an Object-Relational Mapping (ORM) framework for Java that simplifies database interactions by mapping Java objects to database tables. It eliminates the need for boilerplate SQL code and provides features like caching, lazy loading, and transaction management.


Key Features of Hibernate:
ORM: Maps Java classes to database tables.
HQL (Hibernate Query Language): A query language similar to SQL but operates on Java objects.
Caching: Improves performance by reducing database calls.
Lazy/Eager Loading: Controls when related data is fetched.
Transaction Management: Ensures atomicity and consistency.
<hr></hr>
Example: Employee Management System
1. Entity Class
Defines a Java class mapped to a database table.

import jakarta.persistence.*;

@Entity
@Table(name = "employees")
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "department")
    private String department;

    @Column(name = "salary")
    private Double salary;

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }
}
<hr></hr>
2. Hibernate Configuration
Defines database connection and Hibernate properties in hibernate.cfg.xml.
<hibernate-configuration>
    <session-factory>
        <property name="hibernate.connection.driver_class">com.mysql.cj.jdbc.Driver</property>
        <property name="hibernate.connection.url">jdbc:mysql://localhost:3306/employee_db</property>
        <property name="hibernate.connection.username">root</property>
        <property name="hibernate.connection.password">password</property>
        <property name="hibernate.dialect">org.hibernate.dialect.MySQLDialect</property>
        <property name="hibernate.hbm2ddl.auto">update</property>
        <property name="hibernate.show_sql">true</property>
        <property name="hibernate.format_sql">true</property>

        <mapping class="com.example.Employee"/>
    </session-factory>
</hibernate-configuration>

3. CRUD Operations
Perform database operations using Hibernate's Session API.
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class EmployeeApp {
    public static void main(String[] args) {
        // Create SessionFactory
        SessionFactory factory = new Configuration()
                .configure("hibernate.cfg.xml")
                .addAnnotatedClass(Employee.class)
                .buildSessionFactory();

        // Create Session
        Session session = factory.getCurrentSession();

        try {
            // Create an Employee object
            Employee employee = new Employee();
            employee.setName("John Doe");
            employee.setDepartment("IT");
            employee.setSalary(75000.0);

            // Start a transaction
            session.beginTransaction();

            // Save the Employee object
            session.save(employee);

            // Commit the transaction
            session.getTransaction().commit();

            System.out.println("Employee saved successfully!");
        } finally {
            factory.close();
        }
    }
}
Explanation:
Entity Class: Represents the employees table.
Configuration: Specifies database connection and Hibernate settings.
Session: Used to interact with the database (e.g., save, update, delete).
Transaction: Ensures atomicity of operations.
This example demonstrates how Hibernate simplifies database operations by abstracting SQL queries and managing the persistence of Java objects.

To use Hibernate with Spring Boot, follow these steps:


1. Add Dependencies
Include the required dependencies in your pom.xml for Hibernate and Spring Data JPA.

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
</dependency>
2. Configure application.properties
Set up the database connection and Hibernate properties.
spring.datasource.url=jdbc:mysql://localhost:3306/your_database
spring.datasource.username=root
spring.datasource.password=your_password
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQLDialect

3. Create an Entity Class
Define a class annotated with @Entity to map to a database table.
import jakarta.persistence.*;

@Entity
@Table(name = "employees")
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    private String department;

    private Double salary;

    // Getters and Setters
}

4. Create a Repository Interface
Use Spring Data JPA to interact with the database.
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeRepository extends JpaRepository<Employee, Long> {
}
5. Create a Service Class
Add business logic for database operations.

import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class EmployeeService {
    private final EmployeeRepository repository;

    public EmployeeService(EmployeeRepository repository) {
        this.repository = repository;
    }

    public List<Employee> getAllEmployees() {
        return repository.findAll();
    }

    public Employee saveEmployee(Employee employee) {
        return repository.save(employee);
    }
}
6. Create a Controller
Expose REST endpoints to interact with the service.
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/employees")
public class EmployeeController {
    private final EmployeeService service;

    public EmployeeController(EmployeeService service) {
        this.service = service;
    }

    @GetMapping
    public List<Employee> getAllEmployees() {
        return service.getAllEmployees();
    }

    @PostMapping
    public Employee saveEmployee(@RequestBody Employee employee) {
        return service.saveEmployee(employee);
    }
}
7. Run the Application
Run your Spring Boot application, and the database schema will be created automatically based on the Employee entity. Use the REST endpoints to perform CRUD operations.












