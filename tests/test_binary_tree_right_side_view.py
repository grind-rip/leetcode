"""
199. Binary Tree Right Side View

https://leetcode.com/problems/binary-tree-right-side-view
"""

from unittest import TestCase

from src.binary_tree_right_side_view import Solution
from tests.utils import create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 3, 4]
        root = create_binary_tree_from_list([1, 2, 3, None, 5, None, 4])
        assert Solution().rightSideView(root) == exp

    def test_2(self):
        exp = [1, 3, 4, 5]
        root = create_binary_tree_from_list([1, 2, 3, 4, None, None, None, 5])
        assert Solution().rightSideView(root) == exp

    def test_3(self):
        exp = [1, 3]
        root = create_binary_tree_from_list([1, None, 3])
        assert Solution().rightSideView(root) == exp

    def test_4(self):
        exp = []
        root = create_binary_tree_from_list([])
        assert Solution().rightSideView(root) == exp
