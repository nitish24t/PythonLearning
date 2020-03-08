class Empty(Exception):
    """error attempting to access element from queue"""
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        print("Length - ",self._size)
        return self._size

    def isEmpty(self):
        print("isEmpty - ",self._size==0)
        return self._size == 0

    def first(self):
        if self.isEmpty():
            raise Empty("First() - List is empty!")
        print("First - ",self._data[self._front])
        return self._data[self._front]

    def dequeue(self):
        if self.isEmpty():
            raise Empty("Dequeue() - List is empty!")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        print("Dequeue - ",answer," - ",self._data)
        return answer

    def enqueue(self,e):
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        print("Enqueue - ", self._data)

    def resize(self,cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk)%len(old)
        self._front = 0


# if __name__ == "__main__":
#     queue = ArrayQueue()
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)
#     queue.enqueue(4)
#     len(queue)
#     queue.dequeue()
#     queue.dequeue()
#     len(queue)
#     queue.dequeue()
#     queue.enqueue(6)
#     queue.first()
#     queue.isEmpty()
