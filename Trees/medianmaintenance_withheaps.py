import heapq

def setup(filename):
    file = open(filename)
    stream = []
    for i in file.readlines():
        stream.append(int(i))
    stream.reverse()
    return stream

def run(filename):
    stream = setup(filename)
    hiheap = []
    loheap = []
    medians = []
    firstvalue = stream.pop()
    hiheap.append(firstvalue)
    medians.append(firstvalue)
    k = 2
    while len(stream) != 0:
        value = stream.pop()
        if value < hiheap[0]:
            heapq.heappush(loheap, value * -1)
        else:
            heapq.heappush(hiheap, value)
        if len(hiheap) - len(loheap) == 2:
            hivalue = heapq.heappop(hiheap)
            heapq.heappush(loheap, hivalue * -1)
        elif len(loheap) - len(hiheap) == 2:
            lovalue = heapq.heappop(loheap) * -1
            heapq.heappush(hiheap, lovalue)

        # print(loheap, hiheap, k)
        if k % 2 != 0:
            if len(loheap) > len(hiheap):
                medians.append(loheap[0] * -1)
            else:
                medians.append(hiheap[0])
        else:
            medians.append(loheap[0] * -1)
        k += 1
    summedians = sum(medians)
    # print(medians)
    print(summedians % 10000)

run('mediansdata.txt')