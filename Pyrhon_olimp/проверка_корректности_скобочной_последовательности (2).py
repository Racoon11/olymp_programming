def arifm(li):
    stack = []
    operations = '+-/*'
    for i in li:
        if str(i) not in operations:
            stack.append(i)
        else:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '/':
                stack.append(a/b)
            else:
                stack.append(a*b)
    return stack[-1]
a = arifm([2,7,5,'*','+'])
print(a)
