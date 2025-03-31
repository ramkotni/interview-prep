package com.leetcode25;

/**
 * 
 * Problem:
Given a 32-bit signed integer, reverse the digits of the integer. If the reversed integer overflows, return 0.

Constraints:
The input integer x is a 32-bit signed integer. Thus, the integer ranges from -2^31 to 2^31 - 1.

If the reversed integer overflows, return 0.

Approach:
Sign Handling: Check if the number is negative. If it is, make the number positive for easy reversal, and remember to apply the negative sign after the reversal.

Reversal Logic: We can reverse the number by repeatedly taking the last digit (x % 10), adding it to the reversed number, and then removing that digit from x by dividing by 10 (x / 10).

Overflow Handling: Ensure that the reversed number doesn’t overflow. The valid range for a 32-bit signed integer is from -2^31 to 2^31 - 1, which is [-2147483648, 2147483647]. If reversing the number leads to an overflow, return 0.
 * 
 * Explanation:
Sign Handling:

We check if the number is negative by using x < 0. If it is negative, we store the sign in the variable sign and work with the absolute value of x.

Reversal Logic:

We initialize reversed as 0 to accumulate the reversed digits.

We extract each digit from x by taking x % 10 (the last digit).

We multiply reversed by 10 to shift its digits left and then add the new digit.

We remove the last digit from x by dividing it by 10.

Overflow Check:

After updating reversed, we check if it exceeds the maximum value for a 32-bit signed integer (INT_MAX = 2147483647).

If at any point reversed exceeds INT_MAX, we return 0, indicating overflow.

We also check the final result after applying the sign to ensure it doesn't exceed the bounds of a 32-bit signed integer.

Returning the Result:

If no overflow is detected, the reversed number is returned as an integer.

Time Complexity:
O(log(x)): The time complexity is proportional to the number of digits in the integer. We process each digit of x once, and since the number of digits is logarithmic in x, the complexity is O(log(x)).

Space Complexity:
O(1): We use only a constant amount of extra space (for variables like reversed, sign, etc.).

Example Walkthrough:
Input: 123

Step 1: x = 123, reversed = 0

Step 2: digit = 123 % 10 = 3, reversed = 0 * 10 + 3 = 3, x = 12

Step 3: digit = 12 % 10 = 2, reversed = 3 * 10 + 2 = 32, x = 1

Step 4: digit = 1 % 10 = 1, reversed = 32 * 10 + 1 = 321, x = 0

Result: reversed = 321, Return 321

Input: -123

The process is similar, but the sign is stored as -1. After reversal, the result will be -321.

Input: 120

The reversed number is 21 (since leading zeros are discarded).

Input: 1534236469

This will overflow because the reversed number exceeds the 32-bit signed integer range, so the result will be 0.

Edge Cases:
Single digit numbers: These remain unchanged (e.g., 5 becomes 5).

Zero: The reversed number is 0.

Negative numbers: The sign is preserved after the reversal.

Overflow: If the reversed number exceeds the 32-bit signed integer limit, return 0.

Let me know if you have any further questions or need additional clarifications!
 * 
 * 
 * @param x
 * @return
 */





public class ReverseInteger7{

    public int reverse(int x) {
        // Define the bounds for 32-bit signed integer
        int INT_MIN = -2147483648;
        int INT_MAX = 2147483647;
        
        long reversed = 0; // We use long to avoid overflow during reversal process
        int sign = (x < 0) ? -1 : 1; // Store the sign of the number
        x = Math.abs(x); // Work with the absolute value of x

        while (x != 0) {
            int digit = x % 10; // Get the last digit of x
            reversed = reversed * 10 + digit; // Append it to the reversed number
            
            // Check for overflow before assigning the reversed value
            if (reversed > INT_MAX) {
                return 0; // Overflow occurred
            }

            x /= 10; // Remove the last digit from x
        }

        // Apply the sign to the result
        reversed *= sign;

        // Check for overflow for negative numbers as well
        if (reversed < INT_MIN || reversed > INT_MAX) {
            return 0; // Overflow occurred
        }

        return (int) reversed; // Return the reversed number
    }

    public static void main(String[] args) {
        ReverseInteger7 solution = new ReverseInteger7();

        // Example test cases
        System.out.println(solution.reverse(123)); // Output: 321
        System.out.println(solution.reverse(-123)); // Output: -321
        System.out.println(solution.reverse(120)); // Output: 21
        System.out.println(solution.reverse(0)); // Output: 0
        System.out.println(solution.reverse(1534236469)); // Output: 0 (overflow)
    }
}
