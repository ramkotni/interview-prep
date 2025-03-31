package com.leetcode25;

/**
 * The Detect Cycle in a Linked List problem (LeetCode #141) asks us to determine if a linked list has a cycle. A cycle in a linked list occurs when a node's next pointer points back to a previous node in the list, causing an infinite loop.
Problem Statement:
Given a linked list, return true if it has a cycle, or false otherwise.
Approach:
We can solve this problem using the Floyd’s Cycle-Finding Algorithm (also known as the Tortoise and Hare algorithm). This approach uses two pointers:
Slow pointer (slow): Moves one step at a time.
Fast pointer (fast): Moves two steps at a time.
The key observation is:
If the linked list has a cycle, the fast pointer will eventually meet the slow pointer inside the cycle.
If the linked list has no cycle, the fast pointer will eventually reach the end of the list (null).
Steps to Solve:
Initialize two pointers: Start with both the slow and fast pointers at the head of the list.
Move the pointers:
Move slow by one step.
Move fast by two steps.
Check for cycle:
If slow and fast meet at the same node, then there is a cycle, and we return true.
If fast reaches the end of the list (i.e., fast == null or fast.next == null), then there is no cycle, and we return false.
Time Complexity:
O(n): We only traverse the list once, and the pointers move at different speeds.
Space Complexity:
O(1): We only use two pointers, so the space complexity is constant.

Explanation:
Edge Case Handling:
If the list is empty or has only one node (head == null or head.next == null), it is not possible to have a cycle, so we return false immediately.
Slow and Fast Pointer:
We initialize two pointers, slow and fast, both starting at the head of the list.
In the while loop, we move the slow pointer one step at a time and the fast pointer two steps at a time.
If a cycle exists, the slow and fast pointers will eventually meet inside the cycle.
Cycle Detection:
If at any point slow == fast, it means the two pointers have met inside a cycle, and we return true.
If the fast pointer reaches the end of the list (fast == null or fast.next == null), we know that there is no cycle, and we return false.
Main Method:
The main method demonstrates two test cases:
One with a cycle where node4.next = node2 creates a cycle.
One without a cycle with a straightforward linked list.
Example Walkthrough:
Test Case 1: Cycle Detected
For the input head = [3, 2, 0, -4] with a cycle that connects -4 to 2:
The slow pointer will start at 3 and move to 2, 0, -4, and back to 2.
The fast pointer will start at 3 and move to 0, 2, -4, and back to 2.
Eventually, both slow and fast will meet at 2, which confirms a cycle.
Test Case 2: No Cycle
For the input head = [1, 2] with no cycle:
The slow pointer will start at 1 and move to 2.
The fast pointer will start at 1 and move to null (since the list ends after 2).
Since fast reaches the end, there is no cycle, and we return false.
Conclusion:
The Floyd’s Cycle-Finding Algorithm is an optimal solution for detecting cycles in a linked list with O(n) time complexity and O(1) space complexity. This method ensures that we can detect cycles efficiently even for large linked lists.
 * 
 * 
 */




public class LinkedListCycle141 {
    public boolean hasCycle(ListNode head) {
        // Edge case: If the list is empty or has only one node, there can't be a cycle
        if (head == null || head.next == null) {
            return false;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        
        // Move slow pointer one step and fast pointer two steps at a time
        while (fast != null && fast.next != null) {
            slow = slow.next;         // Move slow by 1 step
            fast = fast.next.next;    // Move fast by 2 steps
            
            // If slow and fast meet, a cycle is detected
            if (slow == fast) {
                return true;
            }
        }
        
        // If we reach the end of the list without slow and fast meeting, no cycle
        return false;
    }

    public static void main(String[] args) {
        LinkedListCycle141 solution = new LinkedListCycle141();
        
        // Test case 1: List with a cycle
        ListNode node1 = new ListNode(3);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(0);
        ListNode node4 = new ListNode(-4);
        
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node2;  // Creating a cycle by linking node4 back to node2
        
        System.out.println(solution.hasCycle(node1));  // Output: true
        
        // Test case 2: List without a cycle
        ListNode node5 = new ListNode(1);
        ListNode node6 = new ListNode(2);
        
        node5.next = node6;
        
        System.out.println(solution.hasCycle(node5));  // Output: false
    }
}

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
