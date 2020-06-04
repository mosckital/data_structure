"""This module implements the binary search algorithm in different ways.

All these implementations are for learning purposes.
"""
from typing import TypeVar, Generic, Sequence, Callable


T = TypeVar('T')
"""type: The generic type for the elements in the list for binary search."""


class BinarySearch(Generic[T]):
    """Class of implementations of binary search algorithm.

    All the implementations are static methods.
    """

    @staticmethod
    def search(
            seq: Sequence[T],
            val: T,
            comparer: Callable[[T, T], bool] = lambda a, b: a - b
        ) -> int:
        """Binary search for an ordered list with no repeating element.

        This implementation uses inclusive boundaries for both the left and
        right sides.

        Note:
            If there are repeating elements in the passed in list and such
            element is the target to search for, the algorithm may return any
            of the indexes of the target element and the result is undefined.

        Args:
            seq: a list to search in
            val: the value to search for
            comparer: the function to compare the element in the list and the
                target value

        Returns:
            The index of the target value in the list, or `-1` if not found
        """
        if not seq:
            return -1
        i, j = 0, len(seq) - 1
        while i <= j:
            mid = (i + j) // 2
            comp = comparer(seq[mid], val)
            if comp == 0:
                return mid
            if comp < 0:
                i = mid + 1
            else:
                j = mid - 1
        return -1

    @staticmethod
    def search_right_exclusive(
            seq: Sequence[T],
            val: T,
            comparer: Callable[[T, T], bool] = lambda a, b: a - b
        ) -> int:
        """Binary search for an ordered list with no repeating element.

        This implementation uses inclusive boundaries for the left side but
        exclusive boundary for the right side.

        Note:
            If there are repeating elements in the passed in list and such
            element is the target to search for, the algorithm may return any
            of the indexes of the target element and the result is undefined.

        Args:
            seq: a list to search in
            val: the value to search for
            comparer: the function to compare the element in the list and the
                target value

        Returns:
            The index of the target value in the list, or `-1` if not found
        """
        if not seq:
            return -1
        i, j = 0, len(seq)
        while i < j:
            mid = (i + j) // 2
            comp = comparer(seq[mid], val)
            if comp == 0:
                return mid
            if comp < 0:
                i = mid + 1
            else:
                j = mid
        return -1

    @staticmethod
    def search_left_exclusive(
            seq: Sequence[T],
            val: T,
            comparer: Callable[[T, T], bool] = lambda a, b: a - b
        ) -> int:
        """Binary search for an ordered list with no repeating element.

        This implementation uses inclusive boundary for the right side but
        exclusive boundary for the left side.

        Note:
            If there are repeating elements in the passed in list and such
            element is the target to search for, the algorithm may return any
            of the indexes of the target element and the result is undefined.

        Args:
            seq: a list to search in
            val: the value to search for
            comparer: the function to compare the element in the list and the
                target value

        Returns:
            The index of the target value in the list, or `-1` if not found
        """
        if not seq:
            return -1
        i, j = -1, len(seq) - 1
        while i < j:
            mid = (i + j + 1) // 2
            comp = comparer(seq[mid], val)
            if comp == 0:
                return mid
            if comp < 0:
                i = mid
            else:
                j = mid - 1
        return -1
