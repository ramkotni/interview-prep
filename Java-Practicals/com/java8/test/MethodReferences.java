package com.java8.test;

import java.util.Arrays;
import java.util.List;

public class MethodReferences {

	public static void main(String[] args) {

		List<String> words = Arrays.asList("apple", "banana", "cherry");
		words.forEach(System.out::println);

	}

}
