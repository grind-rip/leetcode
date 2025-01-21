"""
206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list

NOTES
  * Reversing a linked list is similar to merging two sorted linked lists, in
    that a pointer ('prev') keeps a reference to the previous node. However, we
    also need an additional pointer ('next') to keep a reference to the next
    node in the sequence.

    Example:

      1   2   3   4   5
      ● → ● → ● → ● → ● → ○
      ↑

      Starting with head (1), we store its reference to next (2):

        next = curr.next

      Next, we update its reference to next to be the previous node (null):

        curr.next = prev

          1   2   3   4   5
      ○ ← ●   ● → ● → ● → ● → ○

      Then, we update the previous node (null) to be the current node (1):

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
        return prev
