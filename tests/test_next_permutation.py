"""
31. Next Permutation

https://leetcode.com/problems/next-permutation
"""

from unittest import TestCase

from src.next_permutation import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp, nums = [1, 3, 2], [1, 2, 3]
        Solution().nextPermutation(nums)
        assert nums == exp

    def test_2(self):
        exp, nums = [1, 2, 3], [3, 2, 1]
        Solution().nextPermutation(nums)
        assert nums == exp

    def test_3(self):
        exp, nums = [1, 5, 1], [1, 1, 5]
        Solution().nextPermutation(nums)
        assert nums == exp

    def test_4(self):
        exp, nums = [5, 1, 1], [1, 5, 1]
        Solution().nextPermutation(nums)
        assert nums == exp
