import sys

class segment_tree:

    def __init__(self, arr, neutral=-1):
        i = 1
        while i < len(arr):
            i *= 2
        arr = arr + [neutral]*(i-len(arr))
        self.N = len(arr)
        self.neutral = neutral
        
        self.prefix = [0] * (self.N-1) + [1 if x == 0 else 0 for x in arr]
        self.suffix = [0] * (self.N-1) + [1 if x == 0 else 0 for x in arr]
        self.max_segm = [0] * (self.N-1) + [1 if x == 0 else 0 for x in arr]
        self.length = [0] * (self.N-1) + [1] * self.N
        self.count_tree()

    def count_tree(self):
        for node in range(len(self.max_segm) - self.N - 1, -1, -1):
            self.count_node(node)

    def count_node(self, node):
        ch1 = 2 * node + 1
        ch2 = 2 * node + 2
        self.length[node] = self.length[ch1] + self.length[ch2]
        self.max_segm[node] = max(self.max_segm[ch1], self.max_segm[ch2],
                            self.suffix[ch1] + self.prefix[ch2])
        
        self.suffix[node] = self.suffix[ch2]
        if self.length[ch2] == self.max_segm[ch2]:
            self.suffix[node] += self.suffix[ch1]
        self.prefix[node] = self.prefix[ch1]
        if self.length[ch1] == self.max_segm[ch1]:
            self.prefix[node] += self.prefix[ch2]       

    def get_ans(self, l_find, r_find, v, l, r):

        if r <= r_find and l >= l_find:
            return self.max_segm[v], self.prefix[v], self.suffix[v], self.length[v]
        elif r < l_find or l > r_find:
            return 0, 0, 0, 0
        else:
            segm_left, prefix_left, suffix_left, len_left = self.get_ans(l_find, r_find, 2*v+1, l, (l+r)//2)
            segm_right, prefix_right, suffix_right, len_right = self.get_ans(l_find, r_find, 2*v+2, (l+r)//2+1, r)
            segm = max(segm_left, segm_right, suffix_left+prefix_right)
            prefix = prefix_left
            if len_left == segm_left:
                prefix += prefix_right
            suffix = suffix_right
            if len_right == segm_right:
                suffix += suffix_left
            return segm, prefix, suffix, len_left+len_right
        
               
        
    def update_element(self, i, value):
        self.max_segm[self.N - 1 + i] = 1 if value == 0 else 0
        self.suffix[self.N - 1 + i] = 1 if value == 0 else 0
        self.prefix[self.N - 1 + i] = 1 if value == 0 else 0
        
        parent = (self.N - 1 + i - 1) // 2
        self.update_tree(parent)

    def update_tree(self, v):
        self.count_node(v)
        if v != 0:
            self.update_tree((v-1)//2)
            

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

st = segment_tree(arr, -1)

m = int(sys.stdin.readline())
for i in range(m):
    op, *options = sys.stdin.readline().split()
    
    if op == 'QUERY':
        l, r = map(int, options)
        sys.stdout.write(str(st.get_ans(l-1, r-1, 0, 0, st.N-1)[0]) + '\n')
    else:
        ind, v = map(int, options)
        st.update_element(ind-1, v)
        

