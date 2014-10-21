import heapq

def loadgraph(filename, num, initd):
    file = open(filename)
    graph = {}
    for _i in range(num):
        linelist = file.readline().split()
        vert = int(linelist[0])

        if vert not in graph:
            graph[vert] = {
                'mind': initd,
                'nodes': []
            }

        for v in range(1, len(linelist)):
            vertice, weight = [int(x) for x in linelist[v].split(',')]
            graph[vert]['nodes'].append([vertice, weight])

    return graph


def dijkstra(initialv, initd, filename, num, printit=False):
    graph = loadgraph(filename, num, initd)
    outside = []
    for i in range(2, len(graph.keys())):
        outside.append([
            initd,
            {
                'vert': i,
                'pred': None
            }
        ])
    outside.append( [0, {
        'vert': 1,
        'pred': None
        }])
    graph[1]['mind'] = 0

    heapq.heapify(outside)
    finished = []
    while len(outside) != 0:
        minv = heapq.heappop(outside)
        try:
            while minv[0] != graph[minv[1]['vert']]['mind']:
                minv = heapq.heappop(outside)

            for vertex in graph[minv[1]['vert']]['nodes']:
                prediction = minv[0] + vertex[1]
                if  prediction <= graph[vertex[0]]['mind']:
                    graph[vertex[0]]['mind'] = prediction
                    heapq.heappush(outside, [prediction, {
                            'vert': vertex[0],
                            'pred': minv[1]['vert']
                        }])
            finished.append(minv)
        except:
            pass
    
    if printit:
        print('starting print')
        for vertex in finished:
            print(vertex[1]['vert'], graph[vertex[1]['vert']]['mind'])

    minimumdistances = {}
    for vertex in finished:
        minimumdistances[vertex[1]['vert']] = graph[vertex[1]['vert']]['mind']

    return minimumdistances

mindist = dijkstra(1, 1000000, 'dijkstraData.txt', 200)

report = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
reportstring = ""
for v in report:
    reportstring += str(mindist[v])
    if report.index(v) == len(report)-1:
        pass
    else:
        reportstring += ','
print(reportstring)
