import random
import timeit

def bubblesort(presort):
    swapped = True
    passn = len(presort)-1
    while swapped and passn > 0:
        for i in range(passn):
            if presort[i] > presort[i+1]:
                presort[i], presort[i+1] = presort[i+1], presort[i]
        passn -= 1
    return presort


xlist = [random.randint(0, 500) for x in range(1000)]

print(timeit.timeit('bubblesort(xlist)', 'from __main__ import bubblesort, xlist', number=100), 'bubblesort')
print(timeit.timeit('xlist.sort()', 'from __main__ import  xlist', number=100), 'native python sort')
# Bubble sort O(n^2) effecient.
# Bubblesort does not converge in reasonable time for 10,000 items.
