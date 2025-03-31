package com.leetcode25;

/**
 * The Longest Substring Without Repeating Characters problem (LeetCode #3) is a classic problem that tests your ability to handle strings and use efficient algorithms, particularly sliding window or hash maps.
Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.
Example:
Input:
s = "abcabcbb"
Output:
3
Explanation: The answer is "abc", with the length of 3.
Approach:
To solve this problem efficiently, we can use the sliding window technique combined with a hash map (or set) to track characters and their most recent positions.
Key Ideas:
Sliding Window: Use two pointers to maintain a window of characters that contains no duplicates.
One pointer (left) will mark the beginning of the current substring.
The other pointer (right) will expand the window as we traverse through the string.
HashSet/HashMap: The characters in the window are tracked, and when we find a duplicate, we move the left pointer to the right of the last occurrence of that character.
Dynamic Window Size: The size of the window dynamically changes. We try to expand the window by moving right, and when we encounter a duplicate, we shrink the window from the left.
Algorithm:
Initialize two pointers: left at the beginning of the string and right to iterate through the string.
Use a HashSet or HashMap to store characters in the current window.
As we move right through the string:
If the character at right is not in the window, add it to the set and update the longest length.
If the character at right is already in the window, move the left pointer to the right of the last occurrence of the current character.
Keep track of the maximum length of the window at any point.
Explanation of the Code:
HashMap (map): The map stores the most recent index of each character. This helps us quickly find where a repeating character is located in the window.
Two Pointers (left and right):
right: Expands the window to include characters from the string.
left: When a duplicate character is found, move left to the right of the last occurrence of the repeating character.
Max Length Calculation: After processing each character, update the maxLength by checking if the current window size (i.e., right - left + 1) is greater than the previously recorded maxLength.
Time Complexity:
O(n) where n is the length of the string. We only traverse the string once, and each character is added and removed from the HashMap at most once.
Space Complexity:
O(min(n, m)) where n is the length of the string and m is the size of the character set (e.g., 128 for ASCII characters). The space complexity is determined by the space required to store the characters in the current window.
Example Walkthrough:
Input: "abcabcbb"
Initialize left = 0, maxLength = 0, and an empty map.
Start iterating with right = 0:
Character: 'a'. It's not in the map, so add 'a' to the map with index 0.
Update maxLength = 1 (substring: "a").
Move right to 1:
Character: 'b'. It's not in the map, so add 'b' to the map with index 1.
Update maxLength = 2 (substring: "ab").
Move right to 2:
Character: 'c'. It's not in the map, so add 'c' to the map with index 2.
Update maxLength = 3 (substring: "abc").
Move right to 3:
Character: 'a'. It's in the map at index 0. Update left = max(0 + 1, 0) = 1.
Update the map with 'a' at index 3.
Move right to 4:
Character: 'b'. It's in the map at index 1. Update left = max(1 + 1, 1) = 2.
Update the map with 'b' at index 4.
Move right to 5:
Character: 'c'. It's in the map at index 2. Update left = max(2 + 1, 2) = 3.
Update the map with 'c' at index 5.
Move right to 6:
Character: 'b'. It's in the map at index 4. Update left = max(4 + 1, 3) = 5.
Update the map with 'b' at index 6.
Move right to 7:
Character: 'b'. It's in the map at index 6. Update left = max(6 + 1, 5) = 7.
Update the map with 'b' at index 7.
At the end of the iteration, the maximum length of the substring without repeating characters is 3.
Output:
Length of longest substring: 3
 * 
 * 
 */

import java.util.HashMap;

public class LongestSubstringWithoutRepeatingCharacters {
    
    public int lengthOfLongestSubstring(String s) {
        // HashMap to store the most recent index of each character
        HashMap<Character, Integer> map = new HashMap<>();
        int maxLength = 0;
        int left = 0;
        
        // Iterate over the string with the 'right' pointer
        for (int right = 0; right < s.length(); right++) {
            // If the character is already in the window, move the left pointer
            if (map.containsKey(s.charAt(right))) {
                left = Math.max(map.get(s.charAt(right)) + 1, left);
            }
            
            // Update the most recent index of the current character
            map.put(s.charAt(right), right);
            
            // Calculate the current window length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }

    public static void main(String[] args) {
        LongestSubstringWithoutRepeatingCharacters solution = new LongestSubstringWithoutRepeatingCharacters();
        
        String s = "abcabcbb";
        int result = solution.lengthOfLongestSubstring(s);
        
        System.out.println("Length of longest substring: " + result);  // Output: 3
    }
}
