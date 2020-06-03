"""The custom implementation of a binary search tree based on array."""
from __future__ import annotations
from typing import TypeVar, Generic
from .array_binary_tree import ArrayBinaryTree, ArrayBinaryTreeNode
from .binary_search_tree import BinarySearchTree, BinarySearchTreeNode


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the tree."""


class ArrayBinarySearchTreeNode(
        Generic[GT],
        ArrayBinaryTreeNode[GT],
        BinarySearchTreeNode[GT],
    ):  # pylint: disable=too-many-ancestors
    """
    `ArrayBinarySearchTreeNode[T](val)` -> a single node in an array-based
        binary search tree for values of type `T`, which has `val` as the stored
        value of the node and has no child node.

    `ArrayBinarySearchTreeNode[T](val, idx, arr)` -> a node with a value `val`
        of a binary search tree that the list representation of the tree is
        `arr` and the index of the node in the list representation is `idx`.

    This is a custom implementation of a binary search tree node based on array
    for learning purpose.

    Args:
        val (T): the value of the constructed node
        idx (int): the index of the node in the list representation
        arr (Sequence[T]): the list representation of the whole tree

    Attributes:
        val (T): the value of the node
        left (ArrayBinaryTreeNode[T]): the left child node
        right (ArrayBinaryTreeNode[T]): the right child node
    """

    def _delete_root_val_and_promote_closet_val_to_root(self, side: str) -> None:
        other = 'right' if side == 'left' else 'left'
        node = self
        while getattr(node, side):
            closest = getattr(node, side)
            while getattr(closest, other):
                closest = getattr(closest, other)
            node.val = closest.val
            node = closest
        node.val = None


class ArrayBinarySearchTree(
        Generic[GT],
        ArrayBinaryTree[GT],
        BinarySearchTree[GT],
    ):  # pylint: disable=too-many-ancestors
    """The custom implementation of a binary search tree based on an array.

    Attributes:
        root (ArrayBinarySearchTreeNode[T]): the root node of the tree
    """

    NODE = ArrayBinarySearchTreeNode
