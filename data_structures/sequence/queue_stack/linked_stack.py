"""The custom implementation of a stack based on a linked list.

This module illustrates the foundation knowledge of implementing a stack using a
doubly linked list. The implementation does not use Python's language advantages
and looks dumb, because it only serves as an data structure exercise and has no
practical usage.
"""
from typing import TypeVar, Optional, Sequence
from .custom_stack import CustomStack
from .. import LinkedListMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the stack."""


class LinkedStack(CustomStack[GT]):
    """
    `LinkedStack[T]()` -> a stack based on linked list for values of type `T`.

    This is a custom implementation of a stack based on a doubly linked list for
    learning purpose.

    The implementation uses the `DoublyNode` implemented inside
    `LinkedListMixin` as the nodes in the list.

    Attributes:
        head (Optional[Node[T]]): the head node of the linked stack
        tail (Optional[Node[T]]): the tail node of the linked stack
        size (int): the current size of the stack
    """

    Node = LinkedListMixin.DoublyNode
    """type: An alias for the correspondent node type."""

    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            `True` if the stack is empty or `False` otherwise
        """
        return self.size == 0

    def get_size(self) -> int:
        """Get the size of the stack.

        Returns:
            The size of the stack
        """
        return self.size

    def push(self, val: GT) -> None:
        """Push a value into the open end of the stack.

        Args:
            val: the value to push in
        """
        node = self.Node[GT](val)
        if self.size:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1
        else:
            self.head = self.tail = node
            self.size += 1

    def pop(self) -> Optional[GT]:
        """Pop a value out from the open end of the stack.

        Returns:
            The popped value or `None` if an empty stack
        """
        if self.size:
            val = self.tail.val
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1
            return val
        return None

    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the stack and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the stack
        """
        list_ = []
        node = self.head
        while node:
            list_.append(node.val)
            node = node.next
        return list_
