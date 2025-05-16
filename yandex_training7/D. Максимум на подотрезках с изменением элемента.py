
class segment_tree:

    def __init__(self, arr, neutral):
        i = 1
        while i < len(arr):
            i *= 2
        arr = arr + [neutral]*(i-len(arr))
        self.N = len(arr)
        self.neutral = neutral
        
        self.arr = [neutral] * (self.N-1) + arr
        self.count_tree()

    def count_tree(self):
        for node in range(len(self.arr) - self.N - 1, -1, -1):
            ch1 = 2 * node + 1
            ch2 = 2 * node + 2
            self.arr[node] = max(self.arr[ch1], self.arr[ch2])
            
    def get_ans(self, l, r):
        return self.get_ans_recursive(l, r, 0, 0, self.N-1)
    
    def get_ans_recursive(self, l_find, r_find, v, l, r):
        
        if r <= r_find and l >= l_find:
            return self.arr[v]
        elif r < l_find or l > r_find:
            return 0
        else:
            ans_left = self.get_ans_recursive(l_find, r_find, 2*v+1, l, (l+r)//2)
            ans_right = self.get_ans_recursive(l_find, r_find, 2*v+2, (l+r)//2+1, r)
            return max(ans_left, ans_right)
        
    def update_element(self, i, value):
        self.arr[self.N - 1 + i] = value
        parent = (self.N - 1 + i - 1) // 2
        self.update_tree(parent)

    def update_tree(self, v):
        self.arr[v] = max(self.arr[2*v + 1], self.arr[2*v + 2])
        if v != 0:
            self.update_tree((v-1)//2)
            

N = int(input())
arr = list(map(int, input().split()))

st = segment_tree(arr, 0)

k = int(input())
for i in range(k):
    op, l, r = input().split()
    l, r = int(l), int(r)
    if op == 's':
        print(st.get_ans(l-1, r-1), end=' ')
    else:
        st.update_element(l-1, r)

