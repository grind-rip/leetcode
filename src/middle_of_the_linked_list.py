"""
876. Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list

NOTES
  * Use two pointers. Advance the `fast` pointer by 2. Advance the `slow`
    pointer by 1. When `fast` reaches the end of the linked list, `slow` is at
    the middle node.

    Example (where ○ represents null):

      1   2   3   4   5
      ● → ● → ● → ● → ● → ○  middle = 3
      ↑
      slow
      fast

      1   2   3   4   5
      ● → ● → ● → ● → ● → ○  middle = 3
          ↑   ↑
          slow
              fast

      1   2   3   4   5
      ● → ● → ● → ● → ● → ○  middle = 3
              ↑       ↑
              slow
                      fast

    When the list contains an even number of nodes, there are two middle nodes.
    To take the second middle node, use slow.next:

      1   2   3   4   5   6
      ● → ● → ● → ● → ● → ● → ○  middle = 4
      ↑
      slow
      fast

      1   2   3   4   5   6
      ● → ● → ● → ● → ● → ● → ○  middle = 4
          ↑   ↑
          slow
              fast

      1   2   3   4   5   6
      ● → ● → ● → ● → ● → ● → ○  middle = 4
              ↑       ↑
              slow
                      fast
"""

from src.classes import ListNode


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Handle odd and even lists.
        return slow.next if fast.next else slow
