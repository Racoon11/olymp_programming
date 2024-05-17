

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def factorial_last(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
        while (ans % 10 == 0):
            ans //= 10
        ans %= 100000
    return ans%10


n = int(input())
#print(str(factorial(n)))
print(factorial_last(n))
        
