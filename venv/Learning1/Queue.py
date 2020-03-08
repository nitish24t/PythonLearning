class qNode:
    def __init__(self,element):
        self.element = element
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def enqueue(self,element):
        node = qNode(element)
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
            return curr.element

    def printQueue(self):
        curr = self.head
        while curr:
            print(curr.element,end=" ")
            curr = curr.next

    def reverse(self):
        print("reverse queue")
        thead = self.head
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        self.tail = thead

if __name__ == "__main__":
    qu = Queue()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(5)
    qu.enqueue(88)
    qu.enqueue(6)
    qu.printQueue()
    print("\nhead ",qu.head.element)
    print("\ntail ",qu.tail.element)
    qu.reverse()
    qu.printQueue()
    print("\nhead ", qu.head.element)
    print("\ntail ", qu.tail.element)
