import sys

N, M, K = map(int, sys.stdin.readline().split())

sums = [[0]*(M+1) for _ in range(N)]

for i in range(N):
    s = list(map(int, sys.stdin.readline().split()))
    sums[i][0] = s[0]
    for j in range(1, M):
        sums[i][j] = sums[i][j-1] + s[j]

for i in range(K):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    s = 0
    for j in range(y1-1, y2):
        s += sums[j][x2-1] - sums[j][x1 - 2]
    print(s)
