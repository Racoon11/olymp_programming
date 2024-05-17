import sys

n = int(sys.stdin.readline())

mas = list(map(int, sys.stdin.readline().split()))
sums = [0]*(n+1)
xors = [0]*(n+1)
xors[0] = sums[0] = mas[0]

for i in range(1, n):
    sums[i] = sums[i-1] + mas[i]
    xors[i] = xors[i-1] ^ mas[i]

m = int(sys.stdin.readline())
for i in range(m):
    q, l, r = map(int, sys.stdin.readline().split())
    if (q == 1):
        print(sums[r-1] - sums[l-2])
    else:
        print(xors[r-1] ^ xors[l-2])
