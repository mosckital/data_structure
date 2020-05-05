"""Test suite for the sub classes of the CustomSequence abstract base class.

These sub classes are the custom implementations of the sequence-like data
structures, like fixed length array, dynamic length array, singly linked list
and doubly linked list.

A reference array implementation which wraps the Python `list`, named RefArray,
is imported to test the correctness of the above custom implementations by
comparing the results of the operations and the stored data after each
operation. The results and stored data should always be the same.
"""
from random import choice, randint
import pytest
from data_structures.sequence import FixedArray, DynamicArray, \
    SinglyLinkedList, DoublyLinkedList
from .ref_array import RefArray, Op


class TestSequenceImpl():
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

    @staticmethod
    def _check_op_push(arr, alt, i):
        assert arr.push(i) == alt.push(i)

    @staticmethod
    def _check_op_pop(arr, alt):
        assert arr.pop() == alt.pop()

    @staticmethod
    def _check_op_randomly(arr, alt, n_ops, max_size=0):
        if max_size == 0:
            max_size = n_ops
        # list of operations to test
        ops = list(Op)
        # perform n_ops times of operation test
        for i in range(n_ops):
            # randomly choose an operation
            op_to_check = choice(ops)
            if op_to_check == Op.GET_SIZE:
                TestSequenceImpl._check_op_get_size(arr, alt)
            elif op_to_check == Op.INDEX_OF:
                TestSequenceImpl._check_op_index_of(arr, alt, i)
            elif op_to_check == Op.VALUE_AT:
                TestSequenceImpl._check_op_value_at(arr, alt)
            elif op_to_check == Op.INSERT_AT:
                TestSequenceImpl._check_op_insert_at(arr, alt, i, max_size)
            elif op_to_check == Op.DELETE_AT:
                TestSequenceImpl._check_op_delete_at(arr, alt)
            elif op_to_check == Op.UPDATE_AT:
                TestSequenceImpl._check_op_update_at(arr, alt, i)
            elif op_to_check == Op.PUSH:
                TestSequenceImpl._check_op_push(arr, alt, i)
            elif op_to_check == Op.POP:
                TestSequenceImpl._check_op_pop(arr, alt)
            elif op_to_check == Op.TRAVERSE:
                TestSequenceImpl._check_op_traverse(arr, alt)
            # check two array implementations are same after any operation
            assert alt == arr

    @pytest.mark.parametrize(
        'max_size',
        [1, 4, 16],
    )
    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_fixed_array(self, max_size: int, n_ops: int):
        """
        Test the correctness of the FixedArray class.
        """
        # the array implementation to test
        arr = FixedArray[int](max_size)
        # the reference array implementation
        alt = RefArray(max_size)
        # randomly test the operations
        self._check_op_randomly(arr, alt, n_ops, max_size)

    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_dynamic_array(self, n_ops: int):
        """
        Test the correctness of the DynamicArray class.
        """
        # the array implementation to test
        arr = DynamicArray[int]()
        # the reference array implementation
        alt = RefArray()
        # randomly test the operations
        self._check_op_randomly(arr, alt, n_ops)

    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_singly_linked_list(self, n_ops: int):
        """
        Test the correctness of the SinglyLinkedList class.
        """
        # the array implementation to test
        arr = SinglyLinkedList[int]()
        # the reference array implementation
        alt = RefArray()
        # randomly test the operations
        self._check_op_randomly(arr, alt, n_ops)

    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_doubly_linked_list(self, n_ops: int):
        """
        Test the correctness of the DoublyLinkedList class.
        """
        # the array implementation to test
        arr = DoublyLinkedList[int]()
        # the reference array implementation
        alt = RefArray()
        # randomly test the operations
        self._check_op_randomly(arr, alt, n_ops)
