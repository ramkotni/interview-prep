# DSA Pattern Cheat Sheet (All Core Topics)

## 1) Arrays and Hashing
- Use when you need fast lookup/count/frequency.
- Tools: HashMap, HashSet, prefix sum.
- Example: `Two Sum`, `Contains Duplicate`.

## 2) Two Pointers
- Use when array/string is sorted or when checking pairs from ends.
- Example: `Valid Palindrome`, `Container With Most Water`.

## 3) Sliding Window
- Use for contiguous subarray/substring constraints.
- Fixed window: exact size; Variable window: condition-based.
- Example: `Longest Substring Without Repeating`, `Minimum Window Substring`.

## 4) Stack and Monotonic Stack
- Use for nested expressions and next greater/smaller element.
- Example: `Valid Parentheses`, `Daily Temperatures`, `Largest Rectangle`.

## 5) Binary Search (Answer Search too)
- Use on sorted data or monotonic condition.
- Answer-space binary search: guess and validate.
- Example: `Koko Eating Bananas`, `Search Rotated Array`.

## 6) Linked List
- Core operations: reverse, detect cycle, merge, split.
- Techniques: slow/fast pointers, dummy nodes.
- Example: `Reverse Linked List`, `Reorder List`.

## 7) Trees (DFS/BFS)
- DFS for recursion-based properties (height, path sum).
- BFS for level-based traversal.
- Example: `Max Depth`, `Level Order`, `Validate BST`.

## 8) Trie
- Use for prefix operations and dictionary search.
- Example: `Implement Trie`, `Word Search II`.

## 9) Heap / Priority Queue
- Use when repeatedly needing min/max efficiently.
- Example: `Kth Largest`, `Median from Data Stream`.

## 10) Backtracking
- Use for combinations/permutations/constraint placements.
- Pattern: choose -> explore -> unchoose.
- Example: `Subsets`, `Permutations`, `N-Queens`.

## 11) Graphs
- Represent as adjacency list.
- DFS/BFS for reachability/components.
- Topological sort for dependency ordering.
- Example: `Number of Islands`, `Course Schedule`.

## 12) Dynamic Programming
- 1D DP: previous states only (stairs, robber, LIS).
- 2D DP: two-string/grid relation (LCS, edit distance).
- Key steps: state, transition, base case, iteration order.

## 13) Greedy
- Make locally optimal choice with proof/invariant.
- Example: `Jump Game`, `Gas Station`, interval scheduling.

## 14) Intervals
- Sort by start/end and merge or detect overlap.
- Example: `Merge Intervals`, `Insert Interval`, `Meeting Rooms`.

## 15) Bit Manipulation
- Use XOR for pair cancellation and missing/single number.
- Use bit masks for compact state checks.
- Example: `Single Number`, `Counting Bits`, `Reverse Bits`.

## 16) Math and Geometry
- Matrix transform tricks: transpose + reverse.
- Number manipulation with overflow guard.
- Example: `Rotate Image`, `Pow(x,n)`.

## 17) Union-Find (Disjoint Set)
- Use for dynamic connectivity and cycle detection.
- Operations: find with path compression, union by rank/size.
- Example: `Redundant Connection`, `Graph Valid Tree`.

## 18) Topological Sort
- Use on DAG dependencies.
- Methods: Kahn BFS indegree or DFS postorder.
- Example: `Course Schedule II`, `Alien Dictionary`.

## 19) Shortest Path
- Unweighted graph -> BFS.
- Weighted non-negative -> Dijkstra.
- Example: `Network Delay Time`, `Word Ladder`.

## 20) Interview Answer Structure for DSA
1. Brute-force idea and complexity
2. Better pattern choice and why
3. Final algorithm and edge cases
4. Time/space complexity
5. Small dry run

## Mini dry run example (Two Sum)
- nums = [2,7,11,15], target = 9
- map {} -> see 2, need 7, store 2
- see 7, need 2 in map -> answer indices [0,1]

## Complexity memory trick
- One pass scan -> often O(n)
- Nested loops -> often O(n^2)
- Binary search -> O(log n)
- Heap push/pop -> O(log n)
- DFS/BFS graph -> O(V+E)
