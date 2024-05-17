

import sys
from collections import deque

n = int(sys.stdin.readline())
marks = list(map(int, sys.stdin.readline().split())) 

if (n < 7):
    print(-1)
else:
    queue = deque()
    stat = {i:0 for i in range(2, 6)}
    for i in range(6):
        elem = marks[i]
        stat[elem] += 1
        queue.append(elem)
    ans = -1
    for j in range(6, n):
        elem = marks[j]
        queue.append(elem)
        stat[elem] += 1
        if (stat[2] + stat[3]) == 0:
            ans = max(ans, stat[5])
        elem = queue.popleft()
        stat[elem] -= 1
    print(ans)
        
