import sys
from collections import deque


def shortest_way(graph, start_vertex, end_vertex):
    ''' функция для определения кратчайшего пути между вершинами,
        используя поиск в ширину'''
    
    distances = [None] * n
    distances[start_vertex] = 0
    queue = deque([start_vertex])

    parents = [None] * n

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if distances[v] is None:
                queue.append(v)
                distances[v] = distances[cur_v]+1

                parents[v] = cur_v
    path = [end_vertex]
    parent = parents[end_vertex]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]
    if (distances[end_vertex] == None): return -1
    return distances[end_vertex]



m = int(sys.stdin.readline())
i = 0
vertexes = {}
graph = {}
for _ in range(m):
    s, e = sys.stdin.readline().strip().split(' -> ')
    if (s not in vertexes):
        vertexes[i] = s
        vertexes[s] = i
        graph[i] = []
        s = i
        i += 1
    else:
        s = vertexes[s]
    if (e not in vertexes):
        vertexes[i] = e
        vertexes[e] = i
        e = i
        graph[i] = []
        i += 1
    else:
        e = vertexes[e]
    graph[s].append(e)

s = sys.stdin.readline().strip()
e = sys.stdin.readline().strip()
if (s == e):
    print(0)
elif (s not in vertexes or e not in vertexes):
    print(-1)
else:
    s = vertexes[s]
    e = vertexes[e]
    n = len(graph)
    print(shortest_way(graph, s, e))

    
    
    
