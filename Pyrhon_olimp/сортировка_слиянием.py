from time import time
def merge(A:list,B:list):
    ''' функция для слияния двух массивов
        в один '''
    C = [0]*(len(A)+len(B)) #Будующий слитый массив
    x = 0
    x2 = 0
    c = 0
    while x<len(A) and x2<len(B):
        if A[x]<B[x2]:
            C[c] = A[x]
            x+=1
        else:
            C[c] = B[x2]
            x2+=1
        c+=1
    for j in A[x:]:
        C[c] = j
        c+=1
    for j in B[x2:]:
        C[c] = j
        c+=1
    return C
def sort(M:list):
    if len(M) == 1:
        return M
    return merge(sort(M[:len(M)//2]),sort(M[len(M)//2:]))
k = time()
print(sort([1,5,8,1,4,0,12,55,10,33,20,67,1,5,33]))
print(time()-k)
k = time()
print(sorted([1,5,8,1,4,0,12,55,10,33,20,67,1,5,33]))
print(time()-k)
