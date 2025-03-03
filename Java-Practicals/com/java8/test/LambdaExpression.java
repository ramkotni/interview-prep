package com.java8.test;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.Function;

public class LambdaExpression {

	public static void main(String[] args) {

		//Example1: Simple Lambda expression
		Runnable runnable = () -> System.out.println("Hello Lambda!!");
		runnable.run();
		
		//Example2: Lambda expression with parameters
		Function<Integer, Integer> square = x -> x * x;
		System.out.println(square.apply(5));
		
		List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

		// Using a lambda expression to sort names in alphabetical order
		Collections.sort(names, (String a, String b) -> {
		    return a.compareTo(b);
		});

		// Shorter version
		Collections.sort(names, (a, b) -> a.compareTo(b));
		

	}

}
