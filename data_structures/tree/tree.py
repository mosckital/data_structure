"""The abstract base classes for a general tree and a general tree node.
"""
from __future__ import annotations
from typing import TypeVar, Generic, Sequence, Union
from abc import ABC, abstractmethod
from ..sequence import LinkedStack, LinkedQueue


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the general tree."""


class TreeNode(Generic[GT], ABC):
    """The abstract base class for the nodes of a general tree.

    Attributes:
        val (T): the stored value of type `T`
        children (Sequence[GT]): all the child nodes in a sequence
    """

    def __init__(self, val: GT):
        super().__init__()
        self.val = val

    def __bool__(self):
        return self is not None

    def __len__(self):
        length = 1
        for child in self.children:
            length += child.__len__()
        return length

    @property
    @abstractmethod
    def children(self) -> Sequence[TreeNode[GT]]:
        """All the children nodes in a list.

        Returns:
            All the children nodes in a list
        """

    def pre_order_traverse_recursive(self) -> Sequence[GT]:
        """Get the pre-order traverse of the node and all its sub nodes,
        recursively, by a depth first search.

        Returns:
            The pre-order traverse
        """
        ret = [self.val]
        for child in self.children:
            ret.extend(child.pre_order_traverse_recursive())
        return ret

    def post_order_traverse_recursive(self) -> Sequence[GT]:
        """Get the post-order traverse of the node and all its sub nodes,
        recursively, by a depth first search.

        Returns:
            The post-order traverse
        """
        ret = []
        for child in self.children:
            ret.extend(child.post_order_traverse_recursive())
        ret.append(self.val)
        return ret


class Tree(Generic[GT], ABC):
    """The abstract base class for a general tree.

    Attributes:
        root (TreeNode[T]): the root node of the tree
    """

    def __init__(self):
        super().__init__()
        self.root: TreeNode[GT] = None

    def __bool__(self):
        return self.root is not None

    def __len__(self):
        return self.root.__len__() if self.root else 0

    def pre_order_traverse_iterative(self) -> Sequence[GT]:
        """Get the pre-order traverse of the tree, iteratively, by a depth first
        search using a stack.

        Returns:
            The pre-order traverse
        """
        if not self.root:
            return []
        ret = []
        stack = LinkedStack[TreeNode[GT]]()
        stack.push(self.root)
        while not stack.is_empty():
            node = stack.pop()
            ret.append(node.val)
            for child in node.children[::-1]:
                stack.push(child)
        return ret

    def post_order_traverse_iterative(self) -> Sequence[GT]:
        """Get the post-order traverse of the tree, iteratively, by a depth
        first search using a stack.

        Returns:
            The post-order traverse
        """
        if not self.root:
            return []
        ret = []
        stack = LinkedStack[Union[TreeNode[GT], GT]]()
        stack.push(self.root)
        while not stack.is_empty():
            elm = stack.pop()
            if isinstance(elm, TreeNode):
                stack.push(elm.val)
                for child in elm.children[::-1]:
                    stack.push(child)
            else:
                ret.append(elm)
        return ret

    def level_order_traverse_iterative(self) -> Sequence[GT]:
        """Get the level-order traverse of the tree, iteratively, by a breadth
        first search using a queue.

        Returns:
            The level-order traverse
        """
        if not self.root:
            return []
        ret = []
        queue = LinkedQueue[TreeNode[GT]]()
        queue.push(self.root)
        while not queue.is_empty():
            node = queue.pop()
            ret.append(node.val)
            for child in node.children:
                queue.push(child)
        return ret

    def pre_order_traverse_recursive(self) -> Sequence[GT]:
        """Get the pre-order traverse of the tree, recursively, by a recursive
        depth first search starting from the root node.

        Returns:
            The pre-order traverse
        """
        return self.root.pre_order_traverse_recursive()

    def post_order_traverse_recursive(self) -> Sequence[GT]:
        """Get the post-order traverse of the tree, recursively, by a recursive
        depth first search starting from the root node.

        Returns:
            The post-order traverse
        """
        return self.root.post_order_traverse_recursive()
