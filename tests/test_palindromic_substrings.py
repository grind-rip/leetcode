"""
647. Palindromic Substrings

https://leetcode.com/problems/palindromic-substrings
"""

from unittest import TestCase

from src.palindromic_substrings import (
    ExpansionAroundCentersSolution,
    ManachersAlgorithmSolution,
    Solution,
)


class TestSolution(TestCase):
    def test_1(self):
        exp = 3
        assert Solution().countSubstrings("abc") == exp

    def test_2(self):
        exp = 6
        assert Solution().countSubstrings("aaa") == exp


class TestExpansionAroundCentersSolution(TestCase):
    def test_1(self):
        exp = 3
        assert ExpansionAroundCentersSolution().countSubstrings("abc") == exp

    def test_2(self):
        exp = 6
        assert ExpansionAroundCentersSolution().countSubstrings("aaa") == exp


class TestManachersAlgorithmSolution(TestCase):
    def test_1(self):
        exp = 3
        assert ManachersAlgorithmSolution().countSubstrings("abc") == exp

    def test_2(self):
        exp = 6
        assert ManachersAlgorithmSolution().countSubstrings("aaa") == exp
