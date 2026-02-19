#Вариант10
x = [int(i) for i in input('Вводить элементы через пробел: ').split(' ')]
s = [k for k in x if k <= x[0]]
print(sum(s)/len(s))
