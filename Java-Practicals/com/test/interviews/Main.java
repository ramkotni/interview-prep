package com.test.interviews;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        // Create a list of employees
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", 1, "HR"),
            new Employee("Bob", 2, "Finance"),
            new Employee("Charlie", 3, "Engineering")
        );

        // Extract names using Stream API
        List<String> names = employees.stream()
                                      .map(Employee::getName) // Use method reference to map each employee to their name
                                      .collect(Collectors.toList()); // Collect the results into a List

        // Print the names
        names.forEach(System.out::println);
    }
}

class Employee {
    private String name;
    private int id;
    private String department;

    // Constructor
    public Employee(String name, int id, String department) {
        this.name = name;
        this.id = id;
        this.department = department;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Getters and setters for other fields
    // ...
}
