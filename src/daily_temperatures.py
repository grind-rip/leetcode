"""
739. Daily Temperatures

https://leetcode.com/problems/daily-temperatures

NOTES
  * Traverse the array from the right and use a monotonically decreasing stack.

Stacks vs. Queues
-----------------
A monotonic stack and a monotonic queue are similar data structures that
maintain elements in a monotonic order (either strictly decreasing or strictly
increasing), but they differ in their operations and use cases.

  Monotonic Stack
    * Elements are added/removed from the same end (LIFO - Last In, First Out).
    * Uses push and pop operations.
    * When adding a new element, pops existing elements that violate the
      monotonic property.
    * Typically used to find the "next greater/smaller element" or to solve
      problems involving ranges where elements dominate others.

  Monotonic Queue
    * Elements are added at one end and removed from the other (FIFO - First
      In, First Out).
    * Uses enqueue (append) at one end and dequeue (popleft) from the other.
    * When adding a new element, removes existing elements that violate the
      monotonic property.
    * Often used for sliding window problems to efficiently track
      maximum/minimum values within the window.

In Python, a deque can be used for both stacks and queues, however, it is
important to differentiate when/how each data structure should be used:
    * Stack: push, pop
    * Queue: append, popleft
"""

from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: deque[int] = deque()
        ans: list[int] = [0] * len(temperatures)

        for i in reversed(range(len(temperatures))):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack and temperatures[i] < temperatures[stack[-1]]:
                ans[i] = stack[-1] - i
            stack.append(i)

        return ans
