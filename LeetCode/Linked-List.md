To solve this problem, we need to reverse a portion of a linked list from position `m` to position `n`. The key point is to perform the reversal **in-place**, meaning we cannot use extra memory for another list, and we should modify the pointers directly within the original list.

### Approach:

1. **Traverse to the (m-1)th node**: We need to find the node just before the starting node of the sublist we need to reverse. If `m = 1`, this will be the head of the list.

2. **Reverse the sublist**: Starting from the m-th node, we reverse the next `n-m+1` nodes.

3. **Reconnect the sublist to the original list**: After reversing the sublist, we will need to reconnect the m-1th node to the new head of the reversed sublist, and the original m-th node (which becomes the last node of the reversed part) to the node after the n-th node.

### Example Walkthrough:

For the input linked list `head = [1, 2, 3, 4, 5]`, with `m = 2` and `n = 4`:
- We need to reverse the sublist starting from the 2nd node (`2`) to the 4th node (`4`).
- After reversing, the list will look like `[1, 4, 3, 2, 5]`.

### Code Implementation:

```java
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null || m == n) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        
        // Move pre to the (m-1)th node
        for (int i = 1; i < m; i++) {
            pre = pre.next;
        }
        
        // Start the reversal from the m-th node
        ListNode start = pre.next;
        ListNode then = start.next;
        
        // Reverse the sublist between m and n
        for (int i = 0; i < n - m; i++) {
            start.next = then.next;
            then.next = pre.next;
            pre.next = then;
            then = start.next;
        }
        
        return dummy.next;
    }
    
    // Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
```

### Explanation of the Code:

1. **Dummy Node**: A dummy node is created to simplify edge cases where the reversal happens at the head. This helps us avoid special handling for the head node when `m = 1`.

2. **Move to the (m-1)th Node**: We use a pointer `pre` to navigate to the node just before the m-th node. This ensures that we can adjust the next pointer of this node after the reversal is done.

3. **Reverse the Sublist**: 
   - `start` is the m-th node and `then` is the node right after it (m+1-th node).
   - We then reverse the next `n-m` nodes. The idea is to change the `next` pointers to reverse the direction of the links one by one.

4. **Return the New Head**: The `dummy.next` will hold the new head of the list after the reversal.

### Time Complexity:
- The algorithm runs in **O(n)** time, where `n` is the length of the linked list. This is because we only traverse the list once and reverse a portion of it in-place.

### Example Input and Output:

**Input:**
```java
head = [1, 2, 3, 4, 5], m = 2, n = 4
```

**Output:**
```java
[1, 4, 3, 2, 5]
```

### Explanation:

1. **Initial List**: `[1, 2, 3, 4, 5]`
2. We reverse the sublist starting from position `2` (value `2`) to position `4` (value `4`).
3. After reversing the sublist `[2, 3, 4]`, the result is `[1, 4, 3, 2, 5]`.

To solve this problem, we need to reverse a portion of a linked list from position m to position n. The key point is to perform the reversal in-place, meaning we cannot use extra memory for another list, and we should modify the pointers directly within the original list.

Approach:
Traverse to the (m-1)th node: We need to find the node just before the starting node of the sublist we need to reverse. If m = 1, this will be the head of the list.

Reverse the sublist: Starting from the m-th node, we reverse the next n-m+1 nodes.

Reconnect the sublist to the original list: After reversing the sublist, we will need to reconnect the m-1th node to the new head of the reversed sublist, and the original m-th node (which becomes the last node of the reversed part) to the node after the n-th node.

Example Walkthrough:
For the input linked list head = [1, 2, 3, 4, 5], with m = 2 and n = 4:

We need to reverse the sublist starting from the 2nd node (2) to the 4th node (4).

After reversing, the list will look like [1, 4, 3, 2, 5].

Code Implementation:
java
Copy
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null || m == n) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        
        // Move pre to the (m-1)th node
        for (int i = 1; i < m; i++) {
            pre = pre.next;
        }
        
        // Start the reversal from the m-th node
        ListNode start = pre.next;
        ListNode then = start.next;
        
        // Reverse the sublist between m and n
        for (int i = 0; i < n - m; i++) {
            start.next = then.next;
            then.next = pre.next;
            pre.next = then;
            then = start.next;
        }
        
        return dummy.next;
    }
    
    // Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
Explanation of the Code:
Dummy Node: A dummy node is created to simplify edge cases where the reversal happens at the head. This helps us avoid special handling for the head node when m = 1.

Move to the (m-1)th Node: We use a pointer pre to navigate to the node just before the m-th node. This ensures that we can adjust the next pointer of this node after the reversal is done.

Reverse the Sublist:

start is the m-th node and then is the node right after it (m+1-th node).

We then reverse the next n-m nodes. The idea is to change the next pointers to reverse the direction of the links one by one.

Return the New Head: The dummy.next will hold the new head of the list after the reversal.

Time Complexity:
The algorithm runs in O(n) time, where n is the length of the linked list. This is because we only traverse the list once and reverse a portion of it in-place.

Example Input and Output:
Input:

java
Copy
head = [1, 2, 3, 4, 5], m = 2, n = 4
Output:

java
Copy
[1, 4, 3, 2, 5]
Explanation:
Initial List: [1, 2, 3, 4, 5]

We reverse the sublist starting from position 2 (value 2) to position 4 (value 4).

After reversing the sublist [2, 3, 4], the result is [1, 4, 3, 2, 5].

Sure! Below are the solutions to the other two problems you mentioned:

Reverse Linked List (LeetCode #206)

Swap Nodes in Pairs (LeetCode #24)

Problem 1: Reverse Linked List (LeetCode #206)
Problem Statement: Given the head of a singly linked list, reverse the list and return its head.

Approach: To reverse the list, we need to change the next pointers of the nodes such that each node points to its previous node.

Code Implementation:
java
Copy
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode nextTemp = curr.next;  // Save next node
            curr.next = prev;               // Reverse current node's pointer
            prev = curr;                    // Move prev and curr one step forward
            curr = nextTemp;                // Move to the next node
        }
        
        return prev;  // prev will be the new head of the reversed list
    }
    
    // Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
Explanation:
Initialize pointers: We use two pointers, prev (initially null) and curr (which starts at the head).

Iterate through the list: For each node, we:

Save the next node (nextTemp).

Reverse the current node's pointer by pointing curr.next to prev.

Move prev to curr and curr to nextTemp.

Return the new head: After the loop ends, prev will be the new head of the reversed list.

Time Complexity:
The time complexity is O(n) where n is the length of the linked list, since we iterate through the list once.

Example Input and Output:
Input:

java
Copy
head = [1, 2, 3, 4, 5]
Output:

java
Copy
[5, 4, 3, 2, 1]
Problem 2: Swap Nodes in Pairs (LeetCode #24)
Problem Statement: Given a linked list, swap every two adjacent nodes and return its head. You must solve it without modifying the values of the nodes.

Approach:
To swap adjacent nodes, we need to manipulate the next pointers such that the pairs of nodes are swapped in-place.

Code Implementation:
java
Copy
public class Solution {
    public ListNode swapPairs(ListNode head) {
        // Dummy node to simplify edge cases
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        
        // Traverse the list and swap adjacent nodes
        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = first.next;
            
            // Perform the swap
            first.next = second.next;
            second.next = first;
            prev.next = second;
            
            // Move prev to the next pair
            prev = first;
        }
        
        return dummy.next;  // Return the new head of the list
    }
    
    // Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
Explanation:
Dummy Node: A dummy node is used to simplify the handling of edge cases (e.g., when the list has fewer than two nodes).

Traverse and Swap:

We use prev to keep track of the node before the pair of nodes to be swapped.

first and second represent the two adjacent nodes that need to be swapped.

After swapping, we move prev to first, which now comes after second, to process the next pair.

Return the New Head: We return dummy.next, which points to the new head of the list after the swaps.

Time Complexity:
The time complexity is O(n) where n is the length of the linked list because we process each node exactly once.

Example Input and Output:
Input:

java
Copy
head = [1, 2, 3, 4]
Output:

java
Copy
[2, 1, 4, 3]
Summary of the Problems:
Reverse Linked List: Reverses the entire linked list by adjusting the next pointers of the nodes.

Swap Nodes in Pairs: Swaps adjacent nodes by adjusting the next pointers in pairs without modifying the node values.

Both solutions use an iterative approach with constant space complexity (O(1)) and linear time complexity (O(n)), making them efficient for large linked lists.

Certainly! Let me provide a detailed solution for LeetCode #206: Reverse Linked List.

Problem Statement:
Reverse a singly linked list.

Given the head of a singly linked list, reverse the list and return its head.

Approach:
To reverse a singly linked list, we need to change the next pointers of the nodes such that each node points to its previous node instead of the next one.

Steps:
Initialize three pointers:

prev: This pointer will hold the previous node during the reversal.

curr: This pointer will track the current node being processed.

next: This will temporarily store the next node during the reversal process.

Iterate through the list:

At each step, we reverse the next pointer of the curr node.

Move prev to curr, and curr to next to continue processing the rest of the list.

End condition: When curr becomes null, we know that all the nodes have been reversed. At this point, prev will be the new head of the list.

Code Implementation:
java
Copy
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null; // Initially, the previous node is null
        ListNode curr = head; // Start with the head of the list
        
        // Traverse through the list
        while (curr != null) {
            ListNode nextTemp = curr.next; // Save the next node
            curr.next = prev;              // Reverse the current node's pointer
            prev = curr;                   // Move prev to the current node
            curr = nextTemp;               // Move to the next node
        }
        
        return prev; // prev will be the new head of the reversed list
    }

    // Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
Explanation:
Initialization:

We initialize prev as null, since the next of the last node (after reversal) should point to null.

curr is initialized to the head of the list, as this is where we start the reversal.

Reversing the list:

We enter a while loop that continues until curr is null. In each iteration, we do the following:

Save curr.next in nextTemp to keep track of the next node (since we will change curr.next).

Reverse curr.next by setting it to prev.

Move prev to curr because curr is now the previous node.

Move curr to nextTemp to continue to the next node.

Termination:

Once the loop ends (when curr becomes null), prev will point to the new head of the reversed list.

Return:

Return prev as the new head of the reversed list.

Time Complexity:
O(n): The algorithm traverses the list once, where n is the number of nodes in the linked list.

Space Complexity:
O(1): The algorithm uses a constant amount of extra space (only a few pointers), regardless of the size of the input list.

Example Walkthrough:
Example 1:

Input:

java
Copy
head = [1, 2, 3, 4, 5]
Execution steps:

Initially, prev = null and curr = head = 1 -> 2 -> 3 -> 4 -> 5.

In the first iteration:

Save nextTemp = 2 -> 3 -> 4 -> 5.

Set curr.next = prev, so 1 -> null.

Move prev = 1 and curr = 2 -> 3 -> 4 -> 5.

Repeat the process for each node:

Second iteration: Reverse 2 -> 3 -> 4 -> 5 to 2 -> 1 -> null.

Third iteration: Reverse 3 -> 4 -> 5 to 3 -> 2 -> 1 -> null.

Fourth iteration: Reverse 4 -> 5 to 4 -> 3 -> 2 -> 1 -> null.

Fifth iteration: Reverse 5 to 5 -> 4 -> 3 -> 2 -> 1 -> null.

After the loop, prev = 5 -> 4 -> 3 -> 2 -> 1 -> null, which is the new reversed list.

Output:

java
Copy
[5, 4, 3, 2, 1]
Example 2: Edge Case
Input:

java
Copy
head = [1]
Execution steps:

Since the list has only one node, the reversal will not change anything.

After the loop, prev = 1 -> null.

Output:

java
Copy
[1]
Summary:
This solution efficiently reverses a linked list in place with a time complexity of O(n) and space complexity of O(1). It uses a simple iterative approach where the next pointers of the nodes are adjusted without requiring any extra space, making it optimal for large lists.

