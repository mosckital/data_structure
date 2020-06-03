"""The custom implementation of a binary tree based on linked nodes.

This module illustrates the foundation knowledge of implementing a binary tree
using linked nodes. The implementation does not use too much Python's language
advantages and may look dumb. This is by purpose because it only serves as an
data structure exercise and has no practical usage.
"""
from __future__ import annotations
from typing import Optional, Union
from .binary_tree import BinaryTree, BinaryTreeNode, GT


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

    def _assign_child(
            self,
            val: Union[Optional[LinkedBinaryTreeNode[GT]], GT],
            child_name: str
        ) -> None:
        if val is not None:
            # use type() here as the actual type could be a subclass
            if isinstance(val, type(self)):
                # if a node instead of a value is passed in, assign the node to
                # the left child directly
                setattr(self, child_name, val)
            else:
                setattr(self, child_name, type(self)[GT](val))
        else:
            setattr(self, child_name, None)

    @property
    def left(self) -> LinkedBinaryTreeNode[GT]:
        """The left child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._left

    @left.setter
    def left(self, val: Union[Optional[LinkedBinaryTreeNode[GT]], GT]) -> None:
        self._assign_child(val, '_left')

    @property
    def right(self) -> LinkedBinaryTreeNode[GT]:
        """The right child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._right

    @right.setter
    def right(self, val: Union[Optional[LinkedBinaryTreeNode[GT]], GT]) -> None:
        self._assign_child(val, '_right')


class LinkedBinaryTree(BinaryTree[GT]):
    """The custom implementation of a binary tree based on linked nodes.

    Attributes:
        root (LinkedBinaryTreeNode[T]): the root node of the binary tree
    """

    NODE = LinkedBinaryTreeNode
