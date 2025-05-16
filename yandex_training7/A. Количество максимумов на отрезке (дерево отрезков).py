
class segment_tree:

    def __init__(self, arr, neutral):
        i = 1
        while i < len(arr):
            i *= 2
        arr = arr + [neutral]*(i-len(arr))
        self.N = len(arr)
        self.neutral = neutral
        
        self.arr = [neutral] * (self.N-1) + arr
        self.counts = [neutral] * (self.N-1) + self.N * [1]
        self.count_tree()

    def count_tree(self):
        for node in range(len(self.arr) - self.N - 1, -1, -1):
            ch1 = 2 * node + 1
            ch2 = 2 * node + 2
            self.arr[node], self.counts[node] = self.count_ans(self.arr[ch1],
                                                          self.counts[ch1],
                                                          self.arr[ch2],
                                                          self.counts[ch2])            
    def count_ans(self, m1, c1, m2, c2):
        if m1 == m2:
            return m1, c1+c2
        elif m1 > m2:
            return m1, c1
        else:
            return m2, c2
        
    def get_ans(self, l, r):
        return self.get_ans_recursive(l, r, 0, 0, self.N-1)
    
    def get_ans_recursive(self, l_find, r_find, v, l, r):
        
        if r <= r_find and l >= l_find:
            return (self.arr[v], self.counts[v])
        elif r < l_find or l > r_find:
            return (0, 0)
        else:
            ans_left = self.get_ans_recursive(l_find, r_find, 2*v+1, l, (l+r)//2)
            ans_right = self.get_ans_recursive(l_find, r_find, 2*v+2, (l+r)//2+1, r)
            return self.count_ans(*ans_left, *ans_right)
            
        
            

N = int(input())
arr = list(map(int, input().split()))

st = segment_tree(arr, 0)

k = int(input())
for i in range(k):
    l, r = map(int, input().split())
    print(*st.get_ans(l-1, r-1))

