


def maxSubsequencePalindrom(s):
    n = len(s)
    L = [[0] * n for _ in range(n)]
    ans = [[''] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
        ans[i][i] = s[i]
    
    res = 1
    res2 = s[0]
    for ln in range(2, n + 1): # перебираем все длины от 2 (т.к. 1 уже обработали) до n включительно
        for i in range(0, n - ln + 1): # перебираем левую границу
            j = i + ln - 1 # правая граница
            if s[i] == s[j]:
                L[i][j] = 2 + L[i + 1][j - 1]
                ans[i][j] = s[i] + ans[i+1][j-1] + s[i]
            else:
                if (L[i + 1][j] > L[i][j - 1]):
                    L[i][j] = L[i + 1][j]
                    ans[i][j] = ans[i+1][j]
                else:
                    L[i][j] = L[i][j - 1]
                    ans[i][j] = ans[i][j - 1]
                #L[i][j] = max(L[i + 1][j], L[i][j - 1])
            if L[i][j] > res:
                res = L[i][j]
                res2 = ans[i][j]
                
    return res, res2

s = input()
s1, s2 = maxSubsequencePalindrom(s)
print(s1)
print(s2)
