package com.java8.test;
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

public class StreamsExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

        // Using Streams API to filter and print names starting with 'A'
        names.stream()
             .filter(name -> name.startsWith("A"))
             .forEach(System.out::println);
        
        //Consumer<String> startsWithA = n -> n.startsWith("A");
        
        //names.stream()
             //.filter(startsWithA.accept(name))
             //.forEach(System.out::println);
        
        
        
    }
}
