"""
297. Serialize and Deserialize Binary Tree

https://leetcode.com/problems/serialize-and-deserialize-binary-tree
"""

from unittest import TestCase

from src.serialize_and_deserialize_binary_tree import Codec
from tests.utils import deserialize_binary_tree, serialize_binary_tree


class TestSolution(TestCase):
    def test_1(self):
        exp = [1, 2, 3, None, None, 4, 5]
        root = deserialize_binary_tree([1, 2, 3, None, None, 4, 5])
        s = Codec()
        d = Codec()
        assert serialize_binary_tree(root=d.deserialize(s.serialize(root))) == exp

    def test_2(self):
        exp = []
        root = deserialize_binary_tree([])
        s = Codec()
        d = Codec()
        assert serialize_binary_tree(root=d.deserialize(s.serialize(root))) == exp

    def test_3(self):
        exp = [1, 2, 2]
        root = deserialize_binary_tree([1, 2, 2])
        s = Codec()
        d = Codec()
        assert serialize_binary_tree(root=d.deserialize(s.serialize(root))) == exp

    def test_4(self):
        exp = [1, 2, 3, None, None, 4, 5, 6, 7]
        root = deserialize_binary_tree([1, 2, 3, None, None, 4, 5, 6, 7])
        s = Codec()
        d = Codec()
        assert serialize_binary_tree(root=d.deserialize(s.serialize(root))) == exp
