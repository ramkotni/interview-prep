package com.java8.test;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class PredicateStringExample {

    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Edward");

        // Predicate to check if a name starts with 'A'
        Predicate<String> startsWithA = name -> name.startsWith("A");

        // Filter the list using the predicate
        List<String> namesStartingWithA = names.stream()
                                               .filter(startsWithA)
                                               .collect(Collectors.toList());

        // Output the result
        System.out.println("Names starting with A: " + namesStartingWithA);
    }
}
