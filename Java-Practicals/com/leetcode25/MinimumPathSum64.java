package com.leetcode25;

/**
 * The Minimum Path Sum problem (LeetCode #64) asks you to find the minimum path sum from the top-left to the bottom-right corner of a grid. You are only allowed to move either down or right at any point in time.
Problem Statement:
Given an m x n grid filled with non-negative numbers, find a path from the top left to the bottom right, which minimizes the sum of the numbers along the path. You can only move either down or right at any point in time.
Approach:
We can use Dynamic Programming (DP) to solve this problem efficiently. The idea is to calculate the minimum path sum at each cell, considering the minimum path sum from the cell above (if moving down) and the cell to the left (if moving right).
Steps:
Define a DP table where dp[i][j] represents the minimum path sum to reach cell (i, j).
Base Case:
The starting cell (0, 0) will have a path sum equal to its own value: dp[0][0] = grid[0][0].
Recurrence Relation:
For the first row, we can only move from the left: dp[0][j] = dp[0][j-1] + grid[0][j].
For the first column, we can only move from the top: dp[i][0] = dp[i-1][0] + grid[i][0].
For all other cells, the value of dp[i][j] is the minimum of coming from the top or from the left:
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).
Answer:
The value at the bottom-right corner, dp[m-1][n-1], will contain the minimum path sum.
Time Complexity:
O(m * n), where m is the number of rows and n is the number of columns in the grid. We fill out the DP table in a linear scan of the grid.
Space Complexity:
O(m * n) for the DP table. However, we can reduce this to O(n) by using a single row or column for optimization.

Explanation of the Code:
DP Table Initialization:
dp[0][0] = grid[0][0]: The starting point's value is the initial minimum path sum.
First Row: We can only move from left to right. Each subsequent cell in the first row is the sum of the previous cell and the current grid value.
First Column: We can only move from top to bottom. Each subsequent cell in the first column is the sum of the previous cell and the current grid value.
Filling the DP Table:
For every other cell, the minimum path sum to reach that cell is the current cell's value plus the minimum of the path sum from the top (dp[i-1][j]) or from the left (dp[i][j-1]).
Return the Result:
The minimum path sum is stored in dp[m-1][n-1], which is the bottom-right corner of the grid.
Example Walkthrough:
Input:
plaintext
Copy
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
Initialize DP table:
Initially, dp[0][0] = grid[0][0] = 1.
Fill the first row:
dp[0][1] = dp[0][0] + grid[0][1] = 1 + 3 = 4
dp[0][2] = dp[0][1] + grid[0][2] = 4 + 1 = 5
Fill the first column:
dp[1][0] = dp[0][0] + grid[1][0] = 1 + 1 = 2
dp[2][0] = dp[1][0] + grid[2][0] = 2 + 4 = 6
Fill the rest of the DP table:
dp[1][1] = grid[1][1] + min(dp[0][1], dp[1][0]) = 5 + min(4, 2) = 5 + 2 = 7
dp[1][2] = grid[1][2] + min(dp[0][2], dp[1][1]) = 1 + min(5, 7) = 1 + 5 = 6
dp[2][1] = grid[2][1] + min(dp[1][1], dp[2][0]) = 2 + min(7, 6) = 2 + 6 = 8
dp[2][2] = grid[2][2] + min(dp[1][2], dp[2][1]) = 1 + min(6, 8) = 1 + 6 = 7
Final DP table:
plaintext
Copy
dp = [
    [1, 4, 5],
    [2, 7, 6],
    [6, 8, 7]
]
Output: The minimum path sum is dp[2][2] = 7.
Output:
plaintext
Copy
Minimum Path Sum: 7
Time and Space Complexity:
Time Complexity:
O(m * n), where m is the number of rows and n is the number of columns in the grid. We iterate over each cell of the grid once to fill the DP table.
Space Complexity:
O(m * n) for the DP table. Alternatively, we could optimize space to O(n) by using a single row and updating it in-place, as only the current and previous rows are needed at any time.
 */

public class MinimumPathSum64 {

    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        // Create a DP table to store the minimum path sum at each cell
        int[][] dp = new int[m][n];
        
        // Initialize the top-left cell
        dp[0][0] = grid[0][0];
        
        // Fill in the first row (can only move right)
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }
        
        // Fill in the first column (can only move down)
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        
        // Fill the rest of the DP table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + Math.min(dp[i-1][j], dp[i][j-1]);
            }
        }
        
        // The bottom-right cell contains the minimum path sum
        return dp[m-1][n-1];
    }

    public static void main(String[] args) {
        MinimumPathSum64 solution = new MinimumPathSum64();

        int[][] grid = {
            {1, 3, 1},
            {1, 5, 1},
            {4, 2, 1}
        };

        int result = solution.minPathSum(grid);
        System.out.println("Minimum Path Sum: " + result);
    }
}
