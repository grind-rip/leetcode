"""
443. String Compression

https://leetcode.com/problems/string-compression
"""

from unittest import TestCase

from src.string_compression import SimplifiedSolution, Solution


class TestSolution(TestCase):
    def test_1(self):
        exp = 6
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        assert Solution().compress(chars) == exp
        assert chars == ["a", "2", "b", "2", "c", "3"]

    def test_2(self):
        exp = 1
        chars = ["a"]
        assert Solution().compress(chars) == exp
        assert chars == ["a"]

    def test_3(self):
        exp = 4
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        assert Solution().compress(chars) == exp
        assert chars == ["a", "b", "1", "2"]


class TestSimplifiedSolution(TestCase):
    def test_1(self):
        exp = 6
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        assert SimplifiedSolution().compress(chars) == exp
        assert chars == ["a", "2", "b", "2", "c", "3"]

    def test_2(self):
        exp = 1
        chars = ["a"]
        assert SimplifiedSolution().compress(chars) == exp
        assert chars == ["a"]

    def test_3(self):
        exp = 4
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        assert SimplifiedSolution().compress(chars) == exp
        assert chars == ["a", "b", "1", "2"]
