"""Custom implementation of a singly linked list.

This module illustrates the foundation knowledge of a singly linked list by
implementing it. It has no practical usage but only serves as an data structure
exercise.
"""
from typing import TypeVar, Generic, Optional, Sequence
from data_structures.custom_sequence import CustomSequence


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the linked lists."""


class SinglyLinkedList(CustomSequence[GT]):
    """
    `SinglyLinkedList[T]()` -> an empty singly linked list of type `T`

    This is a custom implementation of a singly linked list for learning
    purpose. The implementation uses a internal class `Node` to encapsulate the
    nodes in the list.

    Attributes:
        head (Optional[Node[T]]): the head node of the singly linked list
        size (int): the size of the singly linked list
    """

    class Node(Generic[GT]):
        """Simple plain class for the nodes in a singly linked list.

        `Node[T](val)` -> a node storing a value `val`

        Args:
            val (Optional[T]): the value to store, default to `None`

        Attributes:
            val (Optional[T]): the stored value
            next (Node[T]): the next node
        """

        def __init__(self, val: Optional[GT]):
            self.val = val
            self.next = None

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

    def _node_at(self, idx: int) -> Optional[Node[GT]]:
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
            i += 1
            node = node.next
        return node

    def value_at(self, idx: int) -> Optional[GT]:
        """
        Get the value at the given index.

        Args:
            idx: the index to fetch

        Returns:
            The value at the given index or `None` if index not valid
        """
        node = self._node_at(idx)
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
        if idx == 0:
            new_node = self.Node[GT](val)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        node = self._node_at(idx - 1)
        if node:
            new_node = self.Node[GT](val)
            new_node.next = node.next
            node.next = new_node
            self.size += 1
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
            `True` if deletion is successful or `False` otherwise
        """
        if not self.size:
            return False
        if idx == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        prev_node = self._node_at(idx - 1)
        if prev_node and prev_node.next:
            prev_node.next = prev_node.next.next
            self.size -= 1
            return True
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
        node = self._node_at(idx)
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
        if self.size == 0:
            return None
        if self.size == 1:
            val = self.head.val
            self.head = None
            self.size = 0
            return val
        prev_node = self._node_at(self.size - 2)
        val = prev_node.next.val
        prev_node.next = prev_node.next.next
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
