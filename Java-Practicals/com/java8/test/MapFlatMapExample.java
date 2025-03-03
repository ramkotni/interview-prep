package com.java8.test;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class MapFlatMapExample {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("Hello", "World");

        // Using map
        List<String[]> mapped = words.stream()
                                     .map(word -> word.split(""))
                                     .collect(Collectors.toList());

        // Using flatMap
        List<String> flatMapped = words.stream()
                                       .flatMap(word -> Arrays.stream(word.split("")))
                                       .collect(Collectors.toList());

        // Print results
        System.out.println("Mapped: " + mapped);
        System.out.println("FlatMapped: " + flatMapped);
    }
}
