"""
159. Longest Substring with At Most Two Distinct Characters

https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters
"""

from unittest import TestCase

from src.longest_substring_with_at_most_two_distinct_characters import (
    GeneralSolution,
    Solution,
)


class TestSolution(TestCase):
    def test_1(self):
        exp = 3
        assert Solution().lengthOfLongestSubstringTwoDistinct("eceba") == exp

    def test_2(self):
        exp = 5
        assert Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb") == exp

    def test_3(self):
        exp = 1
        assert Solution().lengthOfLongestSubstringTwoDistinct("a") == exp


class TestGeneralSolution(TestCase):
    def test_1(self):
        exp = 3
        assert GeneralSolution().lengthOfLongestSubstringTwoDistinct("eceba") == exp

    def test_2(self):
        exp = 5
        assert GeneralSolution().lengthOfLongestSubstringTwoDistinct("ccaabbb") == exp

    def test_3(self):
        exp = 1
        assert GeneralSolution().lengthOfLongestSubstringTwoDistinct("a") == exp
