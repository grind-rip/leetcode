"""
76. Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring
"""

from unittest import TestCase

from src.minimum_window_substring import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = "BANC"
        assert Solution().minWindow("ADOBECODEBANC", "ABC") == exp

    def test_2(self):
        exp = "a"
        assert Solution().minWindow("a", "a") == exp

    def test_3(self):
        exp = ""
        assert Solution().minWindow("a", "aa") == exp

    def test_4(self):
        exp = "ba"
        assert Solution().minWindow("bba", "ab") == exp
