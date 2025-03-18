"""
1944. Number of Visible People in a Queue

https://leetcode.com/problems/number-of-visible-people-in-a-queue

NOTES
  * Traverse the array from the right and use a monotonically decreasing stack.

A brute force solution would be to iterate from 0 to n-1 and with each
iteration, count the number of people for which heights[i] > heights[j]. This
solution would require O(n^2) time complexity.

The optimal solution leverages a monotonically decreasing stack, which
maintains the indices of the heights of people, which can be seen.

The solution can be optimized by combining the steps for determining the number
of people the ith person can see to their right in the queue and maintaining
the monotonic property.
"""

from collections import deque


class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        stack: deque[int] = deque()
        ans: list[int] = [0] * n

        for i in reversed(range(n)):
            # Determine the number of people the ith person can see to their
            # right in the queue.
            #
            # The ith person can see the jth person if i < j and
            # min(heights[i], heights[j]) > max(heights[i+1...j-1]).
            if stack:
                min_height = min(heights[i], heights[stack[0]])
                j = len(stack) - 1
                while j >= 0 and min_height > heights[stack[j]]:
                    j -= 1
                ans[i] = len(stack) - j

            # Maintain monotonic property.
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()

            stack.append(i)

        return ans


class OptimizedSolution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        stack: deque[int] = deque()
        ans: list[int] = [0] * n

        for i in reversed(range(n)):
            # Determine the number of people the ith person can see to their
            # right in the queue, while maintaining the monotonic property.
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                ans[i] += 1
            if stack:
                ans[i] += 1

            stack.append(i)

        return ans
