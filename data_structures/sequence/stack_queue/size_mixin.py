"""The implementation of methods about size for the stack or queue type data
structures.

This module defines the common operations about the size for a stack or a queue.
This implementation is mainly for learning purpose.
"""

class SizeMixin():
    """
    The mixin class to provide implementations of methods about size of the
    object (stack or queue). Currently, two methods are implemented by this
    mixin:

    `SizeMixin.is_empty()` -> `True` if empty or `False` otherwise
    `SizeMixin.get_size()` -> The size of the stack or queue
    """

    def __init__(self):
        self.size = 0

    def is_empty(self) -> bool:
        """Check if the instance if empty.

        Returns:
            `True` if empty or `False` otherwise
        """
        return self.size == 0

    def get_size(self) -> int:
        """Get the size of the instance, i.e. the number of stored items.

        Returns:
            The size of the instance
        """
        return self.size
