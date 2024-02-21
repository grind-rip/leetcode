"""
322. Coin Change

https://leetcode.com/problems/coin-change
"""

from unittest import TestCase

from src.coin_change import BruteForceSolution, MemoizationSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = 3
        assert Solution().coinChange([1, 2, 5], 11) == exp

    def test_2(self):
        exp = -1
        assert Solution().coinChange([2], 3) == exp

    def test_3(self):
        exp = 0
        assert Solution().coinChange([1], 0) == exp


class TestMemoizationSolutionSolution(TestCase):
    def test_1(self):
        exp = 2
        assert MemoizationSolution().coinChange([1, 2, 3], 6) == exp

    def test_2(self):
        exp = -1
        assert MemoizationSolution().coinChange([2], 3) == exp

    def test_3(self):
        exp = 0
        assert MemoizationSolution().coinChange([1], 0) == exp


class TestBruteForceSolution(TestCase):
    def test_1(self):
        exp = 3
        assert BruteForceSolution().coinChange([1, 2, 5], 11) == exp

    def test_2(self):
        exp = -1
        assert BruteForceSolution().coinChange([2], 3) == exp

    def test_3(self):
        exp = 0
        assert BruteForceSolution().coinChange([1], 0) == exp
