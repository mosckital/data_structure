"""The custom implementation of a binary tree based on doubly linked nodes.

This module illustrates the foundation knowledge of implementing a binary tree
using doubly linked nodes. The implementation does not use too much Python's
language advantages and may look dumb. This is by purpose because it only serves
as a data structure exercise and has no practical usage.
"""
from .linked_binary_tree import LinkedBinaryTree, LinkedBinaryTreeNode, GT


class DoublyLinkedBinaryTreeNode(LinkedBinaryTreeNode[GT]):
    """
    `DoublyLinkedBinaryTreeNode[T](val)` -> a single node in a doubly linked
        node based binary tree for values of type `T`, which has `val` as the
        stored value of the node and has no child node.

    This is a custom implementation of a binary tree node based on linked nodes
    for learning purpose.

    Args:
        val: the value of the root node

    Attributes:
        val (T): the value of the node
        left (DoublyLinkedBinaryTreeNode[T]): the left child node
        right (DoublyLinkedBinaryTreeNode[T]): the right child node
        parent (DoublyLinkedBinaryTreeNode[T]): the parent node
    """

    def __init__(self, val):
        super().__init__(val)
        self.parent: DoublyLinkedBinaryTreeNode[GT] = None

    def _assign_child(self, val, child_name):
        super()._assign_child(val, child_name)
        if getattr(self, child_name):
            getattr(self, child_name).parent = self

class DoublyLinkedBinaryTree(LinkedBinaryTree[GT]):
    # pylint: disable=too-few-public-methods
    """The custom implementation of a binary tree based on doubly linked nodes.

    Attributes:
        root (DoublyLinkedBinaryTreeNode[T]): the root node of the binary tree
    """

    NODE = DoublyLinkedBinaryTreeNode
