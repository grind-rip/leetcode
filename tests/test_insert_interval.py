"""
57. Insert Interval

https://leetcode.com/problems/insert-interval
"""

from unittest import TestCase

from src.insert_interval import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [[1, 5], [6, 9]]
        assert Solution().insert([[1, 3], [6, 9]], [2, 5]) == exp

    def test_2(self):
        exp = [[1, 2], [3, 10], [12, 16]]
        assert (
            Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
            == exp
        )
