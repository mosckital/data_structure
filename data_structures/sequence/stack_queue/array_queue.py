"""The custom implementation of a queue based on an array.

This module illustrates the foundation knowledge of implementing a queue using a
fixed length array. The implementation does not use Python's language advantages
and looks dumb, because it only serves as an data structure exercise and has no
practical usage.
"""
from typing import TypeVar, Optional, Sequence
from .custom_stack_queue import CustomQueue
from .size_mixin import SizeMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the queue."""


class ArrayQueue(SizeMixin, CustomQueue[GT]):
    """
    `ArrayQueue[T]()` -> a queue based on array for values of type `T`.

    This is a custom implementation of a queue based on an array for learning
    purpose. This implementation uses a list to mimic a fixed length array to
    store data. Only the creation of a list of given length and the
    access/assignment of element by index/subscription are permitted.

    To save space, the technique of circular array has been applied in the
    implementation.

    Attributes:
        data (List[Optional[GT]]): the list to store data
        size (int): the current size of the queue
    """

    BASE_SIZE = 8
    """The starting size of the internal list."""

    def __init__(self):
        super().__init__()
        self.data = [None] * self.BASE_SIZE
        self.head = 0
        self.tail = -1

    def push(self, val: GT) -> None:
        """Push a value into the end of the queue.

        Args:
            val: the value to push in
        """
        # double the size of the storage array if it's full and
        # reset the head to the start of array during array doubling
        if self.size == len(self.data):
            tmp = [None] * (len(self.data) * 2)
            for i in range(self.size):
                tmp[i] = self.data[(self.head + i) % len(self.data)]
            self.data = tmp
            self.head = 0
            self.tail = self.size - 1
        # push value into the circular array
        self.tail = (self.tail + 1) % len(self.data)
        self.data[self.tail] = val
        self.size += 1

    def pop(self) -> Optional[GT]:
        """Pop a value out from the start of the queue.

        Returns:
            The popped value or `None` if an empty queue
        """
        # case of empty queue
        if self.size == 0:
            return None
        # retrieve value and decrease size
        val = self.data[self.head]
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        # reset head and tail if no more stored value
        if self.size == 0:
            self.head = 0
            self.tail = -1
        # shrink the circular array if too many empty slots and
        # reset the head to the start of array during array doubling
        elif self.BASE_SIZE < self.size <= len(self.data) // 4:
            tmp = [None] * (len(self.data) // 2)
            for i in range(self.size):
                tmp[i] = self.data[(self.head + i) % len(self.data)]
            self.data = tmp
            self.head = 0
            self.tail = self.size - 1
        return val

    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the queue and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the queue
        """
        return [self.data[(self.head + i) % len(self.data)] for i in range(self.size)]
