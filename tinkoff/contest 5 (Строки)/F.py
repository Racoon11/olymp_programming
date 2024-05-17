import sys
from time import time

class hasher:

    def __init__(self, t=179):
        self.s = ""
        self.t = t
        self.h = []
        self.k_powers = [1]
        self.m = 10**9 + 7
        for k in range(100000):
            self.k_powers.append((self.k_powers[-1] * t) % self.m)

    def count_hash(self, s):
        self.s = s
        t = self.t
        n = len(s)
        self.h = [0] * (n+1)
        for i in range(n):
            self.h[i+1] = (self.h[i]*t + ord(s[i]))%self.m
            
    def get_hash(self, l, r):
        m = self.m
        return ((self.h[r] - self.h[l-1] * self.k_powers[r - l + 1]) % m + m) % m

s = sys.stdin.readline().strip()
s = 'a'*10**5
t = time()
n = len(s)
h = hasher()
h.count_hash(s)
h2 = hasher()
h2.count_hash(s[::-1])
ans = n

for left in range(1,n+1):
    for right in range(left+1, n+1):
        r = h.get_hash(left, right)
        l = h2.get_hash(n - (right-1), n - (left - 1))
        if (r == l):
            ans += 1
print(ans)
print(time()-t)
            
