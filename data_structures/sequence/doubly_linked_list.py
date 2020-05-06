"""Custom implementation of a doubly linked list.

This module illustrates the foundation knowledge of doubly linked list by
implementing it. It has no practical usage but only serves as an data structure
exercise.
"""
from typing import TypeVar, Optional, Sequence
from .custom_sequence import CustomSequence
from .custom_linked_list import LinkedListMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the linked lists."""


class DoublyLinkedList(LinkedListMixin[GT], CustomSequence[GT]):
    """
    `DoublyLinkedList[T]()` -> an empty doubly linked list of type `T`

    This is a custom implementation of a doubly linked list for learning
    purpose. The implementation uses a internal class `Node` to encapsulate the
    nodes in the list.

    Attributes:
        head (Optional[Node[T]]): the head node of the doubly linked list
        tail (Optional[Node[T]]): the tail node of the doubly linked list
        size (int): the size of the doubly linked list
    """

    Node = LinkedListMixin.DoublyNode
    """type: An alias for the correspondent node type."""

    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self) -> int:
        """
        Get the current size.

        Returns:
            The current size
        """
        return self.size

    def index_of(self, val: GT) -> int:
        """
        Get the index of a value, or -1 if not found.

        Args:
            val: the value to look for

        Returns:
            The index of the value or -1 if not found
        """
        i = 0
        node = self.head
        while node:
            if node.val == val:
                return i
            node = node.next
            i += 1
        return -1

    def value_at(self, idx: int) -> Optional[GT]:
        """
        Get the value at the given index.

        Args:
            idx: the index to fetch

        Returns:
            The value at the given index or `None` if index not valid
        """
        node = self.node_at(idx)
        return node.val if node else None

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
        # case to insert at the head, so no previous node
        if idx == 0:
            new_node = self.Node[GT](val)
            new_node.next = self.head
            if new_node.next:
                new_node.next.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
            self.size += 1
            return True
        # get the previous node if index is valid
        prev_node = self.node_at(idx - 1)
        # insert if there is a previous node
        if prev_node:
            new_node = self.Node[GT](val)
            new_node.next = prev_node.next
            if new_node.next:
                new_node.next.prev = new_node
            else:
                self.tail = new_node
            new_node.prev = prev_node
            new_node.prev.next = new_node
            self.size += 1
            return True
        # previous node is None if index is invalid
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
        # case to delete the head if it exists, so no previous node
        if idx == 0 and self.size > 0:
            if self.head.next:
                self.head.next.prev = None
            else:
                self.tail = None
            self.head = self.head.next
            self.size -= 1
            return True
        # get the previous node if index is valid
        prev_node = self.node_at(idx - 1)
        # delete if there is a previous node
        if prev_node and prev_node.next:
            prev_node.next = prev_node.next.next
            if prev_node.next:
                prev_node.next.prev = prev_node
            else:
                self.tail = prev_node
            self.size -= 1
            return True
        # previous node is None if index is invalid
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
        node = self.node_at(idx)
        if node:
            node.val = val
            return True
        return False

    def push(self, val: GT) -> None:
        """
        Push a value into the list.

        Args:
            val: the value to push in
        """
        new_node = self.Node[GT](val)
        if self.size:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
        else:
            self.head = new_node
            self.tail = new_node
            self.size += 1

    def pop(self) -> Optional[GT]:
        """
        Pop a value out from the list and return the value.

        Returns:
            The popped value or `None` if empty
        """
        # no way to pop element if the list is empty
        if self.size == 0:
            return None
        # case of only one node
        if self.size == 1:
            val = self.head.val
            self.head = None
            self.tail = None
            self.size = 0
            return val
        # case of multiple nodes
        val = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return val

    def traverse(self) -> Sequence[GT]:
        """
        Traverse all elements and return them in a list.

        Returns:
            A list containing all elements in order
        """
        ret = []
        node = self.head
        while node:
            ret.append(node.val)
            node = node.next
        return ret
