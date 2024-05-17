
import sys


n, m = map(int, sys.stdin.readline().split())


ms = list(map(int, sys.stdin.readline().split())) * 2

ans1 = -1
ans2 = -1

for i in range(2**(m*2)):
    ansLoc = 0
    locN = []
    for j in range(2*m):
        if (i & 2**j):
            ansLoc += ms[j]
            locN.append(ms[j])
    if (ansLoc == n and ans2 == -1):
        ans1 = len(locN)
        ans2 = locN
    elif (ansLoc == n and ans1 > len(locN)):
        ans1 = len(locN)
        ans2 = locN
    elif (ansLoc > n and ans1 == -1):
        ans1 = 0
        
print(ans1)
if (ans1 not in [0, -1]):
    print(*ans2)
