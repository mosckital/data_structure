"""The abstract base class for all the custom implementations of a stack or a
queue."""
from typing import TypeVar, Generic, Optional, Sequence
from abc import ABC, abstractmethod


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the instance,"""


class CustomStackQueue(Generic[GT], ABC):
    """The abstract base class for all custom implementations of a stack or a
    queue.
    """

    def __init__(self):
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the instance is empty.

        Returns:
            `True` if the instance is empty or `False` otherwise
        """

    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the instance.

        Returns:
            The size of the instance
        """

    @abstractmethod
    def push(self, val: GT) -> None:
        """Push a value into the input end of the instance.

        Args:
            val: the value to push in
        """

    @abstractmethod
    def pop(self) -> Optional[GT]:
        """Pop a value out from the output end of the instance.

        Returns:
            The popped value or `None` if an empty instance
        """

    @abstractmethod
    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the instance and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the instance
        """


class CustomStack(Generic[GT], CustomStackQueue[GT]):
    """The abstract base class for all custom implementations of a stack."""


class CustomQueue(Generic[GT], CustomStackQueue[GT]):
    """The abstract base class for all custom implementations of a queue."""
