"""The Mixin class to provide the extra functionalities of a binary search tree
and its tree node.
"""
from __future__ import annotations
from typing import TypeVar, Generic, Optional
from abc import abstractmethod


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the tree."""


class BinarySearchTreeNodeMixin(Generic[GT]):
    """The Mixin class to implement the extra functionalities of a binary search
    tree node."""

    def search(self, val: GT) -> bool:
        """Search if a value is present in the sub tree of this node.

        Args:
            val: the value to look for

        Returns:
            `True` if found or `False` otherwise
        """
        if val < self.val:
            return self.left.search(val) if self.left else False
        if val > self.val:
            return self.right.search(val) if self.right else False
        return True

    def insert(self, val: GT) -> bool:
        """To insert a value into the sub tree of this node.

        Notes:
            The insertion will fail and do nothing if the value is already in
            the tree.

        Args:
            val: the value to insert

        Returns:
            `True` if inserted or `False` otherwise
        """
        if val < self.val:
            if not self.left:
                self.left = val
                return True
            return self.left.insert(val)
        if val > self.val:
            if not self.right:
                self.right = val
                return True
            return self.right.insert(val)
        return False

    @abstractmethod
    def delete(self, val: GT) -> bool:
        """To delete a value from the sub tree of this node.

        Notes:
            The deletion will fail if no such value exists.

        Args:
            val: the value to delete

        Returns:
            `True` if deleted or `False` otherwise
        """

    def inorder_successor_node(self, val: GT) \
            -> Optional[BinarySearchTreeNodeMixin[GT]]:
        """Get the node which stores the in-order successor of the given value.

        Notes:
            The function will return None if the given value is larger or equal
            to the maximum of the tree.

        Args:
            val: the reference value

        Returns:
            The node of the successor if exists or `None` otherwise
        """
        if val >= self.val:
            if self.right:
                return self.right.inorder_successor_node(val)
            return None
        if self.left:
            left_successor = self.left.inorder_successor_node(val)
            if left_successor is not None:
                return left_successor
        return self

    def inorder_successor(self, val: GT) -> Optional[GT]:
        """Get the in-order successor value of the given value.

        Notes:
            The function will return None if the given value is larger or equal
            to the maximum of the tree.

        Args:
            val: the reference value

        Returns:
            The in-order successor value if exists or `None` otherwise
        """
        successor_node = self.inorder_successor_node(val)
        return successor_node.val if successor_node else None


class BinarySearchTreeMixin(Generic[GT]):
    """The Mixin class to implement the extra functionalities of a binary search
    tree."""

    def search(self, val: GT) -> bool:
        """Search if a value is present in the tree.

        Args:
            val: the value to look for

        Returns:
            `True` if found or `False` otherwise
        """
        return self.root.search(val)

    def insert(self, val: GT) -> None:
        """To insert a value into the tree.

        Notes:
            The insertion will fail and do nothing if the value is already in
            the tree.

        Args:
            val: the value to insert

        Returns:
            `True` if inserted or `False` otherwise
        """
        self.root.insert(val)

    def delete(self, val: GT) -> None:
        """To delete a value from the sub tree of this node.

        Notes:
            The deletion will fail if no such value exists.

        Args:
            val: the value to delete

        Returns:
            `True` if deleted or `False` otherwise
        """
        self.root.delete(val)

    def inorder_successor(self, val: GT) -> Optional[GT]:
        """Get the in-order successor value of the given value.

        Notes:
            The function will return None if the given value is larger or equal
            to the maximum of the tree.

        Args:
            val: the reference value

        Returns:
            The in-order successor value if exists or `None` otherwise
        """
        return self.root.inorder_successor(val)
