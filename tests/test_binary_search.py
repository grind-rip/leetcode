"""
704. Binary Search

https://leetcode.com/problems/binary-search
"""

from unittest import TestCase

from src.binary_search import (
    Solution,
)


class TestSolution(TestCase):
    def test_1(self):
        exp = 4
        assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == exp

    def test_2(self):
        exp = -1
        assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == exp
