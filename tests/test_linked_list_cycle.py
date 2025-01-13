"""
141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle
"""

from unittest import TestCase

from src.linked_list_cycle import Solution

from .utils import create_cyclic_linked_list_from_list


class TestSolution(TestCase):
    def test_1(self):
        exp = True
        l = create_cyclic_linked_list_from_list([3, 2, 0, -4], 1)
        assert Solution().hasCycle(l) == exp

    def test_2(self):
        exp = True
        l = create_cyclic_linked_list_from_list([1, 2], 0)
        assert Solution().hasCycle(l) == exp

    def test_3(self):
        exp = False
        l = create_cyclic_linked_list_from_list([1], -1)
        assert Solution().hasCycle(l) == exp
