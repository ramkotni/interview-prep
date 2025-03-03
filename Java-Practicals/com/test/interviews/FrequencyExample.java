package com.test.interviews;
import java.util.*;
import java.util.stream.Collectors;
import java.util.function.Function;

public class FrequencyExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 1, 2, 2, 3, 3, 3);

        // Counting frequency of each number
        Map<Integer, Long> frequencyMap = numbers.stream()
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        // Find the maximum occurrence
        Optional<Map.Entry<Integer, Long>> maxEntry = frequencyMap.entrySet()
            .stream()
            .max(Map.Entry.comparingByValue());

        // Find the minimum occurrence
        Optional<Map.Entry<Integer, Long>> minEntry = frequencyMap.entrySet()
            .stream()
            .min(Map.Entry.comparingByValue());

        // Output the frequency map
        System.out.println("Frequency Map: " + frequencyMap);

        // Output maximum occurrence
        if (maxEntry.isPresent()) {
            System.out.println("Number with max occurrence: " + maxEntry.get().getKey() +
                               ", Count: " + maxEntry.get().getValue());
        }

        // Output minimum occurrence
        if (minEntry.isPresent()) {
            System.out.println("Number with min occurrence: " + minEntry.get().getKey() +
                               ", Count: " + minEntry.get().getValue());
        }
    }
}
