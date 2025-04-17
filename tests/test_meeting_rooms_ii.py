"""
253. Meeting Rooms II

https://leetcode.com/problems/meeting-rooms-ii
"""

from unittest import TestCase

from src.meeting_rooms_ii import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = 2
        assert Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == exp

    def test_2(self):
        exp = 1
        assert Solution().minMeetingRooms([[7, 10], [2, 4]]) == exp

    def test_3(self):
        exp = 2
        assert Solution().minMeetingRooms([[5, 8], [6, 8]]) == exp

    def test_4(self):
        exp = 2
        assert Solution().minMeetingRooms([[9, 10], [4, 9], [4, 17]]) == exp
