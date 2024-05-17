n = int(input())
ns = list(map(int, input().split()))
s = sum(ns)
if (s%2 != 0):
    print("NO")
    exit()
s2 = s//2
ans = [[0 for _ in range(s2 + 1)] for _ in range(s2+1)]
ans[0][0] = -1
for k in ns:
    for i in range(s2, -1, -1):
        for j in range(s2, -1, -1):
            if (ans[i][j] == 0):
                if (i - k >= 0) and (ans[i-k][j] != 0):
                    ans[i][j] = k
                elif (j - k >= 0) and (ans[i][j-k] != 0):
                    ans[i][j] = -k
    
if (ans[-1][-1] != 0): print("YES")
else: print("NO")
