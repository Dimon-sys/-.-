#Вариант10
def f(x):
    return 4*x/(x-x**2+1)

x = 0.1
while x <= 10 and f(x) != 4:
    print(x, f(x))
    x += 0.1