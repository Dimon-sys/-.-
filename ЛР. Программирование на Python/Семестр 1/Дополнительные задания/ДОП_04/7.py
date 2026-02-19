#Вариант10
if __name__ == '__main__':
    from random import *
    a = [randint(-10, 11) for _ in range(randint(1, 10))]
    print(a)
    a_neg = []
    a_not_neg = []
    for i in a:
        if i < 0:
            a_neg += [i]
        else:
            a_not_neg += [i]
    print(a_neg)
    print(a_not_neg)
    print(a_neg + a_not_neg)