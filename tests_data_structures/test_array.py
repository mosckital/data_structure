"""Test suite for the Array class which implements a fixed length array and the
DynamicArray class which implements a dynamic array.

The main idea of the tests is to compare the execution results of the class to
test with the results of a reference class. The results should always match.
"""
from random import choice, randint
from enum import Enum
from typing import TypeVar, Generic, Optional, List, Any
import pytest
from data_structures.array import Array
from data_structures.dynamic_array import DynamicArray


class Op(Enum):
    """
    An enum class to list all eligible operations on an Array or DynamicArray.
    """
    GET_SIZE = 0
    INDEX_OF = 1
    VALUE_AT = 2
    INSERT_AT = 3
    DELETE_AT = 4
    UPDATE_AT = 5
    TRAVERSE = 6


KR = TypeVar('KR')
"""The generic type to represent the element type of the reference array."""


class RefArray(Generic[KR]):
    """
    The reference implementation of fixed length array, to be used to test the
    correctness of the custom implementation.

    Attributes:
        data (List[KR]): a list to store data
        max_size (int): the max size of the array
    """

    def __init__(self, max_size: int):
        self.data = []
        self.max_size = max_size

    def get_size(self) -> int:
        """
        Get the current size of the array.

        Returns:
            The current size of the array
        """
        return len(self.data)

    def index_of(self, val: KR) -> int:
        """
        Get the index of a value, or -1 if not found.

        Args:
            val: the value to look for

        Returns:
            The index of the value or -1 if not found
        """
        try:
            return self.data.index(val)
        except ValueError:
            return -1

    def value_at(self, idx: int) -> Optional[KR]:
        """
        Get the value at the given index.

        Args:
            idx: the index to fetch

        Returns:
            The value at the given index or None if index not valid
        """
        if 0 <= idx < len(self.data):
            return self.data[idx]
        return None

    def insert_at(self, idx: int, val: KR) -> bool:
        """
        Insert a value at the given index.

        Note:
            The value will not be inserted if the index is not valid or the
            array is already full.

        Args:
            idx: the index to insert at
            val: the value to insert

        Returns:
            True if insertion is successful or False otherwise
        """
        if len(self.data) == self.max_size:
            return False
        if 0 <= idx <= len(self.data):
            self.data.insert(idx, val)
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
            True if deletion is successful or False otherwise
        """
        if 0 <= idx < len(self.data):
            self.data[idx:idx + 1] = []
            return True
        return False

    def update_at(self, idx: int, val: KR) -> bool:
        """
        Update an element at the given index by the given value.

        Note:
            The update will not perform if the index is not valid.

        Args:
            idx: the index to update
            val: the new value

        Returns:
            True if update is successful or False otherwise
        """
        if 0 <= idx < len(self.data):
            self.data[idx] = val
            return True
        return False

    def traverse(self) -> List[KR]:
        """
        Traverse all elements in the array and return them in a list.

        Returns:
            A list containing all elements of the array in order
        """
        return self.data

    def __eq__(self, value: Any) -> bool:
        """
        Overwritten to permit the comparison in format [RefArray == Array]. It
        is not valid for the inverse order.
        """
        if isinstance(value, (Array, DynamicArray)):
            return len(self.data) == value.curr_size and \
                self.data == value.data[:value.curr_size]
        return super().__eq__(value)


class TestArray():
    """
    The test suite class for the Array class and the DynamicArray class.
    """

    @staticmethod
    def _check_op_get_size(arr, alt):
        assert arr.get_size() == alt.get_size()

    @staticmethod
    def _check_op_index_of(arr, alt, i):
        # check normal case
        if arr.get_size() > 0:
            idx = randint(0, arr.get_size() - 1)
            tmp = arr.value_at(idx)
            assert arr.index_of(tmp) == alt.index_of(tmp) == idx
        # check two edge cases
        tmp = randint(i, i * 2)
        assert arr.index_of(tmp) == alt.index_of(tmp) == -1
        assert arr.index_of(-tmp) == alt.index_of(-tmp) == -1

    @staticmethod
    def _check_op_value_at(arr, alt):
        # check normal case
        if arr.get_size() > 0:
            idx = randint(0, arr.get_size() - 1)
            assert arr.value_at(idx) == alt.value_at(idx)
            assert arr.value_at(idx) is not None
        # check two edge cases
        idx = randint(arr.get_size(), arr.get_size() * 2)
        assert arr.value_at(idx) == alt.value_at(idx) == None
        idx = randint(- arr.get_size() - 1, -1)
        assert arr.value_at(idx) == alt.value_at(idx) == None

    @staticmethod
    def _check_op_insert_at(arr, alt, i, max_size):
        # check two edge cases
        idx = randint(arr.get_size() + 1, arr.get_size() * 2 + 1)
        assert arr.insert_at(idx, i) == alt.insert_at(idx, i) == False
        idx = randint(- arr.get_size() - 1, -1)
        assert arr.insert_at(idx, i) == alt.insert_at(idx, i) == False
        # check normal case
        idx = randint(0, arr.get_size())
        ret = bool(arr.get_size() < max_size)
        assert arr.insert_at(idx, i) == alt.insert_at(idx, i) == ret

    @staticmethod
    def _check_op_delete_at(arr, alt):
        # check two edge cases
        idx = randint(arr.get_size(), arr.get_size() * 2)
        assert arr.delete_at(idx) == alt.delete_at(idx) == False
        idx = randint(- arr.get_size() - 1, -1)
        assert arr.delete_at(idx) == alt.delete_at(idx) == False
        # check normal case
        if arr.get_size() > 0:
            idx = randint(0, arr.get_size() - 1)
            assert arr.delete_at(idx) == alt.delete_at(idx) == True

    @staticmethod
    def _check_op_update_at(arr, alt, i):
        # check two edge cases
        idx = randint(arr.get_size(), arr.get_size() * 2)
        assert arr.update_at(idx, i) == alt.update_at(idx, i) == False
        idx = randint(- arr.get_size() - 1, -1)
        assert arr.update_at(idx, i) == alt.update_at(idx, i) == False
        # check normal case
        if arr.get_size() > 0:
            idx = randint(0, arr.get_size() - 1)
            assert arr.update_at(idx, i) == alt.update_at(idx, i) == True

    @staticmethod
    def _check_op_traverse(arr, alt):
        assert arr.traverse() == alt.traverse()

    @pytest.mark.parametrize(
        'max_size',
        [1, 4, 16],
    )
    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_array_by_random_ops(self, max_size: int, n_ops: int):
        """
        Randomly test the operations of the Array class.
        """
        # the array implementation to test
        arr = Array[int](max_size)
        # the reference array implementation
        alt = RefArray(max_size)
        # list of operations to test
        ops = list(Op)
        # perform n_ops times of operation test
        for i in range(n_ops):
            # randomly choose an operation
            op_to_check = choice(ops)
            if op_to_check == Op.GET_SIZE:
                self._check_op_get_size(arr, alt)
            elif op_to_check == Op.INDEX_OF:
                self._check_op_index_of(arr, alt, i)
            elif op_to_check == Op.VALUE_AT:
                self._check_op_value_at(arr, alt)
            elif op_to_check == Op.INSERT_AT:
                self._check_op_insert_at(arr, alt, i, max_size)
            elif op_to_check == Op.DELETE_AT:
                self._check_op_delete_at(arr, alt)
            elif op_to_check == Op.UPDATE_AT:
                self._check_op_update_at(arr, alt, i)
            elif op_to_check == Op.TRAVERSE:
                self._check_op_traverse(arr, alt)
            # check two array implementations are same after any operation
            assert alt == arr

    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_dynamic_array_by_random_ops(self, n_ops: int):
        """
        Randomly test the operations of the DynamicArray class.
        """
        # In the most extreme case, there will be n_ops insertions
        max_size = n_ops
        # the array implementation to test
        arr = DynamicArray[int]()
        # the reference array implementation
        alt = RefArray(max_size)
        # list of operations to test
        ops = list(Op)
        # perform n_ops times of operation test
        for i in range(n_ops):
            # randomly choose an operation
            op_to_check = choice(ops)
            if op_to_check == Op.GET_SIZE:
                self._check_op_get_size(arr, alt)
            elif op_to_check == Op.INDEX_OF:
                self._check_op_index_of(arr, alt, i)
            elif op_to_check == Op.VALUE_AT:
                self._check_op_value_at(arr, alt)
            elif op_to_check == Op.INSERT_AT:
                self._check_op_insert_at(arr, alt, i, max_size)
            elif op_to_check == Op.DELETE_AT:
                self._check_op_delete_at(arr, alt)
            elif op_to_check == Op.UPDATE_AT:
                self._check_op_update_at(arr, alt, i)
            elif op_to_check == Op.TRAVERSE:
                self._check_op_traverse(arr, alt)
            # check two array implementations are same after any operation
            assert alt == arr
