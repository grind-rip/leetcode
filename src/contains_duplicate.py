"""
217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate

NOTES
  * Easy hash map problem.

An O(n^2) solution will produce "Time Limit Exceeded".
"""


class Solution:
    """
    This solution has O(n) time complexity and O(n) space complexity in the
    worst case.
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        m: dict[int, int] = {}
        for n in nums:
            if n in m:
                return True
            m[n] = 1
        return False
