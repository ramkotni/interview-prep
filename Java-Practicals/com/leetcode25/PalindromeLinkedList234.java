package com.leetcode25;

/**
 * The Palindrome Linked List problem (LeetCode #234) asks you to determine if a singly linked list is a palindrome. A linked list is a palindrome if the sequence of values from the head to the tail is the same as from the tail to the head.
Problem Statement:
Given a singly linked list, return true if it is a palindrome, or false otherwise.
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false
Approach:
We can solve this problem efficiently in O(n) time with O(1) space (excluding the space used for input), by using a two-pointer approach.
Steps to Solve:
Find the middle of the linked list:
Use the fast and slow pointer technique (also known as the tortoise and hare technique) to find the middle of the list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle.
Reverse the second half of the linked list:
After finding the middle, reverse the second half of the list starting from the slow pointer.
Compare the two halves:
Compare the first half of the list with the reversed second half. If they match, the list is a palindrome; otherwise, it is not.
Restore the list (optional):
Optionally, you can restore the original list structure by reversing the second half again and connecting it back to the first half, but this is not strictly required for this problem.
 * 
 * Explanation:
Finding the middle of the list:
We use two pointers: slow and fast. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. When fast reaches the end of the list, slow will be at the middle.
Reversing the second half:
After finding the middle, the reverse() method is used to reverse the second half of the list starting from the slow pointer.
Comparison:
After reversing the second half, we compare it with the first half. If the values match, we return true, indicating the list is a palindrome. If any value doesn't match, we return false.
Space Complexity:
The space complexity is O(1) because we are not using any extra space other than a few pointer variables for the traversal and reversal.
Time Complexity:
The time complexity is O(n), where n is the number of nodes in the linked list. We traverse the list twice — once to find the middle and once to compare the two halves.
Example Walkthrough:
For the input head = [1, 2, 2, 1]:
First, we find the middle using the fast and slow pointer technique. The slow pointer will end up at the value 2 (the middle).
Next, we reverse the second half of the list starting from 2, which results in the list [1].
Finally, we compare the first half [1, 2] with the reversed second half [1, 2]. Since they are equal, the list is a palindrome.
For the input head = [1, 2]:
The fast and slow pointers will detect that there is no palindrome because the first and second half are different (1 != 2).
Conclusion:
This solution is efficient with O(n) time complexity and O(1) space complexity, excluding the input space. It ensures that the list is checked for being a palindrome by using the slow and fast pointers and reversing the second half of the list.
 * 
 * 
 * 
 */




public class PalindromeLinkedList234 {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;  // An empty list or a single element list is always a palindrome
        }
        
        // Step 1: Find the middle of the linked list using the slow and fast pointer technique
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Step 2: Reverse the second half of the linked list
        ListNode secondHalf = reverse(slow);
        ListNode firstHalf = head;
        
        // Step 3: Compare the first half and the second half
        while (secondHalf != null) {
            if (firstHalf.val != secondHalf.val) {
                return false;  // If values don't match, it's not a palindrome
            }
            firstHalf = firstHalf.next;
            secondHalf = secondHalf.next;
        }
        
        return true;  // The list is a palindrome
    }
    
    // Helper function to reverse a linked list
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }
        
        return prev;
    }

    public static void main(String[] args) {
        // Example 1: Palindrome linked list
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(2);
        ListNode node4 = new ListNode(1);
        
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;

        PalindromeLinkedList234 solution = new PalindromeLinkedList234();
        System.out.println(solution.isPalindrome(node1));  // Output: true
        
        // Example 2: Non-palindrome linked list
        ListNode node5 = new ListNode(1);
        ListNode node6 = new ListNode(2);
        
        node5.next = node6;
        
        System.out.println(solution.isPalindrome(node5));  // Output: false
    }
}

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
