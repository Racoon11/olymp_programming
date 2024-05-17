def nod(a, b):
    a, b = max(a,b), min(a,b)
    while (b > 0):
    	b, a = a%b, b
    return a
a = int(input())
b = int(input())
print(a * b // nod(a, b))
