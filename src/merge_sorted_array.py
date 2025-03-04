"""
88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array

NOTES
  * Use three pointer merge algorithm.

The fact that the first array, `nums1`, has additional space (n) should signify
that the problem can be solved without additional space. Since both arrays are
already sorted, only an O(m + n) traversal is required to merge them. By
starting the traversal from m - 1 and n - 1 of `nums1` and `nums2`,
respectively, and by leveraging the additional space appended to `nums1`, the
arrays can be merged in-place without the need for additional space.
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p3 = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
                p3 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1

        while p1 >= 0:
            nums1[p3] = nums1[p1]
            p1 -= 1
            p3 -= 1

        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1
