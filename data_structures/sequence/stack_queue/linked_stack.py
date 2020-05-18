"""The custom implementation of a stack based on a linked list.

This module illustrates the foundation knowledge of implementing a stack using a
doubly linked list. The implementation does not use Python's language advantages
and looks dumb, because it only serves as an data structure exercise and has no
practical usage.
"""
from typing import TypeVar, Optional, Generic
from .custom_stack_queue import CustomStack
from .linked_mixin import LinkedMixin
from .size_mixin import SizeMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the stack."""


class LinkedStack(Generic[GT], LinkedMixin[GT], SizeMixin, CustomStack[GT]):
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

    def pop(self) -> Optional[GT]:
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
