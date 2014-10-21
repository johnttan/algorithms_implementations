import random
import timeit
from profilehooks import profile
# TODO
# Optimize Performance
# Implement string hashing
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key:
            self.data[hashvalue] = data
        else:
            next = self.rehash(hashvalue, len(self.slots))

            while self.slots[next] != None and self.slots[next] != key:
                next = self.rehash(hashvalue, len(self.slots))
            if self.slots[next] == None:
                self.slots[hashvalue] = key
                self.data[hashvalue] = data
            else:
                self.data[hashvalue] = data

    def hashfunction(self, key, size):
        return key*(key+3) % size

    def rehash(self, old, size, i):
        return (old+1+2**i)%size
    def get(self, key, diag=False):
        start = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start
        if diag:
            print(position)
        iteration = 0
        while self.slots[position] != None and not found and not stop:
            if diag:
                print(position)
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots), iteration)
                iteration += 1
                if position == start:
                    stop = True

        return data
    # @profile
    def put(self, key, data):
        if key == None:
            print('key = none')
        start = self.hashfunction(key, len(self.slots))
        stop = False
        position = start
        iteration = 0
        while self.slots[position] != None and not stop:
            position = self.rehash(position, len(self.slots), iteration)
            iteration += 1
            if position == start:
                self.size = self.size * 2
                newdata = list(self.data)
                newslots = list(self.slots)
                self.slots = [None] * self.size
                self.data = [None] * self.size
                for i in range(len(newslots)):
                    if newslots[i] != None:
                        self.put(newslots[i], newdata[i])
                position = self.hashfunction(key, len(self.slots))
                iteration = 0


        if self.slots[position] == None:
            stop = True
            self.slots[position] = key
            self.data[position] = data

        if self.slots[position] != self.data[position]:
            print('Failed put', key, data, position)

    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        return self.put(key, data)


def testhashtable():
    map = HashTable()
    for i in range(1000):
        r = random.randint(1, 10000)
        map[r] = r
        if map[r] != r:
            print('Failed', r, map[r])
            raise Exception
            map.get(r, True)

def testdict():
    testdict = {}
    for i in range(100000):
        r = random.randint(1, 100000)
        testdict[r] = r
        if testdict[r] != r:
            print('Failed', r, map[r])
            testdict[r]
testhashtable()
# Implementation much slower than native python dict for <1000 insertions and lookups?
# Becomes much faster at greater than 100,000 items.
# O(1) insertions and lookups
# Test is O(n) Runs 1 loop in O(1) for each of n items.
print(timeit.timeit('testhashtable()', 'from __main__ import testhashtable', number=100), 'hashtable')
print(timeit.timeit('testdict()', 'from __main__ import testdict', number=100),  'dict')
# print(map.slots)
# print(map.data)
