#Вариант10
#1
a = [int(i) for i in input('Элементы списка A через пробел: ').split(' ')]
b = [int(i) for i in input('Элементы списка B через пробел: ').split(' ')]
c = [max(a[i], b[i]) for i in range(len(a))]
print(c)
