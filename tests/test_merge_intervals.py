"""
56. Merge Intervals

https://leetcode.com/problems/merge-intervals
"""
from unittest import TestCase

from src.merge_intervals import Solution, OptimizedSolution


class TestSolution(TestCase):
    def test_1(self):
        exp = [[1, 6], [8, 10], [15, 18]]
        assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == exp

    def test_2(self):
        exp = [[1, 5]]
        assert Solution().merge([[1, 4], [4, 5]]) == exp


class TestOptimizedSolution(TestCase):
    def test_1(self):
        exp = [[1, 6], [8, 10], [15, 18]]
        assert OptimizedSolution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == exp

    def test_2(self):
        exp = [[1, 5]]
        assert OptimizedSolution().merge([[1, 4], [4, 5]]) == exp
