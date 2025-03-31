package com.leetcode25;

/**
 * The problem ""Find First and Last Position of Element in Sorted Array"" (LeetCode #34) asks you to find the first and last positions of a given target value in a sorted array. If the target value is not found in the array, return [-1, -1].
Problem Statement:
Given an integer array nums sorted in non-decreasing order, find the starting and ending position of a given target value. Your algorithm must run in O(log n) time complexity.
Approach:
Since the array is sorted, we can use binary search to find the first and last positions of the target element. Binary search allows us to efficiently find the target element in O(log n) time.
Binary Search to Find the First Position:
Perform a binary search to find the leftmost (first) occurrence of the target. Once we find the target, continue searching in the left half to ensure we find the first occurrence.
Binary Search to Find the Last Position:
Perform a binary search to find the rightmost (last) occurrence of the target. Once we find the target, continue searching in the right half to ensure we find the last occurrence.
Plan:
Use binary search to find the first and last position of the target.
First binary search will help us find the first position.
Second binary search will help us find the last position.
Time Complexity:
O(log n) for both finding the first and last position because each binary search operation runs in logarithmic time.
Space Complexity:
O(1), as we are using only a constant amount of extra space.
 * 
 * Explanation of the Code:
searchRange Method:
We initialize a result array with [-1, -1], which will be returned if the target is not found.
First, we use the binarySearch method to find the first position of the target. If the first position is -1 (target not found), we return [-1, -1].
If the first position is found, we proceed to find the last position using the same binarySearch method but with the findFirst flag set to false.
binarySearch Method:
This method performs a standard binary search, but it checks if we are looking for the first or last occurrence of the target.
If we find the target, we check whether we are finding the first position (findFirst is true) or the last position (findFirst is false):
First position: If we find the target, continue searching in the left half (high = mid - 1).
Last position: If we find the target, continue searching in the right half (low = mid + 1).
The method returns the index of the found position or -1 if the target is not found.
Example Walkthrough:
Example 1:
plaintext
Copy
nums = [5, 7, 7, 8, 8, 10], target = 8
First position:
Start with low = 0, high = 5, mid = 2.
The element at mid is 7, which is less than 8, so we search to the right (low = 3).
Now mid = 4, and the element at mid is 8.
We continue searching to the left (high = 3) to find the first occurrence.
We find that nums[3] = 8, so the first position is 3.
Last position:
Start with low = 0, high = 5, mid = 2.
The element at mid is 7, which is less than 8, so we search to the right (low = 3).
Now mid = 4, and the element at mid is 8.
We continue searching to the right (low = 5) to find the last occurrence.
We find that nums[4] = 8, so the last position is 4.
Output:
plaintext
Copy
First and Last Position: [3, 4]
Example 2:
plaintext
Copy
nums = [5, 7, 7, 8, 8, 10], target = 6
Since 6 is not found in the array, both the first and last positions remain -1.
Output:
plaintext
Copy
First and Last Position: [-1, -1]
Time and Space Complexity:
Time Complexity:
The binary search runs in O(log n) time to find both the first and last position, so the total time complexity is O(log n).
Space Complexity:
O(1), since we are only using a constant amount of extra space (no extra data structures other than the result array).
This solution efficiently solves the problem in logarithmic time, which is optimal for a sorted array.
 * 
 */


public class FindFirstAndLastPosition34 {
    
    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1, -1};
        
        // Find the first position using binary search
        result[0] = binarySearch(nums, target, true);
        
        // If the target is not found, return [-1, -1]
        if (result[0] == -1) {
            return result;
        }
        
        // Find the last position using binary search
        result[1] = binarySearch(nums, target, false);
        
        return result;
    }
    
    // Binary search to find the first or last position
    private int binarySearch(int[] nums, int target, boolean findFirst) {
        int low = 0, high = nums.length - 1;
        int result = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                result = mid;
                // If we're finding the first position, move left
                if (findFirst) {
                    high = mid - 1;
                }
                // If we're finding the last position, move right
                else {
                    low = mid + 1;
                }
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        FindFirstAndLastPosition34 solution = new FindFirstAndLastPosition34();
        
        // Example 1
        int[] nums = {5, 7, 7, 8, 8, 10};
        int target = 8;
        int[] result = solution.searchRange(nums, target);
        System.out.println("First and Last Position: [" + result[0] + ", " + result[1] + "]"); // Output: [3, 4]
        
        // Example 2
        int[] nums2 = {5, 7, 7, 8, 8, 10};
        int target2 = 6;
        int[] result2 = solution.searchRange(nums2, target2);
        System.out.println("First and Last Position: [" + result2[0] + ", " + result2[1] + "]"); // Output: [-1, -1]
    }
}
