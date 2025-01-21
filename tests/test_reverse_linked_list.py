"""
206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list
"""

from unittest import TestCase

from src.reverse_linked_list import Solution

from .utils import create_linked_list_from_list, create_list_from_linked_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [5, 4, 3, 2, 1]
        l = create_linked_list_from_list([1, 2, 3, 4, 5])
        ll = Solution().reverseList(l)
        assert create_list_from_linked_list(ll) == exp

    def test_2(self):
        exp = [2, 1]
        l = create_linked_list_from_list([1, 2])
        ll = Solution().reverseList(l)
        assert create_list_from_linked_list(ll) == exp

    def test_3(self):
        exp = []
        l = create_linked_list_from_list([])
        ll = Solution().reverseList(l)
        assert create_list_from_linked_list(ll) == exp
