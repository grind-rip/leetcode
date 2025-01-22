"""
19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""

from unittest import TestCase

from src.remove_nth_node_from_end_of_list import Solution

from .utils import create_linked_list_from_list, create_list_from_linked_list


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 2, 3, 5]
        l1 = create_linked_list_from_list([1, 2, 3, 4, 5])
        ll = Solution().removeNthFromEnd(l1, 2)
        assert create_list_from_linked_list(ll) == exp

    def test_2(self):
        exp = []
        l1 = create_linked_list_from_list([1])
        ll = Solution().removeNthFromEnd(l1, 1)
        assert create_list_from_linked_list(ll) == exp

    def test_3(self):
        exp = [1]
        l1 = create_linked_list_from_list([1, 2])
        ll = Solution().removeNthFromEnd(l1, 1)
        assert create_list_from_linked_list(ll) == exp

    def test_4(self):
        exp = [2]
        l1 = create_linked_list_from_list([1, 2])
        ll = Solution().removeNthFromEnd(l1, 2)
        assert create_list_from_linked_list(ll) == exp
