"""
435. Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals

NOTES
  * A common routine for interval problems is to sort the array of intervals
    by each interval's starting index.

We start by sorting the interval array by starting index (O(nlog n)). Since the
starting index is now monotonically increasing, we remove overlapping intervals
while taking the lower ending index until there is no overlap.
"""

import sys


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count, lo = 0, -sys.maxsize
        for interval in intervals:
            if interval[0] < lo:
                count += 1
                lo = min(lo, interval[1])
            else:
                lo = interval[1]
        return count
