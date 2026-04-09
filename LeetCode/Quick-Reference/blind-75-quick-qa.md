# Blind 75 Quick Q&A (Easy Revision)

## Arrays and Hashing
1. **Q: Two Sum**  
   **A:** HashMap from value -> index. For each num, check `target-num` in map.  
   **Why:** One pass gives constant lookup. **TC/SC:** O(n)/O(n)
2. **Q: Best Time to Buy and Sell Stock**  
   **A:** Track minimum so far and max profit so far.  
   **Why:** Greedy keeps best buy point. **TC/SC:** O(n)/O(1)
3. **Q: Contains Duplicate**  
   **A:** Use HashSet and detect repeated insertion.  
   **Why:** Set gives O(1) average lookup. **TC/SC:** O(n)/O(n)
4. **Q: Product of Array Except Self**  
   **A:** Prefix product pass + suffix product pass (no division).  
   **Why:** Reuses left and right products efficiently. **TC/SC:** O(n)/O(1) extra
5. **Q: Maximum Subarray**  
   **A:** Kadane's algorithm: current best ending here, global best.  
   **Why:** Negative prefix is dropped to maximize future sum. **TC/SC:** O(n)/O(1)
6. **Q: Maximum Product Subarray**  
   **A:** Track max and min product ending at each index.  
   **Why:** Negative can turn min to max. **TC/SC:** O(n)/O(1)
7. **Q: Find Minimum in Rotated Sorted Array**  
   **A:** Binary search on pivot side.  
   **Why:** At least one side is sorted each step. **TC/SC:** O(log n)/O(1)
8. **Q: Search in Rotated Sorted Array**  
   **A:** Binary search with sorted-half detection.  
   **Why:** Decide if target lies in sorted side. **TC/SC:** O(log n)/O(1)
9. **Q: 3Sum**  
   **A:** Sort + fix one index + two pointers for pair sum.  
   **Why:** Sorting enables duplicate skip and linear pair search. **TC/SC:** O(n^2)/O(1)

## Two Pointers
10. **Q: Container With Most Water**  
    **A:** Two pointers from ends, move shorter side inward.  
    **Why:** Area limited by shorter line. **TC/SC:** O(n)/O(1)
11. **Q: Valid Palindrome**  
    **A:** Two pointers skip non-alnum and compare lowercase chars.  
    **Why:** Direct mirror check. **TC/SC:** O(n)/O(1)
12. **Q: Two Sum II (Sorted)**  
    **A:** Two pointers, adjust by sum vs target.  
    **Why:** Sorted array removes need for map. **TC/SC:** O(n)/O(1)
13. **Q: Trapping Rain Water**  
    **A:** Two pointers with leftMax/rightMax.  
    **Why:** Water at index depends on smaller max boundary. **TC/SC:** O(n)/O(1)

## Sliding Window
14. **Q: Longest Substring Without Repeating Characters**  
    **A:** Expand right, shrink left until unique.  
    **Why:** Window keeps valid distinct substring. **TC/SC:** O(n)/O(k)
15. **Q: Longest Repeating Character Replacement**  
    **A:** Window + max frequency; shrink when replacements exceed k.  
    **Why:** Valid window rule is `(len - maxFreq) <= k`. **TC/SC:** O(n)/O(26)
16. **Q: Permutation in String**  
    **A:** Fixed-size window with char counts.  
    **Why:** Permutation means exact frequency match. **TC/SC:** O(n)/O(26)
17. **Q: Minimum Window Substring**  
    **A:** Expand to satisfy need, then shrink to minimal valid window.  
    **Why:** Classic variable-size covering window. **TC/SC:** O(n)/O(128)
18. **Q: Sliding Window Maximum**  
    **A:** Monotonic deque stores candidate indices.  
    **Why:** Front always max for current window. **TC/SC:** O(n)/O(k)

## Stack
19. **Q: Valid Parentheses**  
    **A:** Push opening brackets, pop on matching closing bracket.  
    **Why:** LIFO validates nesting order. **TC/SC:** O(n)/O(n)
20. **Q: Min Stack**  
    **A:** Store value stack + min stack.  
    **Why:** Retrieve min in O(1). **TC/SC:** O(1) ops/O(n)
21. **Q: Evaluate Reverse Polish Notation**  
    **A:** Push numbers; on operator pop two and apply.  
    **Why:** Postfix removes precedence ambiguity. **TC/SC:** O(n)/O(n)
22. **Q: Generate Parentheses**  
    **A:** Backtrack with counts of open/close used.  
    **Why:** Build only valid states. **TC/SC:** Catalan/O(n)
23. **Q: Daily Temperatures**  
    **A:** Monotonic decreasing stack of indices.  
    **Why:** Next greater element pattern. **TC/SC:** O(n)/O(n)
24. **Q: Car Fleet**  
    **A:** Sort by position descending and compute arrival times stack.  
    **Why:** Slower ahead merges faster behind into fleet. **TC/SC:** O(n log n)/O(n)
25. **Q: Largest Rectangle in Histogram**  
    **A:** Monotonic increasing stack, compute area on pop.  
    **Why:** Pop gives maximal span for height. **TC/SC:** O(n)/O(n)

## Binary Search
26. **Q: Binary Search**  
    **A:** Standard low/high midpoint search.  
    **Why:** Sorted array halves search space. **TC/SC:** O(log n)/O(1)
27. **Q: Search a 2D Matrix**  
    **A:** Treat matrix as flattened sorted array and binary search.  
    **Why:** Row-major property keeps order. **TC/SC:** O(log(mn))/O(1)
28. **Q: Koko Eating Bananas**  
    **A:** Binary search answer (eating speed).  
    **Why:** Feasibility monotonic with speed. **TC/SC:** O(n log maxPile)/O(1)
29. **Q: Find Minimum in Rotated Sorted Array**  
    **A:** Mid compare with right boundary.  
    **Why:** Detect unsorted side containing pivot. **TC/SC:** O(log n)/O(1)
30. **Q: Search in Rotated Sorted Array**  
    **A:** Sorted-half binary search logic.  
    **Why:** One side is always ordered. **TC/SC:** O(log n)/O(1)
31. **Q: Time Based Key-Value Store**  
    **A:** HashMap key -> list of (time,val), binary search by timestamp.  
    **Why:** Append times sorted, query predecessor. **TC/SC:** O(log n) get/O(n)
32. **Q: Median of Two Sorted Arrays**  
    **A:** Binary search partition on smaller array.  
    **Why:** Left partition size fixed for median condition. **TC/SC:** O(log min(m,n))/O(1)

## Linked List
33. **Q: Reverse Linked List**  
    **A:** Iteratively reverse pointers using prev/curr/next.  
    **Why:** In-place pointer swap. **TC/SC:** O(n)/O(1)
34. **Q: Linked List Cycle**  
    **A:** Floyd slow/fast pointers.  
    **Why:** Fast catches slow if cycle exists. **TC/SC:** O(n)/O(1)
35. **Q: Merge Two Sorted Lists**  
    **A:** Dummy node and merge by smaller current value.  
    **Why:** Standard sorted merge. **TC/SC:** O(n+m)/O(1)
36. **Q: Merge K Sorted Lists**  
    **A:** Min-heap of current heads or divide-and-conquer merge.  
    **Why:** Always pick smallest head efficiently. **TC/SC:** O(N log k)/O(k)
37. **Q: Remove Nth Node from End**  
    **A:** Two pointers with n-gap.  
    **Why:** One pass finds predecessor of target. **TC/SC:** O(n)/O(1)
38. **Q: Reorder List**  
    **A:** Find middle, reverse second half, weave two halves.  
    **Why:** Required order L0 Ln L1 Ln-1... **TC/SC:** O(n)/O(1)

## Trees
39. **Q: Invert Binary Tree**  
    **A:** Swap left/right recursively or BFS.  
    **Why:** Local swap at every node. **TC/SC:** O(n)/O(h)
40. **Q: Maximum Depth of Binary Tree**  
    **A:** DFS depth = 1 + max(left,right).  
    **Why:** Height definition. **TC/SC:** O(n)/O(h)
41. **Q: Diameter of Binary Tree**  
    **A:** DFS height while tracking max `left+right`.  
    **Why:** Longest path passes through some node. **TC/SC:** O(n)/O(h)
42. **Q: Balanced Binary Tree**  
    **A:** Postorder height; return -1 if imbalance >1.  
    **Why:** Early prune unbalanced subtree. **TC/SC:** O(n)/O(h)
43. **Q: Same Tree**  
    **A:** Recursive value and structure equality check.  
    **Why:** Both subtrees must match. **TC/SC:** O(n)/O(h)
44. **Q: Subtree of Another Tree**  
    **A:** DFS nodes, run same-tree check at each candidate.  
    **Why:** Match root then structure. **TC/SC:** O(n*m) worst
45. **Q: Lowest Common Ancestor in BST**  
    **A:** Move left/right by comparing p,q with node value.  
    **Why:** BST ordering gives direction. **TC/SC:** O(h)/O(1)
46. **Q: Binary Tree Level Order Traversal**  
    **A:** BFS queue by level size.  
    **Why:** Natural level grouping. **TC/SC:** O(n)/O(n)
47. **Q: Validate BST**  
    **A:** DFS with min/max range constraints.  
    **Why:** Every node must obey ancestor bounds. **TC/SC:** O(n)/O(h)
48. **Q: Kth Smallest in BST**  
    **A:** Inorder traversal with counter.  
    **Why:** Inorder of BST is sorted. **TC/SC:** O(h+k)/O(h)
49. **Q: Construct Tree from Preorder + Inorder**  
    **A:** Root from preorder, split inorder by root index recursively.  
    **Why:** Traversal properties uniquely rebuild tree. **TC/SC:** O(n)/O(n)

## Trie
50. **Q: Implement Trie**  
    **A:** Node has children map/array and end-of-word flag.  
    **Why:** Prefix operations become character traversal. **TC/SC:** O(L)/O(total chars)
51. **Q: Design Add and Search Words**  
    **A:** Trie + DFS for wildcard '.'.  
    **Why:** Branch only when wildcard appears. **TC/SC:** O(26^k) worst
52. **Q: Word Search II**  
    **A:** Build trie of words, DFS board with prefix pruning.  
    **Why:** Avoid useless paths early. **TC/SC:** Depends on board/words

## Heap / Priority Queue
53. **Q: Kth Largest in Stream**  
    **A:** Min-heap of size k.  
    **Why:** Heap top is kth largest. **TC/SC:** O(log k) add/O(k)
54. **Q: Last Stone Weight**  
    **A:** Max-heap repeatedly smash top two.  
    **Why:** Always need largest two quickly. **TC/SC:** O(n log n)/O(n)
55. **Q: K Closest Points to Origin**  
    **A:** Max-heap size k or quickselect on distance.  
    **Why:** Keep best k seen so far. **TC/SC:** O(n log k)/O(k)
56. **Q: Kth Largest in Array**  
    **A:** Min-heap size k or quickselect.  
    **Why:** Partition-based selection. **TC/SC:** O(n log k)
57. **Q: Task Scheduler**  
    **A:** Max-heap frequencies + cooldown queue simulation.  
    **Why:** Greedy schedule most frequent tasks first. **TC/SC:** O(n log 26)
58. **Q: Find Median from Data Stream**  
    **A:** Two heaps: max-left and min-right balanced.  
    **Why:** Median from tops. **TC/SC:** O(log n) add/O(1) find

## Backtracking
59. **Q: Subsets**  
    **A:** DFS include/exclude each element.  
    **Why:** Binary decision tree. **TC/SC:** O(2^n)/O(n)
60. **Q: Combination Sum**  
    **A:** DFS with same index reuse while target >= 0.  
    **Why:** Explore combinations with pruning. **TC/SC:** Exponential
61. **Q: Permutations**  
    **A:** Backtrack with used[] and path list.  
    **Why:** Choose unused item at each level. **TC/SC:** O(n!)/O(n)
62. **Q: Word Search**  
    **A:** DFS grid with visited marking.  
    **Why:** Path must match sequential chars. **TC/SC:** O(mn*4^L)
63. **Q: Palindrome Partitioning**  
    **A:** DFS partition, add substring if palindrome.  
    **Why:** Build valid cuts recursively. **TC/SC:** Exponential

## Graphs
64. **Q: Number of Islands**  
    **A:** DFS/BFS each unvisited land cell and count components.  
    **Why:** Connected component counting. **TC/SC:** O(mn)/O(mn)
65. **Q: Clone Graph**  
    **A:** DFS/BFS with map old->new node.  
    **Why:** Prevent duplicate clones and cycles. **TC/SC:** O(V+E)/O(V)
66. **Q: Pacific Atlantic Water Flow**  
    **A:** Reverse DFS/BFS from ocean boundaries and intersect reachable sets.  
    **Why:** Reverse flow is easier than per-cell forward checks. **TC/SC:** O(mn)
67. **Q: Course Schedule**  
    **A:** Detect cycle in directed graph via DFS states or Kahn BFS.  
    **Why:** Cycle means impossible ordering. **TC/SC:** O(V+E)
68. **Q: Graph Valid Tree**  
    **A:** Union-Find or DFS check no cycle and connected.  
    **Why:** Tree = connected + acyclic. **TC/SC:** O(V+E)
69. **Q: Number of Connected Components**  
    **A:** DFS/BFS from each unvisited node.  
    **Why:** Each traversal marks one component. **TC/SC:** O(V+E)
70. **Q: Redundant Connection**  
    **A:** Union-Find; edge whose endpoints already connected is answer.  
    **Why:** First cycle-closing edge is redundant. **TC/SC:** O(E alpha(V))

## 1-D Dynamic Programming
71. **Q: Climbing Stairs**  
    **A:** Fibonacci recurrence `dp[i]=dp[i-1]+dp[i-2]`.  
    **Why:** Last move is 1-step or 2-step. **TC/SC:** O(n)/O(1)
72. **Q: House Robber**  
    **A:** `dp[i]=max(dp[i-1], nums[i]+dp[i-2])`.  
    **Why:** Rob or skip each house. **TC/SC:** O(n)/O(1)
73. **Q: House Robber II**  
    **A:** Solve twice (exclude first, exclude last) and take max.  
    **Why:** Circular adjacency constraint. **TC/SC:** O(n)/O(1)
74. **Q: Coin Change**  
    **A:** Bottom-up dp for min coins by amount.  
    **Why:** Optimal substructure on smaller amounts. **TC/SC:** O(amount*coins)
75. **Q: Longest Increasing Subsequence**  
    **A:** Patience sorting tails + binary search.  
    **Why:** Maintain minimal tail for each length. **TC/SC:** O(n log n)/O(n)

## Bonus (extension)
76. **Q: Word Break** -> DP where `dp[i]` true if any `dp[j]` and `s[j:i]` in dict. **TC/SC:** O(n^2)
77. **Q: Combination Sum IV** -> Ordered combinations count DP. **TC/SC:** O(target*n)

Use this rule in interviews: "Pattern first, then edge cases, then complexity."
