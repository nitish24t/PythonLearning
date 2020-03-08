def merge(S1,S2,S):
    length = len(S)
    l1 = len(S1)
    l2 = len(S2)
    i = j = k = 0
    while k < length:
        if (j == l2) or (i < l1 and S1[i] < S2[j]):
            S[k] = S1[i]
            i += 1
        else:
            S[k] = S2[j]
            j += 1
        k += 1

def mergesort(S):
    length = len(S)
    if length < 2:
        return
    mid = length//2
    s1 = S[0:mid]
    s2 = S[mid:]
    mergesort(s1)
    mergesort(s2)
    merge(s1,s2,S)

s1 = [1,6]
s2 = [2,3,4]
s = [0,0,0,0,0]
merge(s1,s2,s)
print(s)


S = [109,99,0,999,8]
mergesort(S)
print(S)

