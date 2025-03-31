package com.leetcode25;

/**
 * The String to Integer (atoi) problem (LeetCode #8) requires implementing a function that converts a string to an integer, similar to how atoi() works in C/C++. This problem involves handling various edge cases, such as leading spaces, signs, non-numeric characters, and overflow.
Problem Description:
You need to implement a function that converts a string to a 32-bit signed integer (int). The function must handle the following rules:
Ignore leading spaces.
Handle optional leading "+" or "-" signs.
Read in numbers until a non-digit character is encountered.
If the number exceeds the 32-bit signed integer range, return the appropriate boundary (INT_MAX or INT_MIN).
Return 0 if no valid conversion can be made.
Approach:
Handle leading whitespaces: Skip any spaces before processing the actual number.
Handle optional signs: If the first non-space character is a + or -, remember the sign.
Parse digits: Continue processing characters until a non-digit is encountered, accumulating the value.
Handle overflow: If the number goes out of the bounds of a 32-bit signed integer, return INT_MAX or INT_MIN.
Return the result.
Explanation:
Skip Leading Whitespaces:
The string can have leading whitespaces, so we move the index i forward until we encounter a non-space character.
Handle the Sign (+ or -):
After skipping spaces, if we find a -, the number will be negative; if it's a +, the number will be positive (default). We move i forward after reading the sign.
Parse the Digits:
We iterate over each character and check if it is a digit (Character.isDigit(s.charAt(i))).
For each digit, we calculate the current result by multiplying the current result by 10 and adding the digit.
Before updating the result, we check for overflow:
If result exceeds Integer.MAX_VALUE / 10, it will overflow on the next multiplication by 10, so we return Integer.MAX_VALUE or Integer.MIN_VALUE accordingly.
If result is equal to Integer.MAX_VALUE / 10, we check if adding the current digit exceeds the maximum allowable value (Integer.MAX_VALUE % 10).
Final Result:
After processing the digits, we apply the sign and return the final result.
Edge Cases:
Empty String: Return 0.
String with only whitespaces: Return 0.
String with no valid digits: Return 0 (e.g., "words and 987").
Overflow and Underflow: Handle cases where the number exceeds the 32-bit integer limits (Integer.MAX_VALUE or Integer.MIN_VALUE).
Time Complexity:
O(n): We only go through the string once, where n is the length of the string. Each character is processed once.
Space Complexity:
O(1): We only use a constant amount of extra space (for variables like sign, result, etc.).
Example Walkthrough:
Input: "42"
Skip spaces → No sign → Parse digits → Result is 42.
Input: " -42"
Skip spaces → Sign is - → Parse digits → Result is -42.
Input: "4193 with words"
Parse digits until non-digit → Result is 4193.
Input: "words and 987"
No valid digits → Return 0.
Input: "-91283472332"
Parse digits → Result exceeds Integer.MIN_VALUE, so return Integer.MIN_VALUE.
Output:
 * 
 * 
 * 
 */

public class StringToIntegerAtoi8 {
    
    public int myAtoi(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }

        int i = 0;
        int n = s.length();
        
        // Step 1: Ignore leading whitespaces
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }
        
        // Step 2: Handle optional '+' or '-' sign
        int sign = 1;
        if (i < n && s.charAt(i) == '-') {
            sign = -1;
            i++;
        } else if (i < n && s.charAt(i) == '+') {
            i++;
        }
        
        // Step 3: Process digits and form the number
        int result = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';
            
            // Check for overflow before updating the result
            if (result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            
            result = result * 10 + digit;
            i++;
        }

        // Step 4: Apply sign and return the result
        return result * sign;
    }

    public static void main(String[] args) {
        StringToIntegerAtoi8 solution = new StringToIntegerAtoi8();
        
        // Test cases
        System.out.println(solution.myAtoi("42")); // Output: 42
        System.out.println(solution.myAtoi("   -42")); // Output: -42
        System.out.println(solution.myAtoi("4193 with words")); // Output: 4193
        System.out.println(solution.myAtoi("words and 987")); // Output: 0
        System.out.println(solution.myAtoi("-91283472332")); // Output: -2147483648 (Integer.MIN_VALUE)
        System.out.println(solution.myAtoi("21474836460")); // Output: 2147483647 (Integer.MAX_VALUE)
    }
}
