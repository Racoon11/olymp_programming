import sys
from collections import deque

def shortest_way(graph, start_vertex, end_vertex):
    ''' функция для определения кратчайшего пути между вершинами,
        используя поиск в ширину'''
    distances = {(i, j):None for i in range(1, N+1) for j in range(1, N+1)}
    distances[start_vertex] = 0
    queue = deque([start_vertex])

    parents = {(i, j):None for i in range(1, N+1) for j in range(1, N+1)}

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
    
    return path, distances[end_vertex]


N = int(sys.stdin.readline())

graph = {(i, j):[] for i in range(1, N+1) for j in range(1, N+1)}

for i in range(1, N+1):
    for j in range(1, N+1):
        dots = [(i+1, j+2), (i-1, j+2), (i+1, j-2), (i-1, j-2),
                (i+2, j+1), (i-2, j+1), (i+2, j-1), (i-2, j-1)]
        for dot in dots:
            if dot in graph:
                graph[(i,j)].append(dot)

start = list(map(int, sys.stdin.readline().split()))
start = (start[0], start[1])
end = list(map(int, sys.stdin.readline().split()))
end = (end[0], end[1])
sh = shortest_way(graph, start, end)

sys.stdout.write(str(sh[1]) + '\n')
for i in range(sh[1], -1, -1):
    sys.stdout.write(str(sh[0][i][0]) + " " + str(sh[0][i][1]) + '\n')
