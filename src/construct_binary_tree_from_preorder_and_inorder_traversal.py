"""
105. Construct Binary Tree from Preorder and Inorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

NOTES
  * Good primer for 'Serialize and Deserialize Binary Tree'. Recall that,

    >No single traversal order (pre-order, post-order, or in-order) uniquely
     identifies the structure of a tree...

If the binary tree was guaranteed to be complete, meaning all levels except
possibly the last are fully filled and the last level is filled from left to
right, this problem would be trivial. Recall that a heap, which is a complete
binary tree, can be represented as a zero-based array where a node at position
i has children at positions 2*i+1 and 2*i+2. So, all we would need to do is
construct the tree by iterating through the pre-order array. Unfortunately,
it's not that simple, since the tree is *not* guaranteed to be a complete tree
and therefore we must account for gaps.

Using the definitions of pre-order and in-order traversal, we can make two key
observations:

  1. The root of the tree is located at `preorder[0]`.
  2. The subarrays created by splitting `inorder` at root represents the left
     and right subtrees of the root of the tree.

From this, a recursive logic emerges: the subtrees rooted at `preorder[i]` are
created by splitting `inorder` at `preorder[i]`.

It should be noted that the range for the subtrees is reduced logarithmically
for each recursive call.

One of the major "gotchas" in this problem is that we cannot assume that a node
in `preorder` is the left or right node. For this reason, we only increment the
pointer to the index of `preorder` if a node can be created (i.e., the
recursive function does not return None).

For example, consider the following tree:

    1
    ●
     \
      2
      ●

Pre-order = [1, 2]
In-order  = [1, 2]

The only way to signify programmatically that 2 is the right node of 1 and not
the left node is to only increment the index of `preorder` if the result of
calling our recursive function does not return None.
"""

from src.classes import TreeNode


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Create a mapping of value -> index for `inorder` (O(1) lookups).
        d: dict[int, int] = {}
        for i, v in enumerate(inorder):
            d[v] = i

        preorder_idx = 0

        def _buildTree(left: int, right: int) -> TreeNode | None:
            """
            Helper function for `buildTree()`.
            """
            nonlocal preorder_idx

            if left > right:
                return None

            preorder_val = preorder[preorder_idx]
            node = TreeNode(preorder_val)

            preorder_idx += 1

            node.left = _buildTree(left, d[preorder_val] - 1)
            node.right = _buildTree(d[preorder_val] + 1, right)

            return node

        return _buildTree(0, len(preorder) - 1)
