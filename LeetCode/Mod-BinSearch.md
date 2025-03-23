Modified Binary Search

The Modified Binary Search pattern adapts binary search to solve a wider range of problems, such as finding elements in rotated sorted arrays.

Use this pattern for problems involving sorted or rotated arrays where you need to find a specific element.

Sample Problem:
Find an element in a rotated sorted array.

Example:

Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0

Output: 4

Explanation:
Perform binary search with an additional check to determine which half of the array is sorted.

We then check if the target is within the range of the sorted half.

If it is, we search that half; otherwise, we search the other half.

LeetCode Problems:
Search in Rotated Sorted Array (LeetCode #33)

Find Minimum in Rotated Sorted Array (LeetCode #153)

Search a 2D Matrix II (LeetCode #240)

The Modified Binary Search pattern is an extension of the standard binary search, adapted to handle problems where the array might be rotated or where we're working with multi-dimensional arrays.

Below are solutions for the Modified Binary Search pattern problems that involve rotated arrays and 2D matrix searches.

Problem 1: Search in Rotated Sorted Array (LeetCode #33)
Problem Statement: Given a rotated sorted array, find the target element. You may assume no duplicates exist in the array.

Approach:
Binary Search: The key observation is that the array is sorted but rotated. We can perform binary search on this rotated array by identifying which half of the array is sorted.

Identify Sorted Half: At each step of binary search, check if the left half or the right half of the array is sorted. Then, determine if the target is within the sorted half. If it is, narrow the search to that half. Otherwise, search the other half.

Code Implementation:
java
Copy
public class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Check if the target is found
            if (nums[mid] == target) {
                return mid;
            }

            // Check if the left half is sorted
            if (nums[left] <= nums[mid]) {
                // Target is in the left half
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        
        return -1;  // Target not found
    }
}
Explanation:
Binary Search: We perform the binary search as usual, but at each step, we check which half of the array is sorted.

Check Sorted Half:

If the left half is sorted (i.e., nums[left] <= nums[mid]), check if the target lies within that half. If so, adjust the search boundaries accordingly.

Otherwise, check the right half and adjust the boundaries similarly.

Return: If the target is found, return its index. If the loop completes without finding the target, return -1.

Time Complexity:
O(log n) where n is the length of the array. This is because we are halving the search space at each step.

Example Input and Output:
Input:

java
Copy
nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output:

java
Copy
4
Problem 2: Find Minimum in Rotated Sorted Array (LeetCode #153)
Problem Statement: Find the minimum element in a rotated sorted array without duplicates.

Approach:
Binary Search: The key observation is that the minimum element in a rotated sorted array is the element where the rotation happens.

Identify Pivot: Perform binary search and check the middle element. If the middle element is greater than the rightmost element, the minimum must lie to the right; otherwise, the minimum lies to the left.

Code Implementation:
java
Copy
public class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // If mid element is greater than the rightmost element, minimum must be to the right
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return nums[left];
    }
}
Explanation:
Binary Search: We apply binary search to find the point of rotation (where the smallest element lies).

Determine Pivot:

If nums[mid] > nums[right], the minimum is on the right half of the array.

If nums[mid] <= nums[right], the minimum is on the left half or could be mid.

Return: After narrowing down to the leftmost element (which is the minimum), return that element.

Time Complexity:
O(log n) where n is the length of the array. Binary search reduces the search space by half at each step.

Example Input and Output:
Input:

java
Copy
nums = [3, 4, 5, 1, 2]
Output:

java
Copy
1
Problem 3: Search a 2D Matrix II (LeetCode #240)
Problem Statement: Write an efficient algorithm that searches for a target value in an m x n matrix. The matrix has the following properties:

Integers in each row are sorted from left to right.

Integers in each column are sorted from top to bottom.

Approach:
Binary Search on Rows or Columns: You can treat the matrix as a "sorted" structure and apply a modified binary search, or more efficiently, use a "staircase" approach.

Staircase Search: Start at the top-right corner and decide whether to move left or down based on whether the target is smaller or larger than the current element.

Code Implementation:
java
Copy
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        
        int row = 0;
        int col = matrix[0].length - 1;

        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                row++;  // Move down
            } else {
                col--;  // Move left
            }
        }
        
        return false;  // Target not found
    }
}
Explanation:
Staircase Search: Start at the top-right corner of the matrix (row = 0, col = n - 1).

Move:

If the current element is equal to the target, return true.

If the current element is less than the target, move down (row++).

If the current element is greater than the target, move left (col--).

Return: If the target is not found by the time we move out of bounds, return false.

Time Complexity:
O(m + n) where m is the number of rows and n is the number of columns. In the worst case, we move across all rows and columns.

Example Input and Output:
Input:

java
Copy
matrix = [
  [1, 4, 7, 11],
  [2, 5, 8, 12],
  [3, 6, 9, 16],
  [10, 13, 14, 17]
], target = 5
Output:

java
Copy
true
Summary:
Search in Rotated Sorted Array: Modified binary search where we identify the sorted half and search within it.

Find Minimum in Rotated Sorted Array: Binary search to find the smallest element, which is the pivot point in a rotated sorted array.

Search a 2D Matrix II: Efficient search by moving either down or left based on comparisons, starting from the top-right corner.

All solutions use variations of binary search, either by directly applying it or using a staircase approach, which makes them efficient for large arrays and matrices.
