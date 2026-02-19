#Вариант10
s = [int(i) for i in input().split(' ')]
a1 = int(input('Диапазон от ...'))
a2 = int(input('...до...'))

flag = True
for i in s:
    if a1 <= i <= a2:
        flag = False
        l = s.index(i)
        break

if flag:
    print('В массиве нет элементов, попадающих в заданный диапазон')
else:
    print(l)
