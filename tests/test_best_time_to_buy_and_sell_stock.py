"""
121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""

from unittest import TestCase

from src.best_time_to_buy_and_sell_stock import NaiveSolution, OptimizedNaiveSolution, Solution, TwoPointersSolution


class TestSolution(TestCase):
    def test_1(self):
        exp = 5
        assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == exp

    def test_2(self):
        exp = 0
        assert Solution().maxProfit([7, 6, 4, 3, 1]) == exp

    def test_3(self):
        exp = 2
        assert Solution().maxProfit([2, 4, 1]) == exp


class TestTwoPointersSolution(TestCase):
    def test_1(self):
        exp = 5
        assert TwoPointersSolution().maxProfit([7, 1, 5, 3, 6, 4]) == exp

    def test_2(self):
        exp = 0
        assert TwoPointersSolution().maxProfit([7, 6, 4, 3, 1]) == exp

    def test_3(self):
        exp = 2
        assert TwoPointersSolution().maxProfit([2, 4, 1]) == exp


class TestOptimizedNaiveSolution(TestCase):
    def test_1(self):
        exp = 5
        assert OptimizedNaiveSolution().maxProfit([7, 1, 5, 3, 6, 4]) == exp

    def test_2(self):
        exp = 0
        assert OptimizedNaiveSolution().maxProfit([7, 6, 4, 3, 1]) == exp

    def test_3(self):
        exp = 2
        assert OptimizedNaiveSolution().maxProfit([2, 4, 1]) == exp


class TestNaiveSolution(TestCase):
    def test_1(self):
        exp = 5
        assert NaiveSolution().maxProfit([7, 1, 5, 3, 6, 4]) == exp

    def test_2(self):
        exp = 0
        assert NaiveSolution().maxProfit([7, 6, 4, 3, 1]) == exp

    def test_3(self):
        exp = 2
        assert NaiveSolution().maxProfit([2, 4, 1]) == exp
