"""Custom implementation of a doubly linked list.

This module illustrates the foundation knowledge of doubly linked list by
implementing it. The class inherits from the implementation of singly linked
list and only implements the changes. This way can highlights the differences
between the implementations of singly and doubly linked lists. This
implementation has no practical usage but only serves as an data structure
exercise.
"""
from typing import TypeVar, Optional
from .singly_linked_list import SinglyLinkedList
from .custom_linked_list import LinkedListMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the linked lists."""


class DoublyLinkedList(SinglyLinkedList[GT]):
    """
    `DoublyLinkedList[T]()` -> an empty doubly linked list of type `T`

    This is a custom implementation of a doubly linked list for learning
    purpose. It inherits from SinglyLinkedList and only implements the changes
    in order to highlight the changes.

    The implementation uses the `DoublyNode` implemented inside
    `LinkedListMixin` as the nodes in the list.

    Attributes:
        head (Optional[Node[T]]): the head node of the doubly linked list
        tail (Optional[Node[T]]): the tail node of the doubly linked list
        size (int): the size of the doubly linked list
    """

    Node = LinkedListMixin.DoublyNode
    """type: An alias for the correspondent node type."""

    def __init__(self):
        super().__init__()
        self.tail = None

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
