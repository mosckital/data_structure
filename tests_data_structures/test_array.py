import pytest
from random import choice, randint
from enum import Enum
from data_structures.array import Array


class Op(Enum):
    GET_SIZE = 0
    INDEX_OF = 1
    VALUE_AT = 2
    INSERT_AT = 3
    DELETE_AT = 4
    UPDATE_AT = 5
    TRAVERSE = 6


class RefArray(object):

    def __init__(self, max_size: int):
        self.data = []
        self.max_size = max_size
    
    def get_size(self) -> int:
        return len(self.data)
    
    def index_of(self, e) -> int:
        try:
            return self.data.index(e)
        except ValueError as e:
            return -1
    
    def value_at(self, idx: int):
        if 0 <= idx < len(self.data):
            return self.data[idx]
        else:
            return None
    
    def insert_at(self, idx: int, e) -> bool:
        if len(self.data) == self.max_size:
            return False
        if 0 <= idx <= len(self.data):
            self.data.insert(idx, e)
            return True
        else:
            return False
    
    def delete_at(self, idx: int) -> bool:
        if 0 <= idx < len(self.data):
            self.data[idx:idx + 1] = []
            return True
        else:
            return False
    
    def update_at(self, idx: int, e) -> bool:
        if 0 <= idx < len(self.data):
            self.data[idx] = e
            return True
        else:
            return False
        
    def traverse(self) -> list:
        return self.data
    
    def __eq__(self, value):
        if isinstance(value, Array):
            return len(self.data) == value.curr_size and \
                self.data == value.data[:value.curr_size]
        return super().__eq__(value)


class TestArray(object):  

    @pytest.mark.parametrize(
        'max_size',
        [1, 4, 16],
    )
    @pytest.mark.parametrize(
        'n_ops',
        [100, 1000, 10000],
    )
    def test_random_ops(self, max_size, n_ops):
        # the array implementation to test
        arr = Array(max_size)
        # the reference array implementation
        alt = RefArray(max_size)
        # list of operations to test
        ops = [o for o in Op]
        # perform n_ops times of operation test
        for i in range(n_ops):
            # randomly choose an operation
            op = choice(ops)
            if op == Op.GET_SIZE:
                assert arr.get_size() == alt.get_size()
            elif op == Op.INDEX_OF:
                # check normal case
                if arr.get_size() > 0:
                    idx = randint(0, arr.get_size() - 1)
                    e = arr.value_at(idx)
                    assert arr.index_of(e) == alt.index_of(e) == idx
                # check two edge cases
                e = randint(i, i * 2)
                assert arr.index_of(e) == alt.index_of(e) == -1
                assert arr.index_of(-e) == alt.index_of(-e) == -1
            elif op == Op.VALUE_AT:
                # check normal case
                if arr.get_size() > 0:
                    idx = randint(0, arr.get_size() - 1)
                    assert arr.value_at(idx) == alt.value_at(idx)
                    assert arr.value_at(idx) is not None
                # check two edge cases
                idx = randint(arr.get_size(), arr.get_size() * 2)
                assert arr.value_at(idx) == alt.value_at(idx) == None
                idx = randint(- arr.get_size() - 1, -1)
                assert arr.value_at(idx) == alt.value_at(idx) == None
            elif op == Op.INSERT_AT:
                # check two edge cases
                idx = randint(arr.get_size() + 1, arr.get_size() * 2 + 1)
                assert arr.insert_at(idx, i) == alt.insert_at(idx, i) == False
                idx = randint(- arr.get_size() - 1, -1)
                assert arr.insert_at(idx, i) == alt.insert_at(idx, i) == False
                # check normal case
                idx = randint(0, arr.get_size())
                ret = True if arr.get_size() < max_size else False
                assert arr.insert_at(idx, i) == alt.insert_at(idx, i) == ret
            elif op == Op.DELETE_AT:
                # check two edge cases
                idx = randint(arr.get_size(), arr.get_size() * 2)
                assert arr.delete_at(idx) == alt.delete_at(idx) == False
                idx = randint(- arr.get_size() - 1, -1)
                assert arr.delete_at(idx) == alt.delete_at(idx) == False
                # check normal case
                if arr.get_size() > 0:
                    idx = randint(0, arr.get_size() - 1)
                    assert arr.delete_at(idx) == alt.delete_at(idx) == True
            elif op == Op.UPDATE_AT:
                # check two edge cases
                idx = randint(arr.get_size(), arr.get_size() * 2)
                assert arr.update_at(idx, i) == alt.update_at(idx, i) == False
                idx = randint(- arr.get_size() - 1, -1)
                assert arr.update_at(idx, i) == alt.update_at(idx, i) == False
                # check normal case
                if arr.get_size() > 0:
                    idx = randint(0, arr.get_size() - 1)
                    assert arr.update_at(idx, i) == alt.update_at(idx, i) == True
            elif op == Op.TRAVERSE:
                assert arr.traverse() == alt.traverse()
            # check two array implementations are same after any operation
            assert alt == arr
