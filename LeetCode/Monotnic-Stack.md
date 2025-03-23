Monotonic Stack

The Monotonic Stack pattern uses a stack to maintain a sequence of elements in a specific order (increasing or decreasing).

Use this pattern for problems that require finding the next greater or smaller element.

Sample Problem:
Find the next greater element for each element in an array. Output -1 if the greater element doesn’t exist.

Example:

Input: nums = [2, 1, 2, 4, 3]

Output: [4, 2, 4, -1, -1]

Explanation:
Use a stack to keep track of elements for which we haven't found the next greater element yet.

Iterate through the array, and for each element, pop elements from the stack until you find a greater element.

If the stack is not empty, set the result for index at the top of the stack to current element.

Push the current element onto the stack.

LeetCode Problems:
Next Greater Element I (LeetCode #496)

Daily Temperatures (LeetCode #739)

Largest Rectangle in Histogram (LeetCode #84)

Sure! Below are the solutions to the problems related to the Monotonic Stack pattern. This pattern is commonly used to solve problems where we need to find the next greater or smaller element in an array.

Problem 1: Next Greater Element I (LeetCode #496)
Problem Statement: Given an array of numbers, for each element, find the next greater element that comes after it in the same array. If no such element exists, return -1 for that element.

Approach:
To solve this problem, we can use a monotonic stack that helps us efficiently find the next greater element for each number.

Iterate through the array from right to left.

Use a stack to keep track of the elements in a decreasing order.

For each element:

Pop elements from the stack that are smaller than or equal to the current element.

If the stack is not empty, the top element of the stack is the next greater element.

Push the current element onto the stack.

Code Implementation:
java
Copy
public class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // Result array to store the next greater element for each number in nums1
        int[] result = new int[nums1.length];
        
        // Map to store the next greater element for each element in nums2
        Map<Integer, Integer> nextGreaterMap = new HashMap<>();
        
        // Monotonic stack (holds elements from nums2)
        Stack<Integer> stack = new Stack<>();
        
        // Iterate through nums2 and build the nextGreaterMap
        for (int num : nums2) {
            // Pop elements smaller than the current num as they can't be the next greater element
            while (!stack.isEmpty() && stack.peek() < num) {
                nextGreaterMap.put(stack.pop(), num);
            }
            stack.push(num); // Push current num onto the stack
        }
        
        // For each number in nums1, find the next greater element using nextGreaterMap
        for (int i = 0; i < nums1.length; i++) {
            result[i] = nextGreaterMap.getOrDefault(nums1[i], -1);
        }
        
        return result;
    }
}
Explanation:
Monotonic Stack: We use the stack to track elements in nums2 in a decreasing order. As we iterate over nums2, we check if the current element is greater than the element at the top of the stack. If it is, we pop elements from the stack (those elements can't be the next greater element for any previous element) and map them to the current element as their next greater element.

Next Greater Map: Once we know the next greater element for an element in nums2, we store it in nextGreaterMap.

Final Result: For each element in nums1, we look up its next greater element in nextGreaterMap. If there's no greater element, we return -1.

Time Complexity:
O(n) where n is the length of nums2. We iterate over nums2 once, and each element is pushed and popped from the stack at most once.

O(m) where m is the length of nums1 for the final look-up.

Example Input and Output:
Input:

java
Copy
nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output:

java
Copy
[-1, 3, -1]
Problem 2: Daily Temperatures (LeetCode #739)
Problem Statement: Given an array of temperatures, where temperatures[i] is the temperature on the ith day, return an array where each element represents the number of days you have to wait until a warmer temperature. If there is no future day with a warmer temperature, the value will be 0.

Approach:
We can solve this using a monotonic stack, where we track the indices of the temperatures in the stack, and for each element, we pop elements from the stack that correspond to temperatures that are smaller than the current one.

Code Implementation:
java
Copy
public class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        // Iterate through the array
        for (int i = 0; i < n; i++) {
            // Pop from the stack until we find a greater temperature
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int index = stack.pop();
                result[index] = i - index; // Calculate the number of days
            }
            stack.push(i); // Push the current index onto the stack
        }
        
        return result; // The result array contains the answer
    }
}
Explanation:
Monotonic Stack: We iterate through the temperatures array and use the stack to keep track of the indices of the temperatures that we haven't found a warmer temperature for yet.

Pop when a warmer temperature is found: Whenever we encounter a temperature that is warmer than the temperature at the top of the stack, we pop from the stack and calculate the number of days it took to find a warmer temperature for that index.

Push the current index onto the stack to be processed later.

Time Complexity:
O(n), where n is the length of the temperatures array. Each element is pushed and popped from the stack at most once.

Example Input and Output:
Input:

java
Copy
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output:

java
Copy
[1, 1, 4, 2, 1, 1, 0, 0]
Problem 3: Largest Rectangle in Histogram (LeetCode #84)
Problem Statement: Given an array of integers representing the histogram's bar heights, find the area of the largest rectangle in the histogram.

Approach:
We can solve this using a monotonic stack to maintain the indices of bars in increasing order of heights. When a smaller height is encountered, we calculate the maximum area for each bar that is taller than the current one.

Code Implementation:
java
Copy
public class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        int n = heights.length;
        
        for (int i = 0; i <= n; i++) {
            // We add a height of 0 at the end to handle remaining bars in stack
            int currentHeight = (i == n) ? 0 : heights[i];
            
            // Pop bars from the stack that are taller than the current height
            while (!stack.isEmpty() && currentHeight < heights[stack.peek()]) {
                int height = heights[stack.pop()];
                int width = (stack.isEmpty()) ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            
            stack.push(i);
        }
        
        return maxArea;
    }
}
Explanation:
Monotonic Stack: We use the stack to maintain the indices of the bars in increasing height order.

Calculate Area: For each bar, we calculate the area using the top of the stack whenever we encounter a smaller bar (or reach the end of the array).

Width Calculation: The width of the rectangle is determined by the difference between the current index and the index of the bar at the top of the stack.

Time Complexity:
O(n), where n is the length of the heights array. Each bar is pushed and popped from the stack at most once.

Example Input and Output:
Input:

java
Copy
heights = [2, 1, 5, 6, 2, 3]
Output:

java
Copy
10
Summary:
Next Greater Element I: Uses a monotonic stack to find the next greater element for each element in the array.

Daily Temperatures: Uses a monotonic stack to efficiently calculate the number of days until a warmer temperature for each day.

Largest Rectangle in Histogram: Uses a monotonic stack to find the largest rectangle in a histogram efficiently.

All three solutions have a time complexity of O(n), where n is the length of the array or histogram, making them efficient for large inputs.
