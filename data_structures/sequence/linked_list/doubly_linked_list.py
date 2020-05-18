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
    # pylint: disable=duplicate-code
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

    def _insert_head(self, val: GT) -> None:
        super()._insert_head(val)
        if self.head.next:
            self.head.next.prev = self.head
        else:
            self.tail = self.head

    def _insert_after(self, val: GT, prev_node: Node[GT]) -> None:
        super()._insert_after(val, prev_node)
        new_node = prev_node.next
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    def _delete_head(self) -> None:
        super()._delete_head()
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def _delete_after(self, prev_node: Node[GT]) -> None:
        super()._delete_after(prev_node)
        if prev_node.next:
            prev_node.next.prev = prev_node
        else:
            self.tail = prev_node

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
        if self.size:
            val = self.tail.val
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1
            return val
        return None
