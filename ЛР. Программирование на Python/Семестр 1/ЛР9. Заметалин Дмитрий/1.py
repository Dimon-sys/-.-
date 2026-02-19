#Вариант10
print('Данные вводить через пробел')
x = [int(i) for i in input('x = ').split(' ')]
y = [int(i) for i in input('y = ').split(' ')]
print(sum[(2/(x[i]+y[i])) for i in range(len(x))])
