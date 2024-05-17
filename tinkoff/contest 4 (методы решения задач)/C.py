import sys



def look_for(arr, k):
    ''' arr - массив частей
        k - минимальное расстояние между коровами
        K - минимум столько'''
    ans = 1
    sCur = 0
    for i in range(N):
        if (sCur >= k):
            ans += 1
            sCur = 0
        sCur += arr[i]
    if (sCur >= k): ans += 1
    return ans

def bin2(parts, k):
    left = 10**15
    right = -1
    while (left - right) > 1:
        mid = (right + left) // 2
        kCur = look_for(parts, mid)
        if (kCur < k):
            left = mid
        else:
            right = mid
    return right

N, K = map(int, sys.stdin.readline().split())
coords = list(map(int, sys.stdin.readline().split()))
parts = [0] + [coords[i] - coords[i-1] for i in range(1, N)]
mini = min(parts)

print(bin2(parts, K))
