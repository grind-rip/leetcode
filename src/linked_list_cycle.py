"""
141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle

NOTES
  * Use Floyd's cycle-finding algorithm (tortoise and hare algorithm). You just
    have to know that you should use this algorithm to detect a cycle in a
    linked list. This algorithm can also be used for directed graphs.

    See: https://en.wikipedia.org/wiki/Cycle_detection

This solution has O(n) runtime complexity and O(1) space complexity.
"""

from src.classes import ListNode


class Solution:
    """
    Robert W. Floyd's tortoise and hare algorithm moves two pointers at
    different speeds through the sequence of values until they both point to
    equal values.
    """

    def hasCycle(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return False

        # The algorithm maintains two pointers into the given sequence, one
        # (the tortoise) at xᵢ, and the other (the hare) at x₂ᵢ. At each step
        # of the algorithm, it increases i by one, moving the tortoise one step
        # forward and the hare two steps forward in the sequence, and then
        # compares the sequence values at these two pointers. The smallest
        # value of i > 0 for which the tortoise and hare point to equal values
        # is the desired value ν (the period of a repetition).
        tortoise, hare = head.next, head.next.next

        while tortoise != hare:
            if not hare or not hare.next:
                return False
            tortoise, hare = tortoise.next, hare.next.next
        return True
