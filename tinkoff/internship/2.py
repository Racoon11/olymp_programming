import sys

n, m = map(int, sys.stdin.readline().split())

matrix = [[0]*n for _ in range(m)]

for i in range(n-1, -1, -1):
    s = input().split()
    for j in range(m):
        matrix[j][i] = s[j]
for i in matrix:
    sys.stdout.write(' '.join(i) + '\n')
