# Adjacency list of form
# graph = {
#   (edgeNum): edge
# }
# edge = {
#   edges: list of [(edgeNum), (weight)],
#   dist: int (init as float("inf"))
# }
def bellford(graph, numV, source, dest):
  graph[source]['dist'] = 0
  for i in range(1, numV+1):
    for j in range(1, numV+1):
      for edge in graph[j]['edges']:
        graph[edge[0]]['dist'] = min(graph[edge[0]]['dist'], graph[j]['dist'] + edge[1]) 
  olddist = graph[dest]['dist']
  for j in range(1, numV+1):
    for edge in graph[j]['edges']:
      graph[edge[0]]['dist'] = min(graph[edge[0]]['dist'], graph[j]['dist'] + edge[1]) 
  newdist = graph[dest]['dist']
  if olddist == newdist:
    print(graph[dest], 'source to dest distance')
  else:
    print('negative cycle exists')

testGraph = {
  1: {
    'dist': float('inf'),
    'edges': [[2, -1], [3, 4]]
  },
  2: {
    'dist': float('inf'),
    'edges': [[4, 2], [5, 2], [3, 3]]
  },
  3: {
    'dist': float('inf'),
    'edges': []
  },
  4: {
    'dist': float('inf'),
    'edges': [[3, 5], [2, 1]]
  },
  5: {
    'dist': float('inf'),
    'edges': [[4, -3]]
  }
}
bellford(testGraph, 5, 1, 5)