Creating a RESTful web service using Spring Boot involves several steps, including setting up the project, creating the required components (like controllers, services, and repositories), and configuring the application. Below, I'll walk you through an end-to-end example of building a simple RESTful web service with Spring Boot.

In this example, we’ll create a basic Employee Management System where you can:

Create an employee
Get all employees
Get an employee by ID
Update an employee
Delete an employee
1. Set Up the Spring Boot Project
First, create a new Spring Boot project using Spring Initializr (https://start.spring.io/), or if you’re using an IDE like IntelliJ IDEA or Eclipse, you can create a new Spring Boot project directly from there. Choose the following dependencies:

Spring Web: For building the RESTful API.
Spring Data JPA: For database interaction.
H2 Database: For a lightweight, in-memory database.
Lombok: To reduce boilerplate code.
2. Project Structure
The final project structure will look something like this:

css
Copy
src
 └── main
      └── java
           └── com
                └── example
                     └── employee
                          ├── Employee.java
                          ├── EmployeeController.java
                          ├── EmployeeService.java
                          ├── EmployeeRepository.java
                          └── EmployeeApplication.java
3. Create the Employee Model
This is the Employee entity that will be mapped to the database.

java
Copy
package com.example.employee;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

@Entity
public class Employee {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String department;

    // Getters and setters
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
}
@Entity: Marks this class as a JPA entity (a table in the database).
@Id: Denotes the primary key.
@GeneratedValue: Automatically generates values for the id field.
4. Create the Employee Repository
The repository will handle CRUD operations using Spring Data JPA.

java
Copy
package com.example.employee;

import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeRepository extends JpaRepository<Employee, Long> {
    // Custom query methods can be added here if needed
}
JpaRepository: This is a Spring Data interface that provides basic CRUD operations without needing to implement them manually.
5. Create the Employee Service
The service layer contains the business logic.

java
Copy
package com.example.employee;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class EmployeeService {

    @Autowired
    private EmployeeRepository employeeRepository;

    // Create or Update an Employee
    public Employee saveEmployee(Employee employee) {
        return employeeRepository.save(employee);
    }

    // Get all employees
    public List<Employee> getAllEmployees() {
        return employeeRepository.findAll();
    }

    // Get employee by ID
    public Optional<Employee> getEmployeeById(Long id) {
        return employeeRepository.findById(id);
    }

    // Delete an employee by ID
    public void deleteEmployee(Long id) {
        employeeRepository.deleteById(id);
    }
}
@Service: Marks this class as a Spring service, and it's used to implement the business logic.
@Autowired: Automatically injects the EmployeeRepository instance.
6. Create the Employee Controller
The controller is responsible for handling HTTP requests and responses.

java
Copy
package com.example.employee;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/employees")
public class EmployeeController {

    @Autowired
    private EmployeeService employeeService;

    // Create or update an employee
    @PostMapping
    public ResponseEntity<Employee> createEmployee(@RequestBody Employee employee) {
        Employee savedEmployee = employeeService.saveEmployee(employee);
        return new ResponseEntity<>(savedEmployee, HttpStatus.CREATED);
    }

    // Get all employees
    @GetMapping
    public List<Employee> getAllEmployees() {
        return employeeService.getAllEmployees();
    }

    // Get employee by ID
    @GetMapping("/{id}")
    public ResponseEntity<Employee> getEmployeeById(@PathVariable Long id) {
        Optional<Employee> employee = employeeService.getEmployeeById(id);
        return employee.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    // Update employee details
    @PutMapping("/{id}")
    public ResponseEntity<Employee> updateEmployee(@PathVariable Long id, @RequestBody Employee employeeDetails) {
        Optional<Employee> existingEmployeeOpt = employeeService.getEmployeeById(id);

        if (existingEmployeeOpt.isPresent()) {
            Employee existingEmployee = existingEmployeeOpt.get();
            existingEmployee.setName(employeeDetails.getName());
            existingEmployee.setDepartment(employeeDetails.getDepartment());
            Employee updatedEmployee = employeeService.saveEmployee(existingEmployee);
            return new ResponseEntity<>(updatedEmployee, HttpStatus.OK);
        }
        return ResponseEntity.notFound().build();
    }

    // Delete an employee by ID
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteEmployee(@PathVariable Long id) {
        Optional<Employee> employee = employeeService.getEmployeeById(id);
        if (employee.isPresent()) {
            employeeService.deleteEmployee(id);
            return ResponseEntity.ok().build();
        }
        return ResponseEntity.notFound().build();
    }
}
@RestController: Indicates that this is a REST controller, and methods return JSON by default.
@RequestMapping("/employees"): Maps the controller to the /employees endpoint.
@PostMapping: Handles HTTP POST requests to create or update resources.
@GetMapping: Handles HTTP GET requests to retrieve resources.
@PutMapping: Handles HTTP PUT requests to update resources.
@DeleteMapping: Handles HTTP DELETE requests to remove resources.
7. Create the Application Class
This is the main entry point of the Spring Boot application.

java
Copy
package com.example.employee;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class EmployeeApplication {

    public static void main(String[] args) {
        SpringApplication.run(EmployeeApplication.class, args);
    }
}
@SpringBootApplication: This annotation marks the class as the entry point for the Spring Boot application. It’s a convenience annotation that includes @Configuration, @EnableAutoConfiguration, and @ComponentScan.
8. Application Properties
You’ll need to configure the database in the application.properties file. Here’s the configuration for an in-memory H2 database:

properties
Copy
# application.properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=update
spring.h2.console.enabled=true
spring.datasource.url: URL for the H2 in-memory database.
spring.jpa.hibernate.ddl-auto=update: Automatically updates the database schema.
spring.h2.console.enabled=true: Enables the H2 console to access the database in the browser.
9. Run the Application
You can run the application by using your IDE’s built-in runner or by using the following command in the terminal:

bash
Copy
mvn spring-boot:run
10. Testing the RESTful API
Once the application is running, you can test the API using a tool like Postman or cURL.

Create an Employee (POST request):

Endpoint: POST http://localhost:8080/employees
Body:
json
Copy
{
  "name": "John Doe",
  "department": "Engineering"
}
Get All Employees (GET request):

Endpoint: GET http://localhost:8080/employees
Get an Employee by ID (GET request):

Endpoint: GET http://localhost:8080/employees/{id}
Update an Employee (PUT request):

Endpoint: PUT http://localhost:8080/employees/{id}
Body:
json
Copy
{
  "name": "Jane Doe",
  "department": "HR"
}
Delete an Employee (DELETE request):

Endpoint: DELETE http://localhost:8080/employees/{id}
Conclusion
This example demonstrates how to build a simple RESTful API using Spring Boot with basic CRUD operations. It covers:

Setting up Spring Boot project
Creating model, repository, service, and controller layers
Configuring H2 in-memory database
Testing the API using HTTP methods (POST, GET, PUT, DELETE)
With this structure