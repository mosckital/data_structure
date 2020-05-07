"""Test suite for the TwoPointer class.

TwoPointer class only has static methods, which are either the implementations
of the algorithms based on the two pointer technique or the helper functions.

The test class will generate linked list with no cycle, full cycle and partial
cycle to test the correctness of the algorithms in different situations.
"""
from random import randint
import pytest
from data_structures.sequence import SinglyLinkedList
from techniques.two_pointer import TwoPointer


class TestTwoPointer():
    """
    The test suite class for the TwoPointer class.
    """

    @staticmethod
    def _generate_linked_list(size_list: int, size_cycle: int = 0):
        """
        Generate a linked list of a given size with a cycle of a given size, or
        with no cycle if the cycle size is 0 or not given (by default).

        Args:
            size_list: the size of the linked list
            size_cycle: the size of the cycle, 0 by default

        Returns:
            The generated singly linked list
        """
        # check the given sizes are valid
        assert size_list >= size_cycle >= 0
        # initiate an empty linked list
        list_ = SinglyLinkedList[int]()
        # return this empty list if the given size is 0
        if not size_list:
            return list_
        # generate the list one node by one node
        prev_node = SinglyLinkedList.Node[int](0)
        list_.head = prev_node
        for i in range(1, size_list):
            node = SinglyLinkedList.Node[int](i)
            prev_node.next = node
            prev_node = node
        # link the last node to the start node of the cycle if cycle size > 0
        if size_cycle:
            prev_node.next = list_.node_at(size_list - size_cycle)
        # assign the list size to the linked list object
        list_.size = size_list
        return list_

    @pytest.mark.parametrize(
        'size_list',
        [10, 100, 1000],
    )
    def test_has_a_cycle(self, size_list: int):
        """
        Test the correctness of the has_a_cycle method.
        """
        # case no cycle
        list_ = self._generate_linked_list(size_list)
        assert not TwoPointer.has_a_cycle(list_)
        # case a circle / full cycle
        list_ = self._generate_linked_list(size_list, size_list)
        assert TwoPointer.has_a_cycle(list_)
        # case a partial cycle
        size_cycle = randint(1, size_list - 1)
        list_ = self._generate_linked_list(size_list, size_cycle)
        assert TwoPointer.has_a_cycle(list_)

    @pytest.mark.parametrize(
        'size_list',
        [10, 100, 1000],
    )
    def test_start_node_of_cycle(self, size_list: int):
        """
        Test the correctness of the start_node_of_cycle method.
        """
        # case no cycle
        list_ = self._generate_linked_list(size_list)
        assert TwoPointer.start_node_of_cycle(list_) is None
        # case a circle / full cycle
        list_ = self._generate_linked_list(size_list, size_list)
        assert TwoPointer.start_node_of_cycle(list_) == list_.head
        # case a partial cycle
        size_cycle = randint(1, size_list - 1)
        list_ = self._generate_linked_list(size_list, size_cycle)
        assert TwoPointer.start_node_of_cycle(list_) == list_.node_at(size_list - size_cycle)
