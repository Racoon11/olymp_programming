ans = 0
def split(a):
    if (len(a) == 1):
        return a
    k = len(a) // 2
    return merge(split(a[:k]), split(a[k:]))

def merge(a, b):
    global ans
    c = []
    k1 = k2 = 0
    while (k1 < len(a) and k2 < len(b)):
        if (a[k1] <= b[k2]):
            c.append(a[k1])
            k1 += 1
        else:
            ans += (len(a) - k1)
            c.append(b[k2])
            k2 += 1
    if (k1 < len(a)):
        c += a[k1:]
    if (k2 < len(b)):
        c += b[k2:]
    return c

n = int(input())
s = list(map(int, input().split()))
s2 = split(s)
print(ans)
print(*s2)
