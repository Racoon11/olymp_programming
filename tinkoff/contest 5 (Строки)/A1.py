import sys

class hasher:

    def __init__(self, t=37):
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
    

s = sys.stdin.readline()
k = 179

g = int(sys.stdin.readline())
my_hasher = hasher(k)
my_hasher.count_hash(s)
    
for _ in range(g):
    a, b, c, d = map(int, sys.stdin.readline().split())
    h1 = my_hasher.get_hash(a, b)
    h2 = my_hasher.get_hash(c, d)
    if (h1 == h2):
        sys.stdout.write("Yes" + '\n')
    else:
        sys.stdout.write("No" + '\n')
