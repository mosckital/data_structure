"""The abstract base class for a binary tree and a binary tree node."""
from __future__ import annotations
from typing import TypeVar, Generic, Sequence, Union
from abc import abstractmethod
from data_structures.sequence import LinkedStack
from .tree import Tree, TreeNode


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the binary tree."""


class BinaryTreeNode(Generic[GT], TreeNode[GT]):
    """The abstract base class for the nodes of a binary tree."""

    @property
    def children(self) -> Sequence[BinaryTreeNode[GT]]:
        ret = []
        if self.left:
            ret.append(self.left)
        if self.right:
            ret.append(self.right)
        return ret

    @classmethod
    def from_list_repr(cls, list_repr: Sequence[GT]) -> BinaryTreeNode[GT]:
        """Construct a binary tree node from its list representation.

        The list representation is the Breadth First Search representation of a
        binary tree node.

        Note:
            The list representation could include None as placeholder.

        Args:
            list_repr: the list representation to construct from

        Returns:
            The constructed binary tree node, an instance of a subclass of
            BinaryTreeNode
        """
        # the empty tree case
        if not list_repr or list_repr[0] is None:
            return None
        root = cls(list_repr[0])
        level = [root]  # to hold the last full level
        next_level = []  # to hold the next level in construction
        idx = 1  # the index of element to process in the list representation
        while idx < len(list_repr):
            # list_repr[idx] could be 0 and 0 is different to None here
            if list_repr[idx] is not None:
                # get the parent node of the current element to process
                parent = level[len(next_level) // 2]
                if len(next_level) % 2 == 0:
                    parent.left = list_repr[idx]
                    next_level.append(parent.left)
                else:
                    parent.right = list_repr[idx]
                    next_level.append(parent.right)
            else:
                next_level.append(None)
            idx += 1
            # proceed to the next level
            if len(next_level) == 2 * len(level):
                level, next_level = next_level, []
        return root

    @property
    @abstractmethod
    def left(self) -> BinaryTreeNode[GT]:
        """Get the left child node.

        Returns:
            The left child node
        """

    @left.setter
    @abstractmethod
    def left(self, val: GT) -> None:
        """Set the left child node with the given value.

        Args:
            val: the value to set in the left child node
        """

    @property
    @abstractmethod
    def right(self) -> BinaryTreeNode[GT]:
        """Get the right child node.

        Returns:
            The right child node
        """

    @right.setter
    @abstractmethod
    def right(self, val: GT) -> None:
        """Set the right child node with the given value.

        Args:
            val: the value to set in the right child node
        """

    def in_order_traverse_recursive(self) -> Sequence[GT]:
        """Get the in-order traverse of the binary tree, recursively.

        Returns:
            The in-order traverse of the binary tree
        """
        list_ = []
        if self.left:
            list_.extend(self.left.in_order_traverse_recursive())
        list_.append(self.val)
        if self.right:
            list_.extend(self.right.in_order_traverse_recursive())
        return list_

class BinaryTree(Generic[GT], Tree[GT]):
    """The abstract base class for a binary tree.

    Attributes:
        root (BinaryTreeNode[T]): the root node of the binary tree
    """

    def in_order_traverse_iterative(self) -> Sequence[GT]:
        """Get the in-order traverse of the tree, iteratively, by a depth first
        search using a stack.

        Returns:
            The in-order traverse
        """
        if not self.root:
            return []
        ret = []
        stack = LinkedStack[Union[BinaryTreeNode[GT], GT]]()
        stack.push(self.root)
        while not stack.is_empty():
            elm = stack.pop()
            if isinstance(elm, BinaryTreeNode):
                if elm.right:
                    stack.push(elm.right)
                stack.push(elm.val)
                if elm.left:
                    stack.push(elm.left)
            else:
                ret.append(elm)
        return ret

    def in_order_traverse_recursive(self) -> Sequence[GT]:
        """Get the in-order traverse of the tree, recursively, by a recursive
        depth first search starting from the root node.

        Returns:
            The in-order traverse
        """
        return self.root.in_order_traverse_recursive()

    @staticmethod
    @abstractmethod
    def from_list_repr(list_repr: Sequence[GT]) -> BinaryTree[GT]:
        """Construct a binary tree from its list representation.

        The list representation is the Breadth First Search representation of a
        binary tree.

        Note:
            The list representation could include None as placeholder.

        Args:
            list_repr: the list representation to construct from

        Returns:
            The constructed binary tree, an instance of a subclass of BinaryTree
        """
