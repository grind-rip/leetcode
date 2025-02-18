"""
Utility functions for testing.
"""

from collections import deque

from src.classes import ListNode, T, TreeNode


def create_linked_list_from_list(l: list[int]) -> ListNode | None:
    """
    Creates a linked list from a list of integers, where each element of the
    list becomes a node in the linked list. Returns the head of the linked
    list.
    """
    if not l:
        return None
    head = ListNode(l[0])
    curr = head
    for val in l[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def create_cyclic_linked_list_from_list(l: list[int], pos: int) -> ListNode | None:
    """
    Creates a cyclic linked list from a list of integers. The `pos` parameter
    specifies the 0-based index from the list, which represents a node in the
    linked list. The last node in the linked list points back to the node at
    this position, creating a cycle.
    """
    if not l:
        return None
    head = ListNode(l[0])
    curr = head
    # `start` is the node that starts the cycle commonly referred to as the
    # "cycle entry node" or "loop starting node".
    start = None
    for i, val in enumerate(l[1:]):
        curr.next = ListNode(val)
        if i == pos:
            start = curr
        curr = curr.next
    curr.next = start
    return head


def create_list_from_linked_list(head: ListNode | None) -> list[int]:
    """
    Creates a list of integers from the head of a linked list.
    """
    if not head:
        return []
    l: list[int] = []
    while head:
        l.append(head.val)
        head = head.next
    return l


def create_binary_tree_from_list(l: list[int | None]) -> TreeNode | None:
    """
    Creates a binary tree from a list of integers, where each element of the
    list becomes a node in the binary tree. Returns the root of the binary
    tree.

    For zero-based arrays, the rule is that a node at position `i` has children
    at positions `2*i+1` and `2*i+2`; in the other direction, a node at
    position `i` has a parent at position `(i-1)/2` (which rounds down). This
    is equivalent to storing a binary tree in an array by reading through the
    tree in breadth-first search order.

    NOTE: Gaps in the binary tree should be denoted by `None`.
    """
    if not l:
        return None
    return _create_binary_tree_from_list(l, 0)


def _create_binary_tree_from_list(l: list[int | None], i: int) -> TreeNode | None:
    """
    Helper function for `create_binary_tree_from_list()`. Given a list of
    integers and an index, which represents a node in the binary tree,
    recursively create the binary tree.
    """
    # If the index is out of bounds of the array, the previous node was a leaf,
    # therefore return None.
    # If the current node is None, it represents a gap in the binary tree,
    # therefore return None.
    if i >= len(l) or l[i] is None:
        return None

    # Create node with current value
    node = TreeNode(l[i])

    # Recursively build left and right subtrees using child indices.
    node.left = _create_binary_tree_from_list(l, 2 * i + 1)
    node.right = _create_binary_tree_from_list(l, 2 * i + 2)

    return node


def create_bfs_list_from_binary_tree(*, root: TreeNode | None, values_only: bool = True) -> list[TreeNode | T]:
    """
    Creates a list of nodes in breadth-first search order given the root node
    of a binary tree. If values_only is False, the list contains the TreeNode
    objects themselves.

    Breadth-first order always attempts to visit the node closest to the root
    that it has not already visited. This is also called a level-order
    traversal.
    """
    if not root:
        return []

    l: list[TreeNode | T] = []
    q: deque[TreeNode] = deque([root])

    while q:
        curr: TreeNode = q.popleft()
        if values_only:
            l.append(curr.val)
        else:
            l.append(curr)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

    return l


def assert_tree(root: TreeNode | None, exp: list[T | None]) -> None:
    """
    Given a list of values in level-order traversal, assert that the tree
    matches the expected values. Gaps in the tree should be denoted by None.
    """

    def _assert_tree(root: TreeNode | None, i: int, exp: list[T | None]) -> None:
        if not root:
            return None
        assert root.val == exp[i]
        _assert_tree(root.left, 2 * i + 1, exp)
        _assert_tree(root.right, 2 * i + 2, exp)

    _assert_tree(root, 0, exp)
