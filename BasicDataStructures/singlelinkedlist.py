import nose
eq = nose.tools.eq_

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def nextnode(self):
        return self.next

    def returnvalue(self):
        return self.value

    def setnext(self, next):
        self.next = next

    def setvalue(self, value):
        self.value = value

class Linkedlist():
    def __init__(self, *args):
        self.head = None
        for value in args:
            self.head = Node(value, next = self.head)
            print(self.head.nextnode())

    def addnode(self, value):
        self.head = Node(value, next = self.head)

    def returnhead(self):
        return self.head.returnvalue()
    def nextelement(self, element):
        return element.nextnode()
    def returnelement(self, index):
        #if index == 0:
        #    print(self.head.returnvalue())
        #    return self.head.returnvalue()
        #elif index == 1:
        #    print(self.nextelement(self.head).returnvalue())
        #    return self.nextelement(self.head).returnvalue()
        #else:
        next = self.head
        for i in range(index):
            next = self.nextelement(next)
        return next.returnvalue()
    def reverse(self):
        current = self.head
        previous = None
        next1 = True
        while current:
            next1 = current.nextnode()
            current.setnext(previous)
            previous = current
            current = next1

        self.head = previous






#
#linklist = Linkedlist(10, 11, 12, 13, 14)
#
#for x in range(5):
#    print('---' + str(x))
#    print(linklist.returnelement(x))
#print('||')
#linklist.reverse()
#print('|||')
#for x in range(6):
#    print(x)
#    print(linklist.returnelement(x))

def test():
    linklist = Linkedlist(10, 11, 12, 13, 14)
    eq(linklist.returnelement(3), 11)
    eq(linklist.returnelement(4), 10)

    linklist.reverse()
    eq(linklist.returnelement(4), 14)





