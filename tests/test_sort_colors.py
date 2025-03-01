"""
75. Sort Colors

https://leetcode.com/problems/sort-colors
"""

from unittest import TestCase

from src.sort_colors import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [0, 0, 1, 1, 2, 2]
        nums = [2, 0, 2, 1, 1, 0]
        Solution().sortColors(nums)
        assert nums == exp

    def test_2(self):
        exp = [0, 1, 2]
        nums = [2, 0, 1]
        Solution().sortColors(nums)
        assert nums == exp
