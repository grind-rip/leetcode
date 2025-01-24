"""
143. Reorder List

https://leetcode.com/problems/reorder-list
"""

from unittest import TestCase

from src.reorder_list import Solution

from .utils import create_linked_list_from_list, create_list_from_linked_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 4, 2, 3]
        ll = create_linked_list_from_list([1, 2, 3, 4])
        Solution().reorderList(ll)
        assert create_list_from_linked_list(ll) == exp

    def test_2(self):
        exp = [1, 5, 2, 4, 3]
        ll = create_linked_list_from_list([1, 2, 3, 4, 5])
        Solution().reorderList(ll)
        assert create_list_from_linked_list(ll) == exp
