"""The Mixin class to provide the extra functionalities of a binary search tree
and its tree node.
"""
from __future__ import annotations
from typing import Optional
from abc import abstractmethod
from .binary_tree import BinaryTree, BinaryTreeNode, GT


class BinarySearchTreeNode(BinaryTreeNode[GT]):
    # pylint: disable=no-member
    """The abstract base class for the nodes of a binary search tree."""

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

    def delete(self, val: GT) -> bool:
        """To delete a value from the sub tree of this node.

        Notes:
            The deletion will fail if no such value exists.

        Args:
            val: the value to delete

        Returns:
            `True` if deleted or `False` otherwise
        """
        # case to potentially delete the value in the left child tree
        if val < self.val:
            return self.left.delete(val) if self.left else False
        # case to potentially delete the value in the right child tree
        if val > self.val:
            return self.right.delete(val) if self.right else False
        # case to delete the root node
        if self.right:
            # if there is value larger than the value of the root node, find the
            # successor value, delete its node and reassign the value to root
            self._delete_root_val_and_promote_closet_val_to_root('right')
        elif self.left:
            # if there is no value larger than the value of the root, but value
            # smaller, find the largest one of the smaller values, delete its
            # node and reassign the value to root
            self._delete_root_val_and_promote_closet_val_to_root('left')
        else:
            # case of no child node, so to delete the root node
            raise NotImplementedError('Cannot delete a node from itself!')
        return True

    @abstractmethod
    def _delete_root_val_and_promote_closet_val_to_root(self, side: str) -> None:
        pass

    def inorder_successor_node(self, val: GT) \
            -> Optional[BinarySearchTreeNode[GT]]:
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


class BinarySearchTree(BinaryTree[GT]):
    # pylint: disable=attribute-defined-outside-init
    """The abstract base class for a binary search tree.

    Attributes:
        root (BinarySearchTreeNode[T]): the root node of the binary tree"""

    NODE = BinarySearchTreeNode

    def search(self, val: GT) -> bool:
        """Search if a value is present in the tree.

        Args:
            val: the value to look for

        Returns:
            `True` if found or `False` otherwise
        """
        return self.root.search(val)

    def insert(self, val: GT) -> bool:
        """To insert a value into the tree.

        Notes:
            The insertion will fail and do nothing if the value is already in
            the tree.

        Args:
            val: the value to insert

        Returns:
            `True` if inserted or `False` otherwise
        """
        if self.root:
            return self.root.insert(val)
        # create a new root node if the tree is empty
        self.root = self.NODE[GT].from_list_repr([val])
        return True

    def delete(self, val: GT) -> bool:
        """To delete a value from the sub tree of this node.

        Notes:
            The deletion will fail if no such value exists.

        Args:
            val: the value to delete

        Returns:
            `True` if deleted or `False` otherwise
        """
        if not self.root:
            return False
        try:
            return self.root.delete(val)
        except NotImplementedError:
            # delete the root node if the tree only has the root node and the
            # root node is the target to delete
            self.root = None
            return True

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
