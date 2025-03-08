"""
5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring
"""

from unittest import TestCase

from src.longest_palindromic_substring import (
    ExpansionAroundCentersSolution,
    ManachersAlgorithmSolution,
    Solution,
)


class TestSolution(TestCase):
    def test_1(self):
        exp = ["bab", "aba"]
        assert Solution().longestPalindrome("babad") in exp

    def test_2(self):
        exp = "bb"
        assert Solution().longestPalindrome("cbbd") == exp


class TestExpansionAroundCentersSolution(TestCase):
    def test_1(self):
        exp = ["bab", "aba"]
        assert Solution().longestPalindrome("babad") in exp

    def test_2(self):
        exp = "bb"
        assert ExpansionAroundCentersSolution().longestPalindrome("cbbd") == exp


class TestManachersAlgorithmSolution(TestCase):
    def test_1(self):
        exp = ["bab", "aba"]
        assert Solution().longestPalindrome("babad") in exp

    def test_2(self):
        exp = "bb"
        assert ManachersAlgorithmSolution().longestPalindrome("cbbd") == exp
