"""
21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists

NOTES
  * Merging two sorted lists in-place is similar to merging two arrays, but
    involves some additional pointer management.

    A good strategy is to use a head sentinel node (also called a dummy node)
    'prehead' and a pointer 'curr' that tracks the current node in the merged
    list.

    Example (where ○ represents null):

      1   3   5
      ● → ● → ● → ○
      ↑

      2   4   6
      ● → ● → ● → ○
      ↑

      Start by instantiating a head sentinel node. This is the current node in
      the merged list:

      ○
      ↑

      Next, compare the heads of the two lists (1) and (2). Since 1 < 2, (1)
      is the next node in the merged list. We update the current node (curr)
      reference to next to be (1). We also update the head of the list from
      which (1) was taken to be the next node in the list (3). Finally, we
      update the current node to be the next node (1):

                   3   5
                   ● → ●
          1        ↑
      ○ → ●
          ↑    2   4   6
               ● → ● → ●
               ↑

      This process is repeated until either of the lists is exhausted
      (head == null). At which point, the remaining list is attached to the
      merged list:

           1   2   3   4   5   6
       ○ → ● → ● → ● → ● → ● → ●
                           ↑

      We then use the head sentinel node to return the actual head of the
      merged list.
"""

from src.classes import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        prehead = ListNode(-1)
        curr = prehead
        # 1. Compare the heads of the two lists.
        # 2. Update the current node's next to be the lesser of the two.
        # 3. Update the head of the list from which the node was taken.
        # 4. Update the current node in the merged list.
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        # At this point, list1 or list2 may still have nodes. The non-null list
        # is attached to the end of the merged list at 'curr'.
        curr.next = list1 if list1 else list2
        return prehead.next
