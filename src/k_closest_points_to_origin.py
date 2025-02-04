"""
973. K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin

NOTES
  * I call it house work, 'cause it's light work. Calculate distance,
    maintain max-heap (closest distance is equivalent to smallest distance) of
    k points.
"""

import heapq
import math


class Solution:
    """
    Maintains a max-heap of size k containing the k closest points to the
    origin. Since the `heapq` module only provides an implementation for a min-
    heap, the distance is negated before being inserted into the heap.
    """

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap: list[tuple[float, list[int]]] = []  # (distance, [xi,yi])

        for i, p in enumerate(points):
            d = math.sqrt(p[0] ** 2 + p[1] ** 2)
            if i < k:
                heapq.heappush(heap, (-d, p))
            elif -d > heap[0][0]:
                heapq.heapreplace(heap, (-d, p))

        return [p[1] for p in heap]
