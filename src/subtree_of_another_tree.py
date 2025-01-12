"""
572. Subtree of Another Tree

https://leetcode.com/problems/subtree-of-another-tree

NOTES
  * A subtree of a binary tree is a tree that consists of a node in the tree
    and its identical tree structure (including all the node's descendants).
"""

from src.classes import TreeNode


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        # Handle empty trees. An empty tree cannot have a subtree. Likewise,
        # an empty tree is not a subtree of a tree.
        if not root or not subRoot:
            return False

        # If the current node in `root` is the same as `subRoot`, the root of
        # the subtree, check if the trees are the same. Otherwise, attempt to
        # find a subtree using the left and right child nodes.
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, t1: TreeNode | None, t2: TreeNode | None) -> bool:
        # This is our base condition, since it is the only statement we can be
        # certain is true (i.e., two trees consisting of a single null node
        # are identical). All other assertions must build from this condition.
        if not t1 and not t2:
            return True

        # Account for gaps.
        if (t1 is None) != (t2 is None):
            return False

        if t1.val == t2.val:
            return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)

        return False
