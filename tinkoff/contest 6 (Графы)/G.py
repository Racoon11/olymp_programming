import sys

def deikstra(matrix, start_vert, n):
    ans = {i:float('inf') for i in range(1,n+1)}
    ans[start_vert] = 0
    been = set(range(1, n+1))
    while (len(been) != 0):
        i = min(been, key=lambda x: ans[x])
        been -= {i}
        for j in range(1, n+1):
            ans[j] = min(ans[j], ans[i] + matrix[i][j])
    return max([ans[i] for i in range(1, n+1)])
        



n, m = map(int, sys.stdin.readline().split())
matrix = [[float('inf') for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    s, e, v = map(int, sys.stdin.readline().split())
    matrix[s][e] = v
    matrix[e][s] = v
ans = float('inf')
ansTown = 0
for i in range(1, n+1):
    d = deikstra(matrix, i, n)
    if (ans > d):
        ans = d
        ansTown = i
print(ansTown)


    
