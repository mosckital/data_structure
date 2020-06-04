"""The custom implementation of a red-black tree based on linked nodes."""
from __future__ import annotations
from .balanced_binary_search_tree import BalancedBinarySearchTreeNode, BalancedBinarySearchTree
from .doubly_linked_binary_search_tree import DoublyLinkedBinarySearchTreeNode, DoublyLinkedBinarySearchTree, GT


class RedBlackTreeNode(
        DoublyLinkedBinarySearchTreeNode[GT],
        BalancedBinarySearchTreeNode[GT],
    ):
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

    def __init__(self, val: GT = None, is_red: bool = True):
        super().__init__(val)
        self._parent = None
        self.is_red = is_red
        if is_red:
            self._left = self.__class__[GT](val=None, is_red=False)
            self._left._parent = self
            self._right = self.__class__[GT](val=None, is_red=False)
            self._right._parent = self

    @property
    def parent(self):
        """The parent node."""
        return self._parent

    @parent.setter
    def parent(self, node: RedBlackTreeNode[GT]):
        # update the color of the node when it's assigned a parent for the first
        # time, which is the time of adding into a tree
        update_color_insert = node and (not self._parent)
        self._parent = node
        if update_color_insert:
            self._update_color_after_insert()

    @property
    def sibling(self):
        """The sibling node."""
        if self == self.parent._left:
            return self.parent._right
        else:
            return self.parent._left

    @property
    def grandparent(self):
        """The grand parent node."""
        return self.parent.parent

    @property
    def uncle(self):
        """The uncle node."""
        if self.grandparent.left == self.parent:
            return self.grandparent.right
        else:
            return self.grandparent.left
    
    def _delete_root_val_and_promote_closet_val_to_root(self, side):
        # pylint: disable=attribute-defined-outside-init
        other = 'right' if side == 'left' else 'left'
        node = getattr(self, side)
        if getattr(node, other) and getattr(node, other).val is not None:
            while getattr(node, other) and getattr(node, other).val is not None:
                node = getattr(node, other)
            self.val = node.val
            setattr(node.parent, other, getattr(node, side))
            getattr(node, side).parent = node.parent
        else:
            self.val = node.val
            setattr(self, side, getattr(node, side))
            getattr(node, side).parent = self
        if not node.is_red:
            # case that the deleted node is black
            # if the deleted node is red, it's safe to delete, otherwise, we
            # need extra update for color
            if getattr(node, side).is_red:
                # if the only child of the deleted node is red, we only need to
                # change its color to black
                getattr(node, side).is_red = False
            else:
                # if both the deleted node and its only child are black, the
                # case becomes complicated, we need to re-establish the colors
                # after performing the deletion, starting from the only child
                # of the deleted node, which replaces the deleted node
                getattr(node, side)._update_color_after_delete()

    def _update_color_after_delete(self):
        # self replaced the deleted node and is black
        if not self.parent:
            # case 1: self is the new root, nothing to update
            return
        sibling = self.sibling
        if sibling.is_red:
            # case 2: the sibling is red, which implies that the parent must be
            # black as no two red nodes should be in a row
            self.parent.is_red = True
            sibling.is_red = False
            if self.val < sibling.val:
                self.parent._rotate_left_down()
            else:
                self.parent._rotate_right_down()
        sibling = self.sibling
        if (not sibling.is_red) and (not self.parent.is_red) and \
            (not sibling._left.is_red) and (not sibling._right.is_red):
            # case 3: self, the parent, the sibling and the children of the
            # sibling are all black
            sibling.is_red = True
            self.parent._update_color_after_delete()
            return
        if (not sibling.is_red) and (self.parent.is_red) and \
            (not sibling._left.is_red) and (not sibling._right.is_red):
            # case 4: the parent is red, but self, the sibling and the children
            # of the sibling are black
            self.parent.is_red = False
            sibling.is_red = True
            return
        if not sibling.is_red:
            # case 5: the sibling is black but the child closer to self is red
            if (self == self.parent.left) and (sibling._left.is_red) and \
                (not sibling._right.is_red):
                sibling.is_red = True
                sibling._left.is_red = False
                sibling._rotate_right_down()
            if (self == self.parent.right) and (not sibling._left.is_red) and \
                (sibling._right.is_red):
                sibling.is_red = True
                sibling._right.is_red = False
                sibling._rotate_left_down()
        sibling = self.sibling
        # case 6: sibling is black and the child further to self is red
        sibling.is_red = self.parent.is_red
        self.parent.is_red = False
        if self == self.parent.left:
            sibling._right.is_red = False
            self.parent._rotate_left_down()
        else:
            sibling._left.is_red = False
            self.parent._rotate_right_down()

    def _update_color_after_insert(self):
        if not self.parent:
            # case 1: insert at root
            self.is_red = False
            return
        if not self.parent.is_red:
            # case 2: parent is black
            return
        # in the remaining cases, the parent exists and is red, so that the
        # parent is not the root node and the grandparent exists
        parent = self.parent
        grandparent = self.grandparent
        uncle = self.uncle
        if (uncle.val is not None) and uncle.is_red:
            # case 3: both parent and uncle are red
            parent.is_red = False
            uncle.is_red = False
            grandparent.is_red = True
            grandparent._update_color_after_insert()
            return
        # in the remaining cases, the parent is red and the uncle is black
        if parent == parent.parent.left:
            # branch that parent is the left child of the grandparent
            if self == self.parent.right:
                # case 4: rotate left of the inserted node and its parent
                parent._rotate_left_down()
                parent._update_color_after_insert()
                return
            else:
                # case 5: rotate right of grand parent and parent nodes
                parent.is_red = False
                grandparent.is_red = True
                grandparent._rotate_right_down()
        else:
            if self == self.parent.left:
                # mirrored case 4
                parent._rotate_right_down()
                parent._update_color_after_insert()
                return
            else:
                # mirrored case 5
                parent.is_red = False
                grandparent.is_red = True
                grandparent._rotate_left_down()

    def _rotate_left_down(self):
        self._rotate_down('_left')

    def _rotate_right_down(self):
        self._rotate_down('_right')

    def _rotate_down(self, side: str):
        """Rotate the node down to the given side and promote the child node of
        the other side to the node's current position.
        """
        other = '_left' if side == '_right' else '_right'
        # self if the parent node
        grandparent = self.parent
        child = getattr(self, other)
        if grandparent:
            up_side = '_left' if grandparent._left == self else '_right'
            setattr(grandparent, up_side, child)
            child.parent = grandparent
        setattr(self, other, getattr(child, side))
        getattr(child, side).parent = self
        self.parent = child
        setattr(child, side, self)

    def is_balanced(self) -> int:
        # pylint: disable=no-member
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
        DoublyLinkedBinarySearchTree[GT],
        BalancedBinarySearchTree[GT],
    ):
    """The custom implementation of a red-black tree based on linked nodes.

    Attributes:
        root (RedBlackTreeNode[T]): the root node of the tree
    """

    NODE = RedBlackTreeNode

    @classmethod
    def from_list_repr(cls, list_repr):
        tree = RedBlackTree()
        for v in list_repr:
            if v is not None:
                tree.insert(v)
        return tree

    def insert(self, val):
        # pylint: disable=all
        if not self.root:
            # insert case 1: insert at root
            self.root = self.NODE[GT](val)
            self.root.is_red = False
            return True
        return super().insert(val)

    def is_balanced(self):
        if self.root and (not self.root.is_red) and self.root.is_balanced():
            return True
        return False
