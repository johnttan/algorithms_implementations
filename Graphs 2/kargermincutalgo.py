from sets import Set

import random
import copy

def setup(filename):
    file = open(filename)
    graph = {}
    for line in file.readlines():
        line = line.split()
        index = line.pop(0)
        graph[index] = line
    return graph
def mergevertices(graph, a, b):
    # removes b and replaces references to b with a if reference to a not already present
    # keeps vertice a
    # print(a, b)
    # print(graph)
    graph[a] = graph[a] + graph[b]
    # print(graph[a])
    for vert, adj in graph.iteritems():
        while b in adj:
            adj.remove(b)
            adj.append(a)
    # Removes self-loops
    for vert, adj in graph.iteritems():
        while vert in adj:
            adj.remove(vert)
    del graph[b]

def findmin(graph):
    mincut = 200**2
    # print(graph)
    for key in graph:
        if len(graph[key]) < mincut:
            mincut = len(graph[key])
    # print(mincut)
    return mincut


def algo(graph):
    while len(graph.keys()) > 2:
        a = random.sample(graph.keys(), 1)[0]
        # print(a, graph)
        b = random.sample(graph[a], 1)[0]
        mergevertices(graph, a, b)
    mincut = findmin(graph)
    return mincut

def run(cycles, filename):
    truegraph = setup(filename)
    mincut = len(truegraph.keys())**2
    for i in range(cycles):
        if i % 10:
            random.seed()
        print('test: {0}'.format(i))
        newgraph = copy.deepcopy(truegraph)
        tempmin = algo(newgraph)
        if tempmin < mincut:
            mincut = tempmin
    return mincut





print(run(100, 'kargerMinCut.txt'))