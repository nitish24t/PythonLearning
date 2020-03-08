class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def enqueue(self,data):
        self.size += 1
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if not self.isEmpty():
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp.data
        else:
            print("Empty Queue!")

    def last(self):
        return self.tail.data

    def first(self):
        return self.head.data

    def printQueue(self):
        thead = self.head
        while thead is not None:
            print(thead.data,end=" ")
            thead = thead.next
        print("\t")


def QuickSort(S):
    if len(S) < 2:
        return
    # pivot = S.last()
    """can take last or first as pivot"""
    pivot = S.last()
    # print("pivot - ",pivot,sep=" ")
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.isEmpty():
        if S.first() < pivot:
            L.enqueue(S.dequeue())
        elif S.first() > pivot:
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    # L.printQueue();E.printQueue();G.printQueue()
    QuickSort(L)
    QuickSort(G)

    while not L.isEmpty():
        S.enqueue(L.dequeue())
    while not E.isEmpty():
        S.enqueue(E.dequeue())
    while not G.isEmpty():
        S.enqueue(G.dequeue())

"""
7   2   9   6   21  5
"""
S = LinkedQueue()
S.enqueue(7)
S.enqueue(2)
S.enqueue(9)
S.enqueue(6)
S.enqueue(21)
S.enqueue(5)
print("input queue : ")
S.printQueue()
QuickSort(S)
print("sorted result : ")
S.printQueue()
