"""
88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array
"""

from unittest import TestCase

from src.merge_sorted_array import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 2, 2, 3, 5, 6]
        nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
        Solution().merge(nums1, 3, nums2, 3)
        assert nums1 == exp

    def test_2(self):
        exp = [1]
        nums1, nums2 = [1], []
        Solution().merge(nums1, 1, nums2, 0)
        assert nums1 == exp

    def test_3(self):
        exp = [1]
        nums1, nums2 = [0], [1]
        Solution().merge(nums1, 0, nums2, 1)
        assert nums1 == exp

    def test_4(self):
        exp = [1, 2, 3, 4, 5, 6]
        nums1, nums2 = [4, 5, 6, 0, 0, 0], [1, 2, 3]
        Solution().merge(nums1, 3, nums2, 3)
        assert nums1 == exp
