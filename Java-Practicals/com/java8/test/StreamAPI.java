package com.java8.test;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamAPI {

	public static void main(String[] args) {

		// Example1: Creating Stream and Operations
		List<Integer> numbers = Arrays.asList(1, 2, 4, 5, 6);

		numbers.stream().filter(x -> x % 2 == 0).map(x -> x * x).forEach(System.out::println);
		
		// Example 2: Collectors
		List<String> names = Arrays.asList("Jobh", "Bob", "Alice", "Sam");
		String concatenated = names.stream()
							.collect(Collectors.joining(" ,"));
		
		System.out.println(concatenated);

	}

}
