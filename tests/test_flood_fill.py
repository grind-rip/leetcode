"""
733. Flood Fill

https://leetcode.com/problems/flood-fill
"""

from unittest import TestCase

from src.flood_fill import Solution, SolutionDFS


class TestSolution(TestCase):
    def test_1(self):
        exp = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        assert Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == exp

    def test_2(self):
        exp = [[0, 0, 0], [0, 0, 0]]
        assert Solution().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == exp


class TestSolutionDFS(TestCase):
    def test_1(self):
        exp = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        assert (
            SolutionDFS().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == exp
        )

    def test_2(self):
        exp = [[0, 0, 0], [0, 0, 0]]
        assert SolutionDFS().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == exp
