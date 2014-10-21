def load(filename):
	file = open(filename)
	nodes, bits = [int(x) for x in file.readline().split(' ')]
	vertices = {}
	for i in range(nodes):
		bitstring = ''.join(file.readline().split(' '))
		bitint = int(bitstring, 2)
		vertices[bitint] = True
	return vertices, bits
# Generates masks with hamming distance 1 and 2 for (n)bit ints. These will be XORed with the input vertices to produce their neighbors.
def generateMasks(n):
	masks1 = {}
	masks2 = {}
	start1 = 1
	for i in range(n):
		masks1[start1] = True
		start1 = start1 << 1 
	for mask in masks1.keys():
		for mask1 in masks1.keys():
			newMask = mask ^ mask1
			if newMask not in masks1 and newMask not in masks2:
				masks2[newMask] = True
	masks = list(masks1.keys()) + list(masks2.keys())
	# print(len(masks))
	return masks
# Generates a graph of all edges with weight hamming distance of 2 or less.
# Finds neighbors for each vertex by XORing with the masks.
def generateClustering(vertices, masks):
	found = {}
	graph = {}

	for vert in vertices.keys():
		for mask in masks:
			xored = vert ^ mask
			if xored in vertices:
				# print(xored, vert)
				if vert not in graph:
					graph[vert] = {xored: True}
				if xored not in graph:
					graph[xored] = {vert: True}
				graph[vert][xored] = True
				graph[xored][vert] = True

	return graph
# Runs DFS to find connected components (clusters)
def DFSclusters(graph):
	clusters = []
	found = {}
	for vert in graph.keys():
		DFSstack = []
		cluster = []
		if vert not in found:
			found[vert] = True
			DFSstack.append(vert)
			for adj in graph[vert].keys():
				if adj not in found:
					found[vert] = True
					DFSstack.append(adj)
			while len(DFSstack) > 0:
				vert = DFSstack.pop()
				for adj in graph[vert].keys():
					if adj not in found:
						DFSstack.append(adj)
				cluster.append(vert)
				found[vert] = True
			# print(cluster, 'cluster')
			clusters.append(cluster)
			cluster = []
	return len(clusters), clusters
vertices, bits = load('clustering_big.txt')
masks = generateMasks(bits)
graph = generateClustering(vertices, masks)
numClusters, clusters = DFSclusters(graph)
# print(vertices)
# print(treeEdges)
# print(clusters)
# print(graph)
print(numClusters)


# print([bin(x) for x in masks])

# 6118