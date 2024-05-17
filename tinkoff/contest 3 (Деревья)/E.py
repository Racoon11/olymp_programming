import sys

class heap:

    def __init__(self):
        self.h = []
        self.n = -1

    def get_max(self):
        return self.h[0]

    def insert(self, a):
        self.h.append(a)
        self.n += 1
        parrent = (self.n - 1)//2
        ind = self.n
        while (a < self.h[parrent]):
            self.h[ind], self.h[parrent] = self.h[parrent], self.h[ind]
            ind = parrent
            if (ind == 0):
                break
            parrent = (ind - 1)//2
            
    def remove_top(self):
        h = self.h
        h[0], h[-1] = h[-1], h[0]
        h.pop()
        self.n -= 1
        if not h: return 0
        elem = h[0]
        child1, child2 = 1, 2
        ind = 0
        children = [child for child in [child1, child2] if child <= self.n]
        while any([h[child] < h[ind] for child in children]):
            child = min(children, key = lambda x: h[x])
            h[child], h[ind] = h[ind], h[child]
            ind = child
            child1, child2 = ind*2 + 1, ind*2 + 2
            children = [child for child in [child1, child2] if child <= self.n]
            
        
    def print(self):
        print(self.h, self.n)
        

n = int(sys.stdin.readline())
heapy = heap()
a = list(map(int, sys.stdin.readline().split()))
for i in a:
    heapy.insert(i)
for i in range(n):
    sys.stdout.write(str(heapy.get_max()) + " ")
    heapy.remove_top()
        
