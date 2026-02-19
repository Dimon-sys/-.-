#Вариант10
#Задание2
from math import *
a = int(input('a = '))
x = int(input('x = '))
b = int(input('b = '))
c = int(input('c = '))
if log10(a) < x:
    print((b**2 + abs(x+c) ** 0.5) ** (1/3))
elif log10(a) == x:
    print(cos(x - b - c))
else:
    print(sin(x + a - b))
