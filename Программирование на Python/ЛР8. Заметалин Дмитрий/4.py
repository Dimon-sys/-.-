#Вариант10
#4
n = input('Элементы массива через пробел: ').split(' ')
a = n[0]
for i in range(1, len(n)):
    if n[i-1] != n[i]:
        a += ' '
    a += n[i]
    
l = a.split(' ')
print(l)
a = a.replace(max(l, key=len), max(l, key=len) + '*')
print(a)
    
