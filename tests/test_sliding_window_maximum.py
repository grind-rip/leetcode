"""
239. Sliding Window Maximum

https://leetcode.com/problems/sliding-window-maximum
"""

from unittest import TestCase

from src.sliding_window_maximum import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [3, 3, 5, 5, 6, 7]
        assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == exp

    def test_2(self):
        exp = [1]
        assert Solution().maxSlidingWindow([1], 1) == exp

    def test_3(self):
        exp = [1, -1]
        assert Solution().maxSlidingWindow([1, -1], 1) == exp
