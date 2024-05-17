import sys
from collections import deque

def get_steps(i, j, F, n):
    ans = []
    if F == 'K':
        steps = [(i-2, j-1), (i-2, j+1), (i-1, j+2), (i+1, j+2),
                 (i+2, j+1), (i+2, j-1), (i+1, j-2), (i-1, j-2)]
        for i, j in steps:
            if (i < 0 or i >= n or j < 0 or j >= n):
                continue
            ans.append((i, j))
    elif F == 'G':
        steps = [(i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j),
                 (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]
        for i, j in steps:
            if (i < 0 or i >= n or j < 0 or j >= n):
                continue
            ans.append((i, j))
    return ans

n = int(sys.stdin.readline())

start = (0, 0)
finish = (0, 0)
field = [0 for _ in range(n)]
for i in range(n):
    s = input()
    if 'S' in s:
        start = (i, s.find('S'))
    if 'F' in s:
        finish = (i, s.find('F'))
    field[i] = list(s)
    
ans = {i: [[float('inf')]*n for _ in range(n)] for i in 'KG'}
ans['K'][start[0]][start[1]] = 0
queue = deque()
queue.append((start, 'K'))
while queue:
    last = queue.popleft()
    i, j = last[0][0], last[0][1]
    steps = get_steps(i, j, last[1], n)
    letter = last[1]
    for p, q in steps:
        update = ans[letter][i][j] + 1
        cur_letter = letter
        if (field[p][q] in '.SF'):
            pass
        elif (field[p][q] != cur_letter):
            cur_letter = field[p][q]
            field[p][q] = '.'
                
        if (ans[cur_letter][p][q] > update):
            ans[cur_letter][p][q] = update
            queue.append([(p, q), cur_letter])
p, q = finish[0], finish[1]
a = min(ans['G'][p][q], ans['K'][p][q])
if a == float('inf'):
    print(-1)
else:
    print(a)
            
        
        
