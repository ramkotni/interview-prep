package com.leetcode25;

/**
 * The Climbing Stairs problem (LeetCode #70) is a classic problem where you are tasked with finding the number of ways to reach the top of a staircase when you can either take 1 step or 2 steps at a time.
Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you reach the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to reach the top:
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to reach the top:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
Approach:
The problem can be approached using dynamic programming or recursion. The key observation is that the number of ways to reach the n-th step depends on the previous two steps. Specifically:
If you are at the n-th step, you could have gotten there either from the (n-1)-th step (taking a 1-step) or from the (n-2)-th step (taking a 2-step).
This results in the recurrence relation:
dp[n] = dp[n-1] + dp[n-2]
Where:
dp[n] is the number of ways to reach the n-th step.
Base Cases:
dp[0] = 1: There is one way to stay at the ground (i.e., not climbing).
dp[1] = 1: There is one way to reach the first step (i.e., taking one 1-step).
Solution:
We will use dynamic programming to store intermediate results and calculate the number of ways to reach each step up to n.

Explanation:
Base Cases:
If n = 1, there is only one way to reach the top (take one 1-step). Return 1.
If n = 2, there are two ways to reach the top: either take two 1-steps or one 2-step. Return 2.
Dynamic Programming:
We use two variables first and second to represent dp[n-2] and dp[n-1] respectively, i.e., the number of ways to reach the previous two steps.
We iteratively calculate the number of ways to reach the n-th step using the recurrence relation: dp[n] = dp[n-1] + dp[n-2].
Space Optimization:
Instead of maintaining a full array for dp, we only store the last two values (first and second) to optimize space. This reduces the space complexity from O(n) to O(1).
Time Complexity:
The time complexity is O(n) because we loop through the range from 3 to n once, performing constant-time operations inside the loop.
Space Complexity:
The space complexity is O(1), as we are only using two variables to store intermediate results.
Example Walkthrough:
For n = 5:
Start with first = 1 (dp[0]) and second = 2 (dp[1]).
For i = 3, calculate current = first + second = 1 + 2 = 3. Update first = 2, second = 3.
For i = 4, calculate current = first + second = 2 + 3 = 5. Update first = 3, second = 5.
For i = 5, calculate current = first + second = 3 + 5 = 8. Update first = 5, second = 8.
Thus, the number of ways to reach step 5 is 8.
Conclusion:
This approach efficiently calculates the number of distinct ways to climb the staircase using dynamic programming with space optimization, making it suitable for large values of n
 * 
 * 
 */

public class ClimbingStairs70 {
    public int climbStairs(int n) {
        // Base cases
        if (n == 1) {
            return 1;
        }
        
        // Two variables to store the ways to reach the previous two steps
        int first = 1; // dp[0]
        int second = 2; // dp[1]
        
        for (int i = 3; i <= n; i++) {
            // The current number of ways to reach the i-th step is the sum of the previous two steps
            int current = first + second;
            first = second;  // Update first to the previous step
            second = current; // Update second to the current step
        }
        
        return second; // Return the number of ways to reach the nth step
    }

    public static void main(String[] args) {
        ClimbingStairs70 solution = new ClimbingStairs70();
        
        // Test case 1
        System.out.println(solution.climbStairs(2));  // Output: 2
        
        // Test case 2
        System.out.println(solution.climbStairs(3));  // Output: 3
        
        // Test case 3
        System.out.println(solution.climbStairs(4));  // Output: 5
        
        // Test case 4
        System.out.println(solution.climbStairs(5));  // Output: 8
    }
}
