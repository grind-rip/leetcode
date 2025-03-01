"""
75. Sort Colors

https://leetcode.com/problems/sort-colors

NOTES
  * Use three-way partitioning (Dutch national flag problem).
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1

        while j <= k:
            if nums[j] > 1:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] < 1:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            else:
                j += 1
