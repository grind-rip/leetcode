"""
23. Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists

NOTES
  * The naive solution to merge k sorted lists is an extension of the solution
    for merging two sorted lists. However, for k lists the time complexity
    becomes non-linear (O(nk)), since every selection costs O(k). To optimize
    the selection process we can use a priority queue, which is implemented as
    a min-heap. A heap offers O(log n) performance for inserts and removals,
    and O(n) to build the heap initially from a set of n elements.

    To start, we build a heap using the head of each list. Next, for each
    selection, we use the find-min operation (O(1)) and delete-min operation
    (O(log k)), removing the minimum value from the heap. Finally, the head of
    the list from which the node was taken is inserted into the heap. The
    selection now has the following time complexity:

      O(k) + O(1) + O(log k) + O(log k) = O(log k)

    This gives an overall time complexity of O(nlog k) and O(k) space
    complexity for the heap.

    Example (where ○ represents null):

      1   4   5
      ● → ● → ● → ○

      1   3   4
      ● → ● → ● → ○

      2   6
      ● → ● → ○

    Build a heap using the head of each list:

         1
         ●
       /   \
      1     2
      ●     ●

    For each selection, remove the minimum value from the heap:

                   4   5
                   ● → ● → ○
                   ↑

          1    1   3   4
      ○ → ●    ● → ● → ● → ○
          ↑    ↑

               2   6
               ● → ● → ○
               ↑

    Insert the head of the list from which the node was taken into the heap:

         1
         ●
       /   \
      2     4
      ●     ●
"""

import heapq

from src.classes import ListNode


class HeapNode:
    """
    Wrapper for a ListNode.

    Enables heap operations by implementing the '<' operation.
    """

    def __init__(self, node: ListNode):
        self.node: ListNode = node

    def __lt__(self, other: "HeapNode") -> bool:
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        # Build a heap using the head of each list.
        heap: list[HeapNode] = []
        for head in lists:
            if head:
                heapq.heappush(heap, HeapNode(node=head))

        # Instantiate a head sentinel node.
        prehead = ListNode(-1)
        curr = prehead

        # For each selection, use `heappop`, which removes the smallest element
        # from the heap, maintaining the heap invariant. The head of the list
        # from which the node was taken is inserted into the heap.
        while heap:
            _next = heapq.heappop(heap).node
            head = _next.next
            curr.next = _next
            curr = curr.next
            if head:
                heapq.heappush(heap, HeapNode(node=head))

        return prehead.next
