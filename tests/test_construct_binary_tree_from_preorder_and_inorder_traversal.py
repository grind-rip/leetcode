"""
105. Construct Binary Tree from Preorder and Inorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""

from unittest import TestCase

from src.construct_binary_tree_from_preorder_and_inorder_traversal import Solution
from tests.utils import assert_tree


class TestSolution(TestCase):
    def test_1(self):
        exp = [3, 9, 20, None, None, 15, 7]
        assert_tree(
            Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]),
            exp,
        )

    def test_2(self):
        exp = [-1]
        assert_tree(Solution().buildTree(preorder=[-1], inorder=[-1]), exp)

    def test_3(self):
        exp = [1, None, 2]
        assert_tree(Solution().buildTree(preorder=[1, 2], inorder=[1, 2]), exp)
