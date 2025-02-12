"""
235. Lowest Common Ancestor of a Binary Search Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
"""

from unittest import TestCase

from src.lowest_common_ancestor_of_a_binary_search_tree import Solution
from tests.utils import create_bfs_list_from_binary_tree, create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = 6
        root = create_binary_tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[1], l[2]  # p = 2, q = 8
        assert Solution().lowestCommonAncestor(root, p, q).val == exp

    def test_2(self):
        exp = 2
        root = create_binary_tree_from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[1], l[4]  # p = 2, q = 4
        assert Solution().lowestCommonAncestor(root, p, q).val == exp

    def test_3(self):
        exp = 2
        root = create_binary_tree_from_list([2, 1])
        l = create_bfs_list_from_binary_tree(root=root, values_only=False)
        p, q = l[0], l[1]  # p = 2, q = 1
        assert Solution().lowestCommonAncestor(root, p, q).val == exp
