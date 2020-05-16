"""The implementation of a linked list mixin for the sequence-like linked list
data structures.

This module defines two common operations of a linked list and the node classes
for the singly and doubly linked lists. All these classes are only implemented
for learning purpose and have no practical usage.
"""
from __future__ import annotations
from typing import TypeVar, Generic, Optional


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the sequence."""


class LinkedListMixin(Generic[GT]):
    """
    The mixin class to provide implementations of two common operations, to get
    the head node and to get the node at a specific index, for linked lists.
    """

    class Node(Generic[GT]):
        """
        The basic node structure for a singly linked list.
        """

        def __init__(self, val: GT):
            self.val = val
            self.next = None

        def insert_after(self, prev: LinkedListMixin.Node[GT]) -> None:
            if not self._check_prev(prev):
                raise ValueError("Invalid 'prev'!")
            self.next = prev.next
            prev.next = self

        def delete_after(self, prev: LinkedListMixin.Node[GT]) -> None:
            if not self._check_prev(prev):
                raise ValueError("Invalid 'prev'!")
            prev.next = self.next

        def _check_prev(self, prev: LinkedListMixin.Node[GT]) -> bool:
            return prev and prev.next == self

    class DoublyNode(Generic[GT], Node[GT]):
        """
        The basic node structure for a doubly linked list.
        """

        def __init__(self, val: GT):
            super().__init__(val)
            self.prev = None

        def insert_after(self, prev: LinkedListMixin.DoublyNode[GT]) -> None:
            super().insert_after(prev)
            self.prev = prev
            if self.next:
                self.next.prev = self

        def delete_after(self, prev: LinkedListMixin.DoublyNode[GT]) -> None:
            super().delete_after(prev)
            if self.next:
                self.next.prev = self.prev

    def __init__(self):
        self.head = None
        self.size = 0

    def get_head(self) -> Optional[Node[GT]]:
        """
        Get the head node of the linked list.

        Returns:
            The head node of the linked list or `None` if empty list
        """
        return self.head

    def node_at(self, idx: int) -> Optional[Node[GT]]:
        """
        Get the node at the given index.

        Args:
            idx: the index to fetch

        Returns:
            The node at the given index or `None` if index not valid
        """
        if idx < 0:
            return None
        i = 0
        node = self.head
        while node and i < idx:
            node = node.next
            i += 1
        # node is None if idx >= self.size
        return node
