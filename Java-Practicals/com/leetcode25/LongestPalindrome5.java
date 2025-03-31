package com.leetcode25;

/**
 * Problem:
Given a string s, return the longest palindromic substring in s.

A palindrome is a string that reads the same forward and backward.

Solution Approach:
The idea is to treat each character (and each pair of consecutive characters) as the potential center of a palindrome.

Expand around each center and check how far you can go while the string remains a palindrome.

The time complexity for this approach is O(n^2), where n is the length of the string, and the space complexity is O(1).
 * 
 * Explanation:
Main Function (longestPalindrome):

We iterate through each character in the string.

For each character, we expand around it twice:

First for the case of an odd-length palindrome (by using expandAroundCenter(s, i, i)).

Then for the case of an even-length palindrome (by using expandAroundCenter(s, i, i + 1)).

We keep track of the longest palindrome found so far using the start and end indices.

Helper Function (expandAroundCenter):

This function checks how far we can expand from a given center (either a single character for odd-length palindromes or two characters for even-length ones).

We expand outwards by moving the left and right pointers until the characters at those positions are no longer equal.

The length of the palindrome is calculated as right - left - 1 (since the while loop expands one step further beyond the actual palindrome).

Time Complexity:
We loop through each character, and for each character, we expand around it in both directions (left and right).

Therefore, the time complexity is O(n^2), where n is the length of the string.

Space Complexity:
The space complexity is O(1) since we are using only a few variables to track the start and end indices.

Example:
Input: "babad"

Output: "bab" (or "aba")

The longest palindromic substring in "babad" is "bab", but the solution could also return "aba" depending on the order of expansion.
 * 
 */


public class LongestPalindrome5 {

    public String longestPalindrome(String s) {
        // Edge case: If the string is empty or has one character, it's a palindrome by default
        if (s == null || s.length() < 1) {
            return "";
        }

        // Variables to store the start and end of the longest palindrome found
        int start = 0, end = 0;

        for (int i = 0; i < s.length(); i++) {
            // Expand around the center (i, i) for odd length palindromes
            int len1 = expandAroundCenter(s, i, i);
            // Expand around the center (i, i + 1) for even length palindromes
            int len2 = expandAroundCenter(s, i, i + 1);
            
            // The maximum length between the two possible palindromes
            int len = Math.max(len1, len2);
            
            // If the new palindrome is longer, update the start and end pointers
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }

        // Return the substring from start to end indices (inclusive)
        return s.substring(start, end + 1);
    }

    // Helper function to expand around the center and return the length of the palindrome
    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // Length of the palindrome is the difference between right and left indices
        return right - left - 1;
    }

    public static void main(String[] args) {
        LongestPalindrome5 solution = new LongestPalindrome5();
        
        // Example test case
        String input = "babad";
        String result = solution.longestPalindrome(input);
        
        System.out.println("Longest Palindromic Substring: " + result); // Output could be "bab" or "aba"
    }
}
