"""
209. Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum

NOTES
  * Use a sliding window.

A subarray is a contiguous, non-empty sequence of elements within an array.
Here, we just apply the canonical subarray/substring solution using a sliding
window.
"""

import sys


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, right, current_sum, current_size, minimum_size = 0, 0, 0, 0, sys.maxsize

        while right < len(nums):
            current_sum += nums[right]
            current_size += 1
            while left <= right and current_sum >= target:
                if current_size < minimum_size:
                    minimum_size = current_size
                current_sum -= nums[left]
                current_size -= 1
                left += 1
            right += 1

        return minimum_size if minimum_size < sys.maxsize else 0
