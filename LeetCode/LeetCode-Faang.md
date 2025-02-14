Here's the content formatted for a Markdown (.md) file:

markdown
Copy
# FAANG Interview Preparation: LeetCode Problems and Java Solutions

## 1. Arrays & Strings

### Problem: Find the maximum product of two integers in an array.

```java
public class MaxProduct {
    public int maxProduct(int[] nums) {
        int max = Integer.MIN_VALUE;
        int secondMax = Integer.MIN_VALUE;

        for (int num : nums) {
            if (num > max) {
                secondMax = max;
                max = num;
            } else if (num > secondMax) {
                secondMax = num;
            }
        }
        return (max - 1) * (secondMax - 1);
    }
}
2. Linked Lists
Problem: Reverse a linked list.
java
Copy
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;

        while (current != null) {
            ListNode nextTemp = current.next;
            current.next = prev;
            prev = current;
            current = nextTemp;
        }
        return prev;
    }
}
3. Trees & Graphs
Problem: Given a binary tree, return the level order traversal of its nodes' values.
java
Copy
import java.util.*;

public class LevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(currentLevel);
        }
        return result;
    }
}
4. Dynamic Programming
Problem: Given a list of integers, find the maximum sum of non-adjacent elements.
java
Copy
public class MaxSumNoAdjacent {
    public int maxSum(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int prev1 = Math.max(0, nums[0]);
        int prev2 = Math.max(prev1, nums[1]);

        for (int i = 2; i < nums.length; i++) {
            int current = Math.max(prev1 + nums[i], prev2);
            prev1 = prev2;
            prev2 = current;
        }

        return prev2;
    }
}
5. Backtracking
Problem: Solve the N-Queens problem.
java
Copy
import java.util.*;

public class NQueens {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        solve(n, 0, new int[n], result);
        return result;
    }

    private void solve(int n, int row, int[] positions, List<List<String>> result) {
        if (row == n) {
            result.add(buildBoard(n, positions));
            return;
        }

        for (int col = 0; col < n; col++) {
            positions[row] = col;
            if (isValid(row, positions)) {
                solve(n, row + 1, positions, result);
            }
        }
    }

    private boolean isValid(int row, int[] positions) {
        for (int i = 0; i < row; i++) {
            if (positions[i] == positions[row] || Math.abs(positions[i] - positions[row]) == row - i) {
                return false;
            }
        }
        return true;
    }

    private List<String> buildBoard(int n, int[] positions) {
        List<String> board = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char[] row = new char[n];
            Arrays.fill(row, '.');
            row[positions[i]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }
}
6. Sorting & Searching
Problem: Implement binary search.
java
Copy
public class BinarySearch {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}
7. System Design (Conceptual)
While you won’t code a full system design in LeetCode, it's important to practice problem-solving in a high-level manner for system design interviews. Some common system design problems:

Design a URL shortening service (like bit.ly).
Design a cache system (LRU Cache).
Design a recommendation system.
Conclusion
These are just a handful of problems you may encounter during FAANG interviews, along with sample solutions in Java. To prepare for your interviews:

Practice on LeetCode: Solve problems by category (Arrays, Strings, Trees, DP, etc.).
Focus on optimization: Practice writing both brute-force solutions and more efficient solutions (O(log n), O(n), O(n^2)).
Understand the time and space complexity of your solutions and be able to explain trade-offs during interviews.
Good luck with your interviews!

pgsql
Copy




