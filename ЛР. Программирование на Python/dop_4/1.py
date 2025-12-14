#Вариант10
if __name__ == '__main__':
    from random import *

    def neg_count(l) -> list:
        return len([i for i in l if i < 0])
    
    n = int(input('n='))
    a = [randint(-10, 11) for i in range(n)]
    b = [randint(-10, 11) for i in range(n)]
    print(a)
    print(b)
    print(' ')
    if neg_count(a) > neg_count(b):
        print('В одномерном массиве A отрицательных элементов больше, чем в одномерном массиве B')
    elif neg_count(b) > neg_count(a):
        print('В одномерном массиве B отрицательных элементов больше, чем в одномерном массиве A')
    else:
        print(neg_count(a))

    