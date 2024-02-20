"""
238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self
"""

from unittest import TestCase

from src.product_of_array_except_self import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [24, 12, 8, 6]
        assert Solution().productExceptSelf([1, 2, 3, 4]) == exp

    def test_2(self):
        exp = [0, 0, 9, 0, 0]
        assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == exp
