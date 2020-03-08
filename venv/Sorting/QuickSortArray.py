"""Quicksort without duplicate elements"""

def partition(A, start, end):
    pivot = A[end]
    pindex = start
    i = start + 1
    for i in range(i, end):
        if A[i] < pivot:
            temp = A[pindex]
            A[pindex] = A[i]
            A[i] = temp
            pindex += 1

    if A[pindex] < pivot:
        pindex += 1
        temp = A[pindex]
        A[pindex] = A[end]
        A[end] = temp
        # print(A," pindex1 : ",pindex)
        return pindex
    elif A[pindex] > pivot:
        temp = A[pindex]
        A[pindex] = A[end]
        A[end] = temp
        # print(A," pindex2 : ",pindex)
        return pindex
    # print(A)


def partition1(A,start,end):
    pivot = A[end]
    i = start -1
    for j in range(start,end):
        i += 1
        if arr[j] < pivot:
            arr[j],arr[i] = arr[i],arr[j]




def QuickSort(A, start, end):
    if start < end:
        pindex = partition(A, start, end)
        QuickSort(A, start, pindex - 1)
        QuickSort(A, pindex + 1, end)

def caller():
    A = [4, 5, 8, 1, 2, 7, 6]
    QuickSort(A, 0,len(A) - 1)
    print(A)

caller()
