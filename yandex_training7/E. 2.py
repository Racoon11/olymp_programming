from random import randint

class segment_tree:

    def __init__(self, arr, neutral=-1):
        i = 1
        while i < len(arr):
            i *= 2
        arr = arr + [neutral]*(i-len(arr))
        self.N = len(arr)
        self.neutral = neutral
        
        self.arr = [0] * (self.N-1) + [1 if x == 0 else 0 for x in arr]
        self.count_tree()

    def count_tree(self):
        for node in range(len(self.arr) - self.N - 1, -1, -1):
            ch1 = 2 * node + 1
            ch2 = 2 * node + 2
            self.arr[node] = self.arr[ch1] + self.arr[ch2]
            

    def get_zeros(self, k, l_find, r_find, v, l, r):

        if r <= r_find and l >= l_find:
            if self.arr[v] == 0 or self.arr[v] < k:
                return self.arr[v], -2
            
        if r < l_find or l > r_find:
            return 0, -2
        if l == r and self.arr[v] == 1 and k == 1:
            return self.arr[v], l

        left_zeros, pos = self.get_zeros(k, l_find, r_find, 2*v+1, l, (l+r)//2)
        if pos != -2:
            return left_zeros, pos
        k -= left_zeros
        right_zeros, pos = self.get_zeros(k, l_find, r_find, 2*v+2, (l+r)//2+1, r)
        if pos != -2:
            return right_zeros, pos
        
        return left_zeros + right_zeros, -2
        
               
        
    def update_element(self, i, value):
        self.arr[self.N - 1 + i] = 1 if value == 0 else 0
        parent = (self.N - 1 + i - 1) // 2
        self.update_tree(parent)

    def update_tree(self, v):
        self.arr[v] = self.arr[2*v + 1] + self.arr[2*v + 2]
        if v != 0:
            self.update_tree((v-1)//2)
            

N = int(input())
arr = list(map(int, input().split()))

st = segment_tree(arr, -1)

m = int(input())
for i in range(m):
    op, *options = input().split()
    
    if op == 's':
        l, r, k = map(int, options)
        print(st.get_zeros(k, l-1, r-1, 0, 0, st.N-1)[1] + 1, end=' ')
    else:
        ind, v = map(int, options)
        st.update_element(ind-1, v)
        

