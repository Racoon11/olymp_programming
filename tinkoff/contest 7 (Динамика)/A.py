


n = int(input())

costs = [0] + list(map(int, input().split()))
ans = [0]*(n+1)
ans[1] = costs[1]
for i in range(2, n+1):
    ans[i] = min(ans[i-1], ans[i-2]) + costs[i]

print(ans[n])
