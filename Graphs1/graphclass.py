class Vertex:
    #0=white, 1=grey, 2=black
    def __init__(self, key, color=0, distance=0, predecessor=None ):
        self.id = key
        self.connections = {}
        self.color = color
        self.distance = distance
        self.predecessor = predecessor

    def addneighbor(self, nb, weight=0):
        self.connections[nb] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connections])

    def getconnections(self):
        return self.connections.keys()

    def getid(self):
        return self.id

    def getweight(self, nb):
        return self.connections[nb]

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numv = 0

    def addvertex(self, key):
        self.numv = self.numv + 1
        newvertex = Vertex(key)
        self.vertices[key] = newvertex
        return newvertex

    def getvertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def addedge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)

        self.vertices[f].addneighbor(self.vertices[t], cost)

    def getvertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

g = Graph()
for i in range(10):
    g.addvertex(i)

g.addedge(0,1,5)
g.addedge(0,5,2)
g.addedge(1,2,4)
g.addedge(2,3,9)
g.addedge(3,4,7)
g.addedge(3,5,3)
g.addedge(4,0,1)
g.addedge(5,4,8)
g.addedge(5,2,1)

for v in g:
    for w in v.getconnections():
        print(v.getid(), w.getid())
