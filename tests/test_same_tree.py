"""
100. Same Tree

https://leetcode.com/problems/same-tree
"""

from unittest import TestCase

from src.same_tree import Solution
from tests.utils import create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        p = create_binary_tree_from_list([1, 2, 3])
        q = create_binary_tree_from_list([1, 2, 3])
        assert Solution().isSameTree(p, q) == exp

    def test_2(self):
        exp = False
        p = create_binary_tree_from_list([1, 2])
        q = create_binary_tree_from_list([1, None, 2])
        assert Solution().isSameTree(p, q) == exp

    def test_3(self):
        exp = False
        p = create_binary_tree_from_list([1, 2, 1])
        q = create_binary_tree_from_list([1, 1, 2])
        assert Solution().isSameTree(p, q) == exp
