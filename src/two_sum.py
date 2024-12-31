"""
1. Two Sum

https://leetcode.com/problems/two-sum

NOTES
  * Use a hash table for complement lookups.

This solution has O(n) time complexity.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d: dict[int, int] = {}  # {num: index}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            else:
                d[n] = i
        return []
