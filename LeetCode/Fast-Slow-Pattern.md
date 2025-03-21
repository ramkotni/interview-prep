Fast & Slow Pointers

The Fast & Slow Pointers (Tortoise and Hare) pattern is used to detect cycles in linked lists and other similar structures.

Sample Problem:
Detect if a linked list has a cycle.

Explanation:
Initialize two pointers, one moving one step at a time (slow) and the other moving two steps at a time (fast).

If there is a cycle, the fast pointer will eventually meet the slow pointer.

If the fast pointer reaches the end of the list, there is no cycle.

LeetCode Problems:
Linked List Cycle (LeetCode #141)

Happy Number (LeetCode #202)

Find the Duplicate Number (LeetCode #287)

Fast & Slow Pointers (Tortoise and Hare) Pattern
The Fast & Slow Pointers pattern, also known as the Tortoise and Hare algorithm, is typically used for problems that involve detecting cycles in data structures like linked lists, arrays, or graphs. The core idea is to use two pointers that traverse the structure at different speeds. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If a cycle exists, the fast pointer will eventually catch up with the slow pointer.

When to Use the Fast & Slow Pointers Pattern:
This pattern is useful when dealing with problems that involve detecting cycles or repetitive patterns, such as finding cycles in a linked list or detecting duplicates in an array.
It is especially efficient in terms of both time and space, requiring only constant space (O(1)).
Problem 1: Linked List Cycle (LeetCode #141)
Problem Description:
Given a linked list, determine if it has a cycle in it. A linked list is said to have a cycle if any node is visited more than once while traversing the list.

Java Solution:
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;            // Move slow pointer by one step
            fast = fast.next.next;       // Move fast pointer by two steps
            
            if (slow == fast) {
                return true;             // If the slow pointer meets fast, there's a cycle
            }
        }
        
        return false;                     // If the fast pointer reaches the end, no cycle
    }
}
Explanation:
Initialization: We start with two pointers (slow and fast), both initialized to the head of the list.
Traversal: The slow pointer moves one step at a time, and the fast pointer moves two steps at a time.
Cycle Detection: If there is a cycle, the fast pointer will eventually meet the slow pointer. If they meet, we return true to indicate a cycle.
End Condition: If the fast pointer reaches the end of the list (fast == null or fast.next == null), then there is no cycle, and we return false.
Time Complexity:
Time Complexity: O(n), where n is the number of nodes in the linked list. Both pointers traverse the list at most once.
Space Complexity: O(1), since we only use two pointers and no additional data structures.
Example Input and Output:
Input:
ListNode head = new ListNode(3);
head.next = new ListNode(2);
head.next.next = new ListNode(0);
head.next.next.next = new ListNode(-4);
head.next.next.next.next = head.next; // Creates a cycle
Solution solution = new Solution();
boolean result = solution.hasCycle(head);
System.out.println(result); // Output: true

Explanation: The linked list has a cycle where the last node points back to the second node.

Problem 2: Happy Number (LeetCode #202)
Problem Description:
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
Return true if the number is happy, otherwise return false.

Java Solution:
public class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;
        
        // Loop until the fast pointer or slow pointer reaches 1
        while (fast != 1 && getNext(fast) != 1) {
            slow = getNext(slow);             // Move slow pointer by one step
            fast = getNext(getNext(fast));    // Move fast pointer by two steps
            
            if (slow == fast) {
                return false;                 // If slow and fast meet, we have a cycle
            }
        }
        
        return true;                          // If fast pointer reaches 1, it's a happy number
    }

    // Helper function to calculate the sum of squares of digits of a number
    private int getNext(int n) {
        int sum = 0;
        while (n != 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
}
xplanation:
Fast & Slow Pointers: We use two pointers (slow and fast) that start at the number n. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
Cycle Detection: If the fast pointer reaches 1, the number is a happy number, and we return true. If the fast pointer and slow pointer meet before reaching 1, there is a cycle, and the number is not happy, so we return false.
Next Number: We calculate the next number by summing the squares of the digits using the helper function getNext.
Time Complexity:
Time Complexity: O(log n) where n is the number because the number of digits decreases as we repeatedly sum the squares of the digits.
Space Complexity: O(1), as we only use a few integer variables.
Example Input and Output:
Input:
Solution solution = new Solution();
boolean result = solution.isHappy(19);
System.out.println(result); // Output: true

Explanation:

19 → 1^2 + 9^2 = 82
82 → 8^2 + 2^2 = 68
68 → 6^2 + 8^2 = 100
100 → 1^2 + 0^2 + 0^2 = 1
Since we reached 1, 19 is a happy number.

Problem 3: Find the Duplicate Number (LeetCode #287)
Problem Description:
Given an array of n + 1 integers where each integer is between 1 and n (inclusive), find the duplicate number. Assume there is only one duplicate number.

Java Solution:
public class Solution {
    public int findDuplicate(int[] nums) {
        int slow = nums[0];
        int fast = nums[0];

        // Phase 1: Detect cycle
        do {
            slow = nums[slow];                // Move slow pointer by one step
            fast = nums[nums[fast]];          // Move fast pointer by two steps
        } while (slow != fast);               // Repeat until they meet

        // Phase 2: Find the entry point to the cycle
        slow = nums[0];                       // Move slow pointer to the start
        while (slow != fast) {
            slow = nums[slow];                // Move slow pointer by one step
            fast = nums[fast];                // Move fast pointer by one step
        }
        
        return slow;                          // The point where slow and fast meet is the duplicate
    }
}

Explanation:
Phase 1 - Cycle Detection: We start with both pointers (slow and fast) at the first index of the array. The slow pointer moves one step at a time, and the fast pointer moves two steps at a time. If there is a cycle, the two pointers will eventually meet.
Phase 2 - Finding the Duplicate: Once a cycle is detected, we reset the slow pointer to the start of the array. Both pointers move one step at a time until they meet again, which will be the entry point of the cycle (the duplicate number).
Time Complexity:
Time Complexity: O(n), where n is the length of the array. The cycle detection phase takes linear time, and the second phase also takes linear time.
Space Complexity: O(1), as we only use a constant amount of extra space for the pointers.
Example Input and Output:
Input:
int[] nums = {1, 3, 4, 2, 2};
Solution solution = new Solution();
int result = solution.findDuplicate(nums);
System.out.println(result); // Output: 2

Explanation: The duplicate number is 2, as it appears twice in the array.

Summary:
Fast & Slow Pointers (Tortoise and Hare) is an efficient algorithm for detecting cycles in data structures like linked lists, arrays, and graphs.
For LeetCode Problems, the Fast & Slow Pointers pattern was applied to:
Linked List Cycle (detect if a linked list has a cycle).
Happy Number (determine if a number is happy).
Find the Duplicate Number (find the duplicate in an array).
Time Complexity of these problems is typically O(n) because we only traverse the structure once, making it highly efficient for cycle detection.
Space Complexity is usually O(1) as we use a constant amount of extra space (only two pointers).
