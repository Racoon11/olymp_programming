import sys
sys.setrecursionlimit(100001)
def check_tree(tree, n):
    if (tree[n] == (-1, -1)):
        return (True, 0, n, n)
    ans, deep, maxi = True, 0, n
    if (tree[n][0] != -1):
        left = tree[n][0]
        ans, deep, maxi, mini = check_tree(tree, left)
        if maxi >= n:
            return (False, -1, -1, -1)
    maxi = max(n, maxi)
    
    ans2, deep2, mini = True, 0, n
    if (tree[n][1] != -1):
        right = tree[n][1]
        ans2, deep2, maxi, mini = check_tree(tree, right)
        if mini <= n:
            return (False, -1, -1, -1)
    mini = min(n, mini)
    if (ans and ans2 and abs(deep - deep2) <= 1):
        return (True, max(deep, deep2)+1, maxi, mini)
    return (False, -1, -1, -1)


n, k = map(int, sys.stdin.readline().split())
tree = {i:(-1, -1) for i in range(n)}

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    tree[i] = (a, b)

sys.stdout.write(str(int(check_tree(tree, k)[0])))
