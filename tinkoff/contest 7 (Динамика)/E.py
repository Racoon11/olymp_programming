


s1 = '1' + input()
s2 = '1' + input()


n = len(s1) - 1
m = len(s2) - 1
ans = [[j if i == 0 else i for i in range(m+1)] for j in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        ans[i][j] = min(ans[i-1][j-1]+1, ans[i-1][j]+1,
                        ans[i][j-1]+1, ans[i-1][j-1] if s1[i] == s2[j] else float('inf'))

        dp = ans[i-2][j-2] + 1
        if (s1[i] != s2[j-1]): dp += 1
        if (s1[i-1] != s2[j]): dp += 1
        ans[i][j] = min(ans[i][j], dp)

print(ans[-1][-1])
