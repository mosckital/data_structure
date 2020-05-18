"""The custom implementation of a stack based on queues.

This module illustrates the foundation knowledge of implementing a stack using
queues. The implementation does not use Python's language advantages and looks
dumb, because it only serves as an data structure exercise and has no practical
usage.
"""
from typing import TypeVar, Optional, Sequence
from .custom_stack_queue import CustomStack
from .linked_queue import LinkedQueue
from .size_mixin import SizeMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the stack."""


class QueuedStack(SizeMixin, CustomStack[GT]):
    """
    `QueuedStack[T]()` -> a stack based on queues for values of type `T`.

    This is a custom implementation of a stack based on queues for learning
    purpose. This implementation uses a queue in circular way to achieve the
    functions of a stack. It chooses to make push operation more efficient in
    O(1) time complexity with a cost of making pop operation less efficient in
    O(n) time complexity. But one can easily change this to O(1) for pop and
    O(n) for push.

    Attributes:
        queue (LinkedQueue[T]): the queue to store pushed values
        size (int): the current size of the stack
    """

    def __init__(self):
        super().__init__()
        self.queue = LinkedQueue[GT]()

    def push(self, val: GT) -> None:
        """Push a value into the open end of the stack.

        Args:
            val: the value to push in
        """
        self.queue.push(val)
        self.size += 1

    def pop(self) -> Optional[GT]:
        """Pop a value out from the open end of the stack.

        Returns:
            The popped value or `None` if an empty stack
        """
        if self.size:
            # circularly move all prior values to be behind
            for _ in range(self.size - 1):
                self.queue.push(self.queue.pop())
            val = self.queue.pop()
            self.size -= 1
            return val
        return None

    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the stack and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the stack
        """
        return self.queue.traverse()
