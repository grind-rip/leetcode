"""
217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate
"""

from unittest import TestCase

from src.contains_duplicate import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        assert Solution().containsDuplicate([1, 2, 3, 1]) == exp

    def test_2(self):
        exp = False
        assert Solution().containsDuplicate([1, 2, 3, 4]) == exp

    def test_3(self):
        exp = True
        assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == exp
