class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.heapsize = 0

    def percup(self, i):
        while i //2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                self.heaplist[i//2], self.heaplist[i] = \
                self.heaplist[i], self.heaplist[i//2]
            i = i//2

    def percdown(self, i):
        while i*2 <= self.heapsize:
            mc = self.minC(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = \
                self.heaplist[mc], self.heaplist[i]
            i = mc
    def minC(self, i):
        if i*2+1 > self.heapsize:
            return i*2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1
    def insert(self, k):
        self.heaplist.append(k)
        self.heapsize += 1
        self.percup(self.heapsize)
    def delmin(self):
        val = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.heapsize]
        self.heapsize = self.heapsize - 1
        self.heaplist.pop()
        self.percdown(1)
        return val

    def buildheap(self, alist):
        i = len(alist) // 2
        self.heapsize = len(alist)-1
        self.heaplist = [0] + alist[:]
        while(i>0):
            self.percdown(i)
            i = i -1
# testheap = BinHeap()
# testheap.buildheap([1, 2, 34, 12, 23, 24, 34, 3, 5, 6, 23, 14, 23, 14, 15, 16, 34, 36])

# print(testheap.heaplist)
