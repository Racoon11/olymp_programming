import sys
from collections import deque

def search(graph, i):

    if (not graph[i]): return {i}
    queue = deque()
    been = {i}
    queue.append(i)
    
    while queue:
        cur_v = queue.popleft()
        for i in graph[cur_v]:
            if i not in been:
                queue.append(i)
                been.add(i)
    return been
            

N, M = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

been = set()
components = []
n = 0
for i in range(1, N+1):
    if (i not in been):
        comp = search(graph, i)
        been |= comp
        n += 1
        components.append(comp)
    
sys.stdout.write(str(n) + '\n')
for i in components:
    sys.stdout.write(str(len(i)) + '\n')
    sys.stdout.write(' '.join(map(str, sorted(i))) + '\n')

    
    
