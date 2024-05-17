

n, m = map(int, input().split())

ans = [[0 for i in range(m+2)] for j in range(n+2)]

ans[1][1] = 1
k = 2
while (k <= m):
    i = k
    j = 1
    while ((i >= 1) and (j <= n)):
        ans[j][i] = ans[j-2][i+1] + ans[j-2][i-1] + ans[j-1][i-2] + ans[j+1][i-2]
        j += 1
        i -= 1
    k += 1
k = 2
while (k <= n):
    i = m
    j = k
    while ((j <= n) and (i >= 1)):
        ans[j][i] = ans[j-2][i+1] + ans[j-2][i-1] + ans[j-1][i-2] + ans[j+1][i-2]
        j += 1
        i -= 1
    k += 1

print(ans[n][m])
        
