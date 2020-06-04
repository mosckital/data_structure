"""Test suite for the BinarySearch class.

The BinarySearch class only has static methods, which are the implementations of
binary search algorithms for a list of values and for different cases.
"""
from random import randint
import pytest
from techniques.binary_search import BinarySearch


class TestBinarySearch():
    """The test suite class for the BinarySearch class."""

    # The constants to control the generation of an ordered list
    _START_HALF_RANGE = 100  # control the first number in the list
    _INTERVAL_RANGE = 5  # control the increase speed
    _REPEAT_RANGE = 5  # control the repeating frequency

    @staticmethod
    def _generate_strict_ordered_list(length: int = 10):
        """Generate an ordered list with no repeating element."""
        if length == 0:
            return []
        ret = [None] * length
        ret[0] = randint(-TestBinarySearch._START_HALF_RANGE, TestBinarySearch._START_HALF_RANGE)
        for i in range(1, length):
            ret[i] = ret[i - 1] + randint(1, TestBinarySearch._INTERVAL_RANGE)
        return ret

    @staticmethod
    def _generate_repeat_ordered_list(n_diff_elms: int = 10):
        """Generate an ordered list where all elements are repeating."""
        if n_diff_elms == 0:
            return []
        val = randint(-TestBinarySearch._START_HALF_RANGE, TestBinarySearch._START_HALF_RANGE)
        ret = []
        for _ in range(n_diff_elms):
            ret += [val] * randint(2, TestBinarySearch._REPEAT_RANGE)
            val += randint(1, TestBinarySearch._INTERVAL_RANGE)
        return ret

    STRICT_ORDERED_LIST_SEARCH_FUNCTIONS = [
        'search',
        'search_right_exclusive',
        'search_left_exclusive',
    ]
    """The list of binary search implementations for an ordered list with no
    repeating elements.
    """

    @pytest.mark.parametrize('length', (0, 1, 2, 3, 5, 10,))
    @pytest.mark.parametrize('n_checks', (10,))
    @pytest.mark.parametrize('func', STRICT_ORDERED_LIST_SEARCH_FUNCTIONS)
    def test_search(self, length, n_checks, func):
        """Test the correctness of the binary search implementations for an
        ordered list with no repeating elements.
        """
        search_func = getattr(BinarySearch, func)
        for _ in range(n_checks):
            _list = self._generate_strict_ordered_list(length)
            if length > 0:
                # case of non-empty list
                # test for value larger than max
                assert search_func(_list, _list[-1] + 100) == -1
                # test for value smaller than min
                assert search_func(_list, _list[0] - 100) == -1
                # test for every value between min and max inclusive
                for val in range(_list[0], _list[-1] + 1):
                    try:
                        correct_idx = _list.index(val)
                    except ValueError:
                        correct_idx = -1
                    assert search_func(_list, val) == correct_idx
            else:
                # case of empty list, all searches should return -1
                rand_val = randint(
                    -TestBinarySearch._START_HALF_RANGE,
                    TestBinarySearch._START_HALF_RANGE
                )
                assert search_func(_list, rand_val) == -1
