def dfs(vertex, g, used):
    ''' функция поиска в глубину'''
    used.add(vertex)
    for neighbour in g[vertex]:
        if neighbour not in used:
            dfs(neighbour,g,used)

g = {}
for i in range(int(input())):
    a, b = map(int,input().split())
    g[a] = g.get(a,[])
    g[a].append(b)
    g[b] = g.get(b,[])
    g[b].append(a)

#подсчёт компонент связности:
used = set()
n = 0
for vertex in g:
    if vertex not in used:
        dfs(vertex,g,used)
        n+=1
print(n)
