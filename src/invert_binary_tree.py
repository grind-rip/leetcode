"""
226. Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree

NOTES
  * Another easy one: visit every node (BFS or DFS), then simply swap the left
    and right pointers.
"""

from src.classes import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        # NOTE: You can also use tuple unpacking for a slightly more Pythonic
        # swap. Tuple unpacking in Python works for swapping because Python
        # creates a temporary tuple with the right-side values before
        # performing the assignment, thus creating the temporary storage
        # implicitly.
        #
        # root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
