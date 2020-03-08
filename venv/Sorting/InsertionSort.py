arr = [2,3,4,1,5,8,7,6]
arr1 = [4,5,1,2,7,3]

def InsertionSort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i                       # j is gonna be correct position for curr
        while j > 0 and arr[j - 1] > curr:      #moving forward all the elements by one index which are greater than curr
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = curr
    return arr

sortedArr = InsertionSort(arr)
for x in sortedArr:
    print(x,end=" ")
