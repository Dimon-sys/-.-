#Вариант10
from random import *

a = 3 * 10 ** 4
b = 6 * 10 ** 4
m = 4

def f(k):
    return k ** 3 - 25 * k ** 2 + 50 * k + 1000

c = 0
l = 0
t1 = (a*b) ** 0.5 + m
for j in range(20):
    i = randrange(-31, 60)
    if f(i) < t1 and f(i) != 250 * m and f(i) != 0:
        print(f'{c+1}. {i}, {f(i)}')
    else:
        l += 1
    c = c + 1
    if c == 20:
        break
print(f'Количество значений, не удовлеворивших условию: {l}')
