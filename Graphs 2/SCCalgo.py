from sets import Set
from Queue import Queue
import random
import copy
import sys
from pprint import pprint
import cProfile

def setup(filename):
    file = open(filename)
    print('starting')

    graph = {}
    reversegraph = {}
    for line in file.readlines():
        line = line.split()
        line = [int(x) for x in line]
        one = line[0]
        two = line[1]
        if one not in graph:
            graph[one] = {
            'outgoing': [],
            'leader': None
            }
        graph[one]['outgoing'].append(two)
        if two not in graph:
            graph[two] = {
            'outgoing': [],
            'leader': None
            }

        if two not in reversegraph:
            reversegraph[two] = {
            'outgoing': [],
            'leader': None
            }
        reversegraph[two]['outgoing'].append(one)
        if one not in reversegraph:
            reversegraph[one] = {
                'outgoing': [],
                'leader': None
                }
    for i in graph.keys():
        graph[i]['outgoing'].sort()
    for i in reversegraph.keys():
        graph[i]['outgoing'].sort()

    return graph, reversegraph

def DFS(graph, order=None):
    # Using a set is critical for O(1) checks for visited. Using a list would result in several O(nlogn) operations.
    # Could also use an attribute in the graph dictionary for each vertice
    visited = Set()
    finish = []
    if order == None:
        order = graph.keys()
        # sorting is important for consistency
        order.sort()
    for i in order:
        if i not in visited:
            # print(i)
            vertex = i
            leader = i
            callstack = [vertex]
            # counter = 0
            while callstack:
                # if counter % 1000 == 0:
                #     print(len(callstack))
                vertex = callstack.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    callstack.append(vertex)
                    graph[vertex]['leader'] = leader
                    # graph[vertex]['outgoing'].sort()
                    for v in graph[vertex]['outgoing']:
                        if v not in visited:
                            callstack.append(v)
                else:
                    finish.append(vertex)

                # counter += 1
    return finish


def run(filename):
    graph, reversegraph = setup(filename)
    print('setupfinished')
    finishstack = []
    finalstack = []
    visited = DFS(reversegraph)
    # reverse allows iteration from start of array, which is the last node to finish.
    visited.reverse()
    print('second run')

    DFS(graph, visited)




    SCCcount = {}
    # pprint(graph)
    for vert in graph.keys():
        leader = graph[vert]['leader']
        if leader not in SCCcount:
            SCCcount[leader] = 1
        else:
            SCCcount[leader] += 1
    countlist = []
    for i in SCCcount:
        countlist.append(SCCcount[i])
    countlist.sort()
    countlist.reverse()
    # print(SCCcount)
    return countlist[:5]





# print(run('testscc.txt'))
# print(run('mediumDG.txt'))
print(run('SCCtest.txt'))

