"""The custom implementation of a binary search tree based on doubly linked
nodes."""
from .doubly_linked_binary_tree import DoublyLinkedBinaryTree, DoublyLinkedBinaryTreeNode
from .binary_search_tree import BinarySearchTree, BinarySearchTreeNode, GT


class DoublyLinkedBinarySearchTreeNode(
        DoublyLinkedBinaryTreeNode[GT],
        BinarySearchTreeNode[GT],
    ):
    """
    `DoublyLinkedBinarySearchTreeNode[G](val)` -> a single node in a doubly
        linked node based binary search tree for values of type `T`, which has
        `val` as the stored value of the node and has no child node.

    This is a custom implementation of a binary search tree node based on doubly
    linked nodes for learning purpose.

    Args:
        val: the value of the root node

    Attributes:
        val (T): the value of the node
        left (DoublyLinkedBinarySearchTreeNode[T]): the left child node
        right (DoublyLinkedBinarySearchTreeNode[T]): the right child node
        parent (DoublyLinkedBinarySearchTreeNode[T]): the parent node
    """

    def _delete_root_val_and_promote_closet_val_to_root(self, side):
        # pylint: disable=attribute-defined-outside-init
        other = 'right' if side == 'left' else 'left'
        node = getattr(self, side)
        if getattr(node, other):
            while getattr(node, other):
                node = getattr(node, other)
            self.val = node.val
            setattr(node.parent, other, getattr(node, side))
            if getattr(node, side):
                getattr(node, side).parent = node.parent
        else:
            self.val = node.val
            setattr(self, side, getattr(node, side))
            if getattr(node, side):
                getattr(node, side).parent = self
        # # to actually remove the node from the tree, this may trigger
        # # consequential clean up action, like in a red black tree
        # setattr(node, side, None)
        # node.parent = None


class DoublyLinkedBinarySearchTree(
        DoublyLinkedBinaryTree[GT],
        BinarySearchTree[GT],
    ):
    """The custom implementation of a binary tree based on doubly linked nodes.

    Attributes:
        root (DoublyLinkedBinarySearchTreeNode[T]): the root node of the binary
            tree
    """

    NODE = DoublyLinkedBinarySearchTreeNode
