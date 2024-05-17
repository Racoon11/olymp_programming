import sys


def getParts(parts, s):
    sCur = 0
    ans = 0

    for i in range(len(parts)):
        if (sCur + parts[i]) > s:
            ans += 1
            sCur = 0
        if (parts[i] > s):
            return maxi
        sCur += parts[i]
    if (sCur): ans+=1
    
    return ans


def bin2(parts, k):
    left = maxi
    right = -1
    while (left - right) > 1:
        mid = (right + left) // 2
        kCur = getParts(parts, mid)
        if (kCur <= k):
            left = mid
        else:
            right = mid
    return left

maxi = 10**15

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(bin2(arr, k))
