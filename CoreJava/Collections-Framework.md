✅ Overview of Java Collections Framework

The Java Collections Framework (JCF) is a unified architecture for representing and manipulating collections (like lists, sets, queues, maps). It provides interfaces, implementations, and algorithms.

Key Interfaces:

Collection (root)

List

Set

Queue

Map (not part of Collection hierarchy)

📊 LIST

Implementations:

ArrayList

LinkedList

Vector (legacy)

Use Case:

Maintain ordered collection, allow duplicates, indexed access.

Example:

List<String> list = new ArrayList<>();
list.add("A");
list.add("B");
System.out.println(list.get(0));

ArrayList vs LinkedList:

Feature

ArrayList

LinkedList

Data Structure

Dynamic Array

Doubly Linked List

Access

Fast (O(1))

Slow (O(n))

Insert/Delete

Slow (shifting)

Fast (no shifting)

📝 SET

Implementations:

HashSet

LinkedHashSet

TreeSet

Use Case:

Store unique elements.

Example:

Set<Integer> set = new HashSet<>();
set.add(10);
set.add(20);
set.add(10); // Duplicate, ignored

HashSet vs TreeSet:

HashSet: Unordered, fast access.

TreeSet: Sorted order, slower (O(log n)).

📆 MAP

Implementations:

HashMap

LinkedHashMap

TreeMap

ConcurrentHashMap

Use Case:

Store key-value pairs.

Example:

Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
System.out.println(map.get("a"));

HashMap vs ConcurrentHashMap:

Feature

HashMap

ConcurrentHashMap

Thread Safety

No

Yes

Null keys/values

1 null key, many null values

No null keys/values

Performance

High (single-threaded)

High (multi-threaded)

Internal Working of HashMap:

Uses array + linked list or tree for buckets.

Computes hash using hashCode().

On collision, uses chaining.

Java 8+: Uses balanced tree when many collisions.

Internal Working of ConcurrentHashMap:

Divides map into segments (buckets).

Each bucket uses lock-striping or CAS.

Thread-safe without blocking entire map.

📤 QUEUE

Implementations:

PriorityQueue

ArrayDeque

LinkedList (implements Queue)

Use Case:

First-In-First-Out (FIFO) or priority processing.

Example:

Queue<String> queue = new LinkedList<>();
queue.add("A");
queue.add("B");
System.out.println(queue.poll()); // A

🔹 STACK (LIFO)

Modern Stack: Use Deque instead of Stack class.

Example:

Deque<Integer> stack = new ArrayDeque<>();
stack.push(1);
stack.push(2);
System.out.println(stack.pop()); // 2

🔜 Major Interview Questions & Answers

What is the difference between ArrayList and LinkedList?

ArrayList is backed by a dynamic array; LinkedList by doubly linked list.

ArrayList is better for frequent read access; LinkedList is better for insert/delete in the middle.

What is the difference between HashMap and ConcurrentHashMap?

HashMap is not thread-safe. ConcurrentHashMap is.

HashMap allows one null key, ConcurrentHashMap does not.

How does HashMap handle collisions?

Uses chaining with LinkedList or Tree.

Why is Hashtable obsolete?

Synchronized on every method, poor performance. Use ConcurrentHashMap instead.

When to use TreeSet or TreeMap?

When you need sorted data.

Difference between HashSet and HashMap?

HashSet uses HashMap internally with dummy values.

What is fail-fast vs fail-safe iterator?

Fail-fast: throws ConcurrentModificationException (e.g., ArrayList).

Fail-safe: works on copy (e.g., ConcurrentHashMap).

What is the initial capacity and load factor in HashMap?

Default initial capacity: 16; load factor: 0.75

Why is LinkedList slower in search than ArrayList?

Because it must traverse nodes sequentially (O(n)).

How to synchronize a List?

Use Collections.synchronizedList(new ArrayList<>())
