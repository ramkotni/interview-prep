package com.test.interviews;

import java.util.*;
import java.util.stream.*;
import java.util.function.Function;

public class FindMaxRepetations2 {

	public static void main(String[] args) {

		// Given array
        List<Integer> numbers = Arrays.asList(1, 2, 3, 3, 3, 2, 1, 2, 3, 3, 3, 4);

        // Count occurrences of each element
        Map<Integer, Long> frequencyMap = numbers.stream()
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        // Find the element with the maximum repetitions
        Map.Entry<Integer, Long> maxEntry = frequencyMap.entrySet().stream()
            .max(Map.Entry.comparingByValue())
            .orElseThrow(() -> new RuntimeException("Empty list"));

        // Find the element with the minimum repetitions
        Map.Entry<Integer, Long> minEntry = frequencyMap.entrySet().stream()
            .min(Map.Entry.comparingByValue())
            .orElseThrow(() -> new RuntimeException("Empty list"));

        // Print the results
        System.out.println("Element with maximum repetitions: " + maxEntry.getKey() + " (repeated " + maxEntry.getValue() + " times)");
        System.out.println("Element with minimum repetitions: " + minEntry.getKey() + " (repeated " + minEntry.getValue() + " times)");

	}

}
