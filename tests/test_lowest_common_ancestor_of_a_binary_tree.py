"""
236. Lowest Common Ancestor of a Binary Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
"""

from unittest import TestCase

from src.lowest_common_ancestor_of_a_binary_tree import IterativeSolution, Solution
from tests.utils import create_bfs_list_from_binary_tree, create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = 3
        root = create_binary_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[1], l[2]  # p = 5, q = 1
        assert Solution().lowestCommonAncestor(root, p, q).val == exp

    def test_2(self):
        exp = 5
        root = create_binary_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[1], l[8]  # p = 5, q = 4
        assert Solution().lowestCommonAncestor(root, p, q).val == exp

    def test_3(self):
        exp = 2
        root = create_binary_tree_from_list([2, 1])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[0], l[1]  # p = 1, q = 2
        assert Solution().lowestCommonAncestor(root, p, q).val == exp


class TestIterativeSolution(TestCase):
    def test_1(self):
        exp = 3
        root = create_binary_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[1], l[2]  # p = 5, q = 1
        assert IterativeSolution().lowestCommonAncestor(root, p, q).val == exp

    def test_2(self):
        exp = 5
        root = create_binary_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[1], l[8]  # p = 5, q = 4
        assert IterativeSolution().lowestCommonAncestor(root, p, q).val == exp

    def test_3(self):
        exp = 2
        root = create_binary_tree_from_list([2, 1])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[0], l[1]  # p = 1, q = 2
        assert IterativeSolution().lowestCommonAncestor(root, p, q).val == exp
