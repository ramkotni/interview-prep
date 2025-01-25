Introduction to Data Structures and Algorithms (DSA)
Data Structures (DS) are ways of organizing and storing data efficiently so that they can be accessed and manipulated effectively. Algorithms (A) are step-by-step procedures or formulas for solving problems, such as sorting or searching.

When we combine Data Structures and Algorithms, we form DSA (Data Structures and Algorithms), which is critical for writing efficient software that can handle large datasets and high performance requirements.

Why DSA is Important:
Helps in organizing data efficiently.
Improves performance in terms of time and space complexity.
Facilitates solving problems using well-known strategies like Divide and Conquer, Greedy, Dynamic Programming, etc.
Provides insights into the efficiency of solutions, especially when dealing with large datasets.
Time Complexity and Space Complexity
Before diving into specific data structures and algorithms, let’s briefly discuss Time Complexity and Space Complexity:

Time Complexity refers to the amount of time an algorithm takes to complete as a function of the size of the input.
Space Complexity refers to the amount of memory an algorithm needs as a function of the input size.
Common notations used to express time complexity:

O(1): Constant time (does not depend on input size)
O(n): Linear time
O(n^2): Quadratic time
O(log n): Logarithmic time
O(n log n): Log-linear time
Data Structures with Examples
Let’s go over three common data structures: Linked List, Queue, and Stack.

1. Linked List
A Linked List is a linear data structure where each element (node) contains two parts:

Data: The value stored in the node.
Next: A reference (or pointer) to the next node in the sequence.
Example of Linked List Structure:
mathematica
Copy
Head -> [Data|Next] -> [Data|Next] -> [Data|Null]
Operations:
Insertion: Insert at the beginning, middle, or end of the list.
Deletion: Remove a node from the list.
Search: Find a node by its data.
Time Complexity for Linked List Operations:
Search: O(n) because you have to traverse each node until you find the target.
Insertion (at the beginning): O(1) since you only need to adjust the head pointer.
Insertion (at the end): O(n) if we don't have a tail pointer; O(1) if we do.
Deletion: O(n) for searching the node, O(1) for deleting the node (if you have a pointer to it).
Use Case for Linked List:
Dynamic Memory Allocation: Linked lists are used in situations where the amount of data is not known ahead of time and dynamic memory allocation is required (e.g., a memory manager).
2. Stack
A Stack is a linear data structure that follows the Last In, First Out (LIFO) principle. The last element added to the stack is the first one to be removed.

Basic Operations:
Push: Add an element to the stack.
Pop: Remove the top element from the stack.
Peek/Top: View the top element of the stack without removing it.
IsEmpty: Check whether the stack is empty.
Example of Stack Operations:
yaml
Copy
Push: 10 -> Stack: [10]
Push: 20 -> Stack: [10, 20]
Pop -> Stack: [10]
Peek -> Top: 10
Time Complexity for Stack Operations:
Push: O(1)
Pop: O(1)
Peek: O(1)
IsEmpty: O(1)
Use Case for Stack:
Expression Evaluation: Stacks are used for evaluating expressions (like postfix or infix expressions).
Function Call Management: Stacks manage function calls and their execution state (call stack in programming languages).
3. Queue
A Queue is a linear data structure that follows the First In, First Out (FIFO) principle. The first element added to the queue is the first one to be removed.

Basic Operations:
Enqueue: Add an element to the queue.
Dequeue: Remove the front element from the queue.
Peek/Front: View the front element without removing it.
IsEmpty: Check whether the queue is empty.
Example of Queue Operations:
yaml
Copy
Enqueue: 10 -> Queue: [10]
Enqueue: 20 -> Queue: [10, 20]
Dequeue -> Queue: [20]
Peek -> Front: 20
Time Complexity for Queue Operations:
Enqueue: O(1)
Dequeue: O(1)
Peek: O(1)
IsEmpty: O(1)
Use Case for Queue:
Task Scheduling: Queues are used in scheduling tasks (e.g., print jobs or CPU task scheduling).
Breadth-First Search (BFS): Queues are used in graph traversal algorithms like BFS to process nodes level by level.
How to Calculate Time Complexity for Algorithms
The time complexity of an algorithm depends on how the number of operations grows with the input size (n). Below are examples of algorithms using Linked Lists, Stacks, and Queues.

Example 1: Linked List Search Algorithm
java
Copy
// Search an element in the Linked List
Node search(Node head, int target) {
    Node current = head;
    while (current != null) {
        if (current.data == target) {
            return current;  // Element found
        }
        current = current.next;
    }
    return null;  // Element not found
}
Time Complexity Analysis:

We traverse through all nodes in the linked list to search for the element, so the time complexity is O(n) where n is the number of nodes.