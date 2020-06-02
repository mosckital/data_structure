"""The custom implementation of a binary search tree based on linked nodes."""
from __future__ import annotations
from typing import TypeVar, Generic, Optional, Union
from .binary_tree import BinaryTree
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

    @property
    def left(self) -> BinaryTree[GT]:
        """The left child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._left

    @left.setter
    def left(self, val: Union[Optional[LinkedBinarySearchTreeNode[GT]], GT]) -> None:
        if val is not None:
            if isinstance(val, LinkedBinarySearchTreeNode):
                # if a node instead of a value is passed in, assign the node to
                # the left child directly
                self._left = val
            else:
                self._left = LinkedBinarySearchTreeNode(val)
        else:
            self._left = None

    @property
    def right(self) -> BinaryTree[GT]:
        """The right child node.

        Just pass in the value of type `GT` instead of a node for assignment.
        """
        return self._right

    @right.setter
    def right(self, val: Union[Optional[LinkedBinarySearchTreeNode[GT]], GT]) -> None:
        if val is not None:
            if isinstance(val, LinkedBinarySearchTreeNode):
                # if a node instead of a value is passed in, assign the node to
                # the right child directly
                self._right = val
            else:
                self._right = LinkedBinarySearchTreeNode(val)
        else:
            self._right = None

    def delete(self, val):
        # pylint: disable=attribute-defined-outside-init, access-member-before-definition
        if val < self.val:
            return self.left.delete(val) if self.left else False
        if val > self.val:
            return self.right.delete(val) if self.right else False
        # case val == self.val
        if self.right:
            if self.right.left:
                parent, node = self.right, self.right.left
                while node.left:
                    parent, node = node, node.left
                self.val = node.val
                parent.left = node.right
            else:
                self.val = self.right.val
                self.right = self.right.right
        elif self.left:
            if self.left.right:
                parent, node = self.left, self.left.right
                while node.right:
                    parent, node = node, node.right
                self.val = node.val
                parent.right = node.left
            else:
                self.val = self.left.val
                self.left = self.left.left
        else:
            raise NotImplementedError('Cannot delete a node from itself!')
        return True


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

    def insert(self, val):
        # pylint: disable=attribute-defined-outside-init
        if self.root:
            super().insert(val)  # pylint: disable=no-member
        else:
            # create a new root node if the tree is empty
            self.root = LinkedBinarySearchTreeNode[GT].from_list_repr([val])

    def delete(self, val):
        try:
            super().delete(val)  # pylint: disable=no-member
        except NotImplementedError:
            # delete the root node if the tree only has the root node and the
            # root node is the target to delete
            # pylint: disable=attribute-defined-outside-init
            self.root = None
