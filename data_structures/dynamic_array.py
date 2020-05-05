"""Custom implementation of a dynamic array.

This module illustrates the foundation knowledge of a dynamic array by
implementing it. It has no practical usage but only serves as an data structure
exercise.
"""
from typing import TypeVar, Optional, Sequence
from .custom_sequence import CustomSequence


GT = TypeVar('GT')
"""The generic type to represent the type of the array element."""


class DynamicArray(CustomSequence[GT]):
    """
    `DynamicArray[T]` -> a dynamic array for values of type `T`.

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
        super().__init__()
        self.data = [None] * self._BASE_LENGTH
        self.curr_size = 0

    def get_size(self) -> int:
        """
        Get the current size of the array.

        Returns:
            The current size of the array
        """
        return self.curr_size

    def index_of(self, val: GT) -> int:
        """
        Get the index of a value, or -1 if not found.

        Args:
            val: the value to look for

        Returns:
            The index of the value or -1 if not found
        """
        for i in range(self.curr_size):
            if self.data[i] == val:
                return i
        return -1

    def value_at(self, idx: int) -> Optional[GT]:
        """
        Get the value at the given index.

        Args:
            idx: the index to fetch

        Returns:
            The value at the given index or `None` if index not valid
        """
        if 0 <= idx < self.curr_size:
            return self.data[idx]
        return None

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
        if 0 <= idx <= self.curr_size:
            if self.curr_size == len(self.data):
                tmp = [None] * (2 * len(self.data))
                for i in range(idx):
                    tmp[i] = self.data[i]
                tmp[idx] = val
                for i in range(idx, self.curr_size):
                    tmp[i + 1] = self.data[i]
                self.data = tmp
            else:
                for i in range(self.curr_size, idx, -1):
                    self.data[i] = self.data[i - 1]
                self.data[idx] = val
            self.curr_size += 1
            return True
        return False

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
        if 0 <= idx < self.curr_size:
            if self.curr_size * 4 <= len(self.data):
                tmp = [None] * (len(self.data) // 2)
                for i in range(idx):
                    tmp[i] = self.data[i]
                for i in range(idx, self.curr_size - 1):
                    tmp[i] = self.data[i + 1]
                self.data = tmp
            else:
                for i in range(idx, self.curr_size - 1):
                    self.data[i] = self.data[i + 1]
            self.curr_size -= 1
            return True
        return False

    def update_at(self, idx: int, val: GT) -> bool:
        """
        Update an element at the given index by the given value.

        Note:
            The update will not perform if the index is not valid.

        Args:
            idx: the index to update
            val: the new value

        Returns:
            `True` if update is successful or `False` otherwise
        """
        if 0 <= idx < self.curr_size:
            self.data[idx] = val
            return True
        return False

    def push(self, val: GT) -> None:
        """
        Push a value into the array's end.

        Note:
            Nothing will happen if the array is already full.

        Args:
            val: the value to push in
        """
        self.insert_at(self.curr_size, val)

    def pop(self) -> Optional[GT]:
        """
        Pop a value out of the array's end and return the value.

        Returns:
            The popped value or `None` if empty array
        """
        if not self.curr_size:
            return None
        val = self.data[self.curr_size - 1]
        self.delete_at(self.curr_size - 1)
        return val

    def traverse(self) -> Sequence[GT]:
        """
        Traverse all elements in the array and return them in a list.

        Returns:
            A list containing all elements of the array in order
        """
        # return a copy of the array instead the original
        return [self.data[i] for i in range(self.curr_size)]
