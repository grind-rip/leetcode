"""
217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate

NOTES
  * Easy hash map problem.

If one were to use an O(n^2) solution, this would produce "Time Limit Exceeded"
on LeetCode. Usually, if an algorithm is O(n^2), LeetCode will allow `n` up to
around 10^4. A solution will produce "Time Limit Exceeded" when n ≥ 10^5.
"""

from typing import Dict, List


class Solution:
    """
    This solution has O(n) time complexity and O(n) space complexity in the
    worst case.
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        m: Dict[int, int] = {}
        for n in nums:
            if n in m:
                return True
            m[n] = 1
        return False
