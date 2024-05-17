import sys


p = sys.stdin.readline()
t = sys.stdin.readline()

k = len(p)-1
k2 = len(t)
ans = 0
ansL = []
for i in range(k2-k):
    was = False
    for j in range(k):
        if (p[j] != t[i+j]) and was:
            break
        elif (p[j] != t[i+j]):
            was = True
    else:
        ans += 1
        ansL.append(i+1)
sys.stdout.write(str(ans)+'\n')
sys.stdout.write(' '.join(map(str, ansL)))
