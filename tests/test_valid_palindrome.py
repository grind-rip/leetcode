"""
125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome
"""

from unittest import TestCase

from src.valid_palindrome import SimplifiedSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        assert Solution().isPalindrome("A man, a plan, a canal: Panama") == exp

    def test_2(self):
        exp = False
        assert Solution().isPalindrome("race a car") == exp

    def test_3(self):
        exp = True
        assert Solution().isPalindrome("") == exp

    def test_4(self):
        exp = True
        assert Solution().isPalindrome(" ") == exp


class TestSimplifiedSolution(TestCase):
    def test_1(self):
        exp = True
        assert (
            SimplifiedSolution().isPalindrome("A man, a plan, a canal: Panama") == exp
        )

    def test_2(self):
        exp = False
        assert SimplifiedSolution().isPalindrome("race a car") == exp

    def test_3(self):
        exp = True
        assert SimplifiedSolution().isPalindrome("") == exp

    def test_4(self):
        exp = True
        assert SimplifiedSolution().isPalindrome(" ") == exp
