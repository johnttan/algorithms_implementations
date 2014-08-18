import heapq
#  load() takes a filename and constructs an adjacency list representation of the graph in the file.
def load(fileName):
	file = open(fileName)
	graph = {}
	numNodes, numEdges = [int(x) for x in file.readline().split()]
	edges = []
	for i in range(1, numNodes+1):
		graph[i] = {}
	for edge in range(numEdges):
		edgeVector = ([int(x) for x in file.readline().split()])
		graph[edgeVector[0]][edgeVector[1]] = edgeVector[2]
		graph[edgeVector[1]][edgeVector[0]] = edgeVector[2]
		edgeVector = (edgeVector[2], edge, [edgeVector[1], edgeVector[2]])
		edges.append(edges)

	return graph, numNodes, numEdges, edges
# Prim's algo finds MST of connected graph with distinct edge weights
# This version uses O(ElogE) time. (E=# of edges) This is from the E extract-min operations on the heap, each taking ~2logE time. 
# (Traverse binary tree height twice due to percolations within heap)
def prim(graph, numNodes, edges):
	marked = {}
	minW = {}
	minHeap = []
	for i in range(1, numNodes+1):
		marked[i] = False
		minW[i] = float('inf')
	marked[1] = True

	MST = []
	MSTcost = 0
	# Init first vertex
	for otherV in graph[1]:
		heapq.heappush(minHeap, (graph[1][otherV], [1, otherV]))
		minW[otherV] = graph[1][otherV]

	# begin main loop for MST construction
	while len(minHeap) > 0:
		# print(marked)
		# print(minHeap)
		current = heapq.heappop(minHeap)
		node1 = current[1][0]
		node2 = current[1][1]
		weight = current[0]
		# print(current)
		# if vectors already in MST, skip
		if marked[node1] and marked[node2]:
			# print('skipped')
			continue
		elif marked[node1]:
			# print('node1')
			if weight <= minW[node2]:
				# print('add node2', node2)
				minW[node1] = weight
				marked[node2] = True
				MSTcost += weight
				MST.append(current)
# 				The (for otherV) loop iterates through nodes connected to the node that was just added to MST.
# 				Only adds nodes that span the cut between the current MST and the Graph minus MST
# 				This loop should probably be taken out. Adds extra time complexity to each loop.
# 				Some level of amortization as edges are pruned?
				for otherV in graph[node2]:
					# Only adds an edge if it's cheapest edge crossing cut to otherV. If it's not, it's not in MST due to Cut property. Would be pruned at later point.
					if not marked[otherV] and graph[node2][otherV] < minW[otherV]:
						heapq.heappush(minHeap, (graph[node2][otherV], [node2, otherV]))
# 		Not necessary to check node2 because MST can't have cycles.
	return MST, MSTcost

graph, numNodes, numEdges, edges = load('edges.txt')
MST, MSTcost = prim(graph, numNodes, edges)

# print(MST)
print(MSTcost)