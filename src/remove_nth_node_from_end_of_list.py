"""
19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list

NOTES
  * To remove the nth node from the end of a linked list, we can use a two
    pointers technique. One pointer (p1) starts at the head, while another
    pointer (p2) starts n nodes ahead of p1. When p2 reaches the end, p1 will
    be at the nth node.

    Example (where ○ represents null):

          1   2   3   4   5
      ○ → ● → ● → ● → ● → ● → ○  n = 2
      ↑   ↑
          p1,p2
      prev

      Start by instantiating a head sentinel node. This allows us to more
      easily handle the case where n is equal to the length of the list.

      Next, advance p2 by n nodes:

          1   2   3   4   5
      ○ → ● → ● → ● → ● → ● → ○  n = 2
      ↑   ↑       ↑
          p1      p2
      prev

      Next, advance p1 and p2 together, maintaining prev as the node before p1,
      until p2 reaches the end of the list:

          1   2   3   4   5
      ○ → ● → ● → ● → ● → ● → ○  n = 2
              ↑   ↑           ↑
                  p1          p2
              prev

      Finally, remove the nth node (p1) by connecting prev to p1.next:

          1   2   3   5
      ○ → ● → ● → ● → ● → ○  n = 2
"""

from src.classes import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return None

        # Use a head sentinel node to handle removing the first node.
        prehead = ListNode(-1)
        prehead.next = head
        prev = prehead

        p1, p2 = head, head

        # Advance p2 by n nodes.
        i = 0
        while p2 and i < n:
            p2 = p2.next
            i += 1

        # Advance both pointers until p2 reaches the end, keeping track of the
        # node before p1.
        while p2:
            prev = p1
            p1 = p1.next
            p2 = p2.next

        # Remove p1 by connecting prev to p1.next.
        prev.next = p1.next

        return prehead.next
