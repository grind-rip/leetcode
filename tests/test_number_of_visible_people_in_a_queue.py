"""
1944. Number of Visible People in a Queue

https://leetcode.com/problems/number-of-visible-people-in-a-queue
"""

from unittest import TestCase

from src.number_of_visible_people_in_a_queue import OptimizedSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [3, 1, 2, 1, 1, 0]
        assert Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9]) == exp

    def test_2(self):
        exp = [4, 1, 1, 1, 0]
        assert Solution().canSeePersonsCount([5, 1, 2, 3, 10]) == exp


class TestOptimizedSolution(TestCase):
    def test_1(self):
        exp = [3, 1, 2, 1, 1, 0]
        assert OptimizedSolution().canSeePersonsCount([10, 6, 8, 5, 11, 9]) == exp

    def test_2(self):
        exp = [4, 1, 1, 1, 0]
        assert OptimizedSolution().canSeePersonsCount([5, 1, 2, 3, 10]) == exp
