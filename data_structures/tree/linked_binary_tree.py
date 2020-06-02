"""The custom implementation of a binary tree based on linked nodes.

This module illustrates the foundation knowledge of implementing a binary tree
using linked nodes. The implementation does not use too much Python's language
advantages and may look dumb. This is by purpose because it only serves as an
data structure exercise and has no practical usage.
"""
from __future__ import annotations
from typing import TypeVar, Optional
from .binary_tree import BinaryTree, BinaryTreeNode


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the binary tree."""


class LinkedBinaryTreeNode(BinaryTreeNode[GT]):
    """
    `LinkedBinaryTreeNode[T](val)` -> a single node in a linked-list-based
        binary tree for values of type `T`, which has `val` as the stored value
        of the node and has no child node.

    This is a custom implementation of a binary tree node based on linked nodes
    for learning purpose.

    Args:
        val: the value of the root node

    Attributes:
        val (T): the value of the node
        left (LinkedBinaryTreeNode[T]): the left child node
        right (LinkedBinaryTreeNode[T]): the right child node
    """

    def __init__(self, val: GT):
        super().__init__(val)
        self._left = None
        self._right = None

    @property
    def left(self) -> LinkedBinaryTreeNode[GT]:
        """The left child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._left

    @left.setter
    def left(self, val: Optional[GT]) -> None:
        if val is not None:
            self._left = LinkedBinaryTreeNode(val)
        else:
            self._left = None

    @property
    def right(self) -> LinkedBinaryTreeNode[GT]:
        """The right child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._right

    @right.setter
    def right(self, val: Optional[GT]) -> None:
        if val is not None:
            self._right = LinkedBinaryTreeNode(val)
        else:
            self._right = None


class LinkedBinaryTree(BinaryTree[GT]):
    """The custom implementation of a binary tree based on linked nodes.

    Attributes:
        root (LinkedBinaryTreeNode[T]): the root node of the binary tree
    """

    NODE = LinkedBinaryTreeNode
