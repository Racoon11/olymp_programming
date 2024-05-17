from math import factorial
from functools import lru_cache

def binSlow(n, k):
    ans = factorial(n)//factorial(k)//factorial(n-k)
    return ans


def binMod(n, k, p):
    ans = 1
    ans = productMod(productMod(factorialMod(n, p), obrMod(factorialMod(k, p), p), p),
                     obrMod(factorialMod(n-k, p), p), p)
    return ans
        
def factorialMod(n, p):
    ans = 1
    for i in range(2, n+1):
        ans *= (i % p)
        ans %= p
    return ans

def productMod(a, b, p):
    return ((a % p) * (b % p)) % p

def obrMod(a, p):
    a = quickPow(a, (p - 2), p) % p
    return a

@lru_cache
def quickPow(a, b, p):
    if (b == 1):
        return a
    if (b == 2): return a * a % p
    if (b % 2 == 0):
        return quickPow(quickPow(a, b//2, p)%p, 2, p)%p
    return (quickPow(a, b - 1, p)%p * (a%p))%p

n, k = map(int, input().split())
p = 10**9 + 7
#print(binSlow(n, k) % p)
print(binMod(n, k, p))

