import sys

class Tree:

    def __init__(self, arr, n):
        self.arr = arr
        self.tree = [0]*(4*n)
        self.n = n
        self.count_tree(0, 0, n)

    def count_tree(self, i, L, R):
        if (R == (L+1)):
            self.tree[i] = self.arr[L]
        else:
            mid = (L+R)//2
            self.count_tree(i*2+1, L, mid)
            self.count_tree(i*2+2, mid, R)
            self.tree[i] = self.tree[i*2+1] + self.tree[i*2+2]

    def update(self, v, j, i=0, L=0, R=None):
        if (R == None): R = self.n
        if (L == j and L == (R-1)):
            self.tree[i] = v
        else:
            mid = (L+R)//2
            if (j < mid):
                self.update(v, j, i*2+1 , L, mid)
            else:
                self.update(v, j, i*2+2, mid, R)
            self.tree[i] = self.tree[i*2+1] + self.tree[i*2+2]

    def count(self, r, l, R=None, L=0, i=0):
        if (R == None): R = self.n
        if (L >= l and R <= r):
            return self.tree[i]
        if (r < L or R < l):
            return 0
        mid = (R + L) // 2
        return self.count(r, l, L, mid, i*2+1) + self.count(r, l, mid, R, i*2+2)


n, m = map(int, sys.stdin.readline().split())


cats = list(map(int, sys.stdin.readline().split()))

tree = Tree(cats, n)
