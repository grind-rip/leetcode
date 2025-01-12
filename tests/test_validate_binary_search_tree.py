"""
98. Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree
"""

from unittest import TestCase

from src.validate_binary_search_tree import Solution
from tests.utils import create_binary_tree


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        root = create_binary_tree([2, 1, 3])
        assert Solution().isValidBST(root) == exp

    def test_2(self):
        exp = False
        root = create_binary_tree([5, 1, 4, None, None, 3, 6])
        assert Solution().isValidBST(root) == exp

    def test_3(self):
        exp = False
        root = create_binary_tree([2, 2, 2])
        assert Solution().isValidBST(root) == exp
