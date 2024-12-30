"""
198. House Robber

https://leetcode.com/problems/house-robber
"""

from unittest import TestCase

from src.house_robber import MemoizationSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = 4
        assert Solution().rob([1, 2, 3, 1]) == exp

    def test_2(self):
        exp = 12
        assert Solution().rob([2, 7, 9, 3, 1]) == exp

    def test_3(self):
        exp = 0
        assert Solution().rob([0]) == exp

    def test_4(self):
        exp = 1
        assert Solution().rob([1, 1]) == exp


class TestMemoizationSolution(TestCase):
    def test_1(self):
        exp = 4
        assert MemoizationSolution().rob([1, 2, 3, 1]) == exp

    def test_2(self):
        exp = 12
        assert MemoizationSolution().rob([2, 7, 9, 3, 1]) == exp

    def test_3(self):
        exp = 0
        assert MemoizationSolution().rob([0]) == exp

    def test_4(self):
        exp = 1
        assert MemoizationSolution().rob([1, 1]) == exp
