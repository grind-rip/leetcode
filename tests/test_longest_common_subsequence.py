"""
1143. Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence
"""

from unittest import TestCase

from src.longest_common_subsequence import (
    MemoizationSolution,
    RecursiveSolution,
    Solution,
)


class TestSolution(TestCase):
    def test_1(self):
        exp = 3
        assert Solution().longestCommonSubsequence("abcde", "ace") == exp

    def test_2(self):
        exp = 3
        assert Solution().longestCommonSubsequence("abc", "abc") == exp

    def test_3(self):
        exp = 0
        assert Solution().longestCommonSubsequence("abc", "def") == exp

    def test_4(self):
        exp = 4
        assert Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == exp


class TestMemoizationSolution(TestCase):
    def test_1(self):
        exp = 3
        assert MemoizationSolution().longestCommonSubsequence("abcde", "ace") == exp

    def test_2(self):
        exp = 3
        assert MemoizationSolution().longestCommonSubsequence("abc", "abc") == exp

    def test_3(self):
        exp = 0
        assert MemoizationSolution().longestCommonSubsequence("abc", "def") == exp

    def test_4(self):
        exp = 4
        assert MemoizationSolution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == exp


class TestRecursiveSolution(TestCase):
    def test_1(self):
        exp = 3
        assert RecursiveSolution().longestCommonSubsequence("abcde", "ace") == exp

    def test_2(self):
        exp = 3
        assert RecursiveSolution().longestCommonSubsequence("abc", "abc") == exp

    def test_3(self):
        exp = 0
        assert RecursiveSolution().longestCommonSubsequence("abc", "def") == exp

    def test_4(self):
        exp = 4
        assert MemoizationSolution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == exp
