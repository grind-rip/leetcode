"""
56. Merge Intervals

https://leetcode.com/problems/merge-intervals

NOTES
  * A common routine for interval problems is to sort the array of intervals
    by each interval's starting index.
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        sorted_intervals = sorted(intervals)
        ans: list[list[int]] = [sorted_intervals[0]]
        # p1 is a pointer into ans. p2 is a pointer into sorted_intervals.
        p1, p2 = 0, 1
        while p2 < len(sorted_intervals):
            if overlap(ans[p1], sorted_intervals[p2]):
                ans[p1] = merge(ans[p1], sorted_intervals[p2])
            else:
                ans.append(sorted_intervals[p2])
                p1 += 1
            p2 += 1
        return ans


def overlap(a: list[int], b: list[int]) -> bool:
    """
    Returns True if `a` and `b` overlap, otherwise returns False.
    """
    return a[0] <= b[1] and b[0] <= a[1]


def merge(a: list[int], b: list[int]) -> list[int]:
    """
    Merges two intervals (`a` and `b`).
    """
    return [min(a[0], b[0]), max(a[1], b[1])]


class OptimizedSolution:
    """
    Since the intervals are already sorted, we only need to check if the end
    index of the last interval is greater than or equal to the start index of
    the current interval.
    """

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged: list[list[int]] = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
