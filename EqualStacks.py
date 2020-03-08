#!/bin/python3

import os
import sys


class ListStack:
    def __init__(self, li=[]):  # initialisation
        self._data = []
        self._adder = sum(li)

    def isEmpty(self):  # empty check
        return len(self._data) == 0

    # def push(self,e):           #insertion
    #     self._adder += e
    #     self._data.append(self._adder)
    def pop(self):  # pop from top of stack
        if self.isEmpty():
            raise Exception("Empty stack for pop operation")
        self._adder -= self._data[-1]
        return self._data.pop()

    def top(self):
        if self.isEmpty():
            raise Exception("Empty stack for top operation")
        return self._adder

    def find(self, e):
        if e in self._data:
            return True
        else:
            return False


#
# Complete the equalStacks function below.
#
def checkEquality(length, checkStack, s2, s3):
    top = 0
    for x in range(length):
        if s2.find(checkStack.top()) == s3.find(checkStack.top()) == True:
            return checkStack.top()
        else:
            checkStack.pop()
    return 0


def equalStacks(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    s1 = ListStack(h1)
    s2 = ListStack(h2)
    s3 = ListStack(h3)
    l1, l2, l3 = len(h1), len(h2), len(h3)
    # for x in h1:
    #     s1.push(x)
    # for x in h2:
    #     s2.push(x)
    # for x in h3:
    #     s3.push(x)
    if l1 < (l2 and l3):
        shortest = l1
        checkStack = s1
        result = checkEquality(shortest, checkStack, s2, s3)
    elif l2 < (l1 and l3):
        shortest = l2
        checkStack = s2
        result = checkEquality(shortest, checkStack, s1, s3)
    else:
        shortest = l3
        checkStack = s3
        result = checkEquality(shortest, checkStack, s1, s2)

    return result


if __name__ == '__main__':

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print((result) + '\n')
