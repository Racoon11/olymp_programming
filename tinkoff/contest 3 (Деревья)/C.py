import sys
from collections import deque

def search(tree, start, n):
    queue = deque()
    queue.append(start)
    ans = {i:0 for i in range(n)}
    ans_paths = {i:[] for i in range(n)}
    while queue:
        cur = queue[0]
        for i in tree[cur]:
            ans[i] = ans[cur] + 1
            ans_paths[i] = ans_paths[cur][:]
            ans_paths[i].append(cur)
            queue.append(i)
        queue.popleft()
        ans_paths[cur].append(cur)
    return ans_paths, ans


n = int(sys.stdin.readline())

tree = {i:[] for i in range(n)}
temp = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    tree[temp[i-1]].append(i)

paths, lengths = search(tree, 0, n)

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    path1 = paths[a]
    path2 = paths[b]
    last = 0
    for i in range(min(lengths[a]+1, lengths[b]+1)):
        if (path1[i] == path2[i]):
            last = path1[i]
        else:
            break
    sys.stdout.write(str(last)+'\n')
    
