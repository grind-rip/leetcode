"""
1. Two Sum

https://leetcode.com/problems/two-sum

NOTES
  * Use a hash table for complement lookups.

This solution has O(n) time complexity.

Additionally, you may be asked to return a list of all pairs, in which case,
instead of immediately returning the complement, it can be added to a list of
tuples.

Q: How would you solve for negative numbers?
A: The complement solution still accomodates negative numbers.

Q: How would you solve for duplicate pairs?
A: To avoid duplicate pairs, store the pairs using a consistent order in a set.
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
