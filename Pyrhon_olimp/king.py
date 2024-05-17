n, m = map(int, input().split())
pole = [[1]+[0]*(m-1) for j in range(n)]
pole[0] = [1]*m
for i in range(1,n):
    for j in range(1,m):
        pole[i][j] = pole[i-1][j] + pole[i][j-1] 
for i in pole:
    print(*i)
