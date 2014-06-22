import random

def pickpivot(ptype, A, l, r):
    if ptype == 'first':
        return l
    elif ptype == 'last':
        A[l], A[r] = A[r], A[l]
        return l
    elif ptype == 'median':
        if (l-r)%2 == 0:
            middle = (l+r)//2
        else:
            middle = (l+r)//2 + 1
        qlist = [l, r, middle]
        qlist.sort()
        A[l], A[qlist[1]] = A[qlist[1]], A[l]
        return l

def partition(A, l, r, comparisons, ptype):
    if r - l < 0:
        return
    comparisons[0] += r - l
    # print(l, r)
    pivot = pickpivot(ptype, A, l, r)
    j = r
    i = pivot + 1

    for j in range(pivot + 1, r+1):
        if A[j] <= A[pivot]:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[pivot], A[i-1] = A[i-1], A[pivot]
    partition(A, l, i-2, comparisons, ptype)
    partition(A, i, r, comparisons, ptype)
    return

def quicksort(A, ptype):
    comparisons = [0]
    partition(A, 0, len(A)-1, comparisons, ptype)
    return A, comparisons


file = open("testcases.txt")
testarray1 = []
for line in file.readlines():
    testarray1.append(int(line.split()[0]))
# testarray = [4, 5, 1, 3, 10, 40, 20, 24, 34, 32, 23]
sortedarray = list(testarray1)
sortedarray.sort()
pivottype = 'last'
# print(quicksort(testarray1, pivottype)[0] == sortedarray)
# print(quicksort(testarray1, pivottype)[0])
print(quicksort(testarray1, pivottype)[1])



    


