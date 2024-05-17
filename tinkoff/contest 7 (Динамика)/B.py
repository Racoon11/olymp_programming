


n = int(input())

ans = [0]*(n+3)
ans[0] = 1
ans[1] = 3

for i in range(2, n+1):
    ans[i] = ans[i-1]*2 + 2*ans[i-2]
    
print(ans[n])
