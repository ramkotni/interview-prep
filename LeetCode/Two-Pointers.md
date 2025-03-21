The Two Pointers pattern involves using two pointers to iterate through an array or list, often used to find pairs or elements that meet specific criteria.

Use this pattern when dealing with sorted arrays or lists where you need to find pairs that satisfy a specific condition.

Sample Problem:
Find two numbers in a sorted array that add up to a target value.

Example:

Input: nums = [1, 2, 3, 4, 6], target = 6

Output: [1, 3]

Explanation:
Initialize two pointers, one at the start (left) and one at the end (right) of the array.

Check the sum of the elements at the two pointers.

If the sum equals the target, return the indices.

If the sum is less than the target, move the left pointer to the right.

If the sum is greater than the target, move the right pointer to the left.

LeetCode Problems:
Two Sum II - Input Array is Sorted (LeetCode #167)

3Sum (LeetCode #15)

Container With Most Water (LeetCode #11)


Explanation of the Two Pointers Pattern:
The Two Pointers pattern is a technique commonly used in problems involving sorted arrays or lists. It helps efficiently solve problems where we need to find pairs, subarrays, or elements that satisfy certain conditions. The pattern works by using two pointers, one starting at the beginning of the array and one at the end. The goal is to move these pointers towards each other while making decisions based on the current values at the pointers.

In this type of problem, the array is usually sorted, and we use the following strategies:

Move the left pointer to the right if the sum of the values at the two pointers is less than the target.
Move the right pointer to the left if the sum of the values at the two pointers is greater than the target.
Return the pair when the sum of the values at the two pointers equals the target.
Problem 1: Two Sum II - Input Array is Sorted (LeetCode #167)
Problem Description:
Given a sorted array of integers nums and a target value target, return the indices of the two numbers such that they add up to the target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Java Solution:
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int sum = nums[left] + nums[right];
            
            if (sum == target) {
                return new int[] {left + 1, right + 1}; // 1-based indexing
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return new int[] {}; // return empty array if no solution is found
    }
}

Explanation:
Initialize Pointers:

Start with two pointers, left at the beginning (0) and right at the end (nums.length - 1) of the array.
While Loop:

In the while loop, we check the sum of the elements at the two pointers (nums[left] + nums[right]):
If the sum equals the target, we return the 1-based indices of left and right as the result.
If the sum is less than the target, it means we need a larger sum, so we move the left pointer one step to the right (left++).
If the sum is greater than the target, it means we need a smaller sum, so we move the right pointer one step to the left (right--).
Exit Condition:

The loop continues until the two pointers meet, ensuring all possible pairs are checked.
Time Complexity:
Time Complexity: O(n) where n is the number of elements in the array. Each pointer moves at most once from the start to the end of the array.
Space Complexity: O(1) as no additional space is used apart from the pointers and the result.
Example Input and Output:
int[] nums = {1, 2, 3, 4, 6};
int target = 6;
Solution solution = new Solution();
int[] result = solution.twoSum(nums, target);
System.out.println(Arrays.toString(result)); // Output: [1, 3]

Explanation:

We start with left = 0 (value 1) and right = 4 (value 6).
The sum of 1 + 6 = 7, which is greater than the target (6), so we move the right pointer left to index 3 (value 4).
The sum of 1 + 4 = 5, which is less than the target (6), so we move the left pointer right to index 1 (value 2).
The sum of 2 + 4 = 6, which matches the target. Thus, we return the indices [1, 3] (1-based indexing).

Problem 2: 3Sum (LeetCode #15)
Problem Description:
Given an array nums, find all unique triplets in the array that sum up to 0. The solution set must not contain duplicate triplets.

Java Solution:
import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums); // Sort the array to apply the two-pointer approach

        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicates
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = nums.length - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    // Skip duplicates for the left pointer
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    // Skip duplicates for the right pointer
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }
}

Explanation:
Sort the Array:

We first sort the array to ensure that we can use the two-pointer technique to find triplets efficiently.
Iterate with a Fixed Element:

We iterate through the array with the index i as the fixed element. For each i, we look for two other elements (left and right) such that their sum with nums[i] is zero.
Two Pointers:

The left pointer starts at i + 1 and the right pointer starts at the end of the array. We check the sum of the three elements:
If the sum is zero, we add the triplet to the result.
If the sum is less than zero, we move the left pointer right to increase the sum.
If the sum is greater than zero, we move the right pointer left to decrease the sum.
Skip Duplicates:

We ensure that the solution set contains only unique triplets by skipping duplicate elements for both i, left, and right pointers.
Time Complexity:
Time Complexity: O(n^2) where n is the length of the array. Sorting takes O(n log n) and the two-pointer traversal takes O(n) for each element.
Space Complexity: O(1) if the result is not counted, otherwise O(k) where k is the number of triplets in the result.
Example Input and Output:
Input:
int[] nums = {-1, 0, 1, 2, -1, -4};
Solution solution = new Solution();
List<List<Integer>> result = solution.threeSum(nums);
System.out.println(result); 
// Output: [[-1, -1, 2], [-1, 0, 1]]

Explanation:

After sorting the array: [-4, -1, -1, 0, 1, 2]
We check the triplet combinations using the two-pointer approach:
For i = 0 (-4), no valid triplet.
For i = 1 (-1), a valid triplet is [-1, -1, 2].
For i = 2 (-1), another valid triplet is [-1, 0, 1].

Problem 3: Container With Most Water (LeetCode #11)
Problem Description:
Given an array of integers where each element represents the height of a vertical line on a 2D plane, find two lines that together with the x-axis form a container that holds the most water. The container's water capacity is determined by the shorter of the two lines.

Java Solution:
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int minHeight = Math.min(height[left], height[right]);
            int width = right - left;
            int area = minHeight * width;
            maxArea = Math.max(maxArea, area);
            
            // Move the pointer pointing to the shorter line
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}

Explanation:
Two Pointers Approach:

Start with left at the beginning of the array and right at the end.
Calculate Area:

The area of the container is determined by the width (distance between left and right) and the height (the shorter of the two lines).
Update the maxArea if the current area is larger.
Move Pointers:

Move the pointer pointing to the shorter line, as the area is constrained by the shorter line. Moving the longer line won't help in increasing the area.
Time Complexity:
Time Complexity: O(n) where n is the length of the array. We only iterate through the array once.
Space Complexity: O(1) as we use only a constant amount of extra space.
Example Input and Output:
Input:
int[] height = {1,8,6,2,5,4,8,3,7};
Solution solution = new Solution();
int result = solution.maxArea(height);
System.out.println(result); 
// Output: 49

Explanation:

The largest area is formed between the lines at indices 1 (height 8) and 8 (height 7), giving an area of 7 * 7 = 49.

Summary:
Two Pointers Pattern is efficient for solving problems involving sorted arrays or conditions where two elements need to meet specific criteria, such as summing to a target.

For LeetCode Problems, we saw how to apply this pattern to problems like:

Two Sum II where we find two numbers that sum to a target.
3Sum to find unique triplets that sum to zero.
Container with Most Water to find the maximum area between two lines.
The Time Complexity for these problems typically involves O(n) or O(n^2) depending on the specifics of the problem, while Space Complexity is usually O(1) for the Two Pointers approach, unless additional storage (like results) is needed.


