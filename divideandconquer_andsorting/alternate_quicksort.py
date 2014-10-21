import random

def pickpivot(ptype, A, l, r):
    if ptype == 'first':
        return l
    elif ptype == 'last':
        A[l], A[r] = A[r], A[l]
        return l
    elif ptype == 'median':
        middle = (l + r)//2 + 1
        qlist = [l, r, middle]
        qlist.sort()
        A[l], A[qlist[1]] = A[qlist[1]], A[l]
        return l

def partition(A, l, r, comparisons, ptype):
    if r - l < 0:
        return
    print(l, r)
    comparisons[0] += r - l
    pivot = pickpivot(ptype, A, l, r)
    j = r
    i = pivot + 1
    while j >= i:
        if A[i] > A[pivot] and A[j] <= A[pivot]:
            A[i], A[j] = A[j], A[i]
            j -= 1
        else:
            if A[j] > A[pivot]:
                j -= 1
            if A[i] <= A[pivot]:
                i += 1
    A[pivot], A[j] = A[j], A[pivot]
    
    partition(A, l, j-1, comparisons, ptype)
    partition(A, j+1, r, comparisons, ptype)
    return

def quicksort(A, ptype):
    comparisons = [0]
    partition(A, 0, len(A)-1, comparisons, ptype)
    return A, comparisons


file = open("hw2_test10.txt")
testarray1 = []
for line in file.readlines():
    testarray1.append(int(line.split()[0]))
# testarray = [4, 5, 1, 3, 10, 40, 20, 24, 34, 32, 23]
sortedarray = list(testarray1)
sortedarray.sort()
pivottype = 'first'
print(quicksort(testarray1, pivottype)[0] == sortedarray)
# print(quicksort(testarray1, pivottype)[0])
# print(quicksort(testarray1, pivottype)[1])



    


