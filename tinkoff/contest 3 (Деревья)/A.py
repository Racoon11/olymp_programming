import sys
from collections import deque

def search(tree, start, n):
    queue = deque()
    queue.append(start)
    ans = {i:0 for i in range(n)}
    max_ans = 0
    while queue:
        cur = queue[0]
        for i in tree[cur]:
            ans[i] = ans[cur] + 1
            queue.append(i)
        max_ans = max(max_ans, ans[i])
        queue.popleft()
    return max_ans, ans

def search2(tree, start, n, parrents):
    queue = deque()
    queue.append(start)
    ans = {i:0 for i in range(n)}
    max_ans = 0
    was = set()
    while queue and (len(was) != n):
        cur = queue[0]
        for i in tree[cur] + parrents[cur]:
            if i in was: continue
            ans[i] = ans[cur] + 1
            max_ans = max(max_ans, ans[i])
            queue.append(i)
        queue.popleft()
        was.add(cur)
    return max_ans

n = int(sys.stdin.readline())

tree = {i:[] for i in range(n)}
parrents = {i:[] for i in range(n)}
temp = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    tree[temp[i-1]].append(i)
    parrents[i].append(temp[i-1])
    
max_ans, ans = search(tree, 0, n)
leaf = max([i for i in tree if (len(tree[i]) == 0)], key=lambda x:ans[x])
max2 = search2(tree, leaf, n, parrents)
sys.stdout.write(str(max_ans) + " " + str(max2) + '\n')
sys.stdout.write(' '.join(list(map(str, ans.values()))))


    
