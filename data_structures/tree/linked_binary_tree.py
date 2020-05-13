"""The custom implementation of a binary tree based on linked nodes.

This module illustrates the foundation knowledge of implementing a binary tree
using linked nodes. The implementation does not use too much Python's language
advantages and may look dumb. This is by purpose because it only serves as an
data structure exercise and has no practical usage.
"""
from typing import TypeVar
from .binary_tree import BinaryTree


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the binary tree,"""


class LinkedBinaryTree(BinaryTree[GT]):
    """
    `LinkedBinaryTree[T](val)` -> a single node binary tree based on linked
        nodes for values of type `T`, which has `val` as the value of the root
        node and has no child node.

    This is a custom implementation of a binary tree based on linked nodes for
    learning purpose.

    Args:
        val: the value of the root node

    Attributes:
        val (T): the value of the node
        left (LinkedBinaryTree[T]): the left child node
        right (LinkedBinaryTree[T]): the right child node
    """

    def __init__(self, val: GT):
        super().__init__(val)
        self._left = None
        self._right = None

    @property
    def left(self) -> BinaryTree[GT]:
        """The left child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._left

    @left.setter
    def left(self, val: GT) -> None:
        self._left = LinkedBinaryTree(val)

    @property
    def right(self) -> BinaryTree[GT]:
        """The right child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._right

    @right.setter
    def right(self, val: GT) -> None:
        self._right = LinkedBinaryTree(val)
