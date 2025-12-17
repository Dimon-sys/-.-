#Вариант10
#3
n = [int(i) for i in input('Элементы списка A через пробел: ').split(' ')]
a = []
for i in n:
    if i % 2 == 0:
        a.append(i)
        a.append(i)
    elif i % 2 == 1:
        a.append(i)
        a.append(i)
        a.append(i)
print(a)
