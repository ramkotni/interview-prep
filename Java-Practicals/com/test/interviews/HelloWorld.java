package com.test.interviews;

import java.util.*;
import java.util.stream.*;
import java.util.function.Function;
public class HelloWorld {

	public static void main(String[] args) {
		
		int[] array = {1,2,3,3,2,1,1,2,3,3,3,4,2,2,2,2};
		
		Map<Integer, Long> counts = Arrays.stream(array)
				.boxed()
				.collect(Collectors.groupingBy(Function.identity(),Collectors.counting()));
		
		System.out.println(counts);
		
		//int max = counts.keys().stream().max(Integer::compareTo).orElseThrow(() -> new RuntimeException(" "));

		Long max = counts.values().stream()
				   .mapToLong(Long::longValue)
				   .max()
				   .orElseThrow(() -> new RuntimeException("Counts empty "));
		
		System.out.println(max);
		
		Long min = counts.values().stream()
				   .mapToLong(Long::longValue)
				   .min()
				   .orElseThrow(() -> new RuntimeException("Counts empty "));
		
		System.out.println(min);
	
	}

}
