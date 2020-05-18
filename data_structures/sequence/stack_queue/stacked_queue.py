"""The custom implementation of a queue using stacks.

This module illustrates the foundation knowledge of implementing a queue using
stacks. The implementation does not use Python's language advantages and looks
dumb, because it only serves as an data structure exercise and has no practical
usage.
"""
from typing import TypeVar, Optional, Sequence
from .custom_stack_queue import CustomQueue
from .linked_stack import LinkedStack
from .size_mixin import SizeMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the queue."""


class StackedQueue(SizeMixin, CustomQueue[GT]):
    """
    `StackedQueue[T]()` -> a queue based on stacks for values of type `T`.

    This is a custom implementation of a queue based on stacks for learning
    purpose. This implementation uses two stacks to achieve amortised O(1) time
    complexity, one stack for recently pushed values and the other stack for
    previously stored values in inverse order. Each value will be in and out
    once for each stack, so concluding a constant time cost in average.

    Attributes:
        stack (LinkedStack[GT]): the stack to store recent pushed values
        inverse (LinkedStack[GT]): the stack to store old inverse values
        size (int): the current size of the queue
    """

    def __init__(self):
        super().__init__()
        self.stack = LinkedStack[GT]()
        self.inverse = LinkedStack[GT]()

    def push(self, val: GT) -> None:
        """Push a value into the end of the queue.

        Args:
            val: the value to push in
        """
        self.stack.push(val)
        self.size += 1

    def pop(self) -> Optional[GT]:
        """Pop a value out from the start of the queue.

        Returns:
            The popped value or `None` if an empty queue
        """
        # transfer all values in `stack` to `inverse` in inverse order
        if self.inverse.is_empty():
            while not self.stack.is_empty():
                self.inverse.push(self.stack.pop())
        # pop the top value of the `inverse` if not empty
        if not self.inverse.is_empty():
            self.size -= 1
            return self.inverse.pop()
        return None

    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the queue and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the queue
        """
        list_ = []
        # traverse `inverse` in inverse order
        node = self.inverse.tail
        while node:
            list_.append(node.val)
            node = node.prev
        # traverse `stack`
        node = self.stack.head
        while node:
            list_.append(node.val)
            node = node.next
        return list_
