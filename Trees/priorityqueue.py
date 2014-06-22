from binaryheap import BinHeap

class Item:
    def __init__(self, p, item):
        self.item = item
        self.p = p

    def __lt__(self, other):
        return self.p < other.p

# Takes a list of Item objects
class PQueue:
    def __init__(self, alist):
        self.heap = BinHeap()
        self.heap.buildheap(alist)

    def enqueue(self, p, item):
        self.heap.insert(Item(p, item))

    def dequeue(self):
        return self.heap.delmin()

