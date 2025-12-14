#Вариант10
if __name__ == '__main__':
    from random import *
    from math import *
    l = randint(1, 10)
    while l % 2 != 0:
        l = randint(1, 10)

    cols = randint(1, 10)

    a = [[randint(-10, 11) for _ in range(cols)] for __ in range(l)]

    print(*a, sep='\n')
    print(' ')

    def t(b, c, f1, f2):
        t = []
        for i in range(len(b)):
            if b[i] >= c[i]:
                t += [f1(b[i])]
            else:
                t += [f2(c[i])]
        return t

    e = []
    for i in range(0, len(a), 2):
        e += [t(a[i], a[i+1], sin, cos)]

    print(*e, sep='\n')
    print(' ')

    r = []
    for i in range(0, len(a), 2):
        r += [t(a[i], a[i+1], cos, abs)]

    print(*r, sep='\n')



        




