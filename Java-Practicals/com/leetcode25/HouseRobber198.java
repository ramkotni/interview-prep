package com.leetcode25;

/**
 * The House Robber problem (LeetCode #198) is a dynamic programming problem where you are given an array of non-negative integers representing the amount of money of each house, and you need to find the maximum amount of money you can rob tonight without alerting the police.
The rule is:
You cannot rob two adjacent houses because the security system will alert the police if two adjacent houses are robbed.
Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money hidden, and you cannot rob two adjacent houses due to the security system.
Given an integer array nums where nums[i] represents the amount of money in the i-th house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:
Input: nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (amount = 2), rob house 3 (amount = 9), and rob house 5 (amount = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
Example 2:
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (amount = 1), rob house 3 (amount = 3).
Total amount you can rob = 1 + 3 = 4.
Approach:
To solve this problem, we will use dynamic programming. The idea is to decide whether to rob the current house or skip it. For each house, we have two choices:
Rob this house, which means we add the value of this house to the maximum money robbed from all previous houses excluding the adjacent one.
Skip this house, and the maximum amount of money robbed is the same as the maximum amount robbed from the previous house.
This leads to the recurrence relation:
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
dp[i-1]: The maximum money we can rob from the previous house.
dp[i-2] + nums[i]: The maximum money we can rob if we include the current house i.
Base cases:
dp[0] = nums[0]: If there is only one house, the maximum money is just the value of that house.
dp[1] = max(nums[0], nums[1]): If there are two houses, the maximum money is the larger of the two.
Solution:
We can optimize the space complexity to O(1) by using two variables to store the last two values of the dynamic programming array (dp[i-1] and dp[i-2]), since we only need the previous two results to compute the current result.
 * 
 * Explanation:
Edge Cases:
If the array is empty, return 0 because there are no houses to rob.
If the array has only one house, return the value of that house.
Dynamic Programming:
We use two variables (prev1 and prev2) to represent the maximum money robbed up to the two previous houses (dp[i-2] and dp[i-1]).
For each house in the array, we calculate the maximum money we can rob by either skipping the current house or robbing it (taking the value from prev1 + nums[i]), and update the variables accordingly.
At the end of the loop, prev2 will store the maximum money we can rob after considering all houses.
Time Complexity:
The time complexity is O(n), where n is the length of the nums array, because we only need to iterate through the array once.
Space Complexity:
The space complexity is O(1), as we only use two variables to store the maximum sums for the last two houses, instead of storing the entire dynamic programming table.
Example Walkthrough:
For the input nums = [2, 7, 9, 3, 1]:
Initialize prev1 = 0 and prev2 = 0.
For the first house (2), current = max(0, 0 + 2) = 2, so prev1 = 0, prev2 = 2.
For the second house (7), current = max(2, 0 + 7) = 7, so prev1 = 2, prev2 = 7.
For the third house (9), current = max(7, 2 + 9) = 11, so prev1 = 7, prev2 = 11.
For the fourth house (3), current = max(11, 7 + 3) = 11, so prev1 = 11, prev2 = 11.
For the fifth house (1), current = max(11, 11 + 1) = 12, so prev1 = 11, prev2 = 12.
The maximum money that can be robbed is stored in prev2, which is 12.
Conclusion:
This solution efficiently calculates the maximum amount of money that can be robbed, ensuring that no two adjacent houses are robbed, and it does so in O(n) time with O(1) space complexity
 * 
 */



public class HouseRobber198 {
    public int rob(int[] nums) {
        // Handle edge cases where the input array is empty or has only one element
        if (nums == null || nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        
        // Initialize variables for the first two houses
        int prev1 = 0; // dp[i-2]
        int prev2 = 0; // dp[i-1]
        
        // Loop through each house
        for (int num : nums) {
            // Calculate the maximum money we can rob up to the current house
            int current = Math.max(prev2, prev1 + num);
            
            // Update prev1 and prev2 for the next iteration
            prev1 = prev2;
            prev2 = current;
        }
        
        // prev2 contains the maximum money we can rob after considering all houses
        return prev2;
    }

    public static void main(String[] args) {
        HouseRobber198 solution = new HouseRobber198();
        
        // Test case 1
        int[] nums1 = {2, 7, 9, 3, 1};
        System.out.println(solution.rob(nums1));  // Output: 12
        
        // Test case 2
        int[] nums2 = {1, 2, 3, 1};
        System.out.println(solution.rob(nums2));  // Output: 4
    }
}
