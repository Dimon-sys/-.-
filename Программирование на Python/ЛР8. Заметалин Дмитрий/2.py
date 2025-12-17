#Вариант10
#2
n = [int(i) for i in input('Элементы списка A через пробел: ').split(' ')]
m = 0
el_1 = 0
el_2 = 0
for i in range(len(n) - 1):
    if n[i] + n[i+1] > m:
        m = n[i] + n[i+1]
        el_1 = n[i]
        el_2 = n[i + 1]
print(el_1, el_2)
