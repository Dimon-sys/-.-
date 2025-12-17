from random import *
n = int(input('Размер массива: '))
a = [[randint(-10, 10) for _ in range(n)] for __ in range(n)]

for i in range(n):
    print(a[i])

print('Сумма элементов двумерного массива - ', sum([sum(i) for i in a]))
print('Количество строк, в пределах каждой из которых элементы упорядочены по возрастанию - ', len([x for x in a if x.sort() == x]))