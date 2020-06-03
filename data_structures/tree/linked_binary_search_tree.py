"""The custom implementation of a binary search tree based on linked nodes."""
from __future__ import annotations
from typing import TypeVar, Generic
from .linked_binary_tree import LinkedBinaryTree, LinkedBinaryTreeNode
from .binary_search_tree import BinarySearchTree, BinarySearchTreeNode


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the tree."""


class LinkedBinarySearchTreeNode(
        Generic[GT],
        LinkedBinaryTreeNode[GT],
        BinarySearchTreeNode[GT],
    ):  # pylint: disable=too-many-ancestors
    """
    `LinkedBinarySearchTreeNode[T](val)` -> a single node in a linked-list-based
        binary search tree for values of type `T`, which has `val` as the stored
        value of the node and has no child node.

    This is a custom implementation of a binary search tree node based on linked
    nodes for learning purpose.

    Args:
        val: the value of the root node

    Attributes:
        val (T): the value of the node
        left (LinkedBinaryTreeNode[T]): the left child node
        right (LinkedBinaryTreeNode[T]): the right child node
    """

    def _delete_root_val_and_promote_closet_val_to_root(self, side: str) -> None:
        other = 'right' if side == 'left' else 'left'
        parent = getattr(self, side)
        node = getattr(parent, other)
        if node:
            while getattr(node, other):
                parent, node = node, getattr(node, other)
            self.val = node.val
            setattr(parent, other, getattr(node, side))
        else:
            self.val = parent.val
            setattr(self, side, getattr(parent, side))


class LinkedBinarySearchTree(
        Generic[GT],
        LinkedBinaryTree[GT],
        BinarySearchTree[GT],
    ):  # pylint: disable=too-many-ancestors
    """The custom implementation of a binary search tree based on linked nodes.

    Attributes:
        root (LinkedBinarySearchTreeNode[T]): the root node of the tree
    """

    NODE = LinkedBinarySearchTreeNode
