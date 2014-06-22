# Linear search for kth smallest number in a list.
import random
from timeit import Timer
import nose



def quicksearch(k, ls):
    #quickselect in linear time

    pindex = random.randint(0, len(ls)-1)
    pivot = ls[pindex]
    ls[len(ls)-1], ls[pindex] = pivot, ls[len(ls)-1]
    lcount = 0
    for i, num in enumerate(ls):
        if num <= pivot:
            # print(ls, pivot)
            # print(i)
            # print(lcount)
            ls[lcount], ls[i] = ls[i], ls[lcount]
            lcount += 1
    lcount -= 1
    # print(k, pivot, lcount, ls)
    if lcount == k:
        return pivot
    elif lcount < k:
        return quicksearch(k-lcount, ls[lcount:])
    else:
        return quicksearch(k, ls[:lcount])


# Sort then select
def sortselect(k, ls):
    # Python sort uses mergesort
    ls.sort()
    return ls[k]


ls = [random.randint(0, 1000) for x in range(1000)]
rvar = random.randint(0, len(ls)-1)
# print(ls)
# print(rvar)
# print(quicksearch(10, ls), 'linearesult')
# print(sortselect(10, ls), 'sortresult')
# ls.sort()
# print(ls)
# # """Test correctness"""
# print(quicksearch(rvar, ls) == sortselect(rvar, ls))


# """Test time efficiency"""
time1 = Timer("quicksearch(6, ls)", "from __main__ import quicksearch, ls")
time2 = Timer("sortselect(6, ls)", "from __main__ import sortselect, ls")

print("linear quickselect", time1.timeit(number=1000), "s")
print("linear sortselect", time2.timeit(number=1000), "s")
# Tremendous gains in efficiency for mergesort.