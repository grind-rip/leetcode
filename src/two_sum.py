"""
1. Two Sum

https://leetcode.com/problems/two-sum

NOTES
  * Use a hash table for complement lookups.
"""
from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d: Dict[int, int] = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in d:
                return [d[c], i]
            else:
                d[n] = i
        return []
