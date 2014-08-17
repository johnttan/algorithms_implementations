import bisect
def setup(filename):
    file = open(filename)
    # returns hashtable of integers
    table = {}
    for i in file.readlines():
        table[int(i)] = True

    return table

# def twosum(table, tablekeys, sumnum):
#     for key in tablekeys:
#         if sumnum-key in table:
#             print(sumnum, key)
#             return True
#     return False

def run(filename):
    table = setup(filename)

    found = {}

    listofnums = table.keys()
    listofnums.sort()
    for i in listofnums:
        low = bisect.bisect_right(listofnums, -10000-i)
        high = bisect.bisect_right(listofnums, 10000-i)
        for j in listofnums[low:high]:
            if j+i >= -10000 and j+i <= 10000:
                found[j+i] = True
                # print(j, i)

    print(len(found.keys()))

run('twosumtest.txt')
# 427