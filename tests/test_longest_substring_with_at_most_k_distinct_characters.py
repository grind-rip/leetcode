"""
340. Longest Substring with At Most K Distinct Characters

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
"""

from unittest import TestCase

from src.longest_substring_with_at_most_k_distinct_characters import (
    Solution,
)


class TestSolution(TestCase):
    def test_1(self):
        exp = 3
        assert Solution().lengthOfLongestSubstringKDistinct("eceba", 2) == exp

    def test_2(self):
        exp = 2
        assert Solution().lengthOfLongestSubstringKDistinct("aa", 1) == exp
