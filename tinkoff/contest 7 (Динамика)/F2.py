import sys

n, m = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


ans = 1
ansCoord = (0, 0)
is_rec = [[0] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if (arr[i][j] == 0): continue
        cur = min(is_rec[i-1][j], is_rec[i][j-1], is_rec[i-1][j-1]) + 1
        is_rec[i][j] = cur
        #print(i, j, right[i][j] - j, down[i][j] - j)
        if (cur >= ans):
            ans = cur
            ansCoord = (i + 1 - (cur - 1), j + 1 - (cur-1))
print(ans)

print(*ansCoord)
