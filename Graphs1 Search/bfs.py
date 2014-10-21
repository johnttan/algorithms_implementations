from graphclass import Graph, Vertex
from queue import Queue

def bfs(g, start):
    vqueue = Queue()
    vqueue.put(start)
    while(vqueue.qsize() > 0):
        currentv = vqueue.get()
        for nbr in currentv.getconnections():
            if(nbr.color == '0'):
                nbr.color = 1
                nbr.distance = currentv.distance + 1
                nbr.predecessor = currentv
                vqueue.put(nbr)
            currentv.color = 2
def traverse(x):
    while (x.predecessor):
        print(x.getid())
        x = x.predecessor
    print(x.id)