package com.leetcode25;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Problem Description:
Given an integer array nums and an integer target, find all unique quadruplets in the array that sum up to the target.
Example:
Input:
nums = [1, 0, -1, 0, -2, 2]
target = 0
Output:
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
Approach:
The idea behind solving the 4Sum problem is similar to 3Sum, but we need to add an additional layer for the 4th number. The general approach will be:
Sort the Array: Sorting helps efficiently avoid duplicate quadruplets and allows us to use the two-pointer technique.
Fix the First Two Numbers: We can fix the first two numbers in the quadruplet and then use the two-pointer technique to find the remaining two numbers that sum up to the target minus the sum of the fixed numbers.
Use Two Pointers: After fixing the first two numbers, the remaining problem is reduced to a 2Sum problem, which can be solved efficiently using two pointers.
Avoid Duplicates: To avoid duplicates, we skip over the same values for both the first two numbers and the second two numbers.
 * 
 * 
 * Explanation:
Sort the Array:
Sorting the array helps to efficiently find potential quadruplets and ensures that we can skip duplicate values.
Fix the First Two Numbers:
The outer loops (i and j) iterate over the array to fix the first two numbers in the quadruplet.
We ensure that we skip over duplicate values by checking if nums[i] == nums[i - 1] for the first loop and nums[j] == nums[j - 1] for the second loop.
Use Two Pointers for the Remaining Sum:
After fixing the first two numbers, the problem reduces to finding two numbers that sum up to the target minus the sum of the fixed numbers.
We use two pointers (left and right) to find these two numbers. If their sum equals the target, we have found a valid quadruplet, and we add it to the result.
Skip Duplicates:
After finding a valid quadruplet, we skip over any duplicate values for the left and right pointers by checking if nums[left] == nums[left + 1] and nums[right] == nums[right - 1].
Return the Result:
After processing all possible combinations, the result list will contain all unique quadruplets.
Time and Space Complexity:
Time Complexity: O(n³), where n is the length of the input array. The algorithm involves two nested loops (i and j) that each iterate through the array, and for each pair of numbers, we perform a two-pointer search (left and right).
The overall time complexity is dominated by the nested loops and the two-pointer traversal, resulting in O(n³).
Space Complexity: O(k), where k is the number of valid quadruplets found. The space complexity is due to the result list storing the quadruplets.
Example Walkthrough:
Input:
nums = [1, 0, -1, 0, -2, 2], target = 0
Step 1: Sort the array: [-2, -1, 0, 0, 1, 2].
Step 2: Iterate with i = 0 (nums[i] = -2):
Iterate with j = 1 (nums[j] = -1):
Left pointer at index 2 (nums[left] = 0), right pointer at index 5 (nums[right] = 2).
The sum is -2 + (-1) + 0 + 2 = -1, which is less than zero. Move the left pointer right.
The sum is -2 + (-1) + 1 + 2 = 0, which is a valid quadruplet: [-2, -1, 1, 2].
Skip duplicates for the left and right pointers, then move the pointers inward.
Continue with j = 2 and further iterations to find the remaining valid quadruplets.
Output:
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
Final Thoughts:
The 4Sum problem is an extension of the 3Sum problem and is solved efficiently using the two-pointer technique in conjunction with fixing the first two numbers. By sorting the array and skipping duplicates, we can find all unique quadruplets that sum up to the target.
 * 
 */


public class FourSum18 {

    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();

        // Sort the array to use two-pointer technique
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 3; i++) {
            // Skip duplicates for the first number
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            for (int j = i + 1; j < nums.length - 2; j++) {
                // Skip duplicates for the second number
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                int left = j + 1;  // Left pointer
                int right = nums.length - 1;  // Right pointer

                while (left < right) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        // Skip duplicates for the third number (left pointer)
                        while (left < right && nums[left] == nums[left + 1]) {
                            left++;
                        }

                        // Skip duplicates for the fourth number (right pointer)
                        while (left < right && nums[right] == nums[right - 1]) {
                            right--;
                        }

                        // Move the pointers after processing a valid quadruplet
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;  // Increase the sum by moving left pointer to the right
                    } else {
                        right--;  // Decrease the sum by moving right pointer to the left
                    }
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        FourSum18 solution = new FourSum18();

        // Test case
        int[] nums = {1, 0, -1, 0, -2, 2};
        int target = 0;
        List<List<Integer>> quadruplets = solution.fourSum(nums, target);

        // Print the result
        System.out.println(quadruplets);  // Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    }
}
