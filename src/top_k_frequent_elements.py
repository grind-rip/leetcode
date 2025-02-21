"""
347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements

NOTES
  * Use a heap or the quickselect algorithm.

Once you understand heaps (and the quickselect algorithm), this class of
problems becomes trivial.

If you see *kth smallest*, *k closest*, or *top k* mentioned in a question, it
typically means the problem can be solved using a heap. The general approach to
solving these problems involves maintaining a max- or min-heap of size k. The
kth smallest value is the root of the max-heap. The kth largest value is the
root of the min-heap. To retrieve all k smallest (or largest) elements, simply
return the sorted heap.

Though a heap offers O(nlog k) time complexity, the quickselect algorithm
solves this problem in linear time (O(n)).
"""

import heapq
from collections import Counter


class Solution:
    """
    This solution relies heavily on the Python Standard library, both for
    counting the frequency of elements (`Counter`) and finding the kth most
    frequent elements (`heapq.nlargest`).

    To fully understand this solution, its advisable to write out the full
    solution.
    """

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums
        # `Counter` provides a means for counting hashable items. Elements are
        # stored as keys and their counts are stored as values.
        count = Counter(nums)
        # `heapq.nlargest` returns the n (or k) largest elements in a dataset.
        # The 'key' parameter is function for retrieving the elements priority.
        return heapq.nlargest(n=k, iterable=count.keys(), key=count.get)


class HeapSolution:
    """
    This solution still leverages the `heapq` module of the Python Standard
    library, but implements its own kth largest algorithm.

    This solution has O(nlog k) time complexity (log(k) comparisons/swaps for n
    elements)).
    """

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        # Build a hash table of integer frequencies.
        # The time complexity of this operation is O(n).
        count: dict[int, int] = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        # The top k frequent elements (or kth largest) problem can be
        # efficiently solved using a min-heap. Maintaining a heap of size k,
        # the kth largest value is always the root of the min-heap. For all k
        # largest elements, simply return the heap.
        heap: list[tuple[int, int]] = []
        for i, (key, val) in enumerate(count.items()):
            # NOTE: Building a heap using k insertions is less performant
            # (O(klog k)), than building the heap using heapification (O(k)),
            # but simplifies the logic.
            if i < k:
                # NOTE: Python compares tuples element by element. Therefore,
                # the element frequency count is used to designate priority.
                heapq.heappush(heap, (val, key))
            elif val > heap[0][0]:
                heapq.heapreplace(heap, (val, key))

        # Since the problem states, "You may return the answer in any order.",
        # we simply need to return the heap. For consistency, the heap is
        # sorted anyway.
        return sorted([k for _, k in heap])


class QuickselectSolution:
    """
    Return the top k frequent elements using the quickselect algorithm.

    Quickselect (also known as Hoare's selection algorithm) is a selection
    algorithm to find the kth smallest (or largest) element in an unordered
    list of n elements.

    Since quickselect returns the kth element in the list, elements less than k
    are guaranteed to be less than (or greater than) k. Thus allowing us to
    return the top k frequent elements in any order.

    This solution has O(n) average-case and O(n^2) worst-case time complexity.

    NOTE: Instead of finding the (n - k)th element, we simply reverse the
    comparison in the `partion()` function, since quickselect typically puts
    elements in ascending order.
    """

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        # Build a hash table of integer frequencies.
        # The time complexity of this operation is O(n).
        count: dict[int, int] = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        # The quickselect algorithm modifies the list in-place. Therefore, we
        # create a list of unique keys, which serves as our list. The values
        # associated with these keys are used for comparisons.
        l = list(count.keys())
        self.quickselect(count, l, 0, len(l) - 1, k)
        # Since the problem states, "You may return the answer in any order.",
        # we simply need to return the list up to k. For consistency, the heap
        # is sorted anyway.
        return sorted(l[:k])

    def quickselect(
        self, d: dict[int, int], l: list[int], left: int, right: int, k: int
    ) -> int:
        """
        Return the kth element (0-based) in the given list.
        """
        if left == right:
            return l[left]

        # Retrieve the index of the pivot by partitioning the list into
        # elements greater than or less than or equal to the pivot.
        pivot = self.partition(d, l, left, right)

        # If k is equal to 'pivot', then l[pivot] is the kth element in the
        # list. Otherwise, execute quickselect on the partition comprising
        # elements greater than or less than or equal to the pivot. This
        # partition is guaranteed to contain the kth element.
        if k == pivot:
            return l[k]
        elif k < pivot:
            return self.quickselect(d, l, left, pivot - 1, k)
        else:
            return self.quickselect(d, l, pivot + 1, right, k)

    def partition(self, d: dict[int, int], l: list[int], left: int, right: int) -> int:
        """
        Reorder the list such that elements greater than the pivot are before
        elements less than or equal to the pivot. When complete, the pivot is
        in its final sorted position. The pivot is chosen as the last element
        in the parition (Lomuto partition scheme).
        """

        # Choose the last element (right) as the pivot.
        pivot = l[right]

        # i (commonly referred to as the "store index") is used to denote the
        # index of the pivot. j is used for scanning the list from left to
        # right-1.
        i, j = left, left

        # The loop maintains the following invariant:
        #
        #   Elements left through i-1 (inclusive) are > pivot
        #   Elements i through j (inclusive) are ≤ pivot
        while j < right:
            if d[l[j]] > d[pivot]:
                l[i], l[j] = l[j], l[i]
                i += 1
            j += 1

        # As a final step, move pivot to its final position. This will be its
        # final position in the sorted array.
        l[i], l[right] = l[right], l[i]

        # Return the index of the pivot. The pivot index is used to determine
        # the new left and right arguments for quickselect.
        return i
