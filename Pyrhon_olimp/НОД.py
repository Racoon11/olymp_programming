def nod(a, b):
    a, b = max(a,b), min(a,b)
    while (b > 0):
    	b, a = a%b, b
    return a
print(nod(int(input()), int(input())))
