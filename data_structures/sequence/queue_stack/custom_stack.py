"""The abstract base class for all the custom implementations of a stack."""
from typing import TypeVar, Generic, Optional, Sequence
from abc import ABC, abstractmethod


GT = TypeVar('GT')


class CustomStack(Generic[GT], ABC):
    """The abstract base class for all custom implementations of a stack."""

    def __init__(self):
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            `True` if the stack is empty or `False` otherwise
        """

    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the stack.

        Returns:
            The size of the stack
        """

    @abstractmethod
    def push(self, val: GT) -> None:
        """Push a value into the open end of the stack.

        Args:
            val: the value to push in
        """

    @abstractmethod
    def pop(self) -> Optional[GT]:
        """Pop a value out from the open end of the stack.

        Returns:
            The popped value or `None` if an empty stack
        """

    @abstractmethod
    def traverse(self) -> Sequence[GT]:
        """Traverse all values in the stack and return as a Python `list`.

        Returns:
            A Python `list` containing all values in the stack
        """
