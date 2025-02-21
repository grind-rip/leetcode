"""
53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray
"""

from unittest import TestCase

from src.maximum_subarray import Solution, TabularizationSolution


class TestSolution(TestCase):
    def test_1(self):
        exp = 6
        assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == exp

    def test_2(self):
        exp = 1
        assert Solution().maxSubArray([1]) == exp

    def test_3(self):
        exp = 23
        assert Solution().maxSubArray([5, 4, -1, 7, 8]) == exp


class TestTabularizationSolution(TestCase):
    def test_1(self):
        exp = 6
        assert (
            TabularizationSolution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == exp
        )

    def test_2(self):
        exp = 1
        assert TabularizationSolution().maxSubArray([1]) == exp

    def test_3(self):
        exp = 23
        assert TabularizationSolution().maxSubArray([5, 4, -1, 7, 8]) == exp
