Sliding Window

The Sliding Window pattern is used to find a subarray or substring that satisfies a specific condition, optimizing the time complexity by maintaining a window of elements.

Use this pattern when dealing with problems involving contiguous subarrays or substrings.

Sample Problem:
Find the maximum sum of a subarray of size k.

Example:

Input: nums = [2, 1, 5, 1, 3, 2], k = 3

Output: 9

Explanation:
Start with the sum of the first k elements.

Slide the window one element at a time, subtracting the element that goes out of the window and adding the new element.

Keep track of the maximum sum encountered.

LeetCode Problems:
Maximum Average Subarray I (LeetCode #643)

Longest Substring Without Repeating Characters (LeetCode #3)

Minimum Window Substring (LeetCode #76)


Sliding Window Pattern
The Sliding Window pattern is a technique used to solve problems involving contiguous subarrays or substrings by maintaining a window of elements and sliding it across the array or string. This approach is especially useful for optimizing time complexity in problems where you need to examine subarrays or substrings, as it avoids the need for recalculating values for every new subarray from scratch.

When to Use the Sliding Window Pattern:
Use the Sliding Window pattern when dealing with problems involving contiguous subarrays or substrings, such as:
Finding maximum or minimum sums of subarrays.
Finding substrings that satisfy certain conditions (e.g., no repeating characters, specific sum, etc.).
The idea is to maintain a window and slide it to the right (or left) while updating the results as the window changes.

Problem 1: Maximum Average Subarray I (LeetCode #643)
Problem Description:
Given an integer array nums and an integer k, find the maximum average of any subarray of size k.

Java Solution:
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // Step 1: Calculate the sum of the first 'k' elements.
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }

        // Step 2: Initialize maxSum with the sum of the first 'k' elements.
        int maxSum = sum;

        // Step 3: Slide the window: add the new element and subtract the old element.
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, sum);
        }

        // Step 4: Return the maximum average.
        return maxSum / (double) k;
    }
}

Explanation:
Initial Sum Calculation: We first calculate the sum of the first k elements.
Sliding the Window: Then we slide the window across the array:
For each step, subtract the element that goes out of the window (nums[i - k]) and add the new element (nums[i]).
Keep Track of Maximum Sum: Keep track of the maximum sum encountered during the sliding window process.
Return Maximum Average: Once we've found the maximum sum, we return the maximum sum divided by k to get the average.
Time Complexity:
Time Complexity: O(n) where n is the length of the array. We only need to loop through the array once.
Space Complexity: O(1) as we only need a few extra variables to store the sum and max sum.
Example Input and Output:
Input:
int[] nums = {2, 1, 5, 1, 3, 2};
int k = 3;
Solution solution = new Solution();
double result = solution.findMaxAverage(nums, k);
System.out.println(result); // Output: 9.0

Explanation:

The subarrays of size 3 are:
[2, 1, 5] → Sum = 8
[1, 5, 1] → Sum = 7
[5, 1, 3] → Sum = 9
[1, 3, 2] → Sum = 6
The maximum sum is 9, so the maximum average is 9 / 3 = 3.0.

Problem 2: Longest Substring Without Repeating Characters (LeetCode #3)
Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Java Solution:
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int left = 0, maxLength = 0;

        // Step 1: Use sliding window to explore all substrings
        for (int right = 0; right < s.length(); right++) {
            // Step 2: Expand the window until a duplicate character is found
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            
            // Step 3: Add the new character to the set and update the maxLength
            set.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}

Explanation:
Sliding Window with Set: Use a sliding window with two pointers (left and right). The right pointer expands the window to include new characters, and the left pointer contracts the window when we encounter a duplicate character.
Window Validity: We maintain a set to ensure all characters in the window are unique. If a duplicate character is encountered, we move the left pointer to remove characters from the left until the window is valid again.
Max Length Calculation: Track the maximum length of the valid window as the right pointer moves.
Time Complexity:
Time Complexity: O(n) where n is the length of the string. Both pointers (left and right) move from the start to the end of the string.
Space Complexity: O(k) where k is the size of the character set (for the set of characters). In the worst case, the set may contain all characters in the string.
Example Input and Output:
Input:
String s = "abcabcbb";
Solution solution = new Solution();
int result = solution.lengthOfLongestSubstring(s);
System.out.println(result); // Output: 3

Explanation:

The longest substring without repeating characters is "abc", which has a length of 3.

Problem 3: Minimum Window Substring (LeetCode #76)
Problem Description:
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If no such substring exists, return the empty string.

Java Solution:

class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";

        Map<Character, Integer> targetMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            targetMap.put(c, targetMap.getOrDefault(c, 0) + 1);
        }

        int left = 0, right = 0, minLength = Integer.MAX_VALUE, start = 0;
        int required = t.length();
        Map<Character, Integer> windowMap = new HashMap<>();

        // Step 1: Expand the window with 'right' pointer
        while (right < s.length()) {
            char rightChar = s.charAt(right);
            windowMap.put(rightChar, windowMap.getOrDefault(rightChar, 0) + 1);
            
            if (windowMap.get(rightChar) <= targetMap.getOrDefault(rightChar, 0)) {
                required--;
            }

            // Step 2: Contract the window with 'left' pointer
            while (required == 0) {
                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    start = left;
                }

                char leftChar = s.charAt(left);
                windowMap.put(leftChar, windowMap.get(leftChar) - 1);
                if (windowMap.get(leftChar) < targetMap.getOrDefault(leftChar, 0)) {
                    required++;
                }
                left++;
            }

            right++;
        }

        return minLength == Integer.MAX_VALUE ? "" : s.substring(start, start + minLength);
    }
}

Explanation:
Initial Setup: Create a map (targetMap) to store the frequency of characters in t. We also use a windowMap to store the frequency of characters in the current window of s.
Sliding Window:
The right pointer expands the window by adding characters from s.
The left pointer contracts the window when all characters of t are found in the window.
Window Validity: The window is valid when the frequency of all characters in the window meets or exceeds the frequency of characters in t.
Track Minimum Length: Whenever the window is valid, we try to shrink it by moving the left pointer while ensuring that the window remains valid. Track the minimum length of valid windows.
Time Complexity:
Time Complexity: O(n + m) where n is the length of s and m is the length of t. Both the left and right pointers traverse the string s once, and the operations within the loop are constant time.
Space Complexity: O(n + m) where n is the length of s and m is the length of t due to the storage of frequency maps.
Example Input and Output:
Input:
String s = "ADOBECODEBANC";
String t = "ABC";
Solution solution = new Solution();
String result = solution.minWindow(s, t);
System.out.println(result); // Output: "BANC"

Explanation:

The minimum window substring in s that contains all characters of t is "BANC".

Summary:
Sliding Window Pattern is particularly effective for problems involving subarrays or substrings where the solution requires examining all possible contiguous windows.

For LeetCode Problems, the Sliding Window pattern was applied to:

Maximum Average Subarray I (find the maximum sum of a subarray of size k).
Longest Substring Without Repeating Characters (find the longest substring without repeating characters).
Minimum Window Substring (find the minimum window in s containing all characters of t).
The Time Complexity of these solutions is typically O(n) where n is the length of the input, as each pointer (left and right) moves linearly through the array or string.

The Space Complexity is usually O(k) or O(n) for maintaining auxiliary data structures like maps or sets.



