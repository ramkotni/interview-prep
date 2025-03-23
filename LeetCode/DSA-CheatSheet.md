# Data Structures and Algorithms Cheat Sheet

## Arrays

| **Topic**              | **Description**                                                       | **Example/Code**                              |
|------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Traversal**           | Access each element sequentially.                                      | `for(int i=0; i < arr.length; i++)`           |
| **Sliding Window**      | Technique for optimizing problems with fixed-length subarrays.        | `currentSum += arr[right] - arr[left]`        |
| **Kadane’s Algorithm**  | Finding the maximum subarray sum.                                      | `maxSum = Math.max(maxSum, currentSum)`       |

## Strings

| **Topic**                 | **Description**                                                       | **Example/Code**                              |
|---------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Palindrome Check**       | Check if a string is the same forward and backward.                  | `s.equals(new StringBuilder(s).reverse().toString())` |
| **Anagram Check**          | Check if two strings contain the same characters.                     | `Arrays.sort(s1.toCharArray()) == Arrays.sort(s2.toCharArray())` |
| **Longest Palindrome**     | Find the longest palindrome substring.                                | `expandAroundCenter(s)`                       |

## Linked Lists

| **Topic**                  | **Description**                                                       | **Example/Code**                              |
|----------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Traversal**               | Iterating through the list.                                           | `while (head != null) { head = head.next; }`   |
| **Reversal**                | Reversing the linked list.                                            | `prev = null; current = head;`                |
| **Cycle Detection**        | Detect if there’s a cycle using Floyd’s Tortoise and Hare.            | `slow = head; fast = head;`                   |

## Stacks & Queues

| **Topic**                  | **Description**                                                       | **Example/Code**                              |
|----------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Stack**                   | Last In First Out (LIFO).                                              | `stack.push(x);`                              |
| **Queue**                   | First In First Out (FIFO).                                             | `queue.offer(x);`                             |
| **Implement Stack using Queue** | Simulating stack operations using two queues.                         | `queue1.offer(x);`                            |

## Binary Trees & BST

| **Topic**                    | **Description**                                                       | **Example/Code**                              |
|------------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Preorder, Inorder, Postorder** | Tree traversal techniques.                                           | `preorder(root) { if (root != null) {...} }`   |
| **Height of Tree**           | Finding the height of a binary tree.                                  | `return 1 + Math.max(height(root.left), height(root.right))` |
| **Lowest Common Ancestor**   | Finding the LCA of two nodes in a BST.                                | `if (root.val > p.val && root.val > q.val) return LCA(root.left, p, q);` |

## Sorting Algorithms

| **Algorithm**               | **Description**                                                       | **Example/Code**                              |
|-----------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Merge Sort**               | Divide and conquer sorting algorithm.                                 | `mergeSort(arr, 0, arr.length - 1);`          |
| **Quick Sort**               | Partition and conquer sorting algorithm.                              | `quickSort(arr, low, high);`                  |
| **Bubble Sort**              | Simple sorting algorithm with O(n^2) time complexity.                 | `for(i=0; i<arr.length-1; i++) {...}`         |

## Graphs

| **Topic**                    | **Description**                                                       | **Example/Code**                              |
|------------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **BFS**                       | Breadth First Search, level-order traversal.                          | `queue.offer(start);`                         |
| **DFS**                       | Depth First Search, recursively visit nodes.                          | `dfs(node) { visited.add(node); }`           |
| **Shortest Path (Dijkstra)**  | Find the shortest path in a graph with weighted edges.                | `dijkstra(graph, start)`                      |

## Dynamic Programming

| **Topic**                    | **Description**                                                       | **Example/Code**                              |
|------------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Fibonacci**                 | Standard dynamic programming problem.                                 | `dp[0] = 0; dp[1] = 1;`                      |
| **Knapsack Problem**          | Solve optimization problems with constraints.                         | `dp[i][w] = Math.max(dp[i-1][w], dp[i-1][w - wt[i-1]] + val[i-1])` |
| **Longest Common Subsequence**| Find the longest common subsequence between two strings.             | `dp[i][j] = (str1[i-1] == str2[j-1]) ? dp[i-1][j-1] + 1 : Math.max(dp[i-1][j], dp[i][j-1]);` |

## Backtracking

| **Topic**                    | **Description**                                                       | **Example/Code**                              |
|------------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **N-Queens Problem**          | Solve the N-Queens problem.                                           | `backtrack(board, row) { if (row == N) return; }` |
| **Permutations**              | Generate all permutations of a set.                                  | `backtrack(nums, start) { swap(nums[i], nums[start]); }` |

## Greedy Algorithms

| **Topic**                    | **Description**                                                       | **Example/Code**                              |
|------------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Activity Selection Problem** | Find the maximum number of non-overlapping activities.                | `activities.sort()`                           |
| **Huffman Encoding**         | Build an optimal encoding using a frequency table.                    | `buildHuffmanTree(freqTable)`                |

## Divide and Conquer

| **Topic**                    | **Description**                                                       | **Example/Code**                              |
|------------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| **Merge Sort**               | Divide the array and merge in sorted order.                           | `merge(arr, left, mid, right);`              |
| **Quick Sort**               | Partition array around a pivot.                                       | `quickSort(arr, low, high);`                 |

---

### How to Use This Cheat Sheet

- **Understand the theory** behind each algorithm and its time complexity.
- **Practice** the code snippets provided by modifying inputs or solving variations of the problems.
- **Apply concepts** to common problems in coding interviews and practice platforms.

--- 

This **cheat sheet** should help you organize and recall important concepts and code patterns while preparing for technical interviews, especially on platforms like **LeetCode**, **Hackerrank**, or **Codeforces**.
