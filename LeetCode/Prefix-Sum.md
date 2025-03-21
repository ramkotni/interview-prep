1. Range Sum Query - Immutable (LeetCode #303)
Problem Description:
You are given an integer array nums and you need to implement a method to calculate the sum of elements between indices i and j for multiple queries. The array is immutable.

Java Solution:
class NumArray {
    private int[] prefix;

    public NumArray(int[] nums) {
        prefix = new int[nums.length + 1];
        // Precompute the prefix sum
        for (int i = 0; i < nums.length; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
    }

    // Returns the sum of elements between indices left and right (inclusive)
    public int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
}

int[] nums = [-2, 0, 3, -5, 2, -1];
NumArray numArray = new NumArray(nums);
System.out.println(numArray.sumRange(0, 2)); // Output: 1
System.out.println(numArray.sumRange(2, 5)); // Output: -1
System.out.println(numArray.sumRange(0, 5)); // Output: -3

2. Contiguous Array (LeetCode #525)
Problem Description:
Given a binary array, find the maximum length of a contiguous subarray with an equal number of 0's and 1's.

Java Solution:
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1); // This is to handle the case when a subarray starts from the first element
        int maxLength = 0;
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i] == 0 ? -1 : 1;

            if (map.containsKey(sum)) {
                maxLength = Math.max(maxLength, i - map.get(sum));
            } else {
                map.put(sum, i);
            }
        }

        return maxLength;
    }
}
Solution sol = new Solution();
int[] nums = [0, 1, 0, 1, 0, 1];
System.out.println(sol.findMaxLength(nums)); // Output: 6

3. Subarray Sum Equals K (LeetCode #560)
Problem Description:
Given an array of integers nums and an integer k, find the total number of continuous subarrays whose sum equals k.

Java Solution:
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1); // Base case for sum 0
        int count = 0;
        int sum = 0;

        for (int num : nums) {
            sum += num;
            if (map.containsKey(sum - k)) {
                count += map.get(sum - k); // Add the number of times (sum - k) occurred before
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1); // Store the current sum
        }

        return count;
    }
}
Solution sol = new Solution();
int[] nums = [1, 1, 1];
int k = 2;
System.out.println(sol.subarraySum(nums, k)); // Output: 2

4. Prefix Sum (LeetCode #304)
Problem Description:
Given a 2D matrix, implement a method that allows you to query the sum of elements in a submatrix. You need to preprocess the matrix so that each query can be answered efficiently.

class NumMatrix {
    private int[][] prefixSum;

    public NumMatrix(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return;
        int m = matrix.length, n = matrix[0].length;
        prefixSum = new int[m + 1][n + 1];

        // Precompute the prefix sum for the 2D matrix
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSum[i][j] = matrix[i - 1][j - 1] 
                                + prefixSum[i - 1][j] 
                                + prefixSum[i][j - 1] 
                                - prefixSum[i - 1][j - 1];
            }
        }
    }

    // Returns the sum of elements within the submatrix from (row1, col1) to (row2, col2)
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefixSum[row2 + 1][col2 + 1] 
             - prefixSum[row1][col2 + 1] 
             - prefixSum[row2 + 1][col1] 
             + prefixSum[row1][col1];
    }
}
int[][] matrix = {
    {3, 0, 1, 4, 2},
    {5, 6, 3, 2, 1},
    {1, 2, 0, 1, 5},
    {4, 1, 1, 1, 4},
    {1, 0, 3, 3, 1}
};
NumMatrix numMatrix = new NumMatrix(matrix);
System.out.println(numMatrix.sumRegion(2, 1, 4, 3)); // Output: 8
System.out.println(numMatrix.sumRegion(1, 1, 2, 2)); // Output: 11
System.out.println(numMatrix.sumRegion(1, 2, 2, 4)); // Output: 12

1. Range Sum Query - Immutable (LeetCode #303)
Problem Summary:
You are given an integer array nums and need to implement a method to calculate the sum of elements between indices i and j for multiple queries. The array is immutable, meaning it cannot be modified after it's initialized.

Approach and Explanation:
Prefix Sum Array:
The idea is to preprocess the array into a prefix sum array. This allows us to compute the sum of any subarray in constant time (O(1)).
A prefix sum array is an auxiliary array where each element at index i contains the sum of all elements in the original array from index 0 to i-1.
For example, for the input array nums = [-2, 0, 3, -5, 2, -1], the prefix sum array will be:
ini
Copy
prefix = [0, -2, -2, 1, -4, -2, -3]
Now, to find the sum of elements between indices i and j (inclusive), we can compute:
swift
Copy
sumRange(i, j) = prefix[j + 1] - prefix[i]
This gives the sum of elements in constant time, after preprocessing.
Time Complexity:
Preprocessing Time:

The preprocessing step involves computing the prefix sum array, which takes O(n) time where n is the length of the array.
Query Time:

Once the prefix sum array is built, each query can be answered in constant time O(1) by subtracting the appropriate prefix values.
Total Time Complexity:

Preprocessing: O(n) for building the prefix sum array.
Query: O(1) for each query.
Space Complexity:
The space complexity is O(n) where n is the size of the input array. We store the prefix sum array which is of size n + 1.
Example:
For the array nums = [-2, 0, 3, -5, 2, -1], the prefix sum array is:

ini
Copy
prefix = [0, -2, -2, 1, -4, -2, -3]
To get the sum from index 0 to 2:

swift
Copy
sumRange(0, 2) = prefix[3] - prefix[0] = 1 - 0 = 1
2. Contiguous Array (LeetCode #525)
Problem Summary:
Given a binary array, find the maximum length of a contiguous subarray with an equal number of 0s and 1s.

Approach and Explanation:
Prefix Sum (or Cumulative Sum) Transformation:
The main idea here is to transform the array such that:
0 becomes -1
1 stays 1
After transforming the array, we need to find the longest subarray with a sum of 0.
This is equivalent to finding a subarray where the number of -1s and 1s are balanced, i.e., the sum is zero.
Hash Map for Storing Cumulative Sum Indices:
We traverse the array while maintaining a cumulative sum.
We use a hash map (map) to store the first occurrence of each cumulative sum.
If a cumulative sum repeats, it means that the subarray between the first occurrence and the current index has a sum of 0.
The length of such a subarray is calculated and we keep track of the maximum length.
Time Complexity:
Preprocessing (Traversal):

We traverse the entire array once, which takes O(n) time where n is the length of the array.
Query Time:

Each query is answered in O(1) time because we are only doing a lookup or update in the hash map during traversal.
Total Time Complexity:

Preprocessing: O(n) where n is the length of the array.
Space Complexity:
The space complexity is O(n) due to the hash map that stores the cumulative sums.
Example:
For the input array nums = [0, 1, 0, 1, 0, 1]:

After transforming the array: [-1, 1, -1, 1, -1, 1]
The cumulative sum at each step is [0, -1, 0, -1, 0, -1]
The longest subarray with sum 0 is of length 6.
3. Subarray Sum Equals K (LeetCode #560)
Problem Summary:
Given an array of integers nums and an integer k, find the total number of continuous subarrays whose sum equals k.

Approach and Explanation:
Prefix Sum and Hash Map:
We maintain a running sum of the array elements. The key observation is that if we have seen a running sum sum at index i, and at some later index j, the running sum is sum + k, then the sum of the subarray from index i+1 to j is k.
We use a hash map (map) to store the frequency of each cumulative sum that we encounter. If we see the cumulative sum sum - k, it means we have found a subarray that sums to k.
Time Complexity:
Preprocessing (Traversal):

We traverse the entire array once, which takes O(n) time where n is the length of the array.
Query Time:

Each query is answered in O(1) time due to the hash map lookup.
Total Time Complexity:

Preprocessing: O(n) where n is the length of the array.
Space Complexity:
The space complexity is O(n) because the hash map stores the cumulative sums.
Example:
For the input array nums = [1, 1, 1] and k = 2:

The cumulative sum at each index is [1, 2, 3].
At each step, we check if the difference between the current cumulative sum and k exists in the hash map.
There are two subarrays that sum to k = 2: [1, 1] and [1, 1].
4. Prefix Sum (LeetCode #304)
Problem Summary:
Given a 2D matrix, implement a method that allows you to query the sum of elements in a submatrix. You need to preprocess the matrix so that each query can be answered efficiently.

Approach and Explanation:
Prefix Sum 2D Array:
We preprocess the matrix into a 2D prefix sum array. The element prefixSum[i][j] stores the sum of the submatrix from (0, 0) to (i-1, j-1).
For any submatrix (row1, col1) to (row2, col2), the sum can be computed as:
markdown
Copy
sumRegion = prefixSum[row2 + 1][col2 + 1] 
           - prefixSum[row1][col2 + 1] 
           - prefixSum[row2 + 1][col1] 
           + prefixSum[row1][col1]
This formula uses the inclusion-exclusion principle.
Time Complexity:
Preprocessing (Building Prefix Sum):

Building the prefix sum array takes O(m * n) where m and n are the number of rows and columns of the matrix, respectively.
Query Time:

Each query can be answered in constant time O(1) using the precomputed prefix sum array.
Total Time Complexity:

Preprocessing: O(m * n) where m is the number of rows and n is the number of columns.
Query: O(1) per query.
Space Complexity:
The space complexity is O(m * n) for the 2D prefix sum array.
Example:
For the input matrix:

makefile
Copy
matrix = {
  {3, 0, 1, 4, 2},
  {5, 6, 3, 2, 1},
  {1, 2, 0, 1, 5},
  {4, 1, 1, 1, 4},
  {1, 0, 3, 3, 1}
}
The prefix sum array would be:

makefile
Copy
prefixSum = {
  {0, 0, 0, 0, 0, 0},
  {0, 3, 3, 4, 8, 10},
  {0, 8, 14, 18, 23, 27},
  {0, 9, 18, 22, 29, 39},
  {0, 13, 27, 30, 39, 50},
  {0, 14, 30, 34, 44, 58}
}
To get the sum of the submatrix (2, 1) to (4, 3):

markdown
Copy
sumRegion(2, 1, 4, 3) = prefixSum[5][4] - prefixSum[2][4] - prefixSum[5][1] + prefixSum[2][1]
                       = 50 - 23 - 14 + 8 = 8
Summary
Time Complexity:

Preprocessing (Prefix Sum Calculation): O(n) or O(m * n) depending on whether it's 1D or 2D.
Query Time: O(1) for each query.
Space Complexity:

Prefix Sum Array: O(n) for 1D and O(m * n) for 2D.
Efficiency:

The prefix sum technique allows us to handle multiple range queries efficiently after an initial preprocessing step.

https://blog.algomaster.io/p/15-leetcode-patterns
Prefix Sum involves preprocessing an array to create a new array where each element at index i represents the sum of the array from the start up to i. This allows for efficient sum queries on subarrays.

Use this pattern when you need to perform multiple sum queries on a subarray or need to calculate cumulative sums.

Sample Problem:
Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].

Example:

Input: nums = [1, 2, 3, 4, 5, 6], i = 1, j = 3

Output: 9

Explanation:
Preprocess the array A to create a prefix sum array: P = [1, 3, 6, 10, 15, 21].

To find the sum between indices i and j, use the formula: P[j] - P[i-1].
