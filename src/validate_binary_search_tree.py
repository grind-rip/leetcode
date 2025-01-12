"""
98. Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree

NOTES
  * In order to validate if a binary tree is a binary search tree (BST), we
    must validate the following assertion regarding binary search trees:

    >A binary search tree is a binary tree that for each internal node the
     node's key is greater than all the keys in the node's left subtree and
     less than all the keys in the node's right subtree.

Example:

       2
     /   \
    1     3

An in-order traversal (left → root → right) of a binary search tree retrieves
the keys in ascending sorted order.

This problem can be solved using recursion, given that the solution to the
minimal subtree problem can be used to solve the problem for the entire tree.

A recursive function that only checks the left and right child of a given node
would erroneously return true even if the node's left or right subtrees contain
keys greater than or less than its key, respectively. For this reason, we need
to keep track of the minimum and maximum possible keys for a node.

Example:

       5
     /   \
    4     6
         / \
        3   7

The root of a substree must have a key between the minimum and maximum possible
keys. For the root node of the tree, this is between -inf and inf. For the left
subtree this is between -inf and the key of the root node. For the right
subtree this is between the key of the root node and inf. By recursively
selecting a possible lower and upper bound for the given subtree, we replicate
the binary search algorithm.
"""

import sys

from src.classes import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # Handle null node, which is implicitly a valid BST.
        if not root:
            return True

        return self._isValidBST(root, -sys.maxsize, sys.maxsize)

    def _isValidBST(self, root: TreeNode, lo: int, hi: int) -> bool:
        # Handle null node, which is implicitly a valid BST. This is our base
        # condition, since we can be certain that all previous subtrees were
        # valid binary search trees.
        if not root:
            return True

        # For each node in the tree, there is a minimum and maximum possible
        # key it can have.
        if root.val >= hi or root.val <= lo:
            return False

        # Recursively apply the minimal subtree solution to all subtrees. Any
        # invalid subtree will cause the bitwise AND operation to return False
        # (0) for the entire tree.
        return self._isValidBST(root.left, lo, root.val) and self._isValidBST(root.right, root.val, hi)
