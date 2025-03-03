package com.test.interviews;

import java.util.Comparator;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

public class SecondLargestRepetition 
{
	public static char findSecondLargestRepetition(String str)
	{
	        Map<Character, Long> charCountMap = str.chars()
	                .mapToObj(c -> (char) c)
	                .collect(Collectors.groupingBy(c -> c, Collectors.counting()));  
	
	
	        Optional<Map.Entry<Character, Long>> secondLargest = charCountMap.entrySet().stream()
	                .sorted(Comparator.comparingLong(Map.Entry::getValue).reversed())
	                .skip(1)
	                .findFirst();
	
	        return secondLargest.map(Map.Entry::getKey).orElse('\0');
	    }

	public static void main(String[] args) {
		String str = "AAABBBCCDD";
		char secondLargestChar = findSecondLargestRepetition(str);
		System.out.println("Second largest repetition: " + secondLargestChar);
	}
}
