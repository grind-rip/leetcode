"""
3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters
"""

from unittest import TestCase

from src.longest_substring_without_repeating_characters import (
    CanonicalSolution,
    Solution,
)


class TestSolution(TestCase):
    def test_1(self):
        exp = 3
        assert Solution().lengthOfLongestSubstring("abcabcbb") == exp

    def test_2(self):
        exp = 1
        assert Solution().lengthOfLongestSubstring("bbbbb") == exp

    def test_3(self):
        exp = 3
        assert Solution().lengthOfLongestSubstring("pwwkew") == exp

    def test_4(self):
        exp = 1
        assert Solution().lengthOfLongestSubstring(" ") == exp

    def test_5(self):
        exp = 2
        assert Solution().lengthOfLongestSubstring("abba") == exp


class TestCanonicalSolution(TestCase):
    def test_1(self):
        exp = 3
        assert CanonicalSolution().lengthOfLongestSubstring("abcabcbb") == exp

    def test_2(self):
        exp = 1
        assert CanonicalSolution().lengthOfLongestSubstring("bbbbb") == exp

    def test_3(self):
        exp = 3
        assert CanonicalSolution().lengthOfLongestSubstring("pwwkew") == exp

    def test_4(self):
        exp = 1
        assert CanonicalSolution().lengthOfLongestSubstring(" ") == exp

    def test_5(self):
        exp = 2
        assert CanonicalSolution().lengthOfLongestSubstring("abba") == exp
