from math import sqrt, ceil


def is_simple(n):
    if n == 1: return False
    for i in range(2, n):
        if (n % i == 0): return False
    return True

def get_two(n):
    
    for i in range(2, n-1):
        if (is_simple(i) and is_simple(n - i)):
            return [i, n - i]
    return [-1, -1]

n = int(input())
print(*get_two(n)) # love u
