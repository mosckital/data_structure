"""The custom implementation of a red-black tree based on linked nodes."""
from typing import TypeVar, Generic, Sequence
from .balanced_binary_search_tree import BalancedBinarySearchTreeNode, BalancedBinarySearchTree
from .linked_binary_search_tree import LinkedBinarySearchTreeNode, LinkedBinarySearchTree


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the tree."""


class RedBlackTreeNode(
        Generic[GT],
        BalancedBinarySearchTreeNode[GT],
        LinkedBinarySearchTreeNode[GT],
    ):
    # pylint: disable=too-many-ancestors
    """
    `RedBlackTree[T](val, is_red)` -> a single node in a red-black tree based on
        linked nodes for values of type `T`, which has `val` as the stored value
        of the node, has no child node and marked as a red node if `is_red` is
        `True` or a black node otherwise.
    `RedBlackTree[T]()` -> a leaf node in a red-black tree based on linked nodes
        where this leaf node has no stored value and is marked as a black node.

    This is a custom implementation of a red-black tree node based on linked
    nodes for learning purpose.

    Args:
        val (T): the value of the node
        is_red (bool): `True` if this node is marked red or `False` if black

    Attributes:
        val (T): the value of the node
        left (LinkedBinaryTreeNode[T]): the left child node
        right (LinkedBinaryTreeNode[T]): the right child node
        is_red (bool): `True` if this node is marked red or `False` if black
    """

    def __init__(self, val: GT = None, is_red: bool = False):
        super().__init__(val)
        self.is_red = is_red

    def is_balanced(self) -> int:
        """Check if the sub tree of this node is actually balanced and return
        the number of black nodes on any path to a leaf node.

        Notes:
            A red-black tree should has same number of black nodes for all paths
            to leaf nodes and this number is at least 1.

        Returns:
            The number of black nodes on any path to a leaf node if the tree is
            balanced or 0 otherwise
        """
        # case of leaf node
        if self.val is None:
            return 0 if self.is_red else 1
        # check that red node must have two black nodes
        if self.is_red:
            if (not self.left) or self.left.is_red or (not self.right) or self.right.is_red:
                return 0
        # check that all paths to leaf node have same number of black nodes
        n_left, n_right = self.left.is_balanced(), self.right.is_balanced()
        if n_left == n_right > 0:
            return n_left + (0 if self.is_red else 1)
        return 0


class RedBlackTree(
        Generic[GT],
        BalancedBinarySearchTree[GT],
        LinkedBinarySearchTree[GT]
    ):
    # pylint: disable=too-many-ancestors
    """The custom implementation of a red-black tree based on linked nodes.

    Attributes:
        root (RedBlackTreeNode[T]): the root node of the tree
    """

    @staticmethod
    def from_list_repr(list_repr: Sequence[GT]) -> RedBlackTree[GT]:
        tree = RedBlackTree[GT]()
        tree.root = RedBlackTreeNode.from_list_repr(list_repr)
        return tree

    def is_balanced(self):
        if self.root and (not self.root.is_red) and self.root.is_balanced():
            return True
        return False
