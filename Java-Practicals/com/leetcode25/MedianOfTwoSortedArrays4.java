package com.leetcode25;

/**
 * The Median of Two Sorted Arrays problem (LeetCode #4) asks you to find the median of two sorted arrays. The challenge here is to do it in an efficient way with a time complexity of O(log(min(n, m))), where n and m are the sizes of the two arrays.

Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example:

java
Copy
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
Explanation: The merged array is [1, 2, 3] and the median is 2.
java
Copy
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
Explanation: The merged array is [1, 2, 3, 4] and the median is (2 + 3) / 2 = 2.5.
Approach:
The naive approach would be to merge the two sorted arrays and then find the median, but this would take O(n + m) time. Since the problem asks for an optimal solution, we can utilize binary search to find the median in O(log(min(n, m))) time.

Key Insights:
The median of an array is the middle element (if the array has an odd number of elements) or the average of the two middle elements (if the array has an even number of elements).

If we combine both arrays and partition them in such a way that the left side has the same number of elements (or one more element) as the right side, the median will be the average of the maximum element on the left side and the minimum element on the right side.

We will perform binary search on the smaller array to find the correct partitioning that satisfies the condition for the median.

Steps:
Partitioning the Arrays:

We partition the two arrays such that the left part has k elements and the right part has k elements, where k = (m + n + 1) / 2. This ensures that if m + n is odd, the left part will have one extra element than the right part.

Binary Search:

We use binary search on the smaller array (nums1 or nums2).

In each iteration, calculate the partition point for both arrays. The partition divides each array into two parts: one part contains the smaller half of the combined arrays and the other part contains the larger half.

Conditions for Correct Partition:

The largest element in the left partition of both arrays should be smaller than or equal to the smallest element in the right partition of both arrays.

Calculate the Median:

If the combined length of both arrays is odd, the median is the maximum element from the left partition.

If the combined length is even, the median is the average of the maximum element from the left partition and the minimum element from the right partition.
 * 
 * Explanation of the Code:
Ensure nums1 is the smaller array: We swap the arrays if nums1 is larger than nums2. This is done to minimize the size of the array we perform binary search on, optimizing the time complexity.

Binary Search:

The binary search runs on the smaller array (nums1), and we calculate the partition indices (partition1 and partition2) for both arrays.

partition1 is the partition index for nums1, and partition2 is calculated as the complement of partition1 to ensure the left half of the combined arrays has exactly half of the total elements.

Max and Min Calculations:

For both arrays, we calculate the maximum element on the left of the partition (maxLeft1 and maxLeft2) and the minimum element on the right of the partition (minRight1 and minRight2).

Special handling is done when the partition is at the boundary of the array (i.e., the left partition is empty or the right partition is empty), in which case we use Integer.MIN_VALUE and Integer.MAX_VALUE to avoid out-of-bounds errors.

Partition Validity Check:

The partition is valid if the maximum element on the left of nums1 and nums2 is less than or equal to the minimum element on the right of the other array.

Median Calculation:

If the total length of the combined arrays is odd, the median is the maximum element of the left partitions.

If the total length is even, the median is the average of the maximum element from the left partitions and the minimum element from the right partitions.

Time Complexity:
O(log(min(n, m))): We perform a binary search on the smaller of the two arrays, which results in logarithmic time complexity.

Space Complexity:
O(1): We use only a constant amount of extra space, aside from the input arrays.

Example Walkthrough:
Example 1:
nums1 = [1, 3], nums2 = [2]

partition1 = 1, partition2 = 1

maxLeft1 = 1, minRight1 = 3

maxLeft2 = 2, minRight2 = Integer.MAX_VALUE

Since maxLeft1 <= minRight2 and maxLeft2 <= minRight1, the partitions are valid.

Since the total number of elements (3) is odd, the median is the larger of maxLeft1 and maxLeft2, which is 2.

Example 2:
nums1 = [1, 2], nums2 = [3, 4]

partition1 = 1, partition2 = 1

maxLeft1 = 1, minRight1 = 2

maxLeft2 = 3, minRight2 = 4

Since the total number of elements (4) is even, the median is the average of max(maxLeft1, maxLeft2) and min(minRight1, minRight2), which is (2 + 3) / 2 = 2.5.

This approach efficiently finds the median in O(log(min(n, m))) time, making it suitable for large inputs.
 * 
 * 
 * 
 */




public class MedianOfTwoSortedArrays4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        
        int m = nums1.length;
        int n = nums2.length;
        int left = 0, right = m;
        
        while (left <= right) {
            int partition1 = (left + right) / 2;
            int partition2 = (m + n + 1) / 2 - partition1;
            
            // Edge cases: if partition is at the edge of the array, use -∞ or ∞
            int maxLeft1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? Integer.MAX_VALUE : nums1[partition1];
            
            int maxLeft2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? Integer.MAX_VALUE : nums2[partition2];
            
            // Check if we found the correct partition
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // Odd combined length, return the max of the left partition
                if ((m + n) % 2 == 1) {
                    return Math.max(maxLeft1, maxLeft2);
                } else {
                    // Even combined length, return the average of the max left and min right
                    return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0;
                }
            } else if (maxLeft1 > minRight2) {
                // Move the partition1 left
                right = partition1 - 1;
            } else {
                // Move the partition1 right
                left = partition1 + 1;
            }
        }
        
        // If we reach here, the input arrays are not sorted properly or empty
        throw new IllegalArgumentException("Input arrays are not sorted correctly");
    }

    public static void main(String[] args) {
        MedianOfTwoSortedArrays4 solution = new MedianOfTwoSortedArrays4();
        
        // Example 1
        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        System.out.println("Median: " + solution.findMedianSortedArrays(nums1, nums2));  // Output: 2.0
        
        // Example 2
       // int[] nums1 = {1, 2};
        //int[] nums2 = {3, 4};
        System.out.println("Median: " + solution.findMedianSortedArrays(nums1, nums2));  // Output: 2.5
    }
}
