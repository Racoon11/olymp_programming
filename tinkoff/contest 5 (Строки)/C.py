import sys

class hasher:

    def __init__(self, t=37):
        self.s = ""
        self.t = t
        self.h = []
        self.h_three = []
        self.k_powers = [1]
        self.m = 10**9 + 7
        for k in range(100000):
            self.k_powers.append((self.k_powers[-1] * t) % self.m)

    def count_hash(self, s, k):
        self.s = s
        t = self.t
        n = len(s)
        self.h = [0] * (n+1)
        for i in range(n):
            self.h[i+1] = (self.h[i]*t + ord(s[i]))%self.m
            if (i+1) >= k:
                self.h_three.append(self.get_hash(i+1-(k-1),i+1))
        return self.h_three
            
    def get_hash(self, l, r):
        m = self.m
        return ((self.h[r] - self.h[l-1] * self.k_powers[r - l + 1]) % m + m) % m


a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip() 
k = len(b)
h = hasher(179)
hash_a = h.count_hash(a, k)
h = hasher(179)
hash_b = set(h.count_hash(b*2, k))
ans = 0
for i in hash_a:
    if (i in hash_b):
        ans += 1
print(ans)
