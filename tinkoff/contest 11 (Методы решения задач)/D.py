

import sys

L, N = map(int, sys.stdin.readline().split())

Cs = [0] + list(map(int, sys.stdin.readline().split())) + [L]

ans = [[0 for i in range(N+2)] for j in range(N+2)]

    
for ln in range(2, N+2):
    for i in range(N + 2 - ln):
        ans[i][i+ln] = Cs[i+ln] - Cs[i] + min(ans[i][k] + ans[k][i+ln]
                                              for k in range(i+1, i+ln))

print(ans[0][N+1])
