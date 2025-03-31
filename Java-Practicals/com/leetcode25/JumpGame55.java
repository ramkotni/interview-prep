package com.leetcode25;
/**
 * The Jump Game problem (LeetCode #55) asks whether you can reach the last index of an array starting from the first index, given that each element in the array represents the maximum number of indices you can jump forward from that position.
Problem Statement:
Given an array of non-negative integers nums, where each element represents the maximum number of indices you can move forward from that position. Starting from the first index, determine if you can reach the last index.
Approach:
We can solve this problem using a greedy algorithm approach. The key observation is that we do not need to explore every jump option; instead, we can track the furthest index we can reach at each point.
We will maintain a variable maxReach to keep track of the farthest index we can reach at any point.
Starting from the first index, we check whether we can move forward by updating maxReach based on the value of nums[i].
If at any point, maxReach becomes greater than or equal to the last index, we can reach the last index and return true.
If we encounter an index i where maxReach is less than or equal to i, it means we're stuck and can't proceed further, so we return false.
Plan:
Initialize maxReach as 0.
Iterate through each index i in the array:
If i is greater than maxReach, return false (because we can't reach this index).
Update maxReach as the maximum of maxReach and i + nums[i].
If maxReach reaches or exceeds the last index at any point, return true.
If the loop ends and we haven't reached the last index, return false.
Time Complexity:
O(n), where n is the length of the array. We only need to pass through the array once.
Space Complexity:
O(1), as we only use a few extra variables for the computation

Explanation of the Code:
canJump Method:
We initialize maxReach to 0, representing the farthest index we can reach starting from the first index.
As we iterate through the array:
If the current index i is greater than maxReach, we return false because we can't reach this index.
We update maxReach by taking the maximum of maxReach and i + nums[i] (the farthest index we can reach from index i).
If maxReach reaches or exceeds the last index (nums.length - 1), we return true, indicating that we can reach the last index.
If the loop completes and we haven't reached the last index, we return false.
main Method:
We test the function with two examples:
Example 1: nums1 = [2, 3, 1, 1, 4] → Output is true, because we can reach the last index.
Example 2: nums2 = [3, 2, 1, 0, 4] → Output is false, because we can't reach the last index.
Example Walkthrough:
Example 1:
plaintext
Copy
nums = [2, 3, 1, 1, 4]
Start with maxReach = 0.
At i = 0, nums[0] = 2, so maxReach = max(0, 0 + 2) = 2. We can reach index 2.
At i = 1, nums[1] = 3, so maxReach = max(2, 1 + 3) = 4. We can reach index 4, which is the last index.
Since maxReach reaches or exceeds the last index, return true.
Example 2:
plaintext
Copy
nums = [3, 2, 1, 0, 4]
Start with maxReach = 0.
At i = 0, nums[0] = 3, so maxReach = max(0, 0 + 3) = 3. We can reach index 3.
At i = 1, nums[1] = 2, so maxReach = max(3, 1 + 2) = 3. We are still stuck at index 3.
At i = 2, nums[2] = 1, so maxReach = max(3, 2 + 1) = 3. We are still stuck at index 3.
At i = 3, nums[3] = 0, so maxReach = max(3, 3 + 0) = 3. We cannot progress further.
Since i > maxReach, return false.
Output:
plaintext
Copy
true
false
Time and Space Complexity:
Time Complexity:
O(n), where n is the length of the array. We only loop through the array once.
Space Complexity:
O(1), as we only use a constant amount of extra space for maxReach and a few other variables.
This greedy approach solves the problem efficiently and is optimal for this scenario.



 * 
 * 
 */




public class JumpGame55 {
    
    public boolean canJump(int[] nums) {
        int maxReach = 0; // Maximum index we can reach
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            // If we are at an index that is not reachable, return false
            if (i > maxReach) {
                return false;
            }
            
            // Update the maxReach at each step
            maxReach = Math.max(maxReach, i + nums[i]);
            
            // If maxReach reaches or exceeds the last index, we can jump to the last index
            if (maxReach >= nums.length - 1) {
                return true;
            }
        }
        
        return false;
    }

    public static void main(String[] args) {
        JumpGame55 solution = new JumpGame55();
        
        // Example 1
        int[] nums1 = {2, 3, 1, 1, 4};
        System.out.println(solution.canJump(nums1)); // Output: true
        
        // Example 2
        int[] nums2 = {3, 2, 1, 0, 4};
        System.out.println(solution.canJump(nums2)); // Output: false
    }
}
