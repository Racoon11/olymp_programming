import sys


n = int(sys.stdin.readline())
forest = [sys.stdin.readline().strip() for _ in range(n)]

ans = [[-float('inf')]*5 for i in range(n+1)]

ans[0] = [0, 0, 0, 0, 0]

for i in range(1, n+1):
    for j in range(1, 4):
        ans[i][j] = max(ans[i-1][j-1], ans[i-1][j], ans[i-1][j+1])
        if forest[i-1][j-1] == 'W':
            ans[i][j] += -float('inf')
        elif forest[i-1][j-1] == 'C':
            ans[i][j] += 1
    if (all([ans[i][k] == -float('inf') for k in range(1, 4)])):
        finish = i-1
        break
else:
    finish = n
print(max(ans[finish]))
