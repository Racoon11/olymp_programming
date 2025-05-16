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
            
    def get_ans(self, k, l, r):
        zeros = self.get_zeros(0, l-1, 0, 0, self.N-1)
        index = self.get_ans_recursive(k + zeros, 0)
        if index > r:
            return -2
        else:
            return index

    def get_zeros(self, l_find, r_find, v, l, r):

        if r <= r_find and l >= l_find:
            return self.arr[v]
        elif r < l_find or l > r_find:
            return 0
        else:
            ans_left = self.get_zeros(l_find, r_find, 2*v+1, l, (l+r)//2)
            ans_right = self.get_zeros(l_find, r_find, 2*v+2, (l+r)//2+1, r)
            return ans_left + ans_right
        
    
    def get_ans_recursive(self, k, v):
        if v >= self.N - 1:
            return v - self.N + 1
        ch1 = 2 * v + 1
        ch2 = 2 * v + 2
        if self.arr[ch1] >= k:
            return self.get_ans_recursive(k, ch1)
        else:
            return self.get_ans_recursive(k - self.arr[ch1], ch2)
        
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
        print(st.get_ans(k, l-1, r-1) + 1, end=' ')
    else:
        ind, v = map(int, options)
        st.update_element(ind-1, v)
        
'''
N = randint(1, 200_000)
arr = [randint(0, 100_000) for i in range(N)]
arr = [arr[i] if i % 2 == 0 else 0 for i in range(N)]
st = segment_tree(arr, -1)

m = randint(1, 200_000)
for i in range(m):
    op = randint(0, 1)
    if op:
        l = randint(1, 200_000)
        r = randint(l, 200_000)
        k = randint(1, N)
        print(l, r, k)
        print(st.get_ans(k, l-1, r-1) + 1)
    else:
        ind = randint(1, N)
        v = 0
        st.update_element(ind-1, v)
        '''
