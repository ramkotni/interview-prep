package com.leetcode25;
import java.util.HashMap;

/**
 * The LRU (Least Recently Used) Cache problem (LeetCode #146) asks you to design and implement a data structure that supports the following operations:
get(key): Returns the value of the key if the key exists, otherwise returns -1.
put(key, value): Inserts or updates the value of the key. If the number of keys exceeds the capacity of the cache, it should evict the least recently used key.
Key Idea:
The goal of an LRU cache is to keep track of the most recently accessed keys and ensure that the least recently used ones are removed when the cache reaches its capacity. This means the cache needs to maintain the order of accesses.
Approach:
Doubly Linked List:
We need a doubly linked list to maintain the order of keys based on their usage. The most recently used elements will be moved to the front (head) of the list, while the least recently used elements will be at the end (tail). This allows us to efficiently remove the least recently used element when the cache exceeds its capacity.
Hash Map:
A hash map (or hash table) is used to store the key-value pairs for quick access. The keys in the hash map will correspond to nodes in the doubly linked list.
Operations:
get(key):
If the key exists in the cache (hash map), we return its value and move that node to the front of the doubly linked list.
If the key does not exist, return -1.
put(key, value):
If the key already exists in the cache, we update its value and move it to the front of the list.
If the key doesn't exist and the cache is at capacity, we remove the least recently used node (i.e., the node at the tail of the doubly linked list) and then add the new node at the front.
Data Structures:
Doubly Linked List: Helps keep track of the order of elements. Each node will store the key, value, and pointers to the previous and next nodes.
Hash Map: Maps the keys to their respective nodes in the doubly linked list for O(1) access.

Explanation of the Code:
Node class:
This represents a single node in the doubly linked list. Each node contains a key, value, and pointers (prev and next) to the previous and next nodes.
LRUCache class:
The class has a capacity, a cache (which is a HashMap to store the key-node mappings), and two dummy nodes (head and tail) to simplify the list manipulation.
The get(int key) method checks if the key exists in the cache. If it does, it moves the node to the front and returns the value; otherwise, it returns -1.
The put(int key, int value) method inserts a new key-value pair or updates the value if the key exists. If the cache exceeds its capacity, the least recently used item is evicted.
The moveToFront(Node node) method moves a node to the front of the linked list.
The removeNode(Node node) method removes a node from the doubly linked list.
The addToFront(Node node) method adds a node to the front of the linked list.
The removeLRU() method removes the least recently used node (i.e., the node just before the tail).
Time Complexity:
O(1) for both get and put operations, as accessing a node in the hash map and modifying the doubly linked list (adding/removing nodes) are both constant time operations.
Space Complexity:
O(capacity): The space complexity is proportional to the number of items in the cache, which is at most the capacity.
Example Walkthrough:
put(1, 1): Adds key 1 with value 1 to the cache. Cache is now {1=1}.
put(2, 2): Adds key 2 with value 2 to the cache. Cache is now {1=1, 2=2}.
get(1): Returns the value of key 1, which is 1, and moves it to the front. Cache is now {2=2, 1=1}.
put(3, 3): Cache is full, so the least recently used key 2 is evicted. Adds key 3 with value 3. Cache is now {1=1, 3=3}.
get(2): Returns -1 as key 2 was evicted.
put(4, 4): Evicts the least recently used key 1 and adds key 4 with value 4. Cache is now {3=3, 4=4}.
get(1): Returns -1 as key 1 was evicted.
get(3): Returns 3, and moves key 3 to the front. Cache is now {4=4, 3=3}.
get(4): Returns 4. Cache is now {3=3, 4=4}.
This is a classic implementation of the LRU cache using both a hash map and a doubly linked list to achieve optimal time complexity for cache operations.
 * 
 * 
 */

public class LRUCache146 {
    // Doubly Linked List Node
    private class Node {
        int key, value;
        Node prev, next;
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final int capacity;
    private final HashMap<Integer, Node> cache; // Maps key to Node
    private final Node head, tail; // Dummy head and tail to simplify code

    public LRUCache146(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.head = new Node(0, 0); // Dummy head
        this.tail = new Node(0, 0); // Dummy tail
        head.next = tail;  // Initially, head points to tail
        tail.prev = head;  // Initially, tail points to head
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            moveToFront(node);  // Move the accessed node to the front
            return node.value;
        }
        return -1;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.value = value;  // Update value
            moveToFront(node);  // Move the updated node to the front
        } else {
            if (cache.size() >= capacity) {
                removeLRU();  // Remove least recently used node if capacity is full
            }
            Node newNode = new Node(key, value);
            cache.put(key, newNode);  // Insert the new node in the hash map
            addToFront(newNode);  // Add the new node to the front of the doubly linked list
        }
    }

    private void moveToFront(Node node) {
        removeNode(node);
        addToFront(node);
    }

    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void addToFront(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }

    private void removeLRU() {
        Node lru = tail.prev;
        cache.remove(lru.key);
        removeNode(lru);
    }
    
    public static void main(String[] args) {
        LRUCache146 cache = new LRUCache146(2);
        
        cache.put(1, 1);   // Cache is {1=1}
        cache.put(2, 2);   // Cache is {1=1, 2=2}
        System.out.println(cache.get(1)); // Returns 1, Cache is {2=2, 1=1}
        cache.put(3, 3);   // LRU key was 2, evicts key 2, Cache is {1=1, 3=3}
        System.out.println(cache.get(2)); // Returns -1 (not found)
        cache.put(4, 4);   // LRU key was 1, evicts key 1, Cache is {3=3, 4=4}
        System.out.println(cache.get(1)); // Returns -1 (not found)
        System.out.println(cache.get(3)); // Returns 3, Cache is {4=4, 3=3}
        System.out.println(cache.get(4)); // Returns 4, Cache is {3=3, 4=4}
    }
}
