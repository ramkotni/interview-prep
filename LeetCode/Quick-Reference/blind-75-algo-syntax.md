# Blind 75 Algorithm Syntax Map (Python)

Use with `LeetCode/Quick-Reference/dsa-algo-template-bank-python.md`.

Format: `Problem -> Template ID -> Quick note`

## 1-25
1. Two Sum -> `T01` -> HashMap complement
2. Best Time to Buy and Sell Stock -> `T02` -> running minimum
3. Contains Duplicate -> `T01` -> set/map lookup variant
4. Product of Array Except Self -> `T03` -> prefix + suffix
5. Maximum Subarray -> `T04` -> Kadane
6. Maximum Product Subarray -> `T04` -> track max/min products
7. Find Minimum in Rotated Sorted Array -> `T09` -> binary pivot search
8. Search in Rotated Sorted Array -> `T09` -> sorted-half binary search
9. 3Sum -> `T05` -> sorted two pointers inside loop
10. Container With Most Water -> `T05` -> move shorter pointer
11. Valid Palindrome -> `T05` -> alnum two pointers
12. Two Sum II -> `T05` -> sorted two pointers
13. Trapping Rain Water -> `T05` -> leftMax/rightMax two pointers
14. Longest Substring Without Repeating -> `T06` -> variable window
15. Longest Repeating Character Replacement -> `T06` -> window + maxFreq
16. Permutation in String -> `T06` -> fixed-size count window
17. Minimum Window Substring -> `T06` -> cover and shrink
18. Valid Parentheses -> `T08` -> bracket stack
19. Min Stack -> `T08` -> stack + min stack
20. Evaluate Reverse Polish Notation -> `T08` -> operand stack
21. Generate Parentheses -> `T18` -> constrained backtracking
22. Daily Temperatures -> `T07` -> monotonic decreasing stack
23. Car Fleet -> `T07` -> stack on arrival time
24. Largest Rectangle in Histogram -> `T07` -> monotonic increasing stack
25. Binary Search -> `T09` -> standard binary search

## 26-50
26. Search a 2D Matrix -> `T09` -> flatten + binary search
27. Koko Eating Bananas -> `T10` -> binary search on speed
28. Time Based Key-Value Store -> `T09` -> binary search by timestamp
29. Median of Two Sorted Arrays -> `T09` -> partition binary search
30. Reverse Linked List -> `T12` -> iterative reverse
31. Linked List Cycle -> `T11` -> slow/fast
32. Merge Two Sorted Lists -> `T13` -> dummy merge
33. Merge K Sorted Lists -> `T17` -> min-heap heads
34. Remove Nth Node From End -> `T11` -> n-gap pointers
35. Reorder List -> `T11` + `T12` -> split/reverse/merge
36. Invert Binary Tree -> `T14` -> DFS swap
37. Maximum Depth of Binary Tree -> `T14` -> depth DFS
38. Diameter of Binary Tree -> `T14` -> postorder heights
39. Balanced Binary Tree -> `T14` -> return -1 imbalance
40. Same Tree -> `T14` -> DFS equality
41. Subtree of Another Tree -> `T14` -> DFS + same-tree
42. Lowest Common Ancestor of BST -> `T14` -> BST direction
43. Binary Tree Level Order Traversal -> `T15` -> BFS levels
44. Validate BST -> `T14` -> min/max range DFS
45. Kth Smallest in BST -> `T14` -> inorder count
46. Construct Tree from Preorder + Inorder -> `T14` -> divide by index
47. Implement Trie -> `T16` -> trie node map
48. Design Add and Search Words -> `T16` + DFS -> wildcard branching
49. Word Search II -> `T16` + `T29` -> trie + board DFS
50. Kth Largest in Stream -> `T17` -> min-heap size k

## 51-75
51. Last Stone Weight -> `T17` -> max-heap simulation
52. K Closest Points to Origin -> `T17` -> heap/quickselect
53. Kth Largest in an Array -> `T17` -> min-heap k
54. Task Scheduler -> `T17` -> heap + cooldown queue
55. Find Median from Data Stream -> `T17` -> two heaps
56. Subsets -> `T18` -> include/exclude DFS
57. Combination Sum -> `T18` -> target backtracking
58. Permutations -> `T18` -> used[] backtracking
59. Word Search -> `T29` + `T18` -> DFS grid
60. Palindrome Partitioning -> `T18` -> DFS cut positions
61. Number of Islands -> `T19` -> grid DFS components
62. Clone Graph -> `T19` -> DFS copy with map
63. Pacific Atlantic Water Flow -> `T19` + `T29` -> reverse reachability
64. Course Schedule -> `T20` -> topo cycle detection
65. Graph Valid Tree -> `T27` -> union-find connectivity
66. Number of Connected Components -> `T19` -> graph DFS count
67. Redundant Connection -> `T27` -> first failed union
68. Climbing Stairs -> `T22` -> Fibonacci DP
69. House Robber -> `T22` -> rob/skip recurrence
70. House Robber II -> `T22` -> two linear runs
71. Coin Change -> `T22` -> min coins DP
72. Longest Increasing Subsequence -> `T09` -> tails binary search
73. Word Break -> `T22` -> boolean DP
74. Combination Sum IV -> `T22` -> count ordered combinations
75. Unique Paths -> `T23` -> 2D grid DP

## Extension quick links (if practicing beyond 75)
- LCS -> `T23`
- Stock with Cooldown -> `T22`
- Coin Change II -> `T23`
- Target Sum -> `T23`
- Jump Game -> `T24`
- Gas Station -> `T24`
- Merge/Insert Interval -> `T25`
- Number of 1 Bits / Missing Number -> `T28`

Interview tip: For any problem, say `Template ID`, then write adapted code.
