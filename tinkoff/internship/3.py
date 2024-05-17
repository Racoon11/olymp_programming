import sys

def deep(graph, vert, spaces=''):
    r = vert.rfind('/')
    if r == -1:
        sys.stdout.write(vert + '\n')
    else:
        sys.stdout.write(spaces + vert[r+1:] + '\n') 
    if vert not in graph: return
    for i in sorted(graph[vert]):
        deep(graph, vert + i, spaces + '  ')


n = int(sys.stdin.readline())

direct = {}
root = 'root'
for i in range(n):
    s = sys.stdin.readline().strip()
    r = s.rfind('/')
    if (r == -1):
        root = s
    else:
        direct[s[:r]] = direct.get(s[:r], [])
        direct[s[:r]].append(s[r:])
deep(direct, root)
