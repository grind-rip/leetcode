"""
236. Lowest Common Ancestor of a Binary Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

NOTES

Wikipedia has an excellent article on lowest common ancestor:

  The lowest common ancestor (LCA) (also called least common ancestor) of two
  nodes v and w in a tree or directed acyclic graph (DAG) T is the lowest
  (i.e., deepest) node that has both v and w as descendants, where we define
  each node to be a descendant of itself (so if v has a direct connection from
  w, w is the lowest common ancestor).

  The LCA of v and w in T is the shared ancestor of v and w that is located
  farthest from the root. Computation of lowest common ancestors may be useful,
  for instance, as part of a procedure for determining the distance between
  pairs of nodes in a tree: the distance from v to w can be computed as the
  distance from the root to v, plus the distance from the root to w, minus
  twice the distance from the root to their lowest common ancestor.

  In a tree data structure where each node points to its parent, the lowest
  common ancestor can be easily determined by finding the first intersection of
  the paths from v and w to the root. In general, the computational time
  required for this algorithm is O(h) where h is the height of the tree (length
  of longest path from a leaf to the root). However, there exist several
  algorithms for processing trees so that lowest common ancestors may be found
  more quickly.

Unlike with 'Lowest Common Ancestor of a Binary Search Tree' we cannot leverage
the fact that the tree is a binary search tree. This makes the problem slightly
more challenging and increases the time complexity from O(log n) to O(n). This
problem can be solved recursively and iteratively.

Recursive Approach
------------------
In order to visualize the recursive solution, imagine moving down the tree in
a depth-first manner. Each recursive call postpones the processing of the
current node until calls higher in the stack (or lower in the tree) have
returned. The first recursive call is the last to fully execute and returns the
solution, which is "passed up" from previous calls. Now, let's recall that the
lowest common ancestor of two nodes is the deepest node of the subtree that
contains both nodes. Therefore, we need to develop a base condition and
recursive logic such that the final recursive call returns the lowest common
ancestor, which may have been determined somewhere within the recursion.

Base Case:

  >If the node is a leaf (root == None) or root is p or q, return root.

Basically, this passes information up the recursive call stack (or up the
tree). Either, no, the current path terminated without finding p or q, or, yes,
p or q was found. Within this conditional is an implicit boolean, which is used
later in the recursive logic.

Recursive Logic:

  >Recurse into the left and right subtrees. If both subtrees find the target,
   return root. Otherwise, return the result of either the left or right
   subtree.

This is where the solution is "passed up". It is also where the both macro- and
microstructure of the recursive solution is codified. If either of the subtrees
returns a non-null, this value is returned up the call stack until both
subtrees return a non-null. The final return call returns the solution.

It is probably helpful here to consider two cases:
  1. The LCA is contained in the left or right subtree of root.
  2. The LCA is the root itself.

As you can see, the recursive invariant holds for all subtrees.

  ```
  # The LCA is the root itself.
  if left and right:
      return root

  # The LCA is contained in the left or right subtree of root.
  return left if left else right
  ```

Iterative Approach
------------------
The iterative approach is more intuitive, since it uses the fact that the node
at which the path from the root to p diverges (or converges if viewed from
bottom-up) from the path from the root to q is the lowest common ancestor.
Since nodes do not inherently contain a pointer to their parent (trees are
typically directed from parent to child), a hash map is used to maintain a
mapping of child->parent for all nodes traversed while searching for p and q.
We can then trace back from p to root using the hash map, producing a set of
nodes (ancestors) for p. Tracing back from q to root, the first node contained
in ancestors is the lowest common ancestor for p and q.
"""

from collections import deque

from src.classes import TreeNode


class Solution:
    """
    Returns the LCA of `p` and `q` for the tree rooted at `root` recursively.
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base Case: If root is a leaf (None) or if root is p or q, return
        # root.
        if not root or root in (p, q):
            return root

        # Recurse into the left and right subtrees of root.
        #
        # left and right may be one of the following:
        #   1. root.left and root.right if root is the LCA.
        #   2. The LCA of the left subtree and None, if the LCA was found in
        #      the left subtree.
        #   3. None and the LCA of the right subtree, if the LCA was found in
        #      the right subtree.
        #
        # This invariant holds for all subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # root is the LCA
        if left and right:
            return root

        # left or right is the LCA (or p or q was found)
        return left if left else right


class IterativeSolution:
    """
    Returns the LCA of `p` and `q` for the tree rooted at `root` iteratively.
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack: deque[TreeNode] = deque([root])
        parents: dict[TreeNode, TreeNode | None] = {root: None}
        curr: TreeNode = root

        # Traverse the tree until both p and q are found. This populates the
        # `parents` hash map and requires O(n) time complexity in the
        # worst-case.
        while stack:
            curr = stack.pop()
            # NOTE: For pre-order traversal, the right child is pushed onto the
            # stack first.
            if curr.right:
                stack.append(curr.right)
                parents[curr.right] = curr
            if curr.left:
                stack.append(curr.left)
                parents[curr.left] = curr

        # Using the populated `parents` hash map, create a set of ancestors by
        # tracing the path from `p` to `root`.
        ancestors: set[TreeNode] = set()

        # NOTE: Remember to add p! This handles the case where the node itself,
        # (p or q) is the LCA:
        #
        #   >...we define each node to be a descendant of itself (so if v has a
        #   direct connection from w, w is the lowest common ancestor).
        while p:
            ancestors.add(p)
            p = parents[p]

        # Now, trace the path from `q` to `root`. The first ancestor in the
        # path that is shared with `p` (is part of the set of ancestors) is the
        # LCA of `p` and `q`.
        while q:
            if q in ancestors:
                return q
            q = parents[q]

        return root
