from binaryheap import BinHeap
import random
import timeit
def heapsort(alist):
    bin = BinHeap()
    bin.buildheap(alist)
    print('builtlist')
    res = []
    for i in range(len(alist)):
        # print(bin.delmin())
        # print(bin.heaplist)
        res.append(bin.delmin())

testlist = [random.randint(0, 1000) for x in range(10000)]
# O(nlogn) heapsort
# Builds heap in O(n), deletes min in O(logn) for each of n items
# n + nlogn
# print(testlist)
heapsort(testlist)