function_text = input("введите функцию от x: ")
f = lambda x: eval(function_text)
a, b = map(float, input("промежуток для поиска корня: ").split())
error = float(input("погрешность поиска корня: "))
if f(a) * f(b) >= 0:
    print("На этом промежутке нельзя воспользоватся двоичным поиском")
    exit(0)
while (b - a) / 2 > error:
    c = (a + b) / 2
    if f(c) == 0 :
        break #наткнулись на корень
    elif f(a)*f(c) < 0:
        b = c
    else:
        a = c
print("Корень f(x) = 0:", (a + b) / 2, "+-", (b - a) / 2)
