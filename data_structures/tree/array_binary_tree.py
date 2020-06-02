"""The custom implementation of a binary tree based on array.

This module illustrates the foundation knowledge of implementing a binary tree
using an array. The implementation does not use too much Python's language
advantages and may look dumb. This is by purpose because it only serves as an
data structure exercise and has no practical usage.
"""
from __future__ import annotations
from typing import TypeVar, Sequence, Optional
from .binary_tree import BinaryTree, BinaryTreeNode


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the binary tree."""


class ArrayBinaryTreeNode(BinaryTreeNode[GT]):
    """
    `ArrayBinaryTreeNode[T](val)` -> a single node in an array-based binary tree
        for values of type `T`, which has `val` as the stored value of the node
        and has no child node.

    `ArrayBinaryTreeNode[T](val, idx, arr)` -> a node with a value `val` of a
        binary tree that the list representation of the tree is `arr` and the
        index of the node in the list representation is `idx`.

    This is a custom implementation of a binary tree node based on array for
    learning purpose.

    Args:
        val (T): the value of the constructed node
        idx (int): the index of the node in the list representation
        arr (Sequence[T]): the list representation of the whole binary tree

    Attributes:
        val (T): the value of the node
        left (ArrayBinaryTreeNode[T]): the left child node
        right (ArrayBinaryTreeNode[T]): the right child node
    """

    def __init__(self, val: GT, idx: int = 1, arr: Optional[Sequence[GT]] = None):
        self._idx = idx
        self._arr = arr if arr else [None, val]
        # move the super init to the end as it will call the _getter()/_setter()
        # and these require _arr to be initiated beforehand
        super().__init__(val)

    def _getter(self, idx: int) -> ArrayBinaryTreeNode[GT]:
        if idx < len(self._arr) and self._arr[idx] is not None:
            return ArrayBinaryTreeNode[GT](self._arr[idx], idx, self._arr)
        return None

    def _setter(self, idx: int, val: Optional[GT]) -> None:
        if idx >= len(self._arr):
            self._arr.extend([None] * len(self._arr))
        self._arr[idx] = val

    @property
    def val(self) -> GT:
        """The stored value of the node."""
        return self._arr[self._idx]

    @val.setter
    def val(self, val: Optional[GT]) -> None:
        self._arr[self._idx] = val

    @property
    def left(self) -> BinaryTree[GT]:
        """The left child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._getter(2 * self._idx)

    @left.setter
    def left(self, val: Optional[GT]) -> None:
        self._setter(2 * self._idx, val)

    @property
    def right(self) -> BinaryTree[GT]:
        """The right child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._getter(2 * self._idx + 1)

    @right.setter
    def right(self, val: Optional[GT]) -> None:
        self._setter(2 * self._idx + 1, val)


class ArrayBinaryTree(BinaryTree[GT]):
    """The custom implementation of a binary tree based on an array.

    Attributes:
        root (ArrayBinaryTreeNode[T]): the root node of the binary tree
    """

    NODE = ArrayBinaryTreeNode
