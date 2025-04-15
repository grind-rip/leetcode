"""
252. Meeting Rooms

https://leetcode.com/problems/meeting-rooms

NOTES
  * Simply sort and check for overlapping intervals.
"""


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
