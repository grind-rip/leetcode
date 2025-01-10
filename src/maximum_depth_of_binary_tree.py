"""
104. Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree

This problem can be solved using breadth-first search or depth-first search,
since we will by necessity have to visit each node in the binary tree, however
it is more intuitive to use depth-first search.

NOTE: Since a binary tree is not cyclic, we do not need to maintain a list of
visited nodes.

If the binary tree is a perfect binary tree[^1], then its depth is 2^x = n + 1,
where x is the depth and n is the length of the array representing
the binary tree. This is also x = log₂(n + 1).

[^1]: A perfect binary tree is a binary tree in which all interior nodes have
two children and all leaves have the same depth or same level (the level of a
node defined as the number of edges or links from the root node to a node).
"""

from src.classes import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def maxDepth_dfs(node: TreeNode, level: int) -> int:
            """
            Return the maximum depth of the binary tree.
            """
            level_l, level_r = level, level
            if node.left:
                level_l = maxDepth_dfs(node.left, level + 1)
            if node.right:
                level_r = maxDepth_dfs(node.right, level + 1)
            return max(level_l, level_r)

        # The number of nodes in the tree is in the range [0, 10^4].
        if not root:
            return 0

        return maxDepth_dfs(root, 1)
