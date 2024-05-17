from functools import lru_cache

@lru_cache
def quickPow(a, b, p):
    if (b == 1):
        return a
    if (b == 2): return a * a % p
    if (b % 2 == 0):
        return quickPow(quickPow(a, b//2, p)%p, 2, p)%p
    return (quickPow(a, b - 1, p)%p * (a%p))%p

def productMod(a, b, p):
    return ((a % p) * (b % p)) % p

def obrMod(a, p):
    a = quickPow(a, (p - 2), p) % p
    return a

def getSeconds(n, m, k, p):
    return productMod(quickPow(m, n, p), obrMod(k, p), p)

n, m, k, mod = map(int, input().split())

print(getSeconds(n, m, k, mod))

'''
k - число операций в секунду
n - число символов в пароле
m - количество символов в множетсве возможных символов
m**n - число комбинаций
m**n / k - число секунд
'''
