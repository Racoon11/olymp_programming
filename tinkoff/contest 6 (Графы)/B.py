import sys
from collections import deque

def search(graph, i):

    if (not graph[i]): return {i}
    queue = deque()
    been = {i}
    queue.append(i)
    
    while queue:
        cur_v = queue.popleft()
        been.add(cur_v)
        for i in graph[cur_v]:
            if i in been:
                return False
            if i not in been:
                queue.append(i)
    return been
            
def deep_search(graph, cur, been=set()):
    for v in graph[cur]:
        if (v in been):
            return False
        return deep_search(graph, v, been | {v})
    return been


N, M = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)

been = set()


for i in range(1, N+1):
    if (i not in been):
        b = deep_search(graph, i)
        if (b == False):
            print(1)
            break
        been |= b
else: print(0)


    
    
