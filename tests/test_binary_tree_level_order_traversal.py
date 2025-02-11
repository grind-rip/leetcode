"""
102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal
"""

from unittest import TestCase

from src.binary_tree_level_order_traversal import Solution, SolutionDFS
from tests.utils import create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [[3], [9, 20], [15, 7]]
        root = create_binary_tree_from_list([3, 9, 20, None, None, 15, 7])
        assert Solution().levelOrder(root) == exp

    def test_2(self):
        exp = [[1]]
        root = create_binary_tree_from_list([1])
        assert Solution().levelOrder(root) == exp

    def test_3(self):
        exp = []
        root = create_binary_tree_from_list([])
        assert Solution().levelOrder(root) == exp


class TestSolutionDFS(TestCase):
    def test_1(self):
        exp = [[3], [9, 20], [15, 7]]
        root = create_binary_tree_from_list([3, 9, 20, None, None, 15, 7])
        assert SolutionDFS().levelOrder(root) == exp

    def test_2(self):
        exp = [[1]]
        root = create_binary_tree_from_list([1])
        assert SolutionDFS().levelOrder(root) == exp

    def test_3(self):
        exp = []
        root = create_binary_tree_from_list([])
        assert SolutionDFS().levelOrder(root) == exp
