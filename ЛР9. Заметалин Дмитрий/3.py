#Вариант10
print('Массивы одинаковой длины, элементы вводить через пробел')
a = [int(i) for i in input('a = ').split(' ')]
c = [int(i) for i in input('c = ').split(' ')]
s = []
for i in range(len(a)):
    d = sum([a[j] * c[j] for j in range(i+1)])
    s.append(d)
print(max(s))
