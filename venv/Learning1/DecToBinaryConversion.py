#recursive approach
def decToBinary(num):
    if num > 1:
        decToBinary(num//2)
    print(num%2)

# decToBinary(7)

#iterative approach
def decToBinaryIterative(num):
    res = []
    while num >= 1:
        res.append(num % 2)
        num = num // 2
    if num is 1:
        res.append(num)
    res.reverse()
    print(res)

decToBinaryIterative(8)
