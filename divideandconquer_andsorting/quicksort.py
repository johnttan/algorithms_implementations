import timeit
import random

def quicksort(presort, left, right):
    if left >= right:
        return
    # print('presort', presort, 'left', left, 'right', right)
    # Had problems with sorting lists with many duplicates when trying to use medians of 3 pivot selection method.
    # Pivot implemented with random.randint instead. Determines pivotindex first, then the pivot value.
    # This was probably due to using presort.index(pivot) to find pivotindex.
    # How to solve?
    if right-left >= 1:
        pivotindex = random.randint(left, right)
    else:
        if presort[left] > presort[right]:
            presort[right], presort[left] = presort[left], presort[right]
        else:
            presort[right], presort[left] = presort[left], presort[right]
        return

    pivot = presort[pivotindex]
    presort[left], presort[pivotindex] = presort[pivotindex], presort[left]
    pivotindex = left
    newleft = left
    newright = right
    foundleft = False
    foundright = False
    while newright >= newleft:
        if presort[newleft] > pivot:
            foundleft = True
        else:
            newleft += 1
        if presort[newright] < pivot:
            foundright = True
        else:
            newright -= 1
        if foundright and foundleft:
            presort[newleft], presort[newright] = presort[newright], presort[newleft]
            foundleft = False
            foundright = False

    presort[pivotindex], presort[newright] = presort[newright], presort[pivotindex]


    quicksort(presort, left, newright-1)
    quicksort(presort, newleft, right)



xlist = [random.randint(0, 5000) for x in range(10000)]
# # print(xlist)
# xlist2 = list(xlist)
# quicksort(xlist, 0, len(xlist)-1)
# # print(xlist)
# xlist2.sort()
# # print(xlist2)
# print(xlist == xlist2)

print(timeit.timeit('xlist.sort()', 'from __main__ import xlist', number = 100), 'native python sort. (Timsort)')
print(timeit.timeit('quicksort(xlist, 0, len(xlist)-1)', 'from __main__ import xlist, quicksort', number = 100), 'quicksort implementation')

# 10,000 item list of integers, 100 cycles. 3.65s vs .024s
# similar to mergesort implementation. 2 orders of magnitudes slower than native sort. O(nlogn) complexity