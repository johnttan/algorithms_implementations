def load(filename):
	file = open(filename)
	file.readline()
	edges = []
	vertices = {}
	for line in file.readlines():
		edgeList = [int(x) for x in line.split(' ')]
		if edgeList[0] not in vertices:
			vertices[edgeList[0]] = {
				'leader': edgeList[0]
			}
		if edgeList[1] not in vertices:
			vertices[edgeList[1]] = {
				'leader': edgeList[1]
			}
		edges.append(edgeList)

	# returns list of edges sorted by weight
	return sorted(edges, key=lambda edge: edge[2]), vertices
# Uses Union-Find to develop constant time cycle checks
# Merges clusters until numClusters left, then returns the spacing (min(distance between clusters))
# By pre-sorting in O(nlogn), guarantees speedy O(ElogE) greedy algo. Next edge weight up is the spacing. (Because the edges are processed in sorted order.)
def cluster(edges, vertices, numClusters):
	clusterLeaders = {}
	for edge in edges:
		leader1 = vertices[edge[0]]['leader']
		leader2 = vertices[edge[1]]['leader']
		if leader1 not in clusterLeaders:
			clusterLeaders[leader1] = [edge[0]]
		if leader2 not in clusterLeaders:
			clusterLeaders[leader2] = [edge[1]]
	def notCycle(edge):
		if vertices[edge[0]]['leader'] != vertices[edge[1]]['leader']:
			return True
		else:
			return False
	def merge(edge):
		leader1 = vertices[edge[0]]['leader']
		leader2 = vertices[edge[1]]['leader']
		if leader1 not in clusterLeaders:
			clusterLeaders[leader1] = [edge[0]]
		if leader2 not in clusterLeaders:
			clusterLeaders[leader2] = [edge[1]]
		if len(clusterLeaders[leader1]) > len(clusterLeaders[leader2]):
			clusterLeaders[leader1] += clusterLeaders[leader2]
			for vert in clusterLeaders[leader2]:
				vertices[vert]['leader'] = leader1
			del clusterLeaders[leader2]
		else:
			clusterLeaders[leader2] += clusterLeaders[leader1]
			for vert in clusterLeaders[leader1]:
				vertices[vert]['leader'] = leader2
			del clusterLeaders[leader1]

	MST = []
	done = False
	previous = False
	for ind, edge in enumerate(edges):
		if notCycle(edge):
			if done:
				return True, MST, clusterLeaders, edge[2]
			merge(edge)
			MST.append(edge)
		if len(clusterLeaders.keys()) == numClusters:
			# Check to make sure the next edge up isn't same weight.
			# If it is, need to merge it.
			done = True
			previous = edge

	return False, MST, clusterLeaders, False

# edges, vertices = load('testcluster.txt')
edges, vertices = load('clustering1.txt')
result, MST, clusters, spacing = cluster(edges, vertices, 4)

print(result, spacing)
# print(clusters)
# print(MST)
