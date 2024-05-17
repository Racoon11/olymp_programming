def check(sk):
    stack = [0]
    skobs_open = ['[','{','(']
    skobs_close = [']','}',')']
    for i in sk:
        if (i not in skobs_open) and (i not in skobs_close):
            continue
        if i in skobs_open:
            stack.append(i)
        elif (i == ']' and stack[-1]=='[') or (i == '}' and stack[-1]=='{') or (i == ')' and stack[-1]=='('):
            stack.pop()
        else:
            return False
    
    return len(stack)==1
def check_2(sk):
    ''' работает, если один вид скобок '''
    n = 0
    skobs_open = ['[','{','(']
    skobs_close = [']','}',')']
    for i in sk:
        if i in skobs_open:
            n+=1
        else:
            n-=1
        if n<0:
            return False
    return n==0
sk = input()
print(check(sk))
print(check_2(sk))
