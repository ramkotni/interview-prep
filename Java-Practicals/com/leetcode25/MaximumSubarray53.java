package com.leetcode25;

/**
 * LeetCode Problem 53 is the Maximum Subarray problem, where you are given an integer array nums, and you need to find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.
Problem:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Approach:
The optimal solution uses Kadane's Algorithm, which runs in O(n) time complexity and uses O(1) space. The key idea is to maintain a running sum of the current subarray (currentSum) and the maximum sum encountered so far (maxSum). If the running sum becomes negative, it's reset to zero since a negative sum would reduce the overall maximum sum.
Kadane's Algorithm:
Traverse through the array and maintain the sum of the current subarray (currentSum).
For each element, decide whether to add it to the current subarray or start a new subarray from the current element.
The maximum sum is updated at each step.
Explanation:
Initialization:
currentSum: Keeps track of the sum of the current subarray.
maxSum: Stores the maximum sum encountered so far.
Iterating through the array:
For each element nums[i], we decide whether to:
Add the current element nums[i] to the existing subarray (currentSum + nums[i]), or
Start a new subarray starting from the current element nums[i] (this happens when nums[i] alone is larger than the sum of the subarray up to this point).
Update maxSum whenever currentSum exceeds the previously recorded maxSum.
Returning the result:
After processing all elements, maxSum will hold the largest sum of any contiguous subarray.
Time and Space Complexity:
Time Complexity: O(n), where n is the number of elements in the array. We only loop through the array once.
Space Complexity: O(1), since we are only using a constant amount of extra space.
Example Walkthrough:
For the input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Start with currentSum = -2 and maxSum = -2.
Move to nums[1] = 1:
currentSum = Math.max(1, -2 + 1) = 1
maxSum = Math.max(-2, 1) = 1
Move to nums[2] = -3:
currentSum = Math.max(-3, 1 + (-3)) = -2
maxSum = Math.max(1, -2) = 1
Move to nums[3] = 4:
currentSum = Math.max(4, -2 + 4) = 4
maxSum = Math.max(1, 4) = 4
Move to nums[4] = -1:
currentSum = Math.max(-1, 4 + (-1)) = 3
maxSum = Math.max(4, 3) = 4
Move to nums[5] = 2:
currentSum = Math.max(2, 3 + 2) = 5
maxSum = Math.max(4, 5) = 5
Move to nums[6] = 1:
currentSum = Math.max(1, 5 + 1) = 6
maxSum = Math.max(5, 6) = 6
Move to nums[7] = -5:
currentSum = Math.max(-5, 6 + (-5)) = 1
maxSum = Math.max(6, 1) = 6
Move to nums[8] = 4:
currentSum = Math.max(4, 1 + 4) = 5
maxSum = Math.max(6, 5) = 6
Thus, the maximum subarray sum is 6.
Maximum Subarray Sum: 6
This solution efficiently finds the maximum subarray sum in O(n) time, and is optimal in terms of both time and space.
 * 
 */



public class MaximumSubarray53 {

    public int maxSubArray(int[] nums) {
        // Initialize the variables
        int currentSum = nums[0];  // The sum of the current subarray
        int maxSum = nums[0];      // The maximum sum found so far

        // Start iterating from the second element
        for (int i = 1; i < nums.length; i++) {
            // Update the current sum: either start a new subarray or extend the current one
            currentSum = Math.max(nums[i], currentSum + nums[i]);

            // Update the maximum sum found so far
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }

    public static void main(String[] args) {
        MaximumSubarray53 solution = new MaximumSubarray53();
        
        // Test the solution with an example
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int result = solution.maxSubArray(nums);
        
        // Print the result
        System.out.println("Maximum Subarray Sum: " + result);
    }
}
