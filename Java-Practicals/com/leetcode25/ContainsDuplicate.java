package com.leetcode25;

/**
 * The Contains Duplicate problem on LeetCode asks you to determine if a given array contains any duplicate elements. If any value appears at least twice in the array, you should return true; otherwise, return false.
Problem:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Optimal Solution:
The optimal solution to this problem uses a HashSet. A HashSet allows for efficient lookup and insertion operations, with an average time complexity of O(1). This makes the solution O(n) in time complexity, where n is the number of elements in the array.
Approach:
Traverse the array and insert each element into a HashSet.
If an element already exists in the HashSet during the traversal, it means that element is a duplicate, and you can return true immediately.
If you finish traversing the array without encountering any duplicates, return false.
 * 
 * Explanation:
HashSet:
A HashSet is used to store elements that we have encountered so far. It automatically handles duplicates for us, ensuring that each element is unique.
Traversal:
We iterate through the nums array.
For each element, we check if it already exists in the HashSet:
If it exists, that means we have found a duplicate, so we return true immediately.
If it doesn't exist, we add it to the set and continue.
Final Answer:
If we complete the loop without encountering any duplicates, we return false.
Time Complexity:
Time Complexity: O(n), where n is the length of the array. Each insertion and lookup operation on the HashSet is O(1) on average.
Space Complexity: O(n), because in the worst case, we may need to store all n elements in the HashSet if there are no duplicates.
 
 */


import java.util.HashSet;

/**
 * 
 */
public class ContainsDuplicate {

    public boolean containsDuplicate(int[] nums) {
        // Create a HashSet to store the elements we have encountered
        HashSet<Integer> set = new HashSet<>();
        
        // Traverse through the array
        for (int num : nums) {
            // If the element already exists in the set, return true
            if (set.contains(num)) {
                return true;
            }
            // Otherwise, add the element to the set
            set.add(num);
        }
        
        // If no duplicates were found, return false
        return false;
    }

    public static void main(String[] args) {
        ContainsDuplicate solution = new ContainsDuplicate();
        
        // Test the solution with an example
        int[] nums = {1, 2, 3, 1};
        boolean result = solution.containsDuplicate(nums);
        
        // Print the result
        System.out.println("Contains Duplicate: " + result);
    }
}
