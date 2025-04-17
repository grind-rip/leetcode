"""
253. Meeting Rooms II

https://leetcode.com/problems/meeting-rooms-ii

NOTES
  * Maintain a min-heap of meeting end times. The minimum (earliest) end time
    is the root node (heap invariant). If the end time of the root node is less
    than or equal to the start time of the current node, delete the root node
    from the heap. Insert the meeting end time into the heap. This is roughly
    equivalent to allocating/deallocating conference rooms for each meeting.
    The minimum number of conference rooms required is then the maximum size of
    the heap.

I really love this one—mainly due to the elegant use of a heap, and because I
just love heaps. <3

Time Complexity
---------------
  * There are three operations that contribute to this solution's time
    complexity:

        1. Sorting the array: O(nlog n)
        2. Removing the smallest element from the heap: O(log n)
        3. Inserting an element into the heap: O(log n)

    In the worst case, we perform the delete-min operation n times. In all
    cases, we perform the insert operation n times. Therefore, the combined
    time complexity is:

        O(nlog n) + O(nlog n) + O(nlog n)

    which condenses to simply O(nlog n).

Space Complexity
----------------
  * The min-heap has a worst-case space complexity of O(n).
"""

import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap: list[int] = []
        min_rooms = 0
        for interval in intervals:
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            min_rooms = max(min_rooms, len(heap))
        return min_rooms
