"""
252. Meeting Rooms

https://leetcode.com/problems/meeting-rooms
"""

from unittest import TestCase

from src.meeting_rooms import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = False
        assert Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]) == exp

    def test_2(self):
        exp = True
        assert Solution().canAttendMeetings([[7, 10], [2, 4]]) == exp
