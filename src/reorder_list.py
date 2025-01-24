"""
143. Reorder List

https://leetcode.com/problems/reorder-list

NOTES
  * This problem is a combination of three easy problems:
      * Middle of the Linked List
      * Reverse Linked List
      * Merge Two Sorted Lists

    First, find the middle node. If the list contains an even number of nodes,
    take the second middle node. Next, reverse the second list. Finally, use
    the process for merging two sorted lists to stitch the lists back together.

    Example (where ○ represents null):

    Find the middle node:

      1   2   3   4   5
      ● → ● → ● → ● → ● → ○  middle = 3
              ↑
              m

    Reverse the second list:

      1   2   3       5   4
      ● → ● → ● → ○   ● → ● → ○
              ↑
              m

    Merge the two lists (starting with the head of the first list):


            1   2   3                       2   3
            ● → ● → ● → ○                   ● → ● → ● → ○
            ↑                     1         ↑
      ○                       ○ → ●
      ↑                       ↑
            5   4                       5   4
            ● → ● → ○                   ● → ● → ○
            ↑                           ↑


      1   5   2   4   3
      ● → ● → ● → ● → ● → ○

This is a tricky one and you just have to know what to do here. Once you know
the solution, the implementation is trivial.
"""

from src.classes import ListNode


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        # Find the middle node.
        m = self.middleNode(head)

        # Create two lists by unlinking the node after the middle node.
        l1, m.next, l2 = head, None, m.next

        # Reverse the second list.
        l2 = self.reverseList(l2)

        # Merge the two lists (starting with the head of the first list).
        _ = self.mergeTwoLists(l1, l2)

        return None

    def middleNode(self, head: ListNode) -> ListNode:
        """
        Given the head of a singly linked-list, return the middle node. If
        there are two middle nodes, return the second middle node.
        """
        if not head:
            return head

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Handle odd and even lists.
        return slow.next if fast.next else slow

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """
        Given the head of a singly linked-list, reverse the list in-place and
        return the new head.
        """
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

    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """
        Given the head of two singly linked-lists, merge them starting with the
        head of the first list.
        """
        prehead = ListNode(-1)
        curr = prehead
        # 1. Alternate between taking from list1 and list2.
        # 2. Update the current node's next to be either head of the two.
        # 3. Update the head of the list from which the node was taken.
        # 4. Update the current node in the merged list.
        i = 1
        while list1 and list2:
            if i % 2:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            i += 1
        # At this point, list1 may still have nodes. If this is the case, list1
        # is attached to the end of the merged list at 'curr'.
        curr.next = list1 if list1 else None
        return prehead.next
