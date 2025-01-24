"""
206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list

NOTES
  * Reversing a linked list in-place iteratively involves some simple pointer
    management. Three variables - prev, curr, and next - are used to store the
    previous, current, and next nodes, respectively. For each iteration, the
    next node (curr.next) is stored. Since we are "unlinking" the current node
    from the next node and "relinking" it to the previous node, we need to keep
    a reference to this node. Next, we point the current node at the previous
    node (prev). We then update the reference to the previous node to be the
    current node and the current node to be the next node. We repeat the
    process until the end of the list is reached.

    Example (where ○ represents null):

      1   2   3   4   5
      ● → ● → ● → ● → ● → ○
      ↑

      Starting with head (1), we store its reference to next (2):

        next = curr.next

      Next, we update its reference to next to be the previous node (○):

        curr.next = prev

          1   2   3   4   5
      ○ ← ●   ● → ● → ● → ● → ○

      Then, we update the previous node (○) to be the current node (1):

        prev = curr

      Finally, we update the current node to be the next node (2):

          1   2   3   4   5
      ○ ← ●   ● → ● → ● → ● → ○
              ↑

      This process is repeated until the current node is null:

          1   2   3   4   5
      ○ ← ● ← ● ← ● ← ● ← ●  ○
                             ↑
"""

from src.classes import ListNode


class Solution:
    """
    The time complexity for this solution is O(n) and the space complexity is
    O(1).
    """

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        # 1. Store the current node's reference to next.
        # 2. Update the current node's next to be the previous node.
        # 3. Update the previous node to be the current node.
        # 4. Update the current node to be the next node (stored in 1).
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
            # A more elegant way using tuple unpacking:
            #   curr.next, prev, curr = prev, curr, curr.next
        return prev
