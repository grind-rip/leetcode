"""
124. Binary Tree Maximum Path Sum

https://leetcode.com/problems/binary-tree-maximum-path-sum

NOTES
  * This one is hard. I had to read through the entire solution, however, once
    you understand the core algorithm, it is relatively straightforward.

First, let's define a "path" in a tree:

  >A path in a binary tree is a sequence of nodes where each pair of adjacent
   nodes in the sequence has an edge connecting them.

Each node in a path can be connected to 0, 1, or 2 nodes. A path does not need
to pass through the root of the tree. A path can also be a single node.

The following are all valid paths:    The following is not a valid path:

                                                     ●
       ●     ● - ●     ●                              \
                      / \                              ●
                     ●   ●                            / \
                                                     ●   ●

From this we observe that the maximum path sum of a tree is calculated using
one of the following cases:

  1. A single node (root).
  2. The maximum path of the left subtree plus the root.
  3. The maximum path of the right subtree plus the root.
  4. The maximum path of both subtrees plus the root.

The minimal subproblem (or base case) is a null node, which has a maximum path
sum of 0. Next, we consider the case of a single node, which itself may
constitute the maximum path sum. From here, cases 2, 3, and 4 can be easily
calculated, and a maximum sum path of the subtree can be determined. This
process represents a bottom-up approach, which can be solved nicely using
recursion and, in particular, using a depth-search traversal of the tree.

NOTE: If we take a top-down approach, that is, enumerating all paths in the
tree starting from root, the time complexity is exponential (O(n^2)), since a
complete binary tree with n nodes has (n^2 - 1)/2 unique paths.

Another insight is that in order to compare the maximum path sum for cases 2,
3, and 4, we need to determine the maximum path of the left and right subtrees
first. This requires a post-order traversal:

  1. Recursively traverse the current node's left subtree.
  2. Recursively traverse the current node's right subtree.
  3. Visit the current node.

Combining this information, the recursive logic is relatively straightforward:

  1. Calculate the maximum sum path of the left and right subtrees.
  2. Check if the current maximum path sum is the overall maximum path sum.
  3. Return the current maximum path sum for the subtree.
"""

import sys

from src.classes import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_path_sum = -sys.maxsize

        def _maxPathSum(root: TreeNode | None) -> int:
            """
            Performs a post-order traversal of the tree rooted at `root` and
            recursively calculates the maximum sum path for the tree.
            """
            nonlocal max_path_sum

            if not root:
                return 0

            # Calculate the maximum path sum of the left subtree.
            max_path_sum_left = _maxPathSum(root.left)

            # Calculate the maximum path sum of the right subtree.
            max_path_sum_right = _maxPathSum(root.right)

            # Calculate the maximum path sum of the current subtree.
            # Checks the four possible cases.
            max_path_sum_curr = max(
                root.val,
                max_path_sum_left + root.val,
                max_path_sum_right + root.val,
                max_path_sum_left + max_path_sum_right + root.val,
            )

            # Update the maximum path sum of all paths.
            max_path_sum = max(max_path_sum, max_path_sum_curr)

            # NOTE: A node cannot have more than 2 connections, so the returned
            # value is the maximum path of the root or the root plus the left
            # or right subtree.
            return max(
                root.val,
                max_path_sum_left + root.val,
                max_path_sum_right + root.val,
            )

        _maxPathSum(root)
        return max_path_sum
