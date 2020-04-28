class Array(object):
    """
    This is a wrapper of list to illustrate the operations of an array of fixed
    length for the purpose of learning data structures.
    """

    def __init__(self, max_size: int):
        self.data = [None] * max_size
        self.max_size = max_size
        self.curr_size = 0
    
    def get_size(self) -> int:
        return self.curr_size
    
    def index_of(self, e) -> int:
        for i in range(self.curr_size):
            if self.data[i] == e:
                return i
        return -1

    def value_at(self, idx: int):
        if 0 <= idx < self.curr_size:
            return self.data[idx]
        else:
            return None
    
    def insert_at(self, idx: int, e) -> bool:
        if 0 <= idx <= self.curr_size < self.max_size:
            for i in range(self.curr_size, idx, -1):
                self.data[i] = self.data[i - 1]
            self.data[idx] = e
            self.curr_size += 1
            return True
        else:
            return False

    def delete_at(self, idx: int) -> bool:
        if 0 <= idx < self.curr_size:
            for i in range(idx, self.curr_size - 1):
                self.data[i] = self.data[i + 1]
            self.curr_size -= 1
            return True
        else:
            return False
    
    def update_at(self, idx: int, e) -> bool:
        if 0 <= idx < self.curr_size:
            self.data[idx] = e
            return True
        else:
            return False
    
    def traverse(self) -> list:
        return [self.data[i] for i in range(self.curr_size)]