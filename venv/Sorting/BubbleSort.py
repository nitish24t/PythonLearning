arr = [99,2,50,6,12,1,8,23,1]

for j in range(len(arr)-1):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp


for x in arr:
    print(x,end=" ")
