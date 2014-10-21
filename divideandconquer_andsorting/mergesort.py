import random
import timeit

def merge(left, right):
    result = []
    if len(left) == 1:
        if left > right:
            return right + left
        else:
            return left + right
    else:
        while left or right:
            if not left:
                result.append(right.pop())
            elif (not right) or left[-1] > right [-1]:
                result.append(left.pop())
            else:
                result.append(right.pop())

    result.reverse()
    return result


def sort(alist, left, right):
    if left == right:
        return [alist[left]]
    else:
        right1 = left + (right-left)//2
        return merge(sort(alist, left, right1), sort(alist, right1+1, right))

alist = [random.randint(0, 10000) for x in range(10000)]

# sortedalist = list(alist)
# print(sort(alist, 0, len(alist)-1))
# sortedalist.sort()
# print(sort(alist, 0, len(alist)-1) == sortedalist)
# 3.6s vs .02s native sort. 10,000 item list, 100 runs
# Despite difference of 100x, still performs O(nlogn)
print(timeit.timeit('alist.sort()', 'from __main__ import alist, sort', number=100), 'python sort')
print(timeit.timeit('sort(alist, 0, len(alist)-1)', 'from __main__ import alist, sort', number=100), 'mergesort')