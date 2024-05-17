import math
from collections import deque
import sys

class LCA:
    def __init__(self, parents): # граф будем передавать как массив предков для всех вершин, у нулевой будет она сама
        self.n = len(parents)
        self.max_deg = math.ceil(math.log(self.n, 2)) # максимальная интересующая нас степень двойки
        self.dp = [[0] * (self.max_deg + 1) for _ in range(self.n)] # массив двоичных подъемов
        for i in range(self.n):
            self.dp[i][0] = parents[i]
            
        # считаем динамику
        for j in range(1, self.max_deg):
            for i in range(self.n):
                self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]
        
        self.d = self.bfs(parents)
        # для подсчета нужно еще посчитать глубину каждой вершины, мне лень это делать, 
        # поэтому просто вобьем для нужного графа
        
            
    def bfs(self, parents):
        ''' функция для обхода графа в ширину'''
        start_vertex = 0
        graph = {i : [] for i in range(self.n)}
        for i in range(self.n):
            graph[parents[i]].append(i)
            
        distances = [None] * self.n
        distances[start_vertex] = 0
        queue = deque([start_vertex])

        while queue:
            cur_v = queue.popleft()
            for v in graph[cur_v]:
                if distances[v] is None:
                    queue.append(v)
                    distances[v] = distances[cur_v]+1
        return distances    
        

    def query(self, u, v):
        if self.d[v] > self.d[u]: # Для удобства будем считать, что u глубже
            u, v = v, u
            
        # хотим сделать высоты вершин одинаковыми для алгоритма, чтобы потом измменять высоту на одинаковое значение
        for i in range(self.max_deg, -1, -1): #хотим добежать до нуля включительно
            if self.d[self.dp[u][i]] >= self.d[v]:
                u = self.dp[u][i]
        
        # если вершины изначально были на одном пути из корня, то мы уже победим к этому моменту, когда выровняем высоты
        if v == u:
            return v
        
        # основная "алгоритмическая часть": бегаем по степеням двойки и поднимаемся, когда не равны предки
        for i in range(self.max_deg, -1, -1):
            if self.dp[v][i] != self.dp[u][i]:
                v = self.dp[v][i]
                u = self.dp[u][i]
                
                
        # На самом последнем шагу обе вершины окажутся прямо под нужной вершиной, 
        # т.к. мы всегда делаем так, чтобы предки не совпадали
        return self.dp[v][0]


n = int(sys.stdin.readline())

graph = [0] + list(map(int, sys.stdin.readline().split()))
lca = LCA(graph)

m = int(sys.stdin.readline())
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(lca.query(u, v)) + '\n')
    



