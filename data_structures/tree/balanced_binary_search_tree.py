"""The abstract base class for a balanced binary search tree and its tree node.

The balance here is not the strict meaning, which requires at most one level
difference between two leaf nodes. The constraint can be softer to adapt the
practical implementations like red black tree, which only requires the level of
the deepest leaf node shall not bypass the double of the shallowest leaf node.
"""
from abc import abstractmethod
from .binary_search_tree import BinarySearchTree, BinarySearchTreeNode, GT


class BalancedBinarySearchTreeNode(
        BinarySearchTreeNode[GT],
    ):
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
        BinarySearchTree[GT],
    ):
    """The abstract base class for a softly balanced binary search tree."""

    NODE = BalancedBinarySearchTreeNode

    @abstractmethod
    def is_balanced(self) -> bool:
        """Check if the tree is actually balanced.

        Notes:
            It should always return `True` for a correctly implemented softly
            balanced binary search tree.

        Returns:
            `True` if balanced or `False` otherwise
        """
