package com.leetcode25;
import java.util.*;

/**
 * The Group Anagrams problem (LeetCode #49) asks you to group anagrams from a list of strings. Two strings are anagrams if they can be rearranged to form the other string (i.e., they have the same characters with the same frequencies).
Problem Description:
You are given an array of strings, and you need to group anagrams together. All strings in an anagram group should be grouped together, and the order of the groups in the result does not matter.
Example:
Input:
strs = [""eat"", ""tea"", ""tan"", ""ate"", ""nat"", ""bat""]
Output:
[[""eat"", ""tea"", ""ate""], [""tan"", ""nat""], [""bat""]]
Approach:
The key observation is that anagrams will always have the same sorted characters, so we can use this property to group them together.
Sort the Strings:
Sort each string alphabetically. Anagrams will have the same sorted representation, which allows us to group them easily.
Use a HashMap:
We can use a HashMap where the key is the sorted version of the string, and the value is a list of strings that are anagrams (i.e., all strings that, when sorted, produce the same key).
Iterate through the Strings:
For each string in the input array, sort it and use this sorted version as the key to insert it into the HashMap.
Return the Groups:
The values of the HashMap will be the groups of anagrams. We can simply return them.
 * 
 * Explanation:
Sorting Each String:
We convert each string to a character array and sort the characters. This sorted version is used as the key in the HashMap. For example, for ""eat"", we would get ""aet"" as the key.
HashMap Usage:
We use a HashMap<String, List<String>> where the key is the sorted string, and the value is a list of strings that are anagrams.
If the sorted string key does not already exist in the map, we create a new list and add the string to it.
Final Result:
Once all strings are processed, the map will contain the anagram groups. We simply return the values of the map as a list of lists.
Time Complexity:
O(n k log k), where n is the number of strings in the input array and k is the maximum length of a string.
Sorting each string takes O(k log k).
We do this for each of the n strings, so the total time complexity is O(n k log k).
Space Complexity:
O(n k), where n is the number of strings and k is the average length of a string.
We store the input strings in the HashMap, and for each string, we also store its sorted version, which requires space proportional to the number of strings and their lengths.
Example Walkthrough:
Input:
strs = [""eat"", ""tea"", ""tan"", ""ate"", ""nat"", ""bat""]
Step 1: Sort the strings:
""eat"" -> ""aet""
""tea"" -> ""aet""
""tan"" -> ""ant""
""ate"" -> ""aet""
""nat"" -> ""ant""
""bat"" -> ""abt""
Step 2: Insert into HashMap:
For ""eat"", key = ""aet"", value = [""eat""]
For ""tea"", key = ""aet"", value = [""eat"", ""tea""]
For ""tan"", key = ""ant"", value = [""tan""]
For ""ate"", key = ""aet"", value = [""eat"", ""tea"", ""ate""]
For ""nat"", key = ""ant"", value = [""tan"", ""nat""]
For ""bat"", key = ""abt"", value = [""bat""]
Step 3: Grouped anagrams:
The final groups in the HashMap are:
Key ""aet"" -> [""eat"", ""tea"", ""ate""]
Key ""ant"" -> [""tan"", ""nat""]
Key ""abt"" -> [""bat""]
Step 4: Convert the values of the HashMap into a list of lists:
Result: [[""eat"", ""tea"", ""ate""], [""tan"", ""nat""], [""bat""]]
Output:
[[""eat"", ""tea"", ""ate""], [""tan"", ""nat""], [""bat""]]
Final Thoughts:
This solution efficiently groups anagrams using sorting and a HashMap. Sorting each string ensures that all anagrams have the same key, and the HashMap makes it easy to group the anagrams together. The time complexity of O(n k log k) is optimal for this problem when considering the sorting step.
 * 
 */


public class GroupAnagrams49 {

    public List<List<String>> groupAnagrams(String[] strs) {
        // Create a map to store groups of anagrams
        Map<String, List<String>> map = new HashMap<>();

        // Loop through each string in the array
        for (String str : strs) {
            // Sort the string and use it as a key
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);

            // If the key doesn't exist, create a new list
            if (!map.containsKey(sortedStr)) {
                map.put(sortedStr, new ArrayList<>());
            }
            
            // Add the original string to the corresponding list
            map.get(sortedStr).add(str);
        }

        // Return the grouped anagrams
        return new ArrayList<>(map.values());
    }

    public static void main(String[] args) {
        GroupAnagrams49 solution = new GroupAnagrams49();

        // Test case
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> result = solution.groupAnagrams(strs);

        // Print the result
        for (List<String> group : result) {
            System.out.println(group);
        }
    }
}
