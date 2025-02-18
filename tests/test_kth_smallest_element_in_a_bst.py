"""
230. Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst
"""

from unittest import TestCase

from src.kth_smallest_element_in_a_bst import RecursiveSolution, Solution
from tests.utils import create_binary_tree_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = 1
        root = create_binary_tree_from_list([3, 1, 4, None, 2])
        assert Solution().kthSmallest(root, 1) == exp

    def test_2(self):
        exp = 3
        root = create_binary_tree_from_list([5, 3, 6, 2, 4, None, None, 1])
        assert Solution().kthSmallest(root, 3) == exp


class TestRecursiveSolution(TestCase):
    def test_1(self):
        exp = 1
        root = create_binary_tree_from_list([3, 1, 4, None, 2])
        assert RecursiveSolution().kthSmallest(root, 1) == exp

    def test_2(self):
        exp = 3
        root = create_binary_tree_from_list([5, 3, 6, 2, 4, None, None, 1])
        assert RecursiveSolution().kthSmallest(root, 3) == exp
