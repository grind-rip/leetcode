"""
424. Longest Repeating Character Replacement

https://leetcode.com/problems/longest-repeating-character-replacement
"""

from unittest import TestCase

from src.longest_repeating_character_replacement import CanonicalSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = 4
        assert Solution().characterReplacement(s="ABAB", k=2) == exp

    def test_2(self):
        exp = 4
        assert Solution().characterReplacement(s="AABABBA", k=1) == exp

    def test_3(self):
        exp = 4
        assert Solution().characterReplacement(s="ABBB", k=2) == exp


class TestCanonicalSolution(TestCase):
    def test_1(self):
        exp = 4
        assert CanonicalSolution().characterReplacement(s="ABAB", k=2) == exp

    def test_2(self):
        exp = 4
        assert CanonicalSolution().characterReplacement(s="AABABBA", k=1) == exp

    def test_3(self):
        exp = 4
        assert CanonicalSolution().characterReplacement(s="ABBB", k=2) == exp
