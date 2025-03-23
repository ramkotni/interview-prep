Overlapping Intervals

The Overlapping Intervals pattern is used to merge or handle overlapping intervals in an array.

In an interval array sorted by start time, two intervals [a, b] and [c, d] overlap if b >= c (i.e., the end time of the first interval is greater than or equal to the start time of the second interval).

Sample Problem:
Problem Statement: Merge all overlapping intervals.

Example:

Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

Output: [[1, 6], [8, 10], [15, 18]]

Explanation:
Sort the intervals by their start time.

Create an empty list called merged to store the merged intervals.

Iterate through the intervals and check if it overlaps with the last interval in the merged list.

If it overlaps, merge the intervals by updating the end time of the last interval in merged.

If it does not overlap, simply add the current interval to the merged list.

LeetCode Problems:
Merge Intervals (LeetCode #56)

Insert Interval (LeetCode #57)

Non-Overlapping Intervals (LeetCode #435)

The Overlapping Intervals pattern is used to merge overlapping intervals or handle cases where intervals may or may not overlap. Below are the solutions to the Overlapping Intervals problems that involve merging or inserting intervals.

Problem 1: Merge Intervals (LeetCode #56)
Problem Statement: Given a collection of intervals, merge all overlapping intervals.

Approach:
Sort Intervals: First, we need to sort the intervals based on their starting times. Sorting is crucial because overlapping intervals will be adjacent after sorting.

Merge Intervals: We initialize an empty list merged to store the merged intervals. Then, we iterate through the sorted intervals:

If the current interval overlaps with the last interval in merged (i.e., the start time of the current interval is less than or equal to the end time of the last interval in merged), we merge them by updating the end time of the last interval.

If there is no overlap, simply add the current interval to merged.

Code Implementation:
java
Copy
import java.util.*;

public class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length == 0) {
            return new int[0][0];
        }

        // Sort intervals by the start time
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        // Initialize the merged intervals list
        List<int[]> merged = new ArrayList<>();
        merged.add(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            // Get the last merged interval
            int[] lastMerged = merged.get(merged.size() - 1);
            int[] current = intervals[i];

            // Check if the current interval overlaps with the last merged interval
            if (current[0] <= lastMerged[1]) {
                // Merge the intervals by updating the end time of the last merged interval
                lastMerged[1] = Math.max(lastMerged[1], current[1]);
            } else {
                // No overlap, add the current interval to the merged list
                merged.add(current);
            }
        }

        // Convert the list to an array and return
        return merged.toArray(new int[merged.size()][]);
    }
}
Explanation:
Sort Intervals: The intervals are first sorted by their start times.

Merge Intervals: We iterate over the sorted intervals and merge them if they overlap by adjusting the end time. If they don't overlap, we simply add the current interval to the result list.

Return Result: The merged intervals are returned as an array.

Time Complexity:
Sorting the intervals takes O(n log n), where n is the number of intervals.

Merging the intervals takes O(n).

Thus, the total time complexity is O(n log n).

Example Input and Output:
Input:

java
Copy
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output:

java
Copy
[[1, 6], [8, 10], [15, 18]]
Problem 2: Insert Interval (LeetCode #57)
Problem Statement: Given a set of non-overlapping intervals and a new interval, insert the new interval into the correct position, ensuring that the intervals remain non-overlapping. If the new interval overlaps with any existing intervals, merge them.

Approach:
Sort and Merge:

First, handle the non-overlapping intervals and insert the new interval where appropriate.

After insertion, merge any overlapping intervals using the same strategy as in the Merge Intervals problem.

Code Implementation:
java
Copy
import java.util.*;

public class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        
        int i = 0;
        
        // Add all intervals that come before the newInterval
        while (i < intervals.length && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i]);
            i++;
        }
        
        // Merge the newInterval with overlapping intervals
        while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        
        // Add the merged newInterval
        result.add(newInterval);
        
        // Add the remaining intervals
        while (i < intervals.length) {
            result.add(intervals[i]);
            i++;
        }
        
        return result.toArray(new int[result.size()][]);
    }
}
Explanation:
Add Non-overlapping Intervals: We first add all intervals that do not overlap with the newInterval to the result list.

Merge Overlapping Intervals: For any intervals that overlap with newInterval, we merge them by adjusting the start and end times of newInterval.

Add Remaining Intervals: After handling the overlaps, we add any remaining intervals that do not overlap with newInterval.

Time Complexity:
O(n), where n is the number of intervals. We traverse the list of intervals once.

Example Input and Output:
Input:

java
Copy
intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
Output:

java
Copy
[[1, 5], [6, 9]]
Problem 3: Non-Overlapping Intervals (LeetCode #435)
Problem Statement: Given an array of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Approach:
Sort the Intervals: Sort the intervals by their end times. The idea is to keep as many non-overlapping intervals as possible by always picking the interval that ends the earliest.

Greedy Strategy: Iterate over the intervals and count how many overlaps there are. For each overlap, we choose to remove the interval that ends later to maximize the number of non-overlapping intervals.

Code Implementation:
java
Copy
import java.util.*;

public class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        
        // Sort intervals by the end time
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        
        int count = 0;
        int end = intervals[0][1];
        
        for (int i = 1; i < intervals.length; i++) {
            // If the current interval starts before the last one ends, we have an overlap
            if (intervals[i][0] < end) {
                count++;  // Remove one of the overlapping intervals
            } else {
                // Otherwise, we can safely include this interval
                end = intervals[i][1];
            }
        }
        
        return count;
    }
}
Explanation:
Sort Intervals: Sort the intervals by their end time to apply a greedy strategy. The idea is to always keep the interval that ends first.

Greedy Removal: We keep track of the end time of the last added interval. If the next interval overlaps (its start time is less than the end), we increment the count of intervals to remove. Otherwise, we update the end time.

Time Complexity:
O(n log n) for sorting the intervals, where n is the number of intervals.

O(n) for iterating through the intervals.

Thus, the total time complexity is O(n log n).

Example Input and Output:
Input:

java
Copy
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output:

java
Copy
1
Summary:
Merge Intervals: Sort the intervals, and merge overlapping intervals by comparing the current interval with the last merged one.

Insert Interval: Insert the new interval into the sorted intervals and merge overlapping intervals.

Non-Overlapping Intervals: Sort the intervals by their end times, and use a greedy strategy to remove the minimum number of overlapping intervals.

All solutions use sorting (O(n log n)) and a single pass through the intervals (O(n)), making them efficient for large inputs.
