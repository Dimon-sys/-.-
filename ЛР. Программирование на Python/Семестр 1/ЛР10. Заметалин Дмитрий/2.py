#Вариант10
from random import *
a = [[randint(-10, 10) for _ in range(10)] for __ in range(2)]
#a = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]]
print(*a, sep='\n')

x_0, y_0 = a[0][0], a[1][0]
flag = True
for i in range(1, 10):
    if a[0][i] * y_0 - a[1][i] * x_0 == 0:
        print(f'Точка №{i+1} лежит на прямой')
    else:
        print(f'Точка №{i+1} не лежит на прямой')
        flag = False
        break

if flag:
    print('Все 10 точек лежат на одной прямой')
else:
    print('Точки не лежат на одной прямой')