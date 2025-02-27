"""
239. Sliding Window Maximum

https://leetcode.com/problems/sliding-window-maximum

NOTES
  * Use a sliding window and monotonic queue.

Old fren. I got this one in an Amazon OA. Here is my analysis adapted for the
'Sliding Window Maximum' problem:

This problem can be solved in linear time (O(n)) using a monotonic queue (or
monotone priority queue), a variant of a priority queue in which the priorities
of extracted items are required to form a monotonic sequence:

  For all n ∈ N,
    n+1 ≥ n for monotonically increasing
    n+1 ≤ n for monotonically decreasing

Using a monotonically decreasing queue, the index of the maximum value for the
current window under consideration is maintained at the front of the queue. For
each subsequent value i in `nums`, we remove any elements from the back of the
queue whose corresponding value is smaller than `nums[i]`. This maintains the
monotonically decreasing property of the queue and `q[0]` is always the index
of the largest integer in `nums` for the sliding window. When the indices of
the window change (e.g., when the left index is increased by one), if the
element at the front of the queue falls outside the window, it is removed.

If a monotonically decreasing queue is not used, the maximum integer would need
to be calculated for each window, which requires a double-nested loop that
scales with n.

**NOTE**: While there is a nested loop in this solution as well, the total
number of operations across all iterations of the inner loop is bounded by
O(n). This is known as amortized analysis - even though there's a nested loop,
the total work done by that inner loop across all iterations of the outer loop
is linear.
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        left, right = 0, 0

        # Maintain a monotonically decreasing queue of maximum size k. The
        # index of the largest integer in `nums` for the sliding window is
        # q[0].
        q: deque[int] = deque()
        l: list[int] = []

        while right < len(nums):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
            if right >= k - 1:
                l.append(nums[q[0]])
                if q[0] <= left:
                    q.popleft()
                left += 1
            right += 1

        return l
