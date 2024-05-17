from collections import deque

def bfs(graph, start_vertex):
    ''' функция для обхода графа в ширину'''
    
    distances = [None] * n
    distances[start_vertex] = 0
    queue = deque([start_vertex])

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if distances[v] is None:
                queue.append(v)
                distances[v] = distances[cur_v]+1
    return distances


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
    
    return path


n, m = map(int,input().split())
graph = {i: set() for i in range(n)}
for i in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

print(shortest_way(graph,0,9))
print(bfs(graph,0))
