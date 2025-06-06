


from collections import deque

def find_min_cost_path_linear(n, k, cost):
    # Инициализируем массив min_cost нулями, так как будем добавлять стоимости к ним
    min_cost = [0] * (n + 1)
    ways = [0] * (n+1)
    # Создаем двустороннюю очередь для индексов, которые обеспечивают минимальные стоимости
    dq = deque([0])  # Стартуем с 0-ой клетки, так как с неё начинаем движение

    # Начинаем с 1, так как стоимость для 0 установлена равной 0
    for i in range(1, n + 1):
        # Убираем индексы, которые вышли за пределы диапазона k
        while dq and dq[0] < i - k:
            dq.popleft()
        
        # Минимальная стоимость для клетки i это стоимость на текущей клетке
        # плюс минимальная стоимость достижения клетки из очереди
        min_cost[i] = min_cost[dq[0]] + cost[i]
        ways[i] = dq[0]
        # Убираем все индексы с более высокой стоимостью, так как они больше не будут использоваться
        while dq and min_cost[i] >= min_cost[dq[-1]]:
            dq.pop()
        
        # Добавляем текущий индекс в очередь
        dq.append(i)
    
    # Возвращаем минимальную стоимость достижения клетки n
    return min_cost[n], ways


n, k = map(int, input().split())

vals = [0,0] + list(map(int, input().split())) + [0]

ans, ways = find_min_cost_path_linear(n, k, vals)
print(ans)

way = [n]
cur = ways[n]
n = 0
while cur != 0:
    way.append(cur)
    n += 1
    cur = ways[cur]
print(n)

print(*way[::-1])
