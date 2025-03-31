package com.leetcode25;

/**
 * 
 * The Search in Rotated Sorted Array problem (LeetCode #33) involves searching for a target value in a rotated version of a sorted array. The array was originally sorted in ascending order, but it has been rotated at an unknown pivot. The goal is to find the target value's index in the array, or return -1 if the target is not found.
Problem Description:
You are given an integer array nums that is rotated at some pivot, and an integer target. Write a function to return the index of target in the array, or -1 if it is not present.
Key Points:
The array is sorted in ascending order before being rotated.
The rotation means that part of the array is in increasing order from the start, and the other part is in increasing order from the end.
Approach:
We can solve this problem using binary search with the following steps:
Identify the Pivot: The rotation point divides the array into two sorted subarrays. One of these subarrays will always be sorted in ascending order. The target will either be in the left sorted part or the right sorted part.
Binary Search: Instead of a regular binary search, we need to modify it to check which part of the array is sorted:
If nums[mid] is greater than nums[left], it means the left half is sorted, and the target must lie in this sorted part if nums[left] <= target < nums[mid].
If nums[mid] is less than nums[left], it means the right half is sorted, and the target must lie in this sorted part if nums[mid] < target <= nums[right].
Move the Pointers: Depending on where the target lies (either in the left or right sorted part), adjust the left or right pointer accordingly.
 * 
 * Explanation:
Initialization:
We initialize two pointers: left at the start of the array and right at the end of the array.
Binary Search Loop:
Condition: As long as left <= right, we perform binary search. Calculate mid as the middle index.
Target Found: If nums[mid] == target, return the index mid.
Determine Sorted Half:
If nums[left] <= nums[mid], the left part is sorted. We check if the target lies in the range nums[left] <= target < nums[mid]. If it does, we move right to mid - 1 to focus on the left half. Otherwise, move left to mid + 1 to focus on the right half.
If nums[left] > nums[mid], the right part is sorted. We check if the target lies in the range nums[mid] < target <= nums[right]. If it does, we move left to mid + 1 to focus on the right half. Otherwise, move right to mid - 1 to focus on the left half.
Return:
If we exit the loop without finding the target, we return -1 indicating that the target is not in the array.
Time Complexity:
O(log n): The time complexity is O(log n) because we are using binary search, which reduces the search space by half in each iteration.
Space Complexity:
O(1): The space complexity is O(1) because we are using only a few extra variables (left, right, and mid).
Example Walkthrough:
Example 1:
Input:
nums = [4, 5, 6, 7, 0, 1, 2], target = 0
First iteration:
left = 0, right = 6, mid = 3 (nums[mid] = 7)
Since nums[left] <= nums[mid] (4 <= 7), the left part is sorted.
The target 0 is not in the range [4, 7], so we move to the right part by setting left = 4.
Second iteration:
left = 4, right = 6, mid = 5 (nums[mid] = 1)
Since nums[left] <= nums[mid] (0 <= 1), the left part is sorted.
The target 0 is in the range [0, 1], so we move to the left part by setting right = 4.
Third iteration:
left = 4, right = 4, mid = 4 (nums[mid] = 0)
nums[mid] == target, so we return 4.
Output:
4
Example 2:
Input:
nums = [4, 5, 6, 7, 0, 1, 2], target = 3
First iteration:
left = 0, right = 6, mid = 3 (nums[mid] = 7)
The target 3 is not in the range [4, 7], so we move to the right part by setting left = 4.
Second iteration:
left = 4, right = 6, mid = 5 (nums[mid] = 1)
The target 3 is not in the range [0, 1], so we move to the right part by setting left = 6.
Third iteration:
left = 6, right = 6, mid = 6 (nums[mid] = 2)
The target 3 is not in the range [2, 2], so we move to the right part by setting left = 7.
Since left > right, we exit the loop and return -1.
Output:
-1
Final Thoughts:
The algorithm efficiently searches for the target in a rotated sorted array using binary search, achieving a time complexity of O(log n).
The key idea is to determine which half of the array is sorted and adjust the search range accordingly.

 * 
 */



public class SearchInRotatedSortedArray33 {

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Check if the target is found
            if (nums[mid] == target) {
                return mid;
            }

            // Determine which part is sorted
            if (nums[left] <= nums[mid]) {
                // Left part is sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1; // Target is in the left part
                } else {
                    left = mid + 1; // Target is in the right part
                }
            } else {
                // Right part is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1; // Target is in the right part
                } else {
                    right = mid - 1; // Target is in the left part
                }
            }
        }

        return -1; // Target not found
    }

    public static void main(String[] args) {
        SearchInRotatedSortedArray33 solution = new SearchInRotatedSortedArray33();

        // Test case
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        int target = 0;
        System.out.println(solution.search(nums, target));  // Output: 4

        target = 3;
        System.out.println(solution.search(nums, target));  // Output: -1
    }
}
