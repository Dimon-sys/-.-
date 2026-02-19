#Вариант10
#Задание3
x = float(input('x = '))
if x < -5:
    print(x+4)
elif x == -5:
    print(-1)
elif -5 < x < -3:
    print(-(4 - (x+3)**2) ** 0.5 - 1)
elif x == -3:
    print(-3)
elif -3 <x< 1:
    print((7/4)*x + (9/4))
elif x == 1:
    print(4)
elif 1 < x < 8:
    print(-(4/7)*x + (32/7))
elif x == 8:
    print(0)
elif 8 < x < 9:
    print(-(1 - (x-8)**2) ** 0.5 + 1)
elif x == 9:
    print(1)
