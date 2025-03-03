package com.java8.copilot;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Java8Code {
    
	//Separate Odd and Even Numbers from a List
	
	public static void main(String[] args) {
        List<Integer> listOfIntegers = Arrays.asList(71, 18, 42, 21, 67, 32, 95, 14, 56, 87);
        Map<Boolean, List<Integer>> oddEvenNumbersMap = listOfIntegers.stream()
            .collect(Collectors.partitioningBy(i -> i % 2 == 0));
        
        oddEvenNumbersMap.forEach((isEven, numbers) -> {
            System.out.println(isEven ? "Even Numbers" : "Odd Numbers");
            numbers.forEach(System.out::println);
        });
    }
}