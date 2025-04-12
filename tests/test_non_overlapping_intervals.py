"""
435. Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals
"""

from unittest import TestCase

from src.non_overlapping_intervals import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = 1
        assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == exp

    def test_2(self):
        exp = 2
        assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == exp

    def test_3(self):
        exp = 0
        assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == exp
