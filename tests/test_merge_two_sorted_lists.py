"""
21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists
"""

from unittest import TestCase

from src.merge_two_sorted_lists import Solution

from .utils import create_linked_list_from_list, create_list_from_linked_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 1, 2, 3, 4, 4]
        l1 = create_linked_list_from_list([1, 2, 4])
        l2 = create_linked_list_from_list([1, 3, 4])
        ll = Solution().mergeTwoLists(l1, l2)
        assert create_list_from_linked_list(ll) == exp

    def test_2(self):
        exp = []
        l1 = create_linked_list_from_list([])
        l2 = create_linked_list_from_list([])
        ll = Solution().mergeTwoLists(l1, l2)
        assert create_list_from_linked_list(ll) == exp

    def test_3(self):
        exp = [0]
        l1 = create_linked_list_from_list([])
        l2 = create_linked_list_from_list([0])
        ll = Solution().mergeTwoLists(l1, l2)
        assert create_list_from_linked_list(ll) == exp
