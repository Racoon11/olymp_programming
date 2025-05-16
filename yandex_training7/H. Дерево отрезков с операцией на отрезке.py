import sys

class segment_tree:

    def __init__(self, arr, neutral=-1):
        i = 1
        while i < len(arr):
            i *= 2
        arr = arr + [neutral]*(i-len(arr))
        self.N = len(arr)
        self.neutral = neutral

        self.maximums = [-1] * (self.N-1) + arr
        self.promises = [0] * (self.N*2-1)
        self.treeL = len(self.maximums)
        self.count_tree()

    def count_tree(self):
        for node in range(len(self.maximums) - self.N - 1, -1, -1):
            self.count_node(node)

    def count_node(self, node):
        ch1 = 2 * node + 1
        ch2 = 2 * node + 2
        self.maximums[node] = max(self.maximums[ch1], self.maximums[ch2])

    def get_elem(self, l, r):
        return self.get_elem_recursive(l, r, 0, 0, self.N-1)

    def get_elem_recursive(self, l_find, r_find, v, l, r):
        self.update(v)
        if r <= r_find and l >= l_find:
            return self.maximums[v]
        elif r < l_find or l > r_find:
            return -1
        else:
            max_left = self.get_elem_recursive(l_find, r_find, 2*v+1, l, (l+r)//2)
            max_right = self.get_elem_recursive(l_find, r_find, 2*v+2, (l+r)//2+1, r)
            return max(max_left, max_right)
                      
        
    def update_element(self, i, value):
        self.maximums[self.N - 1 + i] = value        
        parent = (self.N - 1 + i - 1) // 2
        self.update_tree(parent)

    def update(self, v):
        self.maximums[v] += self.promises[v]
        if 2 * v + 1 < self.treeL:
            self.promises[2*v+1] += self.promises[v]
        if 2 * v + 2 < self.treeL:
            self.promises[2*v+2] += self.promises[v]
        self.promises[v] = 0
        
    def add_value(self, v, value):
        self.maximums[v] += value
        if 2 * v + 1 < self.treeL:
            self.promises[2*v+1] += value
        if 2 * v + 2 < self.treeL:
            self.promises[2*v+2] += value
        #self.update_tree(v) #??????

    def add(self, l, r, v):
        self.add_recursive(l, r, v, 0, 0, self.N-1)

    def add_recursive(self, l_find, r_find, value, v, l, r):
        self.update(v)
        if r <= r_find and l >= l_find:
            self.add_value(v, value)
            return self.maximums[v]
        elif r < l_find or l > r_find:
            return -1
        else:
            left_max = self.add_recursive(l_find, r_find, value, 2*v+1, l, (l+r)//2)
            right_max = self.add_recursive(l_find, r_find, value, 2*v+2,(l+r)//2+1,r)
            self.maximums[v] = max(left_max, right_max)
            return self.maximums[v]
            

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
    
    if op == 'm':
        l, r = map(int, options)
        sys.stdout.write(str(st.get_elem(l-1, r-1)) + ' ')
    else:
        l, r, v = map(int, options)
        st.add(l-1, r-1, v)
        

