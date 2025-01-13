"""
104. Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree
"""

from unittest import TestCase

from src.maximum_depth_of_binary_tree import Solution
from tests.utils import create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = 3
        root = create_binary_tree_from_list([3, 9, 20, None, None, 15, 7])
        assert Solution().maxDepth(root) == exp

    def test_2(self):
        exp = 2
        root = create_binary_tree_from_list([1, None, 2])
        assert Solution().maxDepth(root) == exp
