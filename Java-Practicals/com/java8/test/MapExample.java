package com.java8.test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class MapExample {

	public static void main(String[] args) {
		
		List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
		
		List<String> upperCaseNames = names.stream().map(String::toUpperCase).collect(Collectors.toList());
		
		upperCaseNames.forEach(System.out::println);

	}
	
	

}


