"""
23. Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists
"""

from unittest import TestCase

from src.merge_k_sorted_lists import Solution

from .utils import create_linked_list_from_list, create_list_from_linked_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 1, 2, 3, 4, 4, 5, 6]
        ls = [[1, 4, 5], [1, 3, 4], [2, 6]]
        lls = [create_linked_list_from_list(l) for l in ls]
        ll = Solution().mergeKLists(lls)
        assert create_list_from_linked_list(ll) == exp

    def test_2(self):
        exp = []
        ls = []
        lls = []
        lls = [create_linked_list_from_list(l) for l in ls]
        ll = Solution().mergeKLists(lls)
        assert create_list_from_linked_list(ll) == exp

    def test_3(self):
        exp = []
        ls = [[]]
        lls = [create_linked_list_from_list(l) for l in ls]
        ll = Solution().mergeKLists(lls)
        assert create_list_from_linked_list(ll) == exp
