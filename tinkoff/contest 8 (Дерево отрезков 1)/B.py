import sys

class SimpleSegmentTree:
    def build(self, node, L, R):
        if (L == R):
            self.ST[node] = [self.A[L], 1] # меняется
        else:
            mid = (L + R) // 2
            self.build(2 * node, L, mid)
            self.build(2 * node + 1, mid + 1, R)
            self.ST[node] = self.operation(self.ST[2 * node], self.ST[2 * node + 1])
        
            
    def __init__(self, A):
        self.n = len(A)
        self.A = A
        self.neutral = [float('inf'), 0] # нейтральный элемент нашей операции, меняется
        self.ST = [self.neutral for _ in range(4 * self.n)] 
        self.build(1, 0, self.n - 1) 
        
    def operation(self, x, y): # вот это меняется
        if x[0] < y[0]:
            return x
        if x[0] > y[0]:
            return y
        return [x[0], x[1] + y[1]]
        
    def query(self, l, r):
        return self.query_internal(1, 0, self.n - 1, l, r)
    
    def update(self, idx, val):
        return self.update_internal(1, 0, self.n - 1, idx, val)

    def update_internal(self, node, L, R, idx, val):
        if (L == R):
            self.A[idx] = val
            self.ST[node] = [val, 1] # меняется
        else:
            mid = (L + R) // 2
            if (L <= idx and idx <= mid):
                self.update_internal(2 * node, L, mid, idx, val)
            else:
                self.update_internal(2 * node + 1, mid + 1, R, idx, val)
            self.ST[node] = self.operation(self.ST[2 * node], self.ST[2 * node + 1])


    def query_internal(self, node, tl, tr, l, r):
        if (r < tl or tr < l):
            return self.neutral
        if (l <= tl and tr <= r):
            return self.ST[node]
        tm = (tl + tr) // 2
        return self.operation(self.query_internal(2 * node, tl, tm, l, r), self.query_internal(2 * node + 1, tm + 1, tr, l, r))


n, m = map(int, sys.stdin.readline().split())


cats = list(map(int, sys.stdin.readline().split()))

tree = SimpleSegmentTree(cats)

for i in range(m):
    op, i1, i2 = map(int, sys.stdin.readline().split())
    if (op == 1):
        tree.update(i1, i2)
    else:
        
        print(*tree.query(i1, i2-1))

