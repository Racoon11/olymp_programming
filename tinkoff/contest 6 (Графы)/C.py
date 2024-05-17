import sys


n, m = map(int, sys.stdin.readline().split())
n = 10**5
m = 0

graph = {i:set() for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].add(j)

verts = list(map(int, sys.stdin.readline().split()))
#verts = list(range(1, 10**5+1))

for i in range(1, n):
    for j in range(i):
        if (verts[j] in graph[verts[i]]):
            print("NO")
            exit()
print("YES")
