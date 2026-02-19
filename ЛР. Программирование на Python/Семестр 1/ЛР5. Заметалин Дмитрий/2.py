#Вариант10
#Задание2
x = int(input('x='))
y = int(input('y='))

"""
ink1 = x ** 2 + (y-1) ** 2 <= 1
ink2 = (x + 1) ** 2 + y ** 2 <= 1
ink3 = x ** 2 + y ** 2 <= 1
ink4 = (x - 1) ** 2 + y ** 2 <= 1
ink5 = x ** 2 + (y + 1) ** 2 <= 1
"""

if x <= -1 and y >= 0 and (x + 1) ** 2 + y ** 2 >= 1:
    print('M1')
elif -1 <= x <= 1 and 0 <= y <= 1 and (x + 1) ** 2 + y ** 2 >= 1 and (x - 1) ** 2 + y ** 2 >= 1:
    print('M2')
elif (x + 1) ** 2 + y ** 2 <= 1 and x ** 2 + y ** 2 <= 1 and (x - 1) ** 2 + y ** 2 <= 1:
    print('M3')
elif y <= 0 and x ** 2 + y ** 2 <= 1 and (x - 1) ** 2 + y ** 2 >= 1:
    print('M4')
elif x >= 0 and (x - 1) ** 2 + y ** 2 <= 1 and x ** 2 + y ** 2 >= 1 and (x - 1) ** 2 + y ** 2 >= 1:
    print('M5')
else:
    print('Точка не принадлежит никакой области')
