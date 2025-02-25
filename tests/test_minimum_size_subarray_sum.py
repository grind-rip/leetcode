"""
209. Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum
"""

from unittest import TestCase

from src.minimum_size_subarray_sum import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = 2
        assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == exp

    def test_2(self):
        exp = 1
        assert Solution().minSubArrayLen(4, [1, 4, 4]) == exp

    def test_3(self):
        exp = 0
        assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == exp
