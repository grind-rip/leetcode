"""
704. Binary Search

https://leetcode.com/problems/binary-search
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Return the index of the target value. If the target value is not in the
        list, return -1.

        This implementation uses an iterative approach rather than recursive,
        as it avoids the overhead of recursion. When using the recursive
        approach, it is important to note that the original list must be passed
        to the recursive function along with the target and left and right
        indices.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1
