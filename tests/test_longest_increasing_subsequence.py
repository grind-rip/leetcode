"""
300. Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence
"""

from unittest import TestCase

from src.longest_increasing_subsequence import (
    MemoizationSolution,
    RecursiveSolution,
    Solution,
)


class TestSolution(TestCase):
    def test_1(self):
        exp = 4
        assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == exp

    def test_2(self):
        exp = 4
        assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == exp

    def test_3(self):
        exp = 1
        assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == exp

    def test_4(self):
        exp = 3
        assert Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]) == exp

    def test_5(self):
        exp = 6
        assert Solution().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]) == exp


class TestMemoizationSolution(TestCase):
    def test_1(self):
        exp = 4
        assert MemoizationSolution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == exp

    def test_2(self):
        exp = 4
        assert MemoizationSolution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == exp

    def test_3(self):
        exp = 1
        assert MemoizationSolution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == exp

    def test_4(self):
        exp = 3
        assert MemoizationSolution().lengthOfLIS([4, 10, 4, 3, 8, 9]) == exp

    def test_5(self):
        exp = 6
        assert (
            MemoizationSolution().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12])
            == exp
        )


class TestRecursiveSolution(TestCase):
    def test_1(self):
        exp = 4
        assert RecursiveSolution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == exp

    def test_2(self):
        exp = 4
        assert RecursiveSolution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == exp

    def test_3(self):
        exp = 1
        assert RecursiveSolution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == exp

    def test_4(self):
        exp = 3
        assert RecursiveSolution().lengthOfLIS([4, 10, 4, 3, 8, 9]) == exp

    def test_5(self):
        exp = 6
        assert (
            RecursiveSolution().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]) == exp
        )
