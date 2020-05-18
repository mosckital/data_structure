"""Custom implementation of a singly linked list.

This module illustrates the foundation knowledge of a singly linked list by
implementing it. It has no practical usage but only serves as an data structure
exercise.
"""
from typing import TypeVar, Optional, Sequence
from ..custom_sequence import CustomSequence
from .custom_linked_list import LinkedListMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the linked lists."""


class SinglyLinkedList(LinkedListMixin[GT], CustomSequence[GT]):
    """
    `SinglyLinkedList[T]()` -> an empty singly linked list of type `T`

    This is a custom implementation of a singly linked list for learning
    purpose.

    The implementation uses the `Node` implemented inside `LinkedListMixin` as
    the nodes in the list.

    Attributes:
        head (Optional[Node[T]]): the head node of the singly linked list
        size (int): the size of the singly linked list
    """

    Node = LinkedListMixin.Node
    """type: An alias for the correspondent node type."""

    def __init__(self):
        super().__init__()
        self.head = None
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

    def _insert_head(self, val: GT) -> None:
        new_head = self.Node[GT](val)
        new_head.next = self.head
        self.head = new_head
        self.size += 1

    def _insert_after(self, val: GT, prev_node: Node[GT]) -> None:
        new_node = self.Node[GT](val)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1

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
            self._insert_head(val)
            return True
        # get the previous node if index is valid
        prev_node = self.node_at(idx - 1)
        # insert if there is a previous node
        if prev_node:
            self._insert_after(val, prev_node)
            return True
        # previous node is None if index is invalid
        return False

    def _delete_head(self) -> None:
        self.head = self.head.next
        self.size -= 1

    def _delete_after(self, prev_node: Node[GT]) -> None:
        prev_node.next = prev_node.next.next
        self.size -= 1

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
            self._delete_head()
            return True
        # get the previous node if index is valid
        prev_node = self.node_at(idx - 1)
        # delete if there is a previous node
        if prev_node and prev_node.next:
            self._delete_after(prev_node)
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
        self.insert_at(self.size, val)

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
            self._delete_head()
            return val
        # case of multiple nodes
        prev_node = self.node_at(self.size - 2)
        val = prev_node.next.val
        self._delete_after(prev_node)
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
