"""The abstract base class for the custom implementations of a binary tree."""
from __future__ import annotations
from typing import TypeVar, Generic, Sequence, Union
from abc import ABC, abstractmethod
from data_structures.sequence import LinkedQueue, LinkedStack


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the binary tree,"""


class BinaryTree(Generic[GT], ABC):
    """The ABC for all custom implementations of a binary tree"""

    def __init__(self, val: GT):
        self.val = val

    @classmethod
    def from_list_repr(cls, list_repr: Sequence[GT]) -> BinaryTree[GT]:
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
    def left(self) -> BinaryTree[GT]:
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
    def right(self) -> BinaryTree[GT]:
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

    def pre_order_traverse_recursive(self) -> Sequence[GT]:
        """Get the pre-order traverse of the binary tree, recursively.

        Returns:
            The pre-order traverse of the binary tree
        """
        list_ = [self.val]
        if self.left:
            list_.extend(self.left.pre_order_traverse_recursive())
        if self.right:
            list_.extend(self.right.pre_order_traverse_recursive())
        return list_

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

    def post_order_traverse_recursive(self) -> Sequence[GT]:
        """Get the post-order traverse of the binary tree, recursively.

        Returns:
            The post-order traverse of the binary tree
        """
        list_ = []
        if self.left:
            list_.extend(self.left.post_order_traverse_recursive())
        if self.right:
            list_.extend(self.right.post_order_traverse_recursive())
        list_.append(self.val)
        return list_

    def level_order_traverse_iterative(self) -> Sequence[GT]:
        """Get the level-order traverse of the binary tree, iteratively.

        Returns:
            The level-order traverse of the binary tree
        """
        # use a queue for the breadth first traverse
        queue = LinkedQueue[BinaryTree[GT]]()
        queue.push(self)
        traverse = []
        while not queue.is_empty():
            node = queue.pop()
            traverse.append(node.val)
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
        return traverse

    def pre_order_traverse_iterative(self) -> Sequence[GT]:
        """Get the pre-order traverse of the binary tree, iteratively.

        Returns:
            The pre-order traverse of the binary tree
        """
        # use a stack for the depth first traverse
        stack = LinkedStack[BinaryTree[GT]]()
        list_ = []
        stack.push(self)
        while not stack.is_empty():
            # treat in inverse order as using a stack
            # pre order: value - left - right
            # so treated in: right - left - value
            node = stack.pop()
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)
            list_.append(node.val)
        return list_

    def in_order_traverse_iterative(self) -> Sequence[GT]:
        """Get the in-order traverse of the binary tree, iteratively.

        Returns:
            The in-order traverse of the binary tree
        """
        # use a stack for the depth first traverse
        stack = LinkedStack[Union[BinaryTree[GT], GT]]()
        list_ = []
        stack.push(self)
        while not stack.is_empty():
            # treat in inverse order as using a stack
            # pre order: left - value - right
            # so treated in: right - value - left
            node = stack.pop()
            if isinstance(node, BinaryTree):
                if node.right:
                    stack.push(node.right)
                stack.push(node.val)
                if node.left:
                    stack.push(node.left)
            else:
                list_.append(node)
        return list_

    def post_order_traverse_iterative(self) -> Sequence[GT]:
        """Get the post-order traverse of the binary tree, iteratively.

        Returns:
            The post-order traverse of the binary tree
        """
        # use a stack for the depth first traverse
        stack = LinkedStack[Union[BinaryTree[GT], GT]]()
        list_ = []
        stack.push(self)
        while not stack.is_empty():
            # treat in inverse order as using a stack
            # pre order: left - right - value
            # so treated in: value - right - left
            node = stack.pop()
            if isinstance(node, BinaryTree):
                stack.push(node.val)
                if node.right:
                    stack.push(node.right)
                if node.left:
                    stack.push(node.left)
            else:
                list_.append(node)
        return list_
