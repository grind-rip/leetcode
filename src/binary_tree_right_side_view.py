"""
199. Binary Tree Right Side View

https://leetcode.com/problems/binary-tree-right-side-view

NOTES
  * If you haven't already, solve 'Binary Tree Level Order Traversal'. Using
    the breadth-first approach, the solution is trivial.
"""

from collections import deque

from src.classes import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        nodes: list[int] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            width = len(queue)
            for i in range(width):
                curr = queue.popleft()
                if i == width - 1:
                    nodes.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return nodes
