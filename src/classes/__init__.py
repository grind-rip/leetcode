"""
Class definitions provided by LeetCode.
"""

from typing import Generic, Self, TypeVar

T = TypeVar("T")


class ListNode(Generic[T]):
    """
    A list node in a singly-linked list.
    """

    def __init__(self, val: T, next: Self | None = None) -> None:
        self.val: T = val
        self.next: ListNode | None = next


class TreeNode(Generic[T]):
    """
    A tree node in a binary tree.
    """

    def __init__(self, val: T, left: Self | None = None, right: Self | None = None) -> None:
        self.val: T = val
        self.left: TreeNode[T] | None = right
        self.right: TreeNode[T] | None = left
