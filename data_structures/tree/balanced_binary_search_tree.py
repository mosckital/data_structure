"""The abstract base class for a balanced binary search tree and its tree node.

The balance here is not the strict meaning, which requires at most one level
difference between two leaf nodes. The constraint can be softer to adapt the
practical implementations like red black tree, which only requires the level of
the deepest leaf node shall not bypass the double of the shallowest leaf node.
"""
from typing import TypeVar, Generic
from abc import abstractmethod
from .binary_search_tree import BinarySearchTree, BinarySearchTreeNode


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the tree."""


class BalancedBinarySearchTreeNode(
        Generic[GT],
        BinarySearchTreeNode[GT],
    ):
    # pylint: disable=too-many-ancestors
    """The abstract base class for the nodes of a softly balanced binary search
    tree.
    """

    @abstractmethod
    def is_balanced(self) -> bool:
        """Check if the sub tree of this node is actually balanced.

        Notes:
            It should always return `True` for a correctly implemented softly
            balanced binary search tree node.

        Returns:
            `True` if balanced or `False` otherwise
        """


class BalancedBinarySearchTree(
        Generic[GT],
        BinarySearchTree[GT],
    ):
    # pylint: disable=too-many-ancestors
    """The abstract base class for a softly balanced binary search tree."""

    NODE = BalancedBinarySearchTreeNode

    def is_balanced(self) -> bool:
        """Check if the tree is actually balanced.

        Notes:
            It should always return `True` for a correctly implemented softly
            balanced binary search tree.

        Returns:
            `True` if balanced or `False` otherwise
        """
        if not self.root:
            return True
        return self.root.is_balanced()
