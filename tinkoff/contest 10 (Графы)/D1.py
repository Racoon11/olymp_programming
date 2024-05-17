from collections import deque
import sys
from time import time

class DisjSet: 
    def __init__(self, n): 
        self.a = [0] * n
        self.rank = [1] * n
        self.leftZero = [i for i in range(n)]
        self.rightZero = [i for i in range(n)]
        self.parent = [i for i in range(n)] 
  
    def find(self, x): 
        if (self.parent[x] != x): 
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x] 
  
    def nearestZero(self, i):
        p = self.find(i)
        lz = self.leftZero[p]
        rz = self.rightZero[p]
        if i - lz > rz - i:
            return rz
        return lz
    def nearestLeftZero(self, i):
        p = self.find(i)
        lz = self.leftZero[p]
        return lz
    def nearestRightZero(self, i):
        p = self.find(i)
        rz = self.rightZero[p]
        return rz
        
    # полезно переписать получше...
    def is_one(self, i):
        return self.a[i]
    
    def update(self, i):
        if self.a[i] == 1:
            return
        if i == 0:
            if self.a[i + 1] == 1:
                self.Union(i, i + 1)
                p = self.find(i + 1)
                self.leftZero[p] = -float('inf')
            else:
                self.rightZero[i] = i + 1
                self.leftZero[i] = -float('inf')
        elif i == len(self.a) - 1:
            if self.a[i - 1] == 1:
                self.Union(i, i - 1)
                p = self.find(i - 1)
                self.rightZero[p] = float('inf')
            else:
                self.leftZero[i] = i - 1
                self.rightZero[i] = float('inf')
        else:
            pl = self.find(i - 1)
            pr = self.find(i + 1)
            
            if self.a[i - 1] == 0 and self.a[i + 1] == 0:
                self.leftZero[i] = i - 1
                self.rightZero[i] = i + 1
            elif self.a[i - 1] == 1 and self.a[i + 1] == 1:
                self.Union(i - 1, i + 1)
            elif self.a[i - 1] == 1 and self.a[i + 1] == 0:
                self.Union(i, i - 1)
                p = self.find(i)
                self.rightZero[p] = i + 1
            elif self.a[i + 1] == 1 and self.a[i - 1] == 0:
                self.Union(i, i + 1)
                p = self.find(i)
                self.leftZero[p] = i - 1
                
        self.a[i] = 1
            
        
        
    def Union(self, x, y): 
        xset = self.find(x) 
        yset = self.find(y) 
        if xset == yset: 
            return
                
        if self.rank[xset] < self.rank[yset]: 
            self.parent[xset] = yset 
        elif self.rank[xset] > self.rank[yset]: 
            self.parent[yset] = xset 
        else: 
            self.parent[yset] = xset 
            self.rank[xset] = self.rank[xset] + 1
        pset = self.find(x)
        self.leftZero[pset] = min(self.leftZero[xset], self.leftZero[yset])
        self.rightZero[pset] = max(self.rightZero[xset], self.rightZero[yset])


def while_not_empty(v1, v2, a, d, h):
    global ds
    ondel = []
    while (v1):
        i = v1.popleft()
        if (i >= n+1 or i <= 0): continue
        if ds.is_one(i): continue
        r = ds.nearestRightZero(i+1)
        l = ds.nearestLeftZero(i-1)
        h[i] = a[r] + a[l]
        #print(i, r, l)
        if (d[i] - h[i]) < 0:
            
            ds.update(i)
            r = ds.nearestRightZero(i)
            l = ds.nearestLeftZero(i)
            #print('ondel: ', i, l, r)
            v2.append(l)
            v2.append(r)
            ondel.append(i)
        
    return len(ondel)
        

def game(n, a, d):
    global ds
    
    v1 = deque(range(1, n+1))
    v2 = deque()
    a = [0] + a + [0]
    d = [float('inf')] + d + [float('inf')]
    h = [0] * (n + 2)
    for i in range(n):
        #print(i)
        if v1:
            print(while_not_empty(v1, v2, a, d, h), end=' ')
        else:
            print(while_not_empty(v2, v1, a, d, h), end=' ')
        

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))
t = time()
ds = DisjSet(n + 2)
game(n, a, d)
