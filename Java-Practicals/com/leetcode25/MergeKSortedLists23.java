package com.leetcode25;
import java.util.*;

/**
 * The Merge k Sorted Lists problem (LeetCode #23) asks you to merge k sorted linked lists into one sorted linked list.
Problem Statement:
Given an array of k sorted linked lists, each list is sorted in ascending order, merge all the lists into one sorted list and return it.
Approach:
There are multiple approaches to solving this problem. The most efficient way is to use a min-heap (or priority queue) to handle the merging of multiple sorted lists efficiently. Here's a step-by-step breakdown:
Approach: Min-Heap (Priority Queue)
Why use a min-heap?
A min-heap allows us to efficiently get the smallest element from a group of elements. We can use this property to merge the k sorted lists by always extracting the smallest element across all lists.
Each time we pop an element from the heap, we add the next element from the corresponding list to the heap.
Detailed Steps:
Initialize a Min-Heap:
Create a priority queue (or min-heap) to store nodes, where each node will be represented by the value and its corresponding list index.
Add Initial Nodes to the Heap:
Add the first node from each of the k lists into the min-heap.
Process the Heap:
Extract the minimum element from the heap (this is the smallest value across all lists).
If the extracted node has a next node in its list, add the next node to the heap.
Keep repeating this process until the heap is empty.
Merge the Lists:
Maintain a dummy head node to facilitate the merging process, and add nodes to the result list as you pop them from the heap.
Time Complexity:
O(N log k), where:
N is the total number of nodes across all k lists.
For each node, we perform a log k operation in the heap (since there are at most k lists, the heap size will be k).
Space Complexity:
O(k): We store up to k elements in the heap at any time

Explanation of the Code:
ListNode Class:
This is the definition of the ListNode, which contains an integer value (val) and a pointer to the next node (next).
mergeKLists Method:
PriorityQueue (Min-Heap): We create a priority queue (min-heap) that sorts the nodes by their value (a.val - b.val).
Initialization: We iterate through all k linked lists and add the head of each list to the priority queue (if not null).
Merging: We repeatedly extract the smallest node from the heap, add it to the result list, and then move the pointer to the next node in the same list (if it exists). This process continues until the heap is empty.
Dummy Head: A dummy head is used to simplify the merging process. It provides an easy starting point for the result list, and we return dummy.next as the final merged list.
Main Method:
We create three sorted linked lists and pass them as input to the mergeKLists function.
The result list is printed by traversing it and printing each node's value.
Example Walkthrough:
Input:
plaintext
Copy
List 1: 1 -> 4 -> 5
List 2: 1 -> 3 -> 4
List 3: 2 -> 6
Initially, we add the first node of each list to the heap:
Heap: [1, 1, 2]
Extract the smallest element (1), add it to the merged list, and add the next node of the list it came from (4 from List 1) to the heap:
Heap: [1, 2, 4]
Merged list: 1
Extract the next smallest element (1), add it to the merged list, and add the next node (3 from List 2) to the heap:
Heap: [2, 3, 4]
Merged list: 1 -> 1
Extract the next smallest element (2), add it to the merged list, and add the next node (6 from List 3) to the heap:
Heap: [3, 4, 6]
Merged list: 1 -> 1 -> 2
Continue this process until the heap is empty, resulting in:
Merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
Output:
plaintext
Copy
1 1 2 3 4 4 5 6 
Time Complexity:
O(N log k), where N is the total number of nodes across all k lists. For each node, we perform a log k operation in the heap. Therefore, the time complexity is proportional to the total number of nodes times the logarithm of k.
Space Complexity:
O(k), where k is the number of linked lists. The space complexity is due to the heap storing at most k nodes at any given time (one node from each list).
This solution efficiently merges the k sorted linked lists and handles the problem in an optimal way using a min-heap (priority queue).

 * 
 * 
 * 
 */

public class MergeKSortedLists23 {
    
    // Definition for singly-linked list.
    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        // PriorityQueue to store the nodes, sorting by their values
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);

        // Add the first node of each list to the minHeap
        for (ListNode list : lists) {
            if (list != null) {
                minHeap.offer(list);
            }
        }

        // Dummy node to start the merged list
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        // While the heap is not empty, extract the smallest element and move the pointer
        while (!minHeap.isEmpty()) {
            ListNode node = minHeap.poll();  // Extract the smallest node
            current.next = node;             // Add it to the result list
            current = current.next;          // Move the pointer of the result list

            // If there is a next node in the extracted list, add it to the heap
            if (node.next != null) {
                minHeap.offer(node.next);
            }
        }

        // Return the merged list, which is the next node after the dummy
        return dummy.next;
    }

    public static void main(String[] args) {
        MergeKSortedLists23 solution = new MergeKSortedLists23();

        // Test case 1:
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(4);
        list1.next.next = new ListNode(5);
        
        ListNode list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);
        
        ListNode list3 = new ListNode(2);
        list3.next = new ListNode(6);

        ListNode[] lists = {list1, list2, list3};

        ListNode result = solution.mergeKLists(lists);

        // Print the merged list
        while (result != null) {
            System.out.print(result.val + " ");
            result = result.next;
        }
    }
}
