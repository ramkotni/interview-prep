package com.leetcode25;

/**
 * 
 * Problem:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Solution:
A common and efficient approach to solve the Two Sum problem is to use a HashMap. This allows us to store the numbers we've seen and check if the complement of the current number (i.e., target - current number) is already in the map. This results in a time complexity of O(n), where n is the number of elements in the array.
 * 
 * 
 * Explanation:
HashMap: We use a HashMap<Integer, Integer> to store the numbers we’ve encountered and their corresponding indices.

Loop: We loop through the nums array. For each number nums[i], we calculate its complement (target - nums[i]).

Check Complement: If the complement is already in the map, it means we've previously encountered a number that can sum with the current number to give the target. We then return the indices of the current number and the complement.

Add Current Number: If the complement is not found, we add the current number and its index to the map for future reference.

Time Complexity: This approach runs in O(n) time, where n is the length of the array. The space complexity is also O(n) due to the space required by the HashMap.
 * 
 * 
 */



import java.util.HashMap;

public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        // Create a HashMap to store the number and its index
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // Loop through the array
        for (int i = 0; i < nums.length; i++) {
            // Calculate the complement (the number we need to reach the target)
            int complement = target - nums[i];
            
            // If the complement exists in the map, return the indices
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            
            // Otherwise, store the current number and its index in the map
            map.put(nums[i], i);
        }
        
        // Return an empty array if no solution is found (though the problem guarantees one solution)
        return new int[] {};
    }

    public static void main(String[] args) {
        TwoSum solution = new TwoSum();
        
        // Test the solution with an example
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = solution.twoSum(nums, target);
        
        // Print the result
        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]");
    }
}
