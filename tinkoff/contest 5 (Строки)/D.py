import sys

a = sys.stdin.readline().strip()
k = len(a)
a = a*2
ans = a[:k]
for i in range(1, k):
    s2 = a[i:k+i]
    if (s2 < ans):
        ans = s2
print(ans)

