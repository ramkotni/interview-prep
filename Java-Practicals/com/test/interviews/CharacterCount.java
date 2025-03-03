package com.test.interviews;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class CharacterCount {
    public static void main(String[] args) {
        String input = "helloworld";

        // Step 1: Convert the string to a stream of characters
        Map<Character, Long> characterCountMap = input.chars()
                .mapToObj(c -> (char) c) // Convert each int to a char
                // Step 2: Collect the characters into a map with their counts
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        // Step 3: Filter the map to include only entries with counts greater than 1
        Map<Character, Long> filteredMap = characterCountMap.entrySet().stream()
                .filter(entry -> entry.getValue() > 1)
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

        // Step 4: Print the filtered results
        filteredMap.forEach((character, count) -> 
                System.out.println(character + ": " + count));
    }
}
