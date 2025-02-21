"""
235. Lowest Common Ancestor of a Binary Search Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

NOTES
  * This problem can also be conceptualized as "lowest common root". Given the
    definition of a binary search tree:

      >A binary search tree (BST) is a binary tree in which the key of each
       internal node is greater than all the keys in the node's left subtree
       and less than all the keys in the node's right subtree.

    we simply need to find the deepest root node of the subtree containing both
    p and q. This node marks the root of the small subtree containing both p
    and q.

Initially, I solved this problem using a set of visited nodes when traversing
from root to p, then found where the paths diverged when traversing from root
to q. This can be optimized, however, using the strategy given above.

It is always important to leverage the unique properties of a data structure.
For example, finding the lowest common ancestor of a binary tree (not binary
search tree), requires a different approach.
"""

from src.classes import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        while True:
            if root.val > p.val and root.val > q.val and root.left:
                root = root.left
                continue
            if root.val < p.val and root.val < q.val and root.right:
                root = root.right
                continue
            return root
