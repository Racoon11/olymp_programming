import sys

def z_func(pref, s):
    s = pref + '#' + s
    apchi = len(pref)
    n = len(s)
    z = [0]*n
    l = 0
    ans = []
    for i in range(1, n):
        z[i] = min(z[i - l], max(l + z[l] - i, 0))
    
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > l + z[l]:
            l = i
        if (z[i] == apchi):
            ans.append(i - apchi - 1)
    return ans



T = sys.stdin.readline().strip()

q = int(sys.stdin.readline())
for _ in range(q):
    s = sys.stdin.readline().strip()
    ans = z_func(s, T)
    print(len(ans), *ans)
    
    
