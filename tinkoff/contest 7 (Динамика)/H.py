import sys

n = int(sys.stdin.readline())

posl = list(map(int, sys.stdin.readline().split()))

ans = [1]*n
come = [-1 for i in range(n)]
maxi = 0
for i in range(1, n):
    for j in range(i):
        if (posl[i] > posl[j] and ans[i] < (ans[j] + 1)):
            ans[i] = ans[j] + 1
            come[i] = j
    if (ans[i] > ans[maxi]):
        maxi = i
print(ans[maxi])
cur = maxi
way = []
while (cur != -1):
    way.append(posl[cur])
    cur = come[cur]
print(*way[::-1])
