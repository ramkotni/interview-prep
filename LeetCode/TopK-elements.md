Top ‘K’ Elements

The Top 'K' Elements pattern finds the top k largest or smallest elements in an array or stream of data using heaps or sorting.

Sample Problem:
Find the k-th largest element in an unsorted array.

Example:

Input: nums = [3, 2, 1, 5, 6, 4], k = 2

Output: 5

Explanation:
Use a min-heap of size k to keep track of the k largest elements.

Iterate through the array, adding elements to the heap.

If the heap size exceeds k, remove the smallest element from the heap.

The root of the heap will be the k-th largest element.

LeetCode Problems:
Kth Largest Element in an Array (LeetCode #215)

Top K Frequent Elements (LeetCode #347)

Find K Pairs with Smallest Sums (LeetCode #373)

Sure! Below are the solutions to the Top 'K' Elements problems using heaps or sorting.

The Top 'K' Elements pattern is useful when you're asked to find the k-th largest or k-th smallest element in an array, or find the k most frequent elements in an array, and so on.

Problem 1: Kth Largest Element in an Array (LeetCode #215)
Problem Statement: Find the k-th largest element in an unsorted array. Note that it is not the k-th distinct element.

Approach:
Min-Heap:

We can use a min-heap of size k to keep track of the k largest elements.

As we iterate through the array, if the heap has fewer than k elements, we add the current element.

If the heap already contains k elements, we only add the current element if it's larger than the smallest element (the root of the heap).

If we add a new element, we remove the smallest element to maintain the heap size of k.

The root of the min-heap will be the k-th largest element.

Code Implementation:
java
Copy
import java.util.PriorityQueue;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Min-heap to store the k largest elements
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);

        for (int num : nums) {
            minHeap.offer(num);  // Add the current element to the heap
            if (minHeap.size() > k) {
                minHeap.poll();  // Remove the smallest element to maintain size k
            }
        }
        
        return minHeap.peek();  // The root of the heap is the k-th largest element
    }
}
Explanation:
Min-Heap: We create a PriorityQueue (min-heap) of size k to store the largest k elements.

Iterate through the array: For each element in the array:

Add the element to the heap.

If the heap exceeds size k, remove the smallest element (poll).

Return the root: After processing all elements, the root of the heap contains the k-th largest element.

Time Complexity:
O(n log k) where n is the number of elements in the array. We process each element and perform a log k operation for each insert and removal from the heap.

Example Input and Output:
Input:

java
Copy
nums = [3, 2, 1, 5, 6, 4], k = 2
Output:

java
Copy
5
Problem 2: Top K Frequent Elements (LeetCode #347)
Problem Statement: Given a non-empty array of integers, return the k most frequent elements.

Approach:
Frequency Map: First, we count the frequency of each element using a hashmap.

Max-Heap: We can use a max-heap to keep track of the k most frequent elements. Each element will be paired with its frequency, and the heap will be sorted based on frequency.

We use a min-heap of size k to store the top k frequent elements.

Heap Operations: For each element:

Add the element-frequency pair to the heap.

If the heap exceeds size k, remove the element with the smallest frequency.

Code Implementation:
java
Copy
import java.util.*;

public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Step 1: Count the frequency of each number
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // Step 2: Use a priority queue (min-heap) to store the k most frequent elements
        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(
            (a, b) -> a.getValue() - b.getValue()
        );

        // Step 3: Add each entry to the heap
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > k) {
                minHeap.poll();  // Remove the least frequent element
            }
        }

        // Step 4: Extract the top k elements from the heap
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = minHeap.poll().getKey();  // Get the key (element)
        }
        
        return result;
    }
}
Explanation:
Frequency Map: We first count how many times each element appears in the array.

Min-Heap: We use a PriorityQueue (min-heap) to store the k most frequent elements. The heap stores the elements sorted by frequency in ascending order.

Heap Operations: After adding each element-frequency pair to the heap:

If the heap exceeds size k, we remove the element with the smallest frequency.

Result Construction: Finally, we extract the top k frequent elements from the heap.

Time Complexity:
O(n log k) where n is the number of elements in the input array, and k is the number of most frequent elements we want to retrieve.

Example Input and Output:
Input:

java
Copy
nums = [1,1,1,2,2,3], k = 2
Output:

java
Copy
[1, 2]
Problem 3: Find K Pairs with Smallest Sums (LeetCode #373)
Problem Statement: Given two sorted integer arrays nums1 and nums2, return the k smallest sum pairs from the two arrays. A pair (i, j) is valid if nums1[i] + nums2[j] is a valid sum.

Approach:
Min-Heap: We can use a min-heap to find the smallest sum pairs. Initially, we push the pair (0, 0) into the heap, which corresponds to the sum of the first elements from both arrays.

Heap Operations: Pop the smallest pair from the heap, and for each pair, we add the next potential pair to the heap. Specifically, for a pair (i, j), we add pairs (i+1, j) and (i, j+1) to the heap.

Avoid Duplicates: To avoid duplicate pairs, we use a set to track the visited pairs.

Code Implementation:
java
Copy
import java.util.*;

public class Solution {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<int[]> result = new ArrayList<>();
        
        if (nums1.length == 0 || nums2.length == 0 || k == 0) {
            return result;
        }

        // Min-heap to store pairs (sum, i, j)
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            (a, b) -> (nums1[a[0]] + nums2[a[1]]) - (nums1[b[0]] + nums2[b[1]])
        );

        // Initialize the heap with the first row of possible pairs (0, j)
        for (int i = 0; i < nums1.length; i++) {
            minHeap.offer(new int[]{i, 0});
        }

        // Extract the smallest pairs from the heap and add the next pairs
        while (k-- > 0 && !minHeap.isEmpty()) {
            int[] pair = minHeap.poll();
            int i = pair[0], j = pair[1];
            result.add(new int[]{nums1[i], nums2[j]});
            if (j + 1 < nums2.length) {
                minHeap.offer(new int[]{i, j + 1});
            }
        }

        return result;
    }
}
Explanation:
Min-Heap: The heap stores pairs (i, j) and sorts them by the sum nums1[i] + nums2[j].

Heap Initialization: We start by inserting pairs formed by nums1[i] and nums2[0] into the heap (for all i).

Extract and Add New Pairs: We pop the smallest sum pair, and for each pair, we add the next possible pair by incrementing the second index j.

Time Complexity:
O(k log n) where n is the smaller size of the two arrays. We push and pop from the heap at most k times, and each heap operation takes O(log n) time.

Example Input and Output:
Input:

java
Copy
nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3
Output:

java
Copy
[[1, 2], [1, 4], [1, 6]]
Summary:
Kth Largest Element in an Array: Use a min-heap of size k to keep track of the k largest elements.

Top K Frequent Elements: Use a min-heap to store the most frequent elements based on their counts.

Find K Pairs with Smallest Sums: Use a min-heap to find the k smallest sum pairs from two sorted arrays.

All these solutions efficiently solve the problems in O(n log k) or O(k log n) time complexity, making them suitable for large inputs.



