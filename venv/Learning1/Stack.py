"""Stack Class"""
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else: return False

    def push(self,node):
            thead = self.head
            self.head = node
            self.head.next = thead

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty - Pop not possible")
        else:
            thead = self.head
            self.head = self.head.next
            return thead

    def top(self):
        if self.isEmpty():
            raise Exception("Stack is empty - Top not possible")
        else:
            return self.head
