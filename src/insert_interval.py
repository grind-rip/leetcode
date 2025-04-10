"""
57. Insert Interval

https://leetcode.com/problems/insert-interval

NOTES
  * Two key observations are that the intervals are already sorted in ascending
    order by starting index and initially all intervals are non-overlapping.
    Therefore, there are three cases to consider:
      1. The current interval end before the new interval starts (no overlap).
      2. The current interval starts before the new interval ends (overlap).
      3. The current interval starts after the new interval ends (no overlap).
"""


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)
        ans: list[list[int]] = []

        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            # Update the start and end index of newInterval.
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        ans.append(newInterval)

        while i < n:  # Implicit: intervals[i][0] > newInterval[1]
            ans.append(intervals[i])
            i += 1

        return ans
