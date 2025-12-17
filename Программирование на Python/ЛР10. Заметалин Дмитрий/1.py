#Вариант10
from random import *
a = [[randint(-10, 10) for i in range(10)] for j in range(2)]
print(*a, sep='\n')
print([x for x in range(1, 11) if (a[0][x-1] > 0 and a[1][x-1] > 0 or a[0][x-1] < 0 and a[1][x-1] < 0 or a[0][x-1] == a[1][x-1] == 0)])
