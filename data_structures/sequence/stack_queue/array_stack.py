"""The custom implementation of a stack based on an array.

This module illustrates the foundation knowledge of implementing a stack using a
fixed length array. The implementation does not use Python's language advantages
and looks dumb, because it only serves as an data structure exercise and has no
practical usage.
"""
from typing import TypeVar, Optional, Sequence
from .custom_stack_queue import CustomStack
from .size_mixin import SizeMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the stack."""


class ArrayStack(SizeMixin, CustomStack[GT]):
    """
    `ArrayStack[T]()` -> a stack based on array for values of type `T`.

    This is a custom implementation of a stack based on an array for learning
    purpose. This implementation uses a list to mimic a fixed length array to
    store data. Only the creation of a list of given length and the
    access/assignment of element by index/subscription are permitted.

    Attributes:
        data (List[Optional[GT]]): the list to store data
        size (int): the current size of the stack
    """

    _BASE_SIZE: int = 8
    """The starting size of the internal list."""

    def __init__(self):
        super().__init__()
        self.data = [None] * self._BASE_SIZE

    def push(self, val: GT) -> None:
        """Push a value into the open end of the stack.

        Args:
            val: the value to push in
        """
        # double the size of the storage array if it's full
        if self.size == len(self.data):
            tmp = [None] * (self.size * 2)
            for i in range(self.size):
                tmp[i] = self.data[i]
            self.data = tmp
        # push value into the array
        self.data[self.size] = val
        self.size += 1

    def pop(self) -> Optional[GT]:
        """Pop a value out from the open end of the stack.

        Returns:
            The popped value or `None` if an empty stack
        """
        # case of empty stack
        if self.size == 0:
            return None
        # retrieve value and decrease size
        val = self.data[self.size - 1]
        self.size -= 1
        # shrink the array if too many empty slots
        if self._BASE_SIZE < self.size <= len(self.data) // 4:
            tmp = [None] * (len(self.data) // 2)
            for i in range(self.size):
                tmp[i] = self.data[i]
            self.data = tmp
        return val

    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the stack and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the stack
        """
        return [self.data[i] for i in range(self.size)]
