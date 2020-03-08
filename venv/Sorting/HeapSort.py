def build_max_heap(arr):
    n = len(arr)
    i = int(n/2)-1
    while i >= 0:
        left = arr[2 * i + 1]
        right = 0
        if not 2*i +2 > len(arr)-1:
            right = arr[2 * i + 2]
        # print("index,element =",i,arr[i],"\twith left -",left,"and right -",right,sep="\t",)
        if left >= right and left >= arr[i]:
            arr[2 * i + 1],arr[i] = arr[i],arr[2 * i + 1]
        if right >= left and right >= arr[i]:
            arr[2 * i + 2], arr[i] = arr[i], arr[2 * i + 2]
        i -= 1

arr = [5,7,9,8,6,8,11,2,3,11]
#build_max_heap(arr)
#print(arri)

def heapify(arr):
    if len(arr) > 0:
        n = len(arr)
        build_max_heap(arr)
        arr[0],arr[n-1] = arr[n-1],arr[0]
        print(arr.pop(), end=" ")
        heapify(arr)

heapify(arr)



















