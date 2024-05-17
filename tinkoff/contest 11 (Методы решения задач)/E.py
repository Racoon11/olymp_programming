


Stroka = input()
n = len(Stroka)
ans = [[0]*n for _ in range(n)]

for ln in range(n):
    for i in range(n-ln):
        j = i + ln
        ans[i][j] = (1, Stroka[i:j+1])
        curLen = j - i + 1
        for spl in range(ln):
            f = ans[i][i+spl]
            s = ans[i+spl+1][j]
            if (f[1] == s[1] and curLen > (len(f[1]))):
                # + 2 + len(str(f[0]+s[0])))
                ans[i][j] = (f[0]+s[0], f[1])
                curLen = len(f[1])
            elif (f[1] != s[1]):
                newS = ''
                if (f[0] != 1):
                    newS += str(f[0]) +'(' + f[1] + ')'
                else:
                    newS += f[1]
                if (s[0] != 1):
                    newS += str(s[0]) +'(' + s[1] + ')'
                else:
                    newS += s[1]
                #print(newS)
                if (len(newS) < curLen):
                    ans[i][j] = (1, newS)
                    curLen = len(newS)
ansR = ans[0][-1]
ansR1 = Stroka
newS = ''
if ansR[0] != 1:
    newS += str(ansR[0]) +'(' + ansR[1] + ')'
else:
    newS += ansR[1]
if n < len(newS):
    print(Stroka)
else:
    print(newS)
