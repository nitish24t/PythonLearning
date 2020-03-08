class Empty(Exception):
    """Error attempting to access element from empty stack"""
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def push(self,newdata):
        self._data.append(newdata)
        print("pushed - ",self._data)

    def top(self):
        if self.isEmpty():
            raise Empty("Stack is Empty Man!!")
        print("top - ",self._data[-1])
        return self._data[-1]

    def pop(self):
        if self.isEmpty():
            raise Empty("Stack is Empty Man!!")
        else:
            self._data.pop()
            print("popped - ",self._data)


# if __name__ == "__main__":
#     stack = ArrayStack()
#     stack.isEmpty()
#     stack.push(1)
#     stack.push(2)
#     stack.push(4)
#     stack.top()
#     stack.pop()
#     stack.top()
#     stack.push(6)
#     print(len(stack))
