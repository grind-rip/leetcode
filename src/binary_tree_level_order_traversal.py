"""
102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal

NOTES
  * Use depth-first or breadth-first search. The strategy for keeping track of
    the current level is slightly different for each approach. For depth-first
    search, pass the level with the recursive call. For breadth-first search,
    dequeue the entire level all at once, add the nodes to the result, then
    enqueue all child nodes.
"""

from collections import deque

from src.classes import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        levels: list[list[int]] = []
        queue: deque[TreeNode] = deque([root])
        level = 0

        while queue:
            levels.append([])
            # Loop invariant: The length of the queue is the width of the
            # level.
            for _ in range(len(queue)):
                curr = queue.popleft()
                levels[level].append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1

        return levels


class SolutionDFS:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        levels: list[list[int]] = []
        self._levelOrder(root, 0, levels)
        return levels

    def _levelOrder(
        self, root: TreeNode | None, level: int, levels: list[list[int]]
    ) -> None:
        if not root:
            return
        if len(levels) < level + 1:
            levels.append([])
        levels[level].append(root.val)
        self._levelOrder(root.left, level + 1, levels)
        self._levelOrder(root.right, level + 1, levels)
