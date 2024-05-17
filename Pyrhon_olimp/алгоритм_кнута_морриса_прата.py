def pi_function(s):
    pi = [0]*(len(s)+1)
    for i in range(2,len(s)+1):
        p = pi[i-1]
        while p>0 and s[i-1]!=s[p]:
            p = pi[p]
        if s[i-1] == s[p]:
            p += 1
        pi[i] = p
    return s[:pi[-1]]
print(pi_function('abacabadabacabafabacabadabacabadabacabafaba'))
     
def kmp(s,spod):
    s = spod + '#' + s
    pi = [0]*(len(s)+1)
    ans = []
    for i in range(len(spod)+2,len(s)+1):
        p = pi[i-1]
        while p>0 and s[i-1]!=s[p]:
            p = pi[p]
        if s[i-1] == s[p]:
            p += 1
        pi[i] = p
        if p==len(spod):
            ans.append(i-len(spod)-1-len(spod))
    return ans

