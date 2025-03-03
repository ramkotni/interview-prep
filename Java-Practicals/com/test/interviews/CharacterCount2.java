package com.test.interviews;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class CharacterCount2 {
    public static void main(String[] args) {
        String input = "helloworld";

        Map<Character, Long> characterCount = input.chars()
            .mapToObj(c -> (char) c)
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        characterCount.forEach((character, count) -> 
            System.out.println(character + ": " + count));
        
        //characterCount.values().stream().filter(null)
    }
}

/**
Explanation:
Import Statements: Import necessary classes from java.util and java.util.stream packages.

Main Method: Define the main method where the logic will reside.

Input String: Define the input string input with the value "helloworld".

Stream Creation:

input.chars(): Converts the string into an IntStream of ASCII values.
.mapToObj(c -> (char) c): Converts each ASCII value to its corresponding character, creating a Stream<Character>.
Collecting the Result:

.collect(Collectors.groupingBy(Function.identity(), Collectors.counting())):
Collectors.groupingBy(Function.identity()) groups the characters by themselves.
Collectors.counting() counts the occurrences of each character in the group.
Printing the Result:

characterCount.forEach((character, count) -> System.out.println(character + ": " + count)): Iterates over the Map and prints each character and its count.
This program will output the number of occurrences of each character in the "helloworld" string.
*/