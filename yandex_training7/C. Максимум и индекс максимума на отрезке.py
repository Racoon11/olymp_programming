from math import log

class sparse_table:
    
    def __init__(self, arr):
        self.arr = arr
        self.N = len(arr)
        self.n_layers = int(log(self.N, 2)) + 1
        self.table = [[-1] * self.N for _ in range(self.n_layers)]
        self.count_table()
        self.count_steps()
        
    def count_table(self):
        self.table[0] = list(range(self.N))
        for i in range(1, self.n_layers):
            for j in range(self.N - 2**i + 1):
                self.table[i][j] = max(self.table[i-1][j], self.table[i-1][j+2**(i-1)],
                                       key=lambda x: self.arr[x])

    def count_steps(self):
        steps = [0] * (self.N+1)
        j = 0
        step = 1
        for i in range(1, self.N+1):
            if i >= step:
                j += 1
                step *= 2
            steps[i] = j-1
        self.steps = steps

    def answer(self, l, r):
        k = r - l + 1
        i = self.steps[k]
        #print(self.table[i])
        #print(l, r - 2**i, self.table[i][l], self.table[i][r - 2**i])
        return max(self.table[i][l], self.table[i][r - 2**i + 1], key=lambda x: self.arr[x])
        


N = int(input())
arr = list(map(int, input().split()))

st = sparse_table(arr)

k = int(input())
for i in range(k):
    l, r = map(int, input().split())
    ind = st.answer(l-1, r-1)
    print(st.arr[ind], ind + 1)
