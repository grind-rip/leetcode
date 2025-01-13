"""
572. Subtree of Another Tree

https://leetcode.com/problems/subtree-of-another-tree
"""

from unittest import TestCase

from src.subtree_of_another_tree import Solution
from tests.utils import create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        r = create_binary_tree_from_list([3, 4, 5, 1, 2])
        s = create_binary_tree_from_list([4, 1, 2])
        assert Solution().isSubtree(r, s) == exp

    def test_2(self):
        exp = False
        r = create_binary_tree_from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
        s = create_binary_tree_from_list([4, 1, 2])
        assert Solution().isSubtree(r, s) == exp

    def test_3(self):
        exp = True
        r = create_binary_tree_from_list([1, 1])
        s = create_binary_tree_from_list([1])
        assert Solution().isSubtree(r, s) == exp

    def test_4(self):
        exp = False
        r = create_binary_tree_from_list([3, 4, 5, 1, None, 2])
        s = create_binary_tree_from_list([3, 1, 2])
        assert Solution().isSubtree(r, s) == exp
