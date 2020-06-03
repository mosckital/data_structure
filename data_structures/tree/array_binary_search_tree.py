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

    def delete(self, val):
        # case to potentially delete the value in the left child tree
        if val < self.val:
            if self.left:
                return self.left.delete(val)
            return False
        # case to potentially delete the value in the right child tree
        if val > self.val:
            if self.right:
                return self.right.delete(val)
            return False
        # case to delete the root node
        if self.right:
            # if there is value larger than the value of the root node, find the
            # successor value, delete its node and reassign the value to root
            node = self
            while node.right:
                successor_node = node.right.inorder_successor_node(node.val)
                node.val = successor_node.val
                node = successor_node
            node.val = None
        elif self.left:
            # if there is no value larger than the value of the root, but value
            # smaller, find the largest one of the smaller values, delete its
            # node and reassign the value to root
            node = self
            while node.left:
                less_max = node.left
                while less_max.right:
                    less_max = less_max.right
                node.val = less_max.val
                node = less_max
            node.val = None
        else:
            # case of no child node, so to delete the root node
            self.val = None
        return True


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
