"""
124. Binary Tree Maximum Path Sum

https://leetcode.com/problems/binary-tree-maximum-path-sum
"""

from unittest import TestCase

from src.binary_tree_maximum_path_sum import Solution
from tests.utils import create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = 6
        root = create_binary_tree_from_list([1, 2, 3])
        assert Solution().maxPathSum(root) == exp

    def test_2(self):
        exp = 42
        root = create_binary_tree_from_list([-10, 9, 20, None, None, 15, 7])
        assert Solution().maxPathSum(root) == exp
