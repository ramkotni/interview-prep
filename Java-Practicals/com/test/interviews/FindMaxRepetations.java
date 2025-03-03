package com.test.interviews;

import java.util.*;
import java.util.stream.*;
import java.util.function.Function;

public class FindMaxRepetations {

	public static void main(String[] args) {

		int[] array = { 1, 2, 3, 3, 3, 2, 1, 2, 3, 3, 3, 4 };
		// find out the max and min repetation
		// Step1: convert the array into stream and count the occurrences of each
		// element
		Map<Integer, Long> frequencyMap = Arrays.stream(array).boxed()
				.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

		System.out.println("frequency Map " + frequencyMap);

		// Step2: find the maximum frequency

		long maxFrequency = frequencyMap.values().stream().mapToLong(Long::longValue).max()
				.orElseThrow(() -> new RuntimeException("Array is emtpy"));

		System.out.println("maxFrequency :: " + maxFrequency);

		// Step3: find the minimum frequency
		long minFrequency = frequencyMap.values().stream().mapToLong(Long::longValue).min()
				.orElseThrow(() -> new RuntimeException("Array is empty"));

		System.out.println("minFrequency ::" + minFrequency);

		// Step 4: Identify elements with maximum and minimum frequencies
		var maxElements = frequencyMap.entrySet().stream().filter(entry -> entry.getValue() == maxFrequency)
				.map(Map.Entry::getKey).collect(Collectors.toList());

		var minElements = frequencyMap.entrySet().stream().filter(entry -> entry.getValue() == minFrequency)
				.map(Map.Entry::getKey).collect(Collectors.toList());

		// Output the results
		System.out.println("Elements with maximum repetitions: " + maxElements + " (Frequency: " + maxFrequency + ")");
		System.out.println("Elements with minimum repetitions: " + minElements + " (Frequency: " + minFrequency + ")");
		
		/**
		 * The following are examples of using the predefined collectors to performcommon mutable reduction tasks: 

 // Accumulate names into a List
 List<String> list = people.stream()
   .map(Person::getName)
   .collect(Collectors.toList());

 // Accumulate names into a TreeSet
 Set<String> set = people.stream()
   .map(Person::getName)
   .collect(Collectors.toCollection(TreeSet::new));

 // Convert elements to strings and concatenate them, separated by commas
 String joined = things.stream()
   .map(Object::toString)
   .collect(Collectors.joining(", "));

 // Compute sum of salaries of employee
 int total = employees.stream()
   .collect(Collectors.summingInt(Employee::getSalary));

 // Group employees by department
 Map<Department, List<Employee>> byDept = employees.stream()
   .collect(Collectors.groupingBy(Employee::getDepartment));

 // Compute sum of salaries by department
 Map<Department, Integer> totalByDept = employees.stream()
   .collect(Collectors.groupingBy(Employee::getDepartment,
                                  Collectors.summingInt(Employee::getSalary)));

 // Partition students into passing and failing
 Map<Boolean, List<Student>> passingFailing = students.stream()
   .collect(Collectors.partitioningBy(s -> s.getGrade() >= PASS_THRESHOLD));
Since:• 1.8

		 */

	}

}
