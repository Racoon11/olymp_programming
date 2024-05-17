import sys


N = int(sys.stdin.readline())
k = 24*60*60
day = [0]*k

for _ in range(N):
    h1, m1, s1, h2, m2, s2 = map(int, sys.stdin.readline().split())
    n1 = h1*60*60 + m1*60 + s1
    n2 = h2*60*60 + m2*60 + s2
    if (n1 == n2):
        N -= 1
        continue
    if (n2 < n1):
        day[0] += 1
    day[n1] += 1
    day[n2] -= 1

ans = 0
cur = 0
for i in range(k):
    cur += day[i]
    if (cur == N):
        ans += 1
print(ans)
