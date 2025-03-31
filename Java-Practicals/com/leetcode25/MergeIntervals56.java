package com.leetcode25;
import java.util.*;

/**
 * The Merge Intervals problem (LeetCode #56) asks you to merge all overlapping intervals in a list and return the merged intervals.
Problem Description:
You are given an array of intervals where intervals[i] = [start_i, end_i], and you need to merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example:
Input:
intervals = [[1,3], [2,6], [8,10], [15,18]]
Output:
[[1,6], [8,10], [15,18]]
Explanation:
The intervals [1, 3] and [2, 6] overlap, so they are merged into [1, 6].
The other intervals [8, 10] and [15, 18] don't overlap, so they remain the same.
Approach:
Sort the Intervals:
First, we need to sort the intervals based on their start value. This will allow us to process the intervals in order, ensuring we can easily check for overlaps.
Merge Intervals:
After sorting, we iterate through the intervals. For each interval, we check if it overlaps with the last interval in the merged list.
If it does overlap (i.e., the start of the current interval is less than or equal to the end of the last merged interval), we merge them by updating the end of the last merged interval to the maximum of the current interval’s end and the last merged interval’s end.
If it doesn’t overlap, we simply add the current interval to the merged list.
Return the Merged Intervals:
After processing all intervals, the merged list will contain the non-overlapping intervals.

Explanation:
Sorting the Intervals:
We sort the input intervals based on the starting value. This helps in processing the intervals in the correct order.
The sorting step ensures that we can easily compare the current interval with the last merged interval.
Merging Intervals:
We start by adding the first interval to the merged list.
Then, for each subsequent interval, we check if it overlaps with the last interval in the merged list:
If it does overlap (i.e., current[0] <= lastMerged[1]), we merge the two intervals by updating the end of the last merged interval to be the maximum of the current and last merged interval's end values (Math.max(lastMerged[1], current[1])).
If it does not overlap, we simply add the current interval to the merged list.
Returning the Result:
The merged list now contains the non-overlapping intervals, which we return as the result.
Time Complexity:
Sorting the intervals takes O(n log n), where n is the number of intervals.
The subsequent iteration to merge the intervals takes O(n).
Thus, the overall time complexity is O(n log n) due to the sorting step.
Space Complexity:
O(n), as we are storing the merged intervals in a list, which may contain at most n intervals.
Example Walkthrough:
Input:
intervals = [[1,3], [2,6], [8,10], [15,18]]
Step 1: Sort the intervals:
After sorting, the intervals are: [[1, 3], [2, 6], [8, 10], [15, 18]].
Step 2: Start with the first interval [1, 3] and add it to the merged list: merged = [[1, 3]].
Step 3: Compare [2, 6] with [1, 3]:
Since 2 <= 3, the intervals overlap. Merge them into [1, 6]. Update the merged list: merged = [[1, 6]].
Step 4: Compare [8, 10] with [1, 6]:
Since 8 > 6, the intervals do not overlap. Add [8, 10] to the merged list: merged = [[1, 6], [8, 10]].
Step 5: Compare [15, 18] with [8, 10]:
Since 15 > 10, the intervals do not overlap. Add [15, 18] to the merged list: merged = [[1, 6], [8, 10], [15, 18]].
Output:
[[1, 6], [8, 10], [15, 18]]
Final Thoughts:
This solution efficiently merges overlapping intervals in O(n log n) time complexity by using sorting and a simple linear pass through the intervals. The key is to process the intervals in sorted order and merge them when necessary, ensuring that all overlapping intervals are combined into one.
 * 
 * 
 * 
 */

public class MergeIntervals56 {

    public List<int[]> merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return new ArrayList<>();
        }

        // Sort intervals based on the start value
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        // Initialize a list to store merged intervals
        List<int[]> merged = new ArrayList<>();

        // Start with the first interval
        merged.add(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            // Get the last merged interval and the current interval
            int[] lastMerged = merged.get(merged.size() - 1);
            int[] current = intervals[i];

            // If the current interval overlaps with the last merged interval, merge them
            if (current[0] <= lastMerged[1]) {
                lastMerged[1] = Math.max(lastMerged[1], current[1]);
            } else {
                // Otherwise, add the current interval to the merged list
                merged.add(current);
            }
        }

        return merged;
    }

    public static void main(String[] args) {
        MergeIntervals56 solution = new MergeIntervals56();

        // Test case
        int[][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
        List<int[]> mergedIntervals = solution.merge(intervals);

        // Print merged intervals
        for (int[] interval : mergedIntervals) {
            System.out.println("[" + interval[0] + ", " + interval[1] + "]");
        }
    }
}
