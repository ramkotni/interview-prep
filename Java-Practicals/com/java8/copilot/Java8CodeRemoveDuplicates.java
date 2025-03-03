package com.java8.copilot;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Java8CodeRemoveDuplicates {
    //Remove Duplicate Elements from a List
	public static void main(String[] args) {
        List<String> listOfStrings = Arrays.asList("Java", "Python", "C#", "Java", "Kotlin", "Python");
        List<String> uniqueStrings = listOfStrings.stream()
            .distinct()
            .collect(Collectors.toList());
        
        System.out.println(uniqueStrings);
    }
}