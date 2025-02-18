"""
230. Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst

NOTES
  * A property of a binary search tree is that an in-order traversal will yield
    all the nodes in ascending order, so we should be able to solve this in
    O(H + k), where H is the height of the tree.

The iterative in-order traversal felt like a natural fit, but I implemented the
solution using recursion as well just to flex.
"""

from collections import deque

from src.classes import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack: deque[TreeNode] = deque()
        curr: TreeNode | None = root
        count = 0

        # The iterative in-order traversal is pretty simple:
        #   1. Go as far left as possible.
        #   2. Pop and visit the first node from the stack.
        #   3. Repeat the process with the first non-null right node, otherwise
        #      continue popping nodes from the stack.
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right

        return -1


class RecursiveSolution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        def dfs(root: TreeNode | None) -> tuple[int, int]:  # (count, value)
            if not root:
                return 0, -1

            # Search the left subtree.
            left_count, left_val = dfs(root.left)

            # If the kth element is found, propagate it up. This is a crucial
            # aspect of recursion, basically, the ability to pass information
            # back up the call stack once some condition has been met.
            if left_val != -1:
                return left_count, left_val

            # Check if the current node is the kth element.
            curr_count = left_count + 1
            if curr_count == k:
                return curr_count, root.val

            # Search the right subtree. It's important to note that since
            # searching the right subtree represents a branch in the recursive
            # logic, the count must also reflect this.
            right_count, right_val = dfs(root.right)

            return curr_count + right_count, right_val

        _, result = dfs(root)
        return result
