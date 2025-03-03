package com.leetcodeprobs.test;
import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeating {
    public static int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charIndexMap = new HashMap<>();
        int longest = 0;
        int start = 0;

        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            if (charIndexMap.containsKey(c)) {
                start = Math.max(start, charIndexMap.get(c) + 1);
            }
            charIndexMap.put(c, end);
            longest = Math.max(longest, end - start + 1);
        }

        return longest;
    }

    public static void main(String[] args) {
        
    	/**
    	 * Input: s = "abcabcbb"
			Output: 3
			Explanation: The answer is "abc", with the length of 3.

			Input: s = "bbbbb"
			Output: 1
			Explanation: The answer is "b", with the length of 1.

			Input: s = "pwwkew"
			Output: 3
			Explanation: The answer is "wke", with the length of 3.

    	 */
    	
    	
    	String s = "abcabcbb";
        System.out.println(lengthOfLongestSubstring(s)); // Output: 3

        s = "bbbbb";
        System.out.println(lengthOfLongestSubstring(s)); // Output: 1

        s = "pwwkew";
        System.out.println(lengthOfLongestSubstring(s)); // Output: 3
    }
}
