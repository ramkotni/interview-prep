package com.leetcodeprobs.test;
public class ReverseInteger {
    public static int reverse(int x) {
        long reversed = 0;
        while (x != 0) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
            if (reversed > Integer.MAX_VALUE || reversed < Integer.MIN_VALUE) {
                return 0;
            }
        }
        return (int) reversed;
    }

    public static void main(String[] args) {
        int x = 123;
        System.out.println(reverse(x)); // Output: 321

        x = -123;
        System.out.println(reverse(x)); // Output: -321

        x = 120;
        System.out.println(reverse(x)); // Output: 21
    }
}
