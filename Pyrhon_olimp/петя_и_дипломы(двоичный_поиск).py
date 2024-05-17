w, h, n = map(int, input().split())
f = lambda a: (a//w) * (a//h)  #число дипломов на квадоате со стороной a
left = 0
right = min(h, w) * n #если бы все дипломы расположиди в линию
while right - left > 1: #до двух соседних значений
    middle = (left + right) // 2
    if f(middle) < n:
        left = middle # f(left) < тредуемого числа дипломов
    else:
        right = middle # f(right) >= нужного числа
print(right)
