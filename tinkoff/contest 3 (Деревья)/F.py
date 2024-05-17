import sys

class tree:

    def __init__(self):
        self.max = -1
        self.arr = dict()
        self.top = -1
        self.n = 0

    def add(self, el):
        self.max = max(self.max, el)
        if (self.top == -1):
            self.arr[el] = [-1, -1]
            self.top = el
            return
        if (el in self.arr):
            return
        child = self.top
        prev = self.top
        while child != -1:
            prev = child
            if (child == el):
                self.n -= 1
                break
            elif (child > el):
                child = self.arr[child][0]
            else:
                child = self.arr[child][1]
        if (el < prev):
            self.arr[prev][0] = el
        else:
            self.arr[prev][1] = el
        self.arr[el] = [-1, -1]
        self.n += 1

    def get_cl(self, el):
        ind = self.top
        ans = -1
        if (self.max < el):
            return -1
        while 1:
            if (ind == -1):
                break
            elif (el == ind):
                return el
            elif (el < ind):
                ans = ind
                ind = self.arr[ind][0]
            else:
                ind = self.arr[ind][1]
        return ans
    def print(self):
        print(self.arr)
            


n = int(sys.stdin.readline())
prev = 0
y = 0
tre = tree()
for _ in range(n):
    req, i = sys.stdin.readline().split()
    i = int(i)
    
    if (req == '+'):
        ell = i
        if (prev):
            ell = (i+y)%10**9
        tre.add(ell)
        prev = 0
    else:
        y = tre.get_cl(i)
        sys.stdout.write(str(y) + '\n')
        prev = 1
