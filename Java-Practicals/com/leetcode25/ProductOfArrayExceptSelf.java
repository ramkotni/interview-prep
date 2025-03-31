package com.leetcode25;

/**
 * The Product of Array Except Self problem on LeetCode asks you to compute the product of all the elements of the array except for the current element, for each element of the array, without using division. Additionally, you should solve it in O(n) time and O(1) space (excluding the output array).
Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
You must solve it without using division and in O(n) time complexity.
Optimal Solution:
The optimal approach involves calculating the product of all the elements to the left and to the right of each index without using extra space for the entire left and right product arrays. This can be achieved in two passes over the array.
Steps:
First Pass (Left Products):
Traverse the array from left to right, calculating the product of all elements before the current element and store this in the result array.
Second Pass (Right Products):
Traverse the array from right to left, updating the result array by multiplying it with the product of all elements after the current element.
This solution does not require extra space for the left and right products, and it completes in O(n) time with O(1) extra space (apart from the output array).
 * 
 * Explanation:
Initialization:
We initialize the result array result[] where result[i] will eventually hold the product of all elements except nums[i]. Initially, we set result[0] = 1 because there are no elements to the left of the first element.
First Pass (Left Products):
We iterate over the array from left to right. For each element nums[i], we calculate the product of all elements to the left and store it in result[i]. This is done by multiplying the current value of result[i-1] with nums[i-1].
Second Pass (Right Products):
After calculating the left products, we use a variable rightProduct to keep track of the product of elements to the right of the current element. We iterate over the array from right to left and update the result[] array by multiplying it with the rightProduct.
Final Result:
After both passes, result[i] contains the product of all elements except nums[i].
Time Complexity:
Time Complexity: O(n), where n is the number of elements in the input array. We make two passes through the array, each taking linear time.
Space Complexity: O(1), since we only use the output array and a constant amount of extra space (the rightProduct variable).
Example:
For the input:
nums = {1, 2, 3, 4}
The output will be:
Product of Array Except Self: 
24 12 8 6
Explanation:
For nums = {1, 2, 3, 4}, the product array is:
result[0] = product of all elements except nums[0] = 2 * 3 * 4 = 24
result[1] = product of all elements except nums[1] = 1 * 3 * 4 = 12
result[2] = product of all elements except nums[2] = 1 * 2 * 4 = 8
result[3] = product of all elements except nums[3] = 1 * 2 * 3 = 6
This solution is efficient and adheres to the problem constraints!
*/

public class ProductOfArrayExceptSelf {
    
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        
        // Initialize the result array with 1
        result[0] = 1;
        
        // Step 1: Calculate the left product for each index
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }
        
        // Step 2: Calculate the right product and update result array
        int rightProduct = 1;
        for (int i = n - 2; i >= 0; i--) {
            rightProduct *= nums[i + 1];
            result[i] *= rightProduct;
        }
        
        return result;
    }

    public static void main(String[] args) {
        ProductOfArrayExceptSelf solution = new ProductOfArrayExceptSelf();
        
        // Example input
        int[] nums = {1, 2, 3, 4};
        int[] result = solution.productExceptSelf(nums);
        
        // Print the result
        System.out.println("Product of Array Except Self: ");
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
