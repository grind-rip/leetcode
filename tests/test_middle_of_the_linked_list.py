"""
876. Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list
"""

from unittest import TestCase

from src.middle_of_the_linked_list import Solution

from .utils import create_linked_list_from_list, create_list_from_linked_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [3, 4, 5]
        l1 = create_linked_list_from_list([1, 2, 3, 4, 5])
        ll = Solution().middleNode(l1)
        assert create_list_from_linked_list(ll) == exp

    def test_2(self):
        exp = [4, 5, 6]
        l1 = create_linked_list_from_list([1, 2, 3, 4, 5, 6])
        ll = Solution().middleNode(l1)
        assert create_list_from_linked_list(ll) == exp
