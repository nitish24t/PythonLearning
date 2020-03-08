class Error(Exception):
    """Error attempting to access element from dequeue"""
    pass

class Dequeue:
    DEFAULT_CAPACITY = 5
    def __init__(self):
        self._data = [None]*DEFAULT_CAPACITY
        self._size = 0
        self.front = 0
        self.last = 0
