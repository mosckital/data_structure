"""Custom implementation of a dynamic array.

This module illustrates the foundation knowledge of a dynamic array by
implementing it. It has no practical usage but only serves as an data structure
exercise.
"""
from typing import TypeVar
from .fixed_array import FixedArray


GT = TypeVar('GT')
"""The generic type to represent the type of the array element."""


class DynamicArray(FixedArray[GT]):
    """
    `DynamicArray[T]()` -> a dynamic array for values of type `T`.

    This is a custom implementation of a Dynamic Array for learning purpose. The
    implementation uses a list to store data, but only the creation of a list of
    given length and access/assignment of element by index/subscription is
    permitted.

    Attributes:
        data (List[Optional[GT]]): the list to store data
        curr_size (int): the current size of the array
    """

    _BASE_LENGTH: int = 8
    """The starting length of the internal list."""

    def __init__(self):
        super().__init__(self._BASE_LENGTH)

    def insert_at(self, idx: int, val: GT) -> bool:
        """
        Insert a value at the given index.

        Note:
            The value will not be inserted if the index is not valid

        Args:
            idx: the index to insert at
            val: the value to insert

        Returns:
            `True` if insertion is successful or `False` otherwise
        """
        if 0 <= idx <= self.curr_size == len(self.data):
            tmp = [None] * (2 * len(self.data))
            for i in range(idx):
                tmp[i] = self.data[i]
            tmp[idx] = val
            for i in range(idx, self.curr_size):
                tmp[i + 1] = self.data[i]
            self.data = tmp
            self.curr_size += 1
            return True
        return super().insert_at(idx, val)

    def delete_at(self, idx: int) -> bool:
        """
        Delete an element at the given index.

        Note:
            The deletion will not perform if the index is not valid.

        Args:
            idx: the index to perform deletion

        Returns:
            `True` if deletion is successful or `False` otherwise
        """
        if 0 <= idx < self.curr_size <= len(self.data) // 4:
            tmp = [None] * (len(self.data) // 2)
            for i in range(idx):
                tmp[i] = self.data[i]
            for i in range(idx, self.curr_size - 1):
                tmp[i] = self.data[i + 1]
            self.data = tmp
            self.curr_size -= 1
            return True
        return super().delete_at(idx)
