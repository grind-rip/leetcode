"""
739. Daily Temperatures

https://leetcode.com/problems/daily-temperatures
"""

from unittest import TestCase

from src.daily_temperatures import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 1, 4, 2, 1, 1, 0, 0]
        assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == exp

    def test_2(self):
        exp = [1, 1, 1, 0]
        assert Solution().dailyTemperatures([30, 40, 50, 60]) == exp

    def test_3(self):
        exp = [1, 1, 0]
        assert Solution().dailyTemperatures([30, 60, 90]) == exp

    def test_4(self):
        exp = [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
        assert (
            Solution().dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
            == exp
        )
