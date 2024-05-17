import sys
from collections import deque

def search(graph, i):

    queue = deque()
    been = {i}
    queue.append(i)
    
    while queue:
        cur_v = queue.popleft()
        been.add(cur_v)
        for i in graph[cur_v]:
            if (vs[cur_v] > vs[i]):
                return False
            if i not in been:
                queue.append(i)
    return been


n, m = map(int, sys.stdin.readline().split())

graph = {i:set() for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].add(j)

verts = list(map(int, sys.stdin.readline().split()))
vs = {}
for i in range(n):
    vs[verts[i]] = i

    
been = set()
for i in range(1, n+1):
    if (i not in been):
        b = search(graph, i)
        if (b == False):
            print("NO")
            break
        been |= b
else:
    print("YES")
        
