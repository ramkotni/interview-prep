package com.java8.test;
import java.util.Optional;

public class OptionalExample {
    public static void main(String[] args) {
        Optional<String> optional = Optional.of("Hello");

        // Check if value is present
        if (optional.isPresent()) {
            System.out.println(optional.get());
        }

        // Using ifPresent method
        optional.ifPresent(System.out::println);

        // Using orElse method
        System.out.println(optional.orElse("Default Value"));
    }
}
