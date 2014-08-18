import heapq

def load(fileName):
	file = open(fileName)
	graph = {}
	numNodes, numEdges = [int(x) for x in file.readline().split()]
	for i in range(numNodes):
		graph[i] = {}
	for edge in range(numEdges):
		edgeVector = ([int(x) for x in file.readline().split()])
		graph[edgeVector[0]][edgeVector[1]] = edgeVector[2]
		graph[edgeVector[1]][edgeVector[0]] = edgeVector[2]

	return graph, numNodes, numEdges

def prim(graph, numNodes):
	X = {}
	Xnodes = [1]
	for i in range(1, numNodes+1):
		V[i] = True
		X[i] = False
	X[1] = True
	V[1] = False
	MST = []

edges, numNodes, numEdges = load('testprims.txt')
MST, MSTcost = prim(edges, numNodes)

print(MSTcost)