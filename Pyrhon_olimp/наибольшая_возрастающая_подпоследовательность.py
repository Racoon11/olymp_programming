def gis(A):
    F = [0]*(len(A)+1)
    for i in range(1,len(A)+1):
        m = 0
        for j in range(0,i):
            if A[i-1]>A[j-1] and F[j]>m:
                m = F[j]
        F[i] = m+1
    ans = []
    for i in range(1,F[len(A)]+1):
        ans.append(A[F.index(i)-1])
    return (F[len(A)],ans)
a = gis([0,6,4,3,1,4,3,2,19,23,1,1,0,90])
print(a[0])
print(a[1])
