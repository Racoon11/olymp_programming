import sys

n, m = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

right = [[0] * m for _ in range(n)]

for i in range(n):
    right[i][m-1] = (m - 1) if arr[i][m-1] == 0 else m
    for j in range(m-2, -1, -1):
        right[i][j] = j if arr[i][j] == 0 else right[i][j+1]

down = [[0] * m for _ in range(n)]
for j in range(m):
    down[n-1][j] = (n - 1) if arr[n-1][j] == 0 else n
    for i in range(n-2, -1, -1):
        down[i][j] = i if arr[i][j] == 0 else down[i+1][j]

ans = 1
ansCoord = (0, 0)
for i in range(n):
    for j in range(m):
        if (arr[i][j] == 0): continue
        cur = min(right[i][j] - j, down[i][j] - i)
        #print(i, j, right[i][j] - j, down[i][j] - j)
        if (cur >= ans):
            ans = cur
            ansCoord = (i+1, j+1)
print(ans)
print(*ansCoord)
        
