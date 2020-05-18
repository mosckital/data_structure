"""The implementation of common methods for the linked stack or linked queue
type data structures.

This module defines the common operations about for a linked stack or a linked
queue. As we choose to push new element into the same end for no matter linked
stack or linked queue, the push method shares a common implemention, but the pop
method does not. So only the push and traverse methods are implemented in this
module and the pop method will be implemented by the actual class.
"""
from typing import TypeVar, Generic, Sequence
from ..linked_list.custom_linked_list import LinkedListMixin


GT = TypeVar('GT')


class LinkedMixin(Generic[GT]):
    """
    The mixin class to provide implementations of the push and traverse methods
    for a linked stack or a linked queue. The pop method will be implemented by
    the actual class itself as stack and queue have different definitions.

    `LinkedMixin.push(val)` -> push `val` into the instance
    `LinkedMixin.traverse()` -> traverse the instance and return in a list
    """

    Node = LinkedListMixin.DoublyNode
    """type: An alias for the correspondent node type."""

    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val: GT) -> None:
        """Push a value into the open end of the instance.

        Args:
            val: the value to push in
        """
        node = self.Node[GT](val)
        if self.size:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1
        else:
            self.head = self.tail = node
            self.size += 1

    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the instance and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the instance
        """
        list_ = []
        node = self.head
        while node:
            list_.append(node.val)
            node = node.next
        return list_
