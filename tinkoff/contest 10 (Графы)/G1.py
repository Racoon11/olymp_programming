import sys

class graph:

    def __init__(self, v):
        self.v = v
        self.adj = [list() for i in range(v)]

    def addEdge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def dijkstra(self, s, s2):
        d = [float('inf')] * self.v
        d[s] = 0
        a = [0] * self.v
        for j in range(self.v):
            v = -1
            for u in range(self.v):
                if (not(a[u]) and (v == -1 or d[u] < d[v])):
                    v = u;

            a[v] = True

            for i in self.adj[v]:
                u = i[0]
                w = i[1]
                if (d[u] > (d[v] + w)):
                    d[u] = d[v] + w
        return d[s2]

n, m = map(int, sys.stdin.readline().split())

g = graph(n)

for i in range(m):
    v1, v2, w = map(int, sys.stdin.readline().split())
    g.addEdge(v1-1, v2-1, w)

a, b, c = map(lambda x: int(x)-1, sys.stdin.readline().split())

one, two, three = g.dijkstra(a, b), g.dijkstra(b, c), g.dijkstra(a, c)
p1 = one + two
p2 = three + two
p3 = three + one
if (p1 == p2 == p3 == float('inf')): print(-1)
else:
    print(min(p1, p2, p3))

        
