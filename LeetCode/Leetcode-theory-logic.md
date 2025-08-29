🔹 1. Arrays & Strings

Two Sum

Problem: Find two numbers in a list that add up to a target.

Analogy: You have a shopping budget of $10. You want to buy two items whose prices add up exactly to $10. Which items are they?

Best Time to Buy and Sell Stock

Problem: Maximize profit from buying and selling stock once.

Analogy: Buy at the cheapest price, sell at the highest price after that day.

Maximum Subarray (Kadane’s Algorithm)

Problem: Find the continuous part of an array with the biggest sum.

Analogy: You track your daily mood (+ happy, – sad). Find the longest streak that makes you the happiest overall.

Container With Most Water

Problem: Given heights of lines, find 2 that trap the most water.

Analogy: Imagine putting walls in the ground. Two walls with some distance between them can hold water. You want to find the pair that holds the most.

🔹 2. Hashing / Sets

Valid Anagram

Problem: Check if two words have the same letters.

Analogy: "listen" and "silent" use the exact same letter blocks, just rearranged.

Group Anagrams

Problem: Group words that are made of the same letters.

Analogy: Sorting a basket of words into boxes where each box contains rearrangements of the same word.

Top K Frequent Elements

Problem: Find the most common items.

Analogy: In a survey, find the top 2 favorite fruits people picked the most.

🔹 3. Linked List

Reverse Linked List

Problem: Reverse the chain of nodes.

Analogy: Flip a train — last compartment becomes the first.

Merge Two Sorted Lists

Problem: Merge two already sorted lists into one sorted list.

Analogy: Like merging two sorted decks of cards while keeping order.

Linked List Cycle

Problem: Detect if a linked list loops back into itself.

Analogy: Imagine following a path. Does it ever loop into a circle, or does it end?

🔹 4. Stacks & Queues

Valid Parentheses

Problem: Check if parentheses/brackets are properly closed.

Analogy: Every open bracket must have a matching close bracket — like opening and closing doors in the right order.

Min Stack

Problem: Build a stack that can give the minimum element instantly.

Analogy: Like stacking boxes and always knowing the smallest one inside without searching.

🔹 5. Trees & Graphs

Binary Tree Level Order Traversal

Problem: Traverse a tree level by level.

Analogy: Visiting people floor by floor in a building.

Maximum Depth of Binary Tree

Problem: Find the longest path from root to leaf.

Analogy: Tallest branch in a family tree.

Clone Graph

Problem: Copy a graph with all connections.

Analogy: Copying a social network: each person (node) and their friends (edges).

🔹 6. Dynamic Programming (DP)

Climbing Stairs

Problem: How many ways to climb n steps if you can take 1 or 2 steps at a time?

Analogy: Climbing a staircase — either step by step or skip one. How many different paths exist?

Coin Change

Problem: Minimum coins needed for a given amount.

Analogy: You want to pay $27 using coins of $1, $5, and $10. What’s the fewest coins possible?

Longest Common Subsequence

Problem: Find the longest sequence that appears in both strings.

Analogy: Comparing “abcde” and “ace” → common letters in order are “ace.”

🔹 7. Others (Greedy / Search)

Meeting Rooms

Problem: Can a person attend all meetings (given start/end times)?

Analogy: You can’t attend two meetings if they overlap.

Merge Intervals

Problem: Merge overlapping time ranges.

Analogy: If a meeting is from 1–3 and another from 2–6, merge them into 1–6.

Binary Search

Problem: Find an element in a sorted list.

🔑 1. Two Sum (Array)

Problem:
Given an array of numbers and a target, find two numbers that add up to the target.

Layman’s Example:
If you have [2,7,11,15] and target 9, the answer is [2,7] because 2+7=9.

High-Level Logic (Java):

Map<Integer, Integer> map = new HashMap<>();
for (int i = 0; i < nums.length; i++) {
    int complement = target - nums[i];
    if (map.containsKey(complement)) {
        return new int[]{map.get(complement), i}; // found
    }
    map.put(nums[i], i);
}


Store numbers in a map (value → index).

For each number, check if complement exists.

🔑 2. Valid Parentheses (Stack)

Problem:
Check if brackets are properly closed.

Layman’s Example:
"{[()]}" is valid, but "{[(])}" is not.

High-Level Logic:

Stack<Character> stack = new Stack<>();
for (char c : str.toCharArray()) {
    if (c is opening bracket) push it
    else if (c is closing bracket) check top of stack matches
}
return stack.isEmpty();

🔑 3. Merge Two Sorted Lists (Linked List)

Problem:
Merge two sorted linked lists into one sorted list.

Layman’s Example:
List A: 1 -> 3 -> 5
List B: 2 -> 4 -> 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6.

High-Level Logic:

ListNode dummy = new ListNode(0);
ListNode tail = dummy;

while (l1 != null && l2 != null) {
    if (l1.val < l2.val) { tail.next = l1; l1 = l1.next; }
    else { tail.next = l2; l2 = l2.next; }
    tail = tail.next;
}
tail.next = (l1 != null) ? l1 : l2;
return dummy.next;

🔑 4. Maximum Subarray (Kadane’s Algorithm)

Problem:
Find the maximum sum of a contiguous subarray.

Layman’s Example:
Array: [-2,1,-3,4,-1,2,1,-5,4]
Answer: 6 ([4,-1,2,1]).

High-Level Logic:

int currentMax = nums[0];
int globalMax = nums[0];

for (int i = 1; i < nums.length; i++) {
    currentMax = Math.max(nums[i], currentMax + nums[i]);
    globalMax = Math.max(globalMax, currentMax);
}
return globalMax;

🔑 5. Binary Tree Level Order Traversal

Problem:
Print values level by level.

Layman’s Example:
Tree:

    3
   / \
  9  20
     / \
    15  7


Output: [[3],[9,20],[15,7]].

High-Level Logic:

Queue<TreeNode> q = new LinkedList<>();
q.add(root);
while (!q.isEmpty()) {
    for (int i = 0; i < q.size(); i++) {
        process node
        add children to queue
    }
}

🔑 6. Longest Substring Without Repeating Characters

Problem:
Find length of longest substring with unique chars.

Layman’s Example:
Input: "abcabcbb" → Output: 3 ("abc").

High-Level Logic:

Set<Character> set = new HashSet<>();
int left = 0, max = 0;

for (int right = 0; right < s.length(); right++) {
    while (set.contains(s.charAt(right))) {
        set.remove(s.charAt(left));
        left++;
    }
    set.add(s.charAt(right));
    max = Math.max(max, right - left + 1);
}

🔑 7. Search in Rotated Sorted Array

Problem:
Array sorted but rotated, search for target.

Layman’s Example:
Input: [4,5,6,7,0,1,2], target 0 → Output: index 4.

High-Level Logic (Modified Binary Search):

while (low <= high) {
    int mid = (low+high)/2;
    if (nums[mid] == target) return mid;
    if (nums[low] <= nums[mid]) { // left sorted
        if (target in range) high = mid-1; else low = mid+1;
    } else { // right sorted
        if (target in range) low = mid+1; else high = mid-1;
    }
}

🔑 8. Climbing Stairs (DP)

Problem:
You can climb 1 or 2 steps, how many ways to reach top?

Layman’s Example:
n=3 → [1+1+1], [1+2], [2+1] = 3 ways.

High-Level Logic:

int[] dp = new int[n+1];
dp[0] = 1; dp[1] = 1;
for (int i = 2; i <= n; i++) {
    dp[i] = dp[i-1] + dp[i-2];
}
return dp[n];


Analogy: Searching a word in a dictionary by flipping to the middle instead of starting from the front.
