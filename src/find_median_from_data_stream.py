"""
295. Find Median from Data Stream

https://leetcode.com/problems/find-median-from-data-stream

NOTES
  * There are a few different approaches to this problem:
      1. Maintain an unsorted array. Sort the array to find the median.
      2. Maintain a sorted array.
      3. Use two heaps.
      4. Self-balancing BST.

We will focus on 3 and 4, since they are most interesting solutions.

Two Heaps
---------
Two heaps are maintained:
  * A max-heap for elements smaller than the median
  * A min-heap for elements greater than the median

If the heaps are balanced, the median can be calculated from the root of each
heap. If the heaps are unbalanced (the max-heap contains one more element than
the min-heap), the median is the root of the max-heap.

When performing an insertion, the new element is compared to the root of the
max-heap. If the element is less than or equal to the median, the element is
added to the max-heap. If the element is greater than the median, it is added
to the min-heap. If the insertion causes the heaps to become unbalanced, the
root of the offending heap is removed and added to the other heap.

Self-balancing BST
------------------
TODO
"""

import heapq


class MedianFinder:
    def __init__(self) -> None:
        # max-heap for elements smaller than the median
        self.max_heap: list[int] = []
        # min-heap for elements greater than the median
        self.min_heap: list[int] = []

    def addNum(self, num: int) -> None:
        if not len(self.max_heap):
            self.max_heap.append(-num)
            return

        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            e = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -e)

        if len(self.min_heap) > len(self.max_heap):
            e = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -e)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return float(-self.max_heap[0])
