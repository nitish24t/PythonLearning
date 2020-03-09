class Stack:
    def __init__(self):
        self.li = []

    def push(self,elem):
        self.li.append(elem)

    def isEmpty(self):
        if len(self.li) == 0:
            return True
        else: return False

    def pop(self):
        if not self.isEmpty():
            temp = self.li[-1]
            self.li = self.li[:-1]
            print("\n",temp)
        else:
            print("List is Empty")

    def printStack(self):
        for x in self.li:
            print(x,end="  ")


if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(4)
    st.push(7)
    st.pop()
    st.printStack()
    st.push(55)
    st.pop()
    st.printStack()
