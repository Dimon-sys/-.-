#Вариант10
from math import *
a = 1.5
x1 = -a
dx = 3*a/10

n = int(input('n= '))

print('x     y')
def y(x):
    if x < 0:
        return 2 * a * (1 - (x**2/a**2)) ** 0.5
    else:
        return a / (2*cos(x)) + 3 * a / 2

for i in range(n):
    print(x1, y(x1))
    x1 += dx