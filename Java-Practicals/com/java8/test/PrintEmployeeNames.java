package com.java8.test;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class PrintEmployeeNames {

	public static void main(String[] args) {

		List<Employee> employees = Arrays.asList(new Employee("Alice", 45, "HR"), new Employee("Bob", 40, "Engineering"),
				new Employee("Charlie", 35, "Sales"));

		List<String> employeeNames = employees.stream().map(Employee::getName).collect(Collectors.toList());
		employeeNames.forEach(System.out::println);
		
		employees.stream().map(Employee::getName).forEach(System.out::println);

	}

}

class Employee {
	String name;
	int age;
	String department;

	Employee(String ename, int age, String department) {
		this.name = ename;
		this.age = age;
		this.department = department;
	}

	public String getName() {
		return name;
	}
}
