"""
1768. Merge Strings Alternately

https://leetcode.com/problems/merge-strings-alternately
"""

from unittest import TestCase

from src.merge_strings_alternately import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = "apbqcr"
        assert Solution().mergeAlternately("abc", "pqr") == exp

    def test_2(self):
        exp = "apbqrs"
        assert Solution().mergeAlternately("ab", "pqrs") == exp

    def test_3(self):
        exp = "apbqcd"
        assert Solution().mergeAlternately("abcd", "pq") == exp
