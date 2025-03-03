package com.test.interviews;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class SortingByName {

	public static void main(String[] args) {
		// Create a list of employees
		List<Employee> employees = Arrays.asList(new Employee("Alice", 1, "HR"), new Employee("Bob", 2, "Finance"),
				new Employee("Charlie", 3, "Engineering"));

		// Sort employees by name using Stream API
		List<Employee> sortedByName = employees.stream().sorted((e1, e2) -> e1.getName().compareTo(e2.getName()))
				.collect(Collectors.toList());

		// Print sorted employees
		sortedByName.forEach(System.out::println);
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

	// Getters
	public String getName() {
		return name;
	}

	public int getId() {
		return id;
	}

	public String getDepartment() {
		return department;
	}

	@Override
	public String toString() {
		return "Employee{" + "name='" + name + '\'' + ", id=" + id + ", department='" + department + '\'' + '}';
	}
}
