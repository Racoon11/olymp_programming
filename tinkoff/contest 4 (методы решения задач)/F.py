import sys

def addToCoords(l, p):
    
    coords[l] = coords.get(l, 0) + p

n = int(sys.stdin.readline())
coords = dict()
for i in range(n):
    l, r = map(int, sys.stdin.readline().split())
    addToCoords(l, 1)
    addToCoords(r, -1)

parts = sorted(coords)
cur = coords[parts[0]]
ans = 0
for i in range(1, len(parts)):
    if (cur > 0):
        ans += (parts[i] - parts[i-1])
    cur += coords[parts[i]]
print(ans)
