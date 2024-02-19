"""
1. Two Sum

https://leetcode.com/problems/two-sum
"""
from unittest import TestCase

from src.two_sum import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [0, 1]
        assert Solution().twoSum([2, 7, 11, 15], 9) == exp

    def test_2(self):
        exp = [1, 2]
        assert Solution().twoSum([3, 2, 4], 6) == exp

    def test_3(self):
        exp = [0, 1]
        assert Solution().twoSum([3, 3], 6) == exp
