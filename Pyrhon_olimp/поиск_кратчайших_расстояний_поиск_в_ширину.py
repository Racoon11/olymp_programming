
from collections import deque

def shortest_distances(graph, start):
    '''поиск кратчайших путей до каждой вершины'''
    queue = deque([start])
    shorts = {i:sums+1 for i in graph}
    shorts[start] = 0
    while queue:
        last = queue.popleft()
        for neighbor,s in graph[last]:
            if shorts[neighbor] > shorts[last]+s:
                queue.append(neighbor)
                shorts[neighbor] = shorts[last]+s
    return shorts

    
n,m = map(int,input('Введите колличество вершин и ребер графа: ').split())
graph = {}
sums = 0
print("Введите ребра в формате: 'первая вершина' 'вторая вершина' 'вес ребра' ")
for j in range(m):
    v1,v2,s = input().split()
    graph[v1] = graph.get(v1,[])
    graph[v1].append((v2,int(s)))
    graph[v2] = graph.get(v2,[])
    graph[v2].append((v1,int(s)))
    sums+=int(s)


start = input('С какой начать? ')
shorts = shortest_distances(graph, start)

end = input('До какой вершины? ')
way = shorts[end]
ans = [end]
while way!= 0:
    '''получение кратчайшего пути из списка кратчайших'''
    for v,s in graph[end]:
        if way - s == shorts[v]:
            way-=s
            end = v
            ans.append(v)
            break
print(*ans[::-1])
            
