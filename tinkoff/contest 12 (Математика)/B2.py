import sys
from math import sqrt, ceil

def to_simple(n):
    ans = {}
    for i in range(2, ceil(sqrt(n)) + 1):
        while n % i == 0:
            ans[i] = ans.get(i, 0) + 1
            n //= i
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans

def get_str(arr):
    ans = ""
    
    for i in sorted(arr):
        if arr[i] != 0:
            ans += '*' + str(i)
        if arr[i] > 1:
            ans += '^' + str(arr[i])
    return ans[1:]
n = int(input())
print(get_str(to_simple(n)))
