
import sys

def change(ind, value, place, n, l):
    global ans, ansL
    right = make_right(l, value)
    
    while place != right:
        value = ind[right[0]][right[1]]
        ind[right[0]][right[1]], ind[place[0]][place[1]] = ind[place[0]][place[1]], ind[right[0]][right[1]]
        #print(place[0], place[1], right[0], right[1])
        ansL[ans] = (place[0], place[1], right[0], right[1])
        ans += 1
        right = make_right(l, value)
    return ind
def make_right(l, value):
    if l == 'L':
        return (value[1], n - value[0] - 1)
    return (n - value[1] - 1, value[0])

n, L = sys.stdin.readline().split()
n = int(n)
[sys.stdin.readline() for i in range(n)]

ind = [[(j,i) for i in range(n)] for j in range(n)]
ans = 0
ansL = [0] * n**2
for i in range(n):
    for j in range(n):
        change(ind, ind[i][j], (i,j), n, L)
sys.stdout.write(str(ans) + '\n')
for i in range(ans):
    sys.stdout.write(' '.join(map(str, ansL[i])) + '\n')
    
