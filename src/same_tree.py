"""
100. Same Tree

https://leetcode.com/problems/same-tree

NOTES
  * Light work. Two queues, two BFS traversals. The only tricky part is taking
    into account gaps in either of the binary trees:

    The following binary trees have the same BFS traversal:

       1   1
     /       \
    2         2

    To account for this, we enqueue both left and right child nodes regardless
    of if they are None or not.
"""

from collections import deque

from src.classes import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # The number of nodes in both trees is in the range [0, 100], a tree
        # with 0 nodes is still considered identical.
        if not p or not q:
            return p == q

        qp, qq = deque([p]), deque([q])

        while qp and qq:
            curr_p, curr_q = qp.popleft(), qq.popleft()

            # Both binary trees have a gap in the same position.
            if not curr_p and not curr_q:
                continue

            # One binary tree has a gap while the other does not or the values
            # of the nodes in the same position are not the same.
            if bool(curr_p) != bool(curr_q) or curr_p.val != curr_q.val:
                return False

            for n, q in [(curr_p, qp), (curr_q, qq)]:
                q.append(n.left)
                q.append(n.right)

        # If both queues are empty, then the trees have an identical structure.
        return not qp and not qq
