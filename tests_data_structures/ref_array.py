
"""A reference array which implements the CustomSequence base class.

This reference array wraps the functionalities of Python `list` data type for a
correct implementation of CustomSequence and serves as the counterpart checker
in the unit tests of the custom implementations of the sequence-like data
structures.
"""
from enum import Enum
from typing import TypeVar, Optional, List, Any
from data_structures import CustomSequence


class Op(Enum):
    """
    An enum class to list the permitted operations in the subclasses of
    CustomSequence, which are the custom implementations of the sequence-like
    data structures.
    """
    GET_SIZE = 0
    INDEX_OF = 1
    VALUE_AT = 2
    INSERT_AT = 3
    DELETE_AT = 4
    UPDATE_AT = 5
    PUSH = 6
    POP = 7
    TRAVERSE = 8


GT = TypeVar('GT')
"""The generic type to represent the element type of the reference array."""


class RefArray(CustomSequence[GT]):
    """
    The reference implementation of an array, to be used to test the correctness
    of the custom implementations of the sequence-like data structures.

    `RefArray[T]()` -> a dynamic length array of type T
    `RefArray[T](n)` -> a fixed length array of type T and max size n

    Args:
        max_size (int): the max size of the array if given a positive number, or
            the array has a dynamic length if given 0, the default value

    Attributes:
        data (List[T]): a list to store data of type T
        max_size (int): the max size of the array, 0 means a dynamic length
            array
    """

    def __init__(self, max_size: int = 0):
        super().__init__()
        self.data = []
        self.max_size = max_size

    def get_size(self) -> int:
        return len(self.data)

    def index_of(self, val: GT) -> int:
        try:
            return self.data.index(val)
        except ValueError:
            return -1

    def value_at(self, idx: int) -> Optional[GT]:
        if 0 <= idx < len(self.data):
            return self.data[idx]
        return None

    def insert_at(self, idx: int, val: GT) -> bool:
        if self.max_size and len(self.data) == self.max_size:
            return False
        if 0 <= idx <= len(self.data):
            self.data.insert(idx, val)
            return True
        return False

    def delete_at(self, idx: int) -> bool:
        if 0 <= idx < len(self.data):
            self.data[idx:idx + 1] = []
            return True
        return False

    def update_at(self, idx: int, val: GT) -> bool:
        if 0 <= idx < len(self.data):
            self.data[idx] = val
            return True
        return False

    def traverse(self) -> List[GT]:
        return self.data

    def push(self, val: GT) -> None:
        self.insert_at(len(self.data), val)

    def pop(self) -> Optional[GT]:
        if not self.data:
            return None
        val = self.data[-1]
        self.delete_at(len(self.data) - 1)
        return val

    def __eq__(self, value: Any) -> bool:
        """
        Overwritten to permit the comparison in format [RefArray == Array]. It
        is not valid for the inverse order.
        """
        if isinstance(value, CustomSequence):
            return len(self.data) == value.get_size() and \
                self.data == value.traverse()
        return super().__eq__(value)
