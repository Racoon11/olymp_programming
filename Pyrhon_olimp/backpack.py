ms = [0]
cs = [0]
for i in range(int(input())):
    m,c = map(int, input().split())
    ms.append(m)
    cs.append(c)
M = int(input())
ans = [[0 for m in range(M)] for c in range(len(cs))]
for i in range(1,len(cs)):
    for w in range(1,M):
        ans[i][w] =  max(cs[i]+ans[i-1][w-ms[i]],ans[i-1][w]) if (w-ms[i])>=0 else ans[i-1][w]
for i in ans:
    print(*i)
