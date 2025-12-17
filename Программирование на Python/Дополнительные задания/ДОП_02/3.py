#Вариант10
from math import *

n = int(input('n = '))
x_0 = float(input('x_нач = '))
hx = float(input('hx = '))
z_0 = float(input('z_нач = '))
hz = float(input('hz = '))

def f(x, z):
    return (3.8 + z**0.5 * sin(x**2/2))/(x ** 0.2 + e ** (z*x))

print('№ | x | z | f(x, z)')

for i in range(1, n+1):
    print(f'{i} | {x_0} | {z_0} | {f(x_0, z_0)}')
    x_0 += hx
    z_0 += hz
