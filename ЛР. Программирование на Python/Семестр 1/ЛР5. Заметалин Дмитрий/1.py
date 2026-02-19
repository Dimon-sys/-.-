#Вариант10
#Задание1
a = int(input('a='))
b = int(input('b='))
x = int(input('x='))
y = int(input('y='))
r = int(input('r='))

if (0 < y < b and x > 0 and x ** 2 + y ** 2 > r ** 2) or (x < 0 and -b < y < 0 and x ** 2 + y ** 2 < r ** 2):
    print('in')
elif ((y<0 or y>b) or x < 0 or x ** 2 + y ** 2 < r ** 2) and (x > 0 or y > 0 or y < -b or x ** 2 + y ** 2 > r ** 2):
    print('out')
else:
    print('border')
