"""The abstract base class for all the custom implementations of a queue."""
from typing import TypeVar, Generic, Optional, Sequence
from abc import ABC, abstractmethod


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the queue,"""


class CustomQueue(Generic[GT], ABC):
    """The abstract base class for all custom implementations of a queue."""

    def __init__(self):
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            `True` if the queue is empty or `False` otherwise
        """

    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the queue.

        Returns:
            The size of the queue
        """

    @abstractmethod
    def push(self, val: GT) -> None:
        """Push a value into the end of the queue.

        Args:
            val: the value to push in
        """

    @abstractmethod
    def pop(self) -> Optional[GT]:
        """Pop a value out from the start of the queue.

        Returns:
            The popped value or `None` if an empty queue
        """

    @abstractmethod
    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the queue and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the queue
        """
