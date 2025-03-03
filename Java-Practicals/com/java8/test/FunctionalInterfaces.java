package com.java8.test;

import java.util.function.BiConsumer;
import java.util.function.BiFunction;
import java.util.function.BiPredicate;
import java.util.function.BinaryOperator;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.IntPredicate;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.function.UnaryOperator;

public class FunctionalInterfaces {

	public static void main(String[] args) {

		// Example1 : Predicate Functional Interface
		Predicate<Integer> isEven = x -> x % 2 == 0;
		System.out.println(isEven.test(6));

		// Example2: Consumer Functional Interface
		Consumer<String> toUpperCase = str -> System.out.println(str.toUpperCase());
		toUpperCase.accept("hello lambda");
		
		// Example3: Function<T,R> Functional Interface
		Function<String, Integer> stringLength = str -> str.length();
		String testString = "Hello, World!";
		int length = stringLength.apply(testString);
		System.out.println("Length of the string: " + length);
		
		// Example4: Supplier<T> Functional Interface
		Supplier<String> stringSupplier = () -> "Hello from Supplier!";
		String result = stringSupplier.get();
		System.out.println(result);
		
		BinaryOperator<Integer> sum = (a, b) -> a + b;
		int result12 = sum.apply(5, 3);
		System.out.println("Sum: " + result12);

		UnaryOperator<Integer> square = x -> x * x;
		int result1 = square.apply(4);
		System.out.println("Square: " + result1);

		BiFunction<String, String, String> concatenate = (str1, str2) -> str1 + str2;
		String resultStr = concatenate.apply("Hello, ", "World!");
		System.out.println(resultStr);

		BiConsumer<String, Integer> printDetails = (name, age) -> System.out.println("Name: " + name + ", Age: " + age);
		printDetails.accept("Alice", 30);

		BiPredicate<String, Integer> checkLength = (str, len) -> str.length() == len;
		boolean resultb = checkLength.test("Hello", 5);
		System.out.println("String length matches: " + resultb);

		IntPredicate isEven1 = number -> number % 2 == 0;
		boolean resultA = isEven1.test(4);
		System.out.println("Is even: " + resultA);

	}

}
