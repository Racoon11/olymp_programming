from random import randint

class segment_tree:

    def __init__(self, arr, neutral=-1):
        i = 1
        while i < len(arr):
            i *= 2
        arr = arr + [neutral]*(i-len(arr))
        self.N = len(arr)
        self.neutral = neutral
        
        self.arr = [0] * (self.N-1) + arr
        self.count_tree()

    def count_tree(self):
        for node in range(len(self.arr) - self.N - 1, -1, -1):
            ch1 = 2 * node + 1
            ch2 = 2 * node + 2
            self.arr[node] = max(self.arr[ch1], self.arr[ch2])
            

    def get_ans(self, x, l_find, r_find, v, l, r):

        if r <= r_find and l >= l_find:
            if self.arr[v] < x:
                return -1, -2
            
        if r < l_find or l > r_find:
            return -1, -2

        if l == r and self.arr[v] >= x:
            return self.arr[v], l

        max_elem_left, pos = self.get_ans(x, l_find, r_find, 2*v+1, l, (l+r)//2)
        if pos != -2:
            return max_elem_left, pos
        max_elem_right, pos = self.get_ans(x, l_find, r_find, 2*v+2, (l+r)//2+1, r)
        if pos != -2:
            return max_elem_right, pos
        
        return max(max_elem_left, max_elem_right), -2
        
               
        
    def update_element(self, i, value):
        self.arr[self.N - 1 + i] = value
        parent = (self.N - 1 + i - 1) // 2
        self.update_tree(parent)

    def update_tree(self, v):
        self.arr[v] = max(self.arr[2*v + 1], self.arr[2*v + 2])
        if v != 0:
            self.update_tree((v-1)//2)
            

N, m = map(int, input().split())
arr = list(map(int, input().split()))

st = segment_tree(arr, -1)

for i in range(m):
    op, *options = input().split()
    
    if op == '1':
        ind, x = map(int, options)
        print(st.get_ans(x, ind-1, st.N-1, 0, 0, st.N-1)[1] + 1, end=' ')
    else:
        ind, v = map(int, options)
        st.update_element(ind-1, v)
        

