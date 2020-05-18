"""The custom implementation of a queue based on a linked list.

This module illustrates the foundation knowledge of implementing a queue using a
doubly linked list. The implementation does not use Python's language advantages
and looks dumb, because it only serves as an data structure exercise and has no
practical usage.
"""
from typing import TypeVar, Optional, Sequence
from .custom_queue import CustomQueue
from .. import LinkedListMixin
from .size_mixin import SizeMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the queue."""


class LinkedQueue(SizeMixin, CustomQueue[GT]):
    """
    `LinkedQueue[T]()` -> a queue based on linked list for values of type `T`.

    This is a custom implementation of a queue based on a doubly linked list for
    learning purpose.

    The implementation uses the `DoublyNode` implemented inside
    `LinkedListMixin` as the nodes in the list.

    Attributes:
        head (Optional[Node[T]]): the head node of the linked queue
        tail (Optional[Node[T]]): the tail node of the linked queue
        size (int): the current size of the queue
    """

    Node = LinkedListMixin.DoublyNode

    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None

    def push(self, val: GT) -> None:
        """Push a value into the end of the queue.

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
        """Pop a value out from the start of the queue.

        Returns:
            The popped value or `None` if an empty queue
        """
        if self.size:
            val = self.head.val
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return val
        return None

    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the queue and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the queue
        """
        list_ = []
        node = self.head
        while node:
            list_.append(node.val)
            node = node.next
        return list_
