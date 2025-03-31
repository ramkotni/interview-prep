package com.leetcode25;
import java.util.Stack;

/**
 * The Valid Parentheses problem (LeetCode #20) asks you to determine if a given string containing parentheses, square brackets, and curly brackets is valid. A string is valid if the brackets are properly closed and nested.
Problem Description:
Given a string containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid. An input string is valid if:
Open brackets must be closed by the corresponding closing bracket.
Open brackets must be closed in the correct order.
Example 1:
Input:
s = ""()"" 
Output:
true
Example 2:
Input:
s = ""()[]{}""
Output:
true
Example 3:
Input:
s = ""(]""
Output:
false
Example 4:
Input:
s = ""([)]""
Output:
false
Example 5:
Input:
s = ""{[]}""
Output:
true
Approach:
The key idea is to use a stack to keep track of the opening brackets. As we iterate through the string:
Push opening brackets ('(', '{', '[') onto the stack.
Pop the stack when encountering a closing bracket (')', '}', ']') and check if it corresponds to the top of the stack.
If the stack is empty when encountering a closing bracket, the string is invalid because there is no matching opening bracket.
If the popped element does not match the expected opening bracket for the current closing bracket, the string is invalid.
At the end of the iteration, if the stack is empty, the string is valid. If the stack is not empty, there are unmatched opening brackets, and the string is invalid.
Algorithm:
Create a stack to store the opening brackets.
Traverse through each character in the string:
If the character is an opening bracket, push it onto the stack.
If it’s a closing bracket, check if the stack is non-empty and if the top of the stack matches the corresponding opening bracket. If so, pop the stack. Otherwise, return false.
If the stack is empty at the end, return true. Otherwise, return false.
 * 
 * 
 * Explanation:
Stack Usage:
The Stack<Character> is used to store the opening brackets as we encounter them in the string.
When we encounter a closing bracket, we check if it matches the most recent opening bracket stored in the stack.
isMatchingPair() Function:
This helper function checks if the opening bracket and closing bracket form a valid pair. For example, (' with ) or { with }.
Iterating Through the String:
We loop through the string using s.toCharArray() to get each character.
If the character is an opening bracket ((, {, or [), we push it onto the stack.
If the character is a closing bracket (), }, or ]), we check if the stack is empty or the top of the stack does not match the expected opening bracket. If either condition is true, we return false.
Final Check:
After processing the entire string, if the stack is empty, it means all the opening brackets were matched and closed properly, so we return true.
If the stack is not empty, it means there are unmatched opening brackets, so we return false.
Time Complexity:
O(n), where n is the length of the string. We traverse the string once, and each operation (push and pop) on the stack takes constant time.
Space Complexity:
O(n), where n is the length of the string. In the worst case, all characters could be opening brackets, and the stack will store all of them.
Example Walkthrough:
Input: ""()""
Step 1: Encounter '(' → Push to stack: stack = ['(']
Step 2: Encounter ')' → Pop from stack and check if it matches '(' → Stack is empty.
Step 3: Stack is empty → Return true.
Input: ""([)]""
Step 1: Encounter '(' → Push to stack: stack = ['(']
Step 2: Encounter '[' → Push to stack: stack = ['(', '[']
Step 3: Encounter ')' → Pop from stack, but '[' does not match ')'. Return false.
Input: ""{}[]""
Step 1: Encounter '{' → Push to stack: stack = ['{']
Step 2: Encounter '}' → Pop from stack, matching {. Stack is empty.
Step 3: Encounter '[' → Push to stack: stack = ['[']
Step 4: Encounter ']' → Pop from stack, matching [. Stack is empty.
Step 5: Stack is empty → Return true.
Conclusion:
The Valid Parentheses problem is solved efficiently using a stack to track the opening brackets and ensure they match the corresponding closing brackets in the correct order. This solution has a time complexity of O(n) and space complexity of O(n), making it optimal for this problem.
 * 
 */

public class ValidParentheses20 {

    public boolean isValid(String s) {
        // Create a stack to keep track of opening parentheses
        Stack<Character> stack = new Stack<>();

        // Traverse through each character in the string
        for (char c : s.toCharArray()) {
            // If the character is an opening parenthesis, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } 
            // If the character is a closing parenthesis, check for matching opening parenthesis
            else {
                // If stack is empty or the top of the stack doesn't match the corresponding opening parenthesis
                if (stack.isEmpty() || !isMatchingPair(stack.pop(), c)) {
                    return false;
                }
            }
        }

        // The string is valid if the stack is empty at the end (all opened parentheses have been closed)
        return stack.isEmpty();
    }

    // Helper function to check if a pair of parentheses match
    private boolean isMatchingPair(char open, char close) {
        return (open == '(' && close == ')') || 
               (open == '{' && close == '}') || 
               (open == '[' && close == ']');
    }

    public static void main(String[] args) {
        ValidParentheses20 solution = new ValidParentheses20();

        // Test cases
        System.out.println(solution.isValid("()"));      // Output: true
        System.out.println(solution.isValid("()[]{}"));  // Output: true
        System.out.println(solution.isValid("(]"));      // Output: false
        System.out.println(solution.isValid("([)]"));    // Output: false
        System.out.println(solution.isValid("{[]}"));    // Output: true
    }
}
