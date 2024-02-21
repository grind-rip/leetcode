"""
70. Climbing Stairs

https://leetcode.com/problems/climbing-stairs
"""

from unittest import TestCase

from src.climbing_stairs import BruteForceSolution, MemoizationSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = 2
        assert Solution().climbStairs(2) == exp

    def test_2(self):
        exp = 3
        assert Solution().climbStairs(3) == exp

    def test_3(self):
        exp = 8
        assert Solution().climbStairs(5) == exp


class TestMemoizationSolution(TestCase):
    def test_1(self):
        exp = 2
        assert MemoizationSolution().climbStairs(2) == exp

    def test_2(self):
        exp = 3
        assert MemoizationSolution().climbStairs(3) == exp

    def test_3(self):
        exp = 8
        assert MemoizationSolution().climbStairs(5) == exp


class BruteForceSolutionSolution(TestCase):
    def test_1(self):
        exp = 2
        assert BruteForceSolution().climbStairs(2) == exp

    def test_2(self):
        exp = 3
        assert BruteForceSolution().climbStairs(3) == exp

    def test_3(self):
        exp = 8
        assert BruteForceSolution().climbStairs(5) == exp
