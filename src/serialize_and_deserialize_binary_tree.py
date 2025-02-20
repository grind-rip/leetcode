"""
297. Serialize and Deserialize Binary Tree

https://leetcode.com/problems/serialize-and-deserialize-binary-tree

NOTES
  * Serialization and deserialization has applicability in real world software
    engineering, making this a great problem!

/!\ NOTE /!\
This solution description comprises my original thought process, backtracking
when a solution was nonviable, and a final correct solution. I've retroactively
provided additional context in order call attention to flaws in my original
approach.

---

Serialization is the process of converting information (e.g., a data structure
or object) into a sequence of bits, so that it can be stored on disk or in
memory, or transmitted over a network. Deserialization is the process of
constructing the serialized information.

Serialization and deserialization is facilitated by a codec (short for
coder/decoder), which enables both data compression and data conversion.

Let's recall from 'Construct Binary Tree from Preorder and Inorder Traversal'
that:

    >No single traversal order (pre-order, post-order, or in-order) uniquely
     identifies the structure of a tree...

/!\ NOTE /!\
This statement is only true when we do not account for gaps in the tree. Adding
gaps as well as node values gives us enough information to uniquely determine
the structure of the tree.

Therefore, the serialized tree will need to store both the pre-order and
in-order traversal in order to uniquely reconstruct the binary tree.

Each node has a value between -1000 and 1000, which means we will need to
represent 2001 numbers. To find the minimum number of bits required to
represent all possible node values in the tree, we need to find n where 2^n ≥
2001, since each bit pattern must uniquely identify a number. Taking the log
(base-2) of both sides, results in the following:

  n ≥ log(2001) ≈ 10.97

Therefore, rounding up, we need 11 bits, 2^11 = 2048, to represent 2001 values.
Further leveraging the fact that node values are constrained to -1000 and 1000,
we can create a simple codec by concatenating both the pre-order and in-order
traversals. A special sequence, 01111111111 (1023 in base-10), is used to
denote the termination of the pre-order sequence and start of the in-order
sequence. NOTE: 01111111111 is 1023 in two's complement.

/!\ NOTE /!\
This approach only works for trees with node values that are unique. Looking
back at 'Construct Binary Tree from Preorder and Inorder Traversal', this was
one of the problem constraints:

  >preorder and inorder consist of *unique* values.

So, the correct solution involves using either a depth-first or breadth-first
traversal, while accounting for gaps. Null nodes are denoted by a null marker.
Here, we can reuse the special sequence above to denote gaps in the tree. An
added element of complexity to this approach is the deserialization logic must
account for the fact that the serialization does not include all gaps.

/!\ NOTE /!\
Creating a serialization that accounts for all gaps in the tree, essentially
representing a complete binary tree, exceeds the time limit.

In the end, I learned a new algorithm for serializing and deserializing binary
trees. This is the same algorithm used by LeetCode.

Example:

    [1, 2, 3, None, None, 4, 5, 6, 7]

        1
        ●
      /   \
    2       3
    ●       ●
          /   \
         4     5
         ●     ●
       /   \
      6     7
      ●     ●
"""

from collections import deque

from src.classes import TreeNode


class Codec:
    NULL_MARKER = 1023  # 01111111111 in two's complement

    def serialize(self, root: TreeNode | None) -> str:
        """
        Encodes a tree into a string.
        """
        s = ""

        if not root:
            return s

        q: deque[TreeNode | None] = deque([root])

        while q:
            curr: TreeNode | None = q.popleft()
            if curr:
                s += format(curr.val, "011b")
            else:
                s += format(self.NULL_MARKER, "011b")
            if curr:
                q.append(curr.left)
                q.append(curr.right)

        return s

    def deserialize(self, data: str) -> TreeNode | None:
        """
        Decodes a string into a tree.
        """
        l: list[int | None] = []

        # Iterate over the data in 11 bit chunks.
        for i in range(0, len(data), 11):
            bits = data[i : i + 11]
            # Convert the chunk to an integer using two's complement.
            value = int(bits, 2)
            # If the leftmost bit is 1, the value was negative, so we have to
            # convert from unsigned to two's complement by subtracting 2^11
            # (2048).
            if bits[0] == "1":
                value -= 1 << 11
            if value == self.NULL_MARKER:
                l.append(None)
            else:
                l.append(value)

        if not l:
            return None

        root = TreeNode(val=l[0])
        q: deque[TreeNode] = deque([root])
        i = 1

        # The crucial property of this algorithm is that i increments by 2
        # every iteration, while nodes are only enqueued if l[i] is not None.
        # This ensures our index into l is always aligned with the possible
        # left and right child nodes of the current node under consideration.
        # This allows the tree structure to be determined without storing
        # additional null nodes.
        while q and i < len(l):
            curr: TreeNode = q.popleft()
            if l[i] is not None:
                left = TreeNode(val=l[i])
                curr.left = left
                q.append(left)
            i += 1
            if l[i] is not None:
                right = TreeNode(val=l[i])
                curr.right = right
                q.append(right)
            i += 1

        return root
