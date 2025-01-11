"""
242. Valid Anagram

https://leetcode.com/problems/valid-anagram
"""

from unittest import TestCase

from src.valid_anagram import SimplifiedSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        assert Solution().isAnagram("anagram", "nagaram") == exp

    def test_2(self):
        exp = False
        assert Solution().isAnagram("rat", "car") == exp


class TestSimplifiedSolution(TestCase):
    def test_1(self):
        exp = True
        assert SimplifiedSolution().isAnagram("anagram", "nagaram") == exp

    def test_2(self):
        exp = False
        assert SimplifiedSolution().isAnagram("abc", "def") == exp
