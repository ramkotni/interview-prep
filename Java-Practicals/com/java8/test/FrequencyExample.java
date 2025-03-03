package com.java8.test;

import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

public class FrequencyExample {
    public static void main(String[] args) {
        List<Integer> diceRolls = Arrays.asList(1, 2, 3, 4, 5, 6, 1, 2, 2, 3, 3, 3);

        // Counting frequency of each number
        Map<Integer, Long> frequencyMap = diceRolls.stream()
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        // Output the frequency map
        frequencyMap.forEach((number, count) -> 
            System.out.println("Number: " + number + ", Count: " + count));
    }
}
