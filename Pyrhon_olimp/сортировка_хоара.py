from time import time
def sort(mass,t):
    if len(mass)<=1:
        return mass
    sr = []
    more = []
    less = []
    for i in mass:
        if i>t: more.append(i)
        elif i==t: sr.append(i)
        else: less.append(i)
    return (sort(less,less[0]) if less else []) + sr + (sort(more,more[0]) if more else [])
n = list(map(int, input().split()))
k = time()
print(sort(n,n[0]))
print(time()-k)
k = time()
print(sorted(n))
print(time()-k)
