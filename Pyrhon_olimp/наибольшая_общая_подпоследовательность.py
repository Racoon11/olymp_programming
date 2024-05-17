def lcs(a,b):
    f = [[0]*(len(b)+1) for j in range(len(a)+1)]
    posl = []
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                f[i][j] = 1 + f[i-1][j-1]
                if f[i][j]>len(posl):
                    posl.append(a[i-1])
            else:
                f[i][j] = max(f[i][j-1],f[i-1][j])
    return (f[-1][-1],posl)
a = lcs([9,1,5,7,8,1,4,6,10,58,0,1],[9,1,4,56,8,7,6,4,0,3,65])
print(a[0])
print(*a[1])
