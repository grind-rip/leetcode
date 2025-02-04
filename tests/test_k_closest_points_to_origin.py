"""
973. K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin
"""

from unittest import TestCase

from src.k_closest_points_to_origin import Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = sorted([[-2, 2]])
        assert sorted(Solution().kClosest([[1, 3], [-2, 2]], 1)) == exp

    def test_2(self):
        exp = sorted([[3, 3], [-2, 4]])
        assert sorted(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == exp
