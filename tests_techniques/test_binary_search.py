"""Test suite for the BinarySearch class.

The BinarySearch class only has static methods, which are the implementations of
binary search algorithms for a list of values and for different cases.
"""
from bisect import bisect_left
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

    @staticmethod
    def _common_test_procedure(n_elms, n_checks, func, list_gen, idx_calc):
        """The common test procedure for all binary search implementations.
        """
        search_func = getattr(BinarySearch, func)
        for _ in range(n_checks):
            _list = list_gen(n_elms)
            if n_elms > 0:
                # case of non-empty list
                # test for value larger than max
                assert search_func(_list, _list[-1] + 100) == -1
                # test for value smaller than min
                assert search_func(_list, _list[0] - 100) == -1
                # test for every value between min and max inclusive
                for val in range(_list[0], _list[-1] + 1):
                    correct_idx = idx_calc(_list, val)
                    assert search_func(_list, val) == correct_idx
            else:
                # case of empty list, all searches should return -1
                rand_val = randint(
                    -TestBinarySearch._START_HALF_RANGE,
                    TestBinarySearch._START_HALF_RANGE
                )
                assert search_func(_list, rand_val) == -1

    STRICT_ORDERED_LIST_SEARCH_FUNCTIONS = [
        'search',
        'search_right_exclusive',
        'search_left_exclusive',
    ]
    """The list of binary search implementations for an ordered list with no
    repeating elements.
    """

    @staticmethod
    def _calc_correct_search_idx(_list, val):
        try:
            return _list.index(val)
        except ValueError:
            return -1

    @pytest.mark.parametrize('length', (0, 1, 2, 3, 5, 10,))
    @pytest.mark.parametrize('n_checks', (10,))
    @pytest.mark.parametrize('func', STRICT_ORDERED_LIST_SEARCH_FUNCTIONS)
    def test_search(self, length, n_checks, func):
        """Test the correctness of the binary search implementations for an
        ordered list with no repeating elements.
        """
        self._common_test_procedure(
            length, n_checks, func,
            self._generate_strict_ordered_list,
            self._calc_correct_search_idx,
        )

    REPEAT_ORDERED_LIST_SEARCH_FUNCTIONS = [
        'search_left_bound',
        'search_left_bound_right_exclusive',
        'search_left_bound_left_exclusive',
    ]
    """The list of binary search implementations for an ordered list with all
    repeating elements.
    """

    @staticmethod
    def _calc_correct_search_left_bound_idx(_list, val):
        correct_idx = bisect_left(_list, val)
        if _list[correct_idx] != val:
            correct_idx = -1
        return correct_idx

    @pytest.mark.parametrize('n_diff_elms', (0, 1, 2, 3, 5, 10,))
    @pytest.mark.parametrize('n_checks', (10,))
    @pytest.mark.parametrize('func', REPEAT_ORDERED_LIST_SEARCH_FUNCTIONS)
    def test_search_left_bound(self, n_diff_elms, n_checks, func):
        """Test the correctness of the binary search implementations for an
        ordered list with all repeating elements.
        """
        self._common_test_procedure(
            n_diff_elms, n_checks, func,
            self._generate_repeat_ordered_list,
            self._calc_correct_search_left_bound_idx,
        )
