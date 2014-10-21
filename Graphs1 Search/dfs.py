from graphclass import Graph, Vertex

class DFSVertex(Vertex):
    def __init__():
        super().__init__()
        self.initialt = 0
        self.finalt = 0

Vertex = DFSVertex

class DFSGraph(Graph):
    def __init__():
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.color = 0
            vertex.predecessor = -1
        for vertex in self:
            if vertex.color == 0:
                self.dfsvisit(vertex)
    def dfsvisit(self, startv):
        startv.color = 1
        self.time += 1
        startv.initialt = self.time
        for nextv in startv.getconnections():
            if nextv.color == 0:
                nextv.predecessor = startv
                self.dfsvisit(nextv)

        startv.color = 2
        self.time += 1
        startv.finalt = self.time