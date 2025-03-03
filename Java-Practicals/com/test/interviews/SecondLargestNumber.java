package com.test.interviews;
import java.util.Arrays;
import java.util.Comparator;
import java.util.OptionalInt;
import java.util.stream.IntStream;

public class SecondLargestNumber {
    public static int findSecondLargest(int[] numbers) {
        return IntStream.of(numbers)
                .boxed()
                .sorted(Comparator.reverseOrder())
                .skip(1)
                .findFirst()
                .orElse(-1); // Or any default value you prefer
    }

    public static void main(String[] args) {
        int[] numbers = {12, 35, 1, 10, 34, 1};
        int secondLargest = findSecondLargest(numbers);
        System.out.println("Second largest number: " + secondLargest);
    }
}
