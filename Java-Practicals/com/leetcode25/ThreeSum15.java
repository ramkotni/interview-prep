package com.leetcode25;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Problem Description:
Given an integer array nums, find all unique triplets in the array that sum up to zero. Your answer should not contain duplicate triplets.
Example:
Input:
nums = [-1, 0, 1, 2, -1, -4]
Output:
[[-1, -1, 2], [-1, 0, 1]]
Approach:
To solve the 3Sum problem efficiently, we can use the two-pointer technique in conjunction with sorting:
Sort the Array: Sort the input array. This allows us to use the two-pointer technique to find pairs that sum up to a given target.
Iterate with a Fixed Element: Fix one element nums[i], and then find two other elements nums[left] and nums[right] such that their sum is equal to -nums[i] (this will give a sum of zero).
Two-pointer Technique:
Initialize two pointers, one (left) just after the fixed element and the other (right) at the end of the array.
Calculate the sum of nums[i] + nums[left] + nums[right].
If the sum is zero, it’s a valid triplet.
If the sum is less than zero, move the left pointer right to increase the sum.
If the sum is greater than zero, move the right pointer left to decrease the sum.
Avoid Duplicates:
Skip over duplicate elements for the fixed element (nums[i]).
Skip over duplicate elements for the left and right pointers.

Explanation:
Sorting: First, we sort the array. This helps us in efficiently using the two-pointer technique and in handling duplicate triplets.
Iterating with the First Element: We iterate over the array, treating each element as a potential first element of a triplet. For each element nums[i], we attempt to find two other numbers that sum up to -nums[i].
Two-pointer Search:
For each nums[i], we place one pointer at i + 1 (left) and the other at the end of the array (right).
We calculate the sum of the three numbers. If the sum is zero, it’s a valid triplet, and we add it to the result.
If the sum is less than zero, we need a larger sum, so we move the left pointer right (left++).
If the sum is greater than zero, we need a smaller sum, so we move the right pointer left (right--).
Avoiding Duplicates:
After finding a valid triplet, we skip over any duplicate values for the left pointer and right pointer by checking if the next value is the same as the current one.
We also skip duplicate values for the fixed element nums[i] by checking if nums[i] is the same as nums[i - 1] when i > 0.
Return the Result: The result is a list of triplets that sum up to zero, and no duplicates are included.
Time and Space Complexity:
Time Complexity: O(n²), where n is the length of the input array. Sorting takes O(n log n), and the two-pointer search runs in O(n) for each element in the array, resulting in a total time complexity of O(n²).
Space Complexity: O(k), where k is the number of valid triplets found. The space complexity comes from the result list that stores the triplets.
Example Walkthrough:
Input:
nums = [-1, 0, 1, 2, -1, -4]
Step 1: Sort the array: [-4, -1, -1, 0, 1, 2].
Step 2: Iterate with nums[i] = -4:
Left pointer at index 1 (-1), right pointer at index 5 (2).
The sum is -4 + (-1) + 2 = -3, which is less than zero. Move the left pointer right.
Step 3: Iterate with nums[i] = -1:
Left pointer at index 2 (-1), right pointer at index 5 (2).
The sum is -1 + (-1) + 2 = 0, which is a valid triplet. Add it to the result: [-1, -1, 2].
Skip duplicates for the left and right pointers.
Step 4: Continue to find other valid triplets, resulting in: [-1, 0, 1].
Output:
[[-1, -1, 2], [-1, 0, 1]]
Final Thoughts:
This solution efficiently finds all unique triplets that sum up to zero using sorting and the two-pointer technique. The main challenge is managing duplicate triplets by skipping over repeated elements during the iteration.

 * 
 * 
 */

public class ThreeSum15 {

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        // Sort the array to use two-pointer technique
        Arrays.sort(nums);

        // Iterate through the array
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate values for the fixed element nums[i]
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;  // Left pointer
            int right = nums.length - 1;  // Right pointer

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    // Found a triplet
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // Skip duplicate values for the left pointer
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }

                    // Skip duplicate values for the right pointer
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    // Move both pointers after processing a valid triplet
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;  // We need a larger sum, move left pointer to the right
                } else {
                    right--;  // We need a smaller sum, move right pointer to the left
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        ThreeSum15 solution = new ThreeSum15();
        
        // Test case
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> triplets = solution.threeSum(nums);
        
        // Print the result
        System.out.println(triplets);  // Output: [[-1, -1, 2], [-1, 0, 1]]
    }
}
