"""Test suite for the sub classes of the CustomStack and CustomQueue abstract
base classes.

These sub classes are the custom implementations of stack and queue type data
structures. For a stack/queue, it can be implemented on an array, a linked list
or a queue/stack. This module tests the correctness of all these custom
implementations.
"""
from collections import deque
from typing import Union
from enum import Enum
from random import choice
import pytest
from data_structures.sequence import CustomStack, LinkedStack, ArrayStack, \
    CustomQueue, LinkedQueue, ArrayQueue


CustomStackQueue = Union[CustomStack, CustomQueue]
"""type: either a stack or a queue."""


class Op(Enum):
    """
    An enum class to list the permitted operations in the subclasses of
    CustomStack and CustomQueue, which are the custom implementations of stack
    or queue type data structures.
    """
    IS_EMPTY = 0
    GET_SIZE = 1
    PUSH = 2
    POP = 3
    TRAVERSE = 4


class TestStackQueue():
    """
    The test suite class for subclasses of CustomStack and CustomQueue.
    """

    @staticmethod
    def _check_op_is_empty(tar: CustomStackQueue, ref: deque):
        assert tar.is_empty() == (len(ref) == 0)

    @staticmethod
    def _check_op_get_size(tar: CustomStackQueue, ref: deque):
        assert tar.get_size() == len(ref)

    @staticmethod
    def _check_op_push(tar: CustomStackQueue, ref: deque, i: int):
        assert tar.push(i) == ref.append(i)

    @staticmethod
    def _check_op_pop(tar: CustomStackQueue, ref: deque):
        ret_tar = tar.pop()
        try:
            if isinstance(tar, CustomStack):
                ret_ref = ref.pop()
            else:
                ret_ref = ref.popleft()
        except IndexError:
            ret_ref = None
        assert ret_tar == ret_ref

    @staticmethod
    def _check_op_traverse(tar: CustomStackQueue, ref: deque):
        assert tar.traverse() == list(ref)

    @staticmethod
    def _check_op_randomly(tar: CustomStackQueue, ref: deque, n_ops: int):
        ops = list(Op)
        for i in range(n_ops):
            op_to_check = choice(ops)
            if op_to_check == Op.IS_EMPTY:
                TestStackQueue._check_op_is_empty(tar, ref)
            elif op_to_check == Op.GET_SIZE:
                TestStackQueue._check_op_get_size(tar, ref)
            elif op_to_check == Op.PUSH:
                TestStackQueue._check_op_push(tar, ref, i)
            elif op_to_check == Op.POP:
                TestStackQueue._check_op_pop(tar, ref)
            TestStackQueue._check_op_traverse(tar, ref)

    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_linked_stack(self, n_ops: int):
        """Test the correctness of the LinkedStack class."""
        tar = LinkedStack[int]()
        ref = deque()
        self._check_op_randomly(tar, ref, n_ops)

    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_array_stack(self, n_ops: int):
        """Test the correctness of the ArrayStack class."""
        tar = ArrayStack[int]()
        ref = deque()
        self._check_op_randomly(tar, ref, n_ops)

    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_linked_queue(self, n_ops: int):
        """Test the correctness of the LinkedQueue class."""
        tar = LinkedQueue[int]()
        ref = deque()
        self._check_op_randomly(tar, ref, n_ops)

    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_array_queue(self, n_ops: int):
        """Test the correctness of the ArrayQueue class."""
        tar = ArrayQueue[int]()
        ref = deque()
        self._check_op_randomly(tar, ref, n_ops)
