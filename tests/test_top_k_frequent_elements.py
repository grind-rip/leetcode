"""
347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements
"""

from unittest import TestCase

from src.top_k_frequent_elements import HeapSolution, QuickselectSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 2]
        assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == exp

    def test_2(self):
        exp = [1]
        assert Solution().topKFrequent([1], 1) == exp

    def test_3(self):
        exp = [1, 2, 3]
        assert Solution().topKFrequent([1, 1, 1, 2, 2, 2, 3, 3, 3], 3) == exp


class TestHeapSolution(TestCase):
    def test_1(self):
        exp = [1, 2]
        assert HeapSolution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == exp

    def test_2(self):
        exp = [1]
        assert HeapSolution().topKFrequent([1], 1) == exp

    def test_3(self):
        exp = [1, 2, 3]
        assert HeapSolution().topKFrequent([1, 1, 1, 2, 2, 2, 3, 3, 3], 3) == exp


class TestQuickselectSolution(TestCase):
    def test_1(self):
        exp = [1, 2]
        assert QuickselectSolution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == exp

    def test_2(self):
        exp = [1]
        assert QuickselectSolution().topKFrequent([1], 1) == exp

    def test_3(self):
        exp = [1, 2, 3]
        assert QuickselectSolution().topKFrequent([1, 1, 1, 2, 2, 2, 3, 3, 3], 3) == exp
