"""The abstract base class for all the custom implementations of the
sequence-like data structures, like arrays and linked lists.

This module defines the abstract base class and the operations available on its
sub-classes. All its sub classes are only implemented for learning purpose and
have no practical usage.
"""
from typing import TypeVar, Generic, Optional, Sequence
from abc import ABC, abstractmethod


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the sequence."""


class CustomSequence(Generic[GT], ABC):
    """
    The abstract base class for all the custom implementations of the
    sequence-like data structures.
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_size(self) -> int:
        """
        Get the current size.

        Returns:
            The current size
        """
        return 0

    @abstractmethod
    def index_of(self, val: GT) -> int:
        """
        Get the index of a value, or -1 if not found.

        Args:
            val: the value to look for

        Returns:
            The index of the value or -1 if not found
        """
        return -1

    @abstractmethod
    def value_at(self, idx: int) -> Optional[GT]:
        """
        Get the value at the given index.

        Args:
            idx: the index to fetch

        Returns:
            The value at the given index or `None` if index not valid
        """
        return None

    @abstractmethod
    def insert_at(self, idx: int, val: GT) -> bool:
        """
        Insert a value at the given index.

        Note:
            The value will not be inserted if the index is not valid.

        Args:
            idx: the index to insert at
            val: the value to insert

        Returns:
            `True` if insertion is successful or `False` otherwise
        """
        return False

    @abstractmethod
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
        return False

    @abstractmethod
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
        return False

    @abstractmethod
    def push(self, val: GT) -> None:
        """
        Push a value in.

        Args:
            val: the value to push in
        """
        return

    @abstractmethod
    def pop(self) -> Optional[GT]:
        """
        Pop a value out and return the value.

        Returns:
            The popped value or `None` if empty
        """
        return None

    @abstractmethod
    def traverse(self) -> Sequence[GT]:
        """
        Traverse all elements and return them in a list.

        Returns:
            A list containing all elements in order
        """
        return []
