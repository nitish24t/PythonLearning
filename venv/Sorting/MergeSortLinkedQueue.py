class Node:
    def __init__(self,element):
        self.element = element
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.size

    def enqueue(self,element):
        node = Node(element)
        self.size += 1
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        else:
            curr = self.head
            self.head = curr.next
            if self.head == None:
                self.tail == None
            self.size -= 1
            return curr.element

    def first(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        else:
            return self.head.element

    def printQueue(self):
        curr = self.head
        while curr:
            print(curr.element,end=" ")
            curr = curr.next
        print("\n")


def MergeSort(S):
    n = len(S)
    if n > 1:
        S1 = LinkedQueue()
        S2 = LinkedQueue()

        while len(S1) < n // 2:
            S1.enqueue(S.dequeue())

        while not S.isEmpty():
            S2.enqueue(S.dequeue())

        MergeSort(S1)
        MergeSort(S2)
        Merge(S1,S2,S)

def Merge(S1,S2,S):
    while not S1.isEmpty() and not S2.isEmpty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue((S2.dequeue()))
    while not S1.isEmpty():
        S.enqueue(S1.dequeue())
    while not S2.isEmpty():
        S.enqueue(S2.dequeue())


S1 = LinkedQueue()
S1.enqueue(24)
S1.enqueue(45)
S1.enqueue(63)
S1.enqueue(85)
S1.enqueue(17)
S1.enqueue(31)
S1.enqueue(96)
S1.enqueue(50)
MergeSort(S1)
S1.printQueue()


 """merge check (add S.dequeue() before every enqueue while doing only merge check"""
# s1 = LinkedQueue()
# s1.enqueue(1)
# s1.enqueue(3)
# s2 = LinkedQueue()
# s2.enqueue(4)
# s2.enqueue(5)
#
# s = LinkedQueue()
# s.enqueue(5)
# s.enqueue(9)
# s.enqueue(5)
# s.enqueue(9)
# Merge(s1,s2,s)
# s.printQueue()






