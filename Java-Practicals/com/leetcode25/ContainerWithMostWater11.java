package com.leetcode25;

/**
 * 
 * Problem Description:
You are given an array height where each element represents the height of a vertical line drawn at that position. You need to find two lines that, together with the x-axis, form a container that holds the most water.
The water that the container can hold is determined by the shorter of the two lines and the distance between them. Thus, the area of water held by two lines at indices i and j is given by:
Area=min(height[i],height[j])×(j−i)
Where i and j are the indices of the two lines.
Approach:
The brute-force approach involves checking all pairs of lines, but this would have a time complexity of O(n²), where n is the number of elements in the input array. We can solve this problem more efficiently using the two-pointer technique, which reduces the time complexity to O(n).
Two-pointer approach:
Start with two pointers: one at the beginning (left) and one at the end (right) of the array.
Compute the area formed by the lines at these two pointers and keep track of the maximum area found.
Move the pointer pointing to the shorter line inward. This is because the area is limited by the shorter line, and moving the taller line inward wouldn't increase the area.
Explanation:
Two Pointers Initialization: We start with left pointer at index 0 (the first line) and right pointer at the last index (height.length - 1).
Calculate Area: For each pair of lines at indices left and right, we calculate the area using the formula:
currentArea=min(height[left],height[right])×(right−left)
We then update maxArea if the current area is larger.
Move Pointers: After calculating the area, we move the pointer pointing to the shorter line inward:
If the line at left is shorter than the line at right, we increment the left pointer (left++).
Otherwise, we decrement the right pointer (right--).
End Condition: The loop stops when the two pointers meet. At this point, we've explored all possible pairs and found the maximum area.
Return the Result: The variable maxArea will hold the maximum area found, which is then returned.
Time Complexity:
O(n): The algorithm only passes through the array once, where n is the length of the height array.
Space Complexity:
O(1): We only use a few extra variables (left, right, maxArea), so the space complexity is constant.
Example Walkthrough:
Example 1:
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Start with left = 0 and right = 8 (first and last indices).
Calculate the area for the lines at left and right:
Area = min(1, 7) * (8 - 0) = 1 * 8 = 8
Move the pointer pointing to the shorter line (left), increment left.
Continue this process until the two pointers meet, calculating areas and updating maxArea as necessary.
Final result: The maximum area found is 49.
Example 2:
Input: height = [1, 1]
Only two lines, so the area is simply min(1, 1) * (1 - 0) = 1.
Final result: The maximum area is 1.
Output for the test cases:
49
1
16

 */

public class ContainerWithMostWater11 {

    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        // Two-pointer approach
        while (left < right) {
            // Calculate the area between the current pair of lines
            int currentArea = Math.min(height[left], height[right]) * (right - left);
            maxArea = Math.max(maxArea, currentArea);

            // Move the pointer pointing to the shorter line inward
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        ContainerWithMostWater11 solution = new ContainerWithMostWater11();
        
        // Test cases
        System.out.println(solution.maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7})); // Output: 49
        System.out.println(solution.maxArea(new int[]{1, 1})); // Output: 1
        System.out.println(solution.maxArea(new int[]{4, 3, 2, 1, 4})); // Output: 16
    }
}
