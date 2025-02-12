"""
226. Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree
"""

from unittest import TestCase

from src.invert_binary_tree import Solution
from tests.utils import create_bfs_list_from_binary_tree, create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [4, 7, 2, 9, 6, 3, 1]
        t = create_binary_tree_from_list([4, 2, 7, 1, 3, 6, 9])
        assert create_bfs_list_from_binary_tree(root=Solution().invertTree(t)) == exp

    def test_2(self):
        exp = [2, 3, 1]
        t = create_binary_tree_from_list([2, 1, 3])
        assert create_bfs_list_from_binary_tree(root=Solution().invertTree(t)) == exp

    def test_3(self):
        exp = []
        t = create_binary_tree_from_list([])
        assert create_bfs_list_from_binary_tree(root=Solution().invertTree(t)) == exp
