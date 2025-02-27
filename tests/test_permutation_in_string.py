"""
567. Permutation in String

https://leetcode.com/problems/permutation-in-string
"""

from unittest import TestCase

from src.permutation_in_string import ArraySolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        assert Solution().checkInclusion("ab", "eidbaooo") == exp

    def test_2(self):
        exp = False
        assert Solution().checkInclusion("ab", "eidboaoo") == exp

    def test_3(self):
        exp = False
        assert Solution().checkInclusion("hello", "ooolleoooleh") == exp

    def test_4(self):
        exp = False
        assert Solution().checkInclusion("dd", "rroogzkdktk") == exp


class TestArraySolution(TestCase):
    def test_1(self):
        exp = True
        assert ArraySolution().checkInclusion("ab", "eidbaooo") == exp

    def test_2(self):
        exp = False
        assert ArraySolution().checkInclusion("ab", "eidboaoo") == exp

    def test_3(self):
        exp = False
        assert ArraySolution().checkInclusion("hello", "ooolleoooleh") == exp

    def test_4(self):
        exp = False
        assert ArraySolution().checkInclusion("dd", "rroogzkdktk") == exp
