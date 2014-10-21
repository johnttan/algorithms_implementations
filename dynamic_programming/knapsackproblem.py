import timeit
from pprint import pprint
# Solved

"""
Possible Improvements:
Optimize data structures for memory efficiency.
Reduce # of comparisons in loops.
Select O(1) operations for accessing/removing from lists.
"""
def solveknapsack(w, items, printed=False):
    lengthitems = len(items)
    items.insert(0, [0, 0])
    table = {}
    for i in range(0, lengthitems+1):
        table[i] = {}
        for z in range(0, w+1):
            table[i][z] = 0
    itemspicked = []
    for i in table.keys():
        if i == 0:
            for we in table[0].keys():
                table[i][we] = 0
        else:
            for we in table[0].keys():
                if items[i][1] <= we:
                    if items[i][0] + table[i-1][we-items[i][1]] > table[i-1][we]:
                        table[i][we] = items[i][0] + table[i-1][we - items[i][1]]
                    else:
                        table[i][we] = table[i-1][we]
                else:
                    table[i][we] = table[i-1][we]
    return table








itemslist = [[3, 2], [4, 3], [8, 4], [8, 5], [10, 9]]
# itemslist2 = [[4, 12], [2, 1], [6, 4], [1, 1], [2, 2]]
# itemslist3 = [[3, 2], [4, 3], [5, 4], [6, 5]]
# itemslist4 = [[50, 5], [49, 1], [10, 4]]
# solveknapsack(30, itemslist, True)
# solveknapsack(5, itemslist3, True)

# print timeit.timeit('solveknapsack(20, itemslist, False)', "from __main__ import solveknapsack, itemslist", number=100), 'knapsack'
# Solved
# O(nW) Loop through weights within loop through items.