"""
20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses

NOTES
  * Use a stack or two pointers.
"""

from unittest import TestCase

from src.valid_parentheses import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        assert Solution().isValid("()") == exp

    def test_2(self):
        exp = True
        assert Solution().isValid("()[]{}") == exp

    def test_3(self):
        exp = False
        assert Solution().isValid("(])") == exp
