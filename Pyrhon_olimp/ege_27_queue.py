import time
import sys
sys.stdin = open('27-13b.txt')
t1 = time.process_time_ns()
n = int(input())
Q = []
lens = [0, 0, 0, 0] #7, 2, 14, _
ans = 0
m = 7
k = 0
for _ in range(m):
    Q.append(int(input()))
for i in range(m, n):
    x = int(input())
    new_left = Q[k]
    if new_left % 14 == 0:
        lens[2] += 1
    elif new_left % 7 == 0:
        lens[0] += 1
    elif new_left % 2 == 0:
        lens[1] += 1
    else:
        lens[-1] += 1
        
    if x % 14 == 0:
        ans += sum(lens)
    elif x % 7 == 0:
        ans += lens[1] + lens[2]
    elif x % 2 == 0:
        ans += lens[0] + lens[2]
    else:
        ans += lens[2]
    Q[k] = x
    k = (k+1)%m
print(ans)
print(time.process_time_ns() - t1)
