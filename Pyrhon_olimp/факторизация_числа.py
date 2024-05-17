def factorization(a):
    ans = []
    i = 2
    while (a != 1):
        while (a % i == 0):
            ans.append(i)
            a //= i
        i += 1
    return ans 
a = int(input())
print(*factorization(a))
