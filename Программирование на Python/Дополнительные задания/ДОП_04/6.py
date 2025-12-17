#Вариант10
if __name__ == '__main__':
    from random import *
    a_cols = randint(1, 10)
    a = [[randint(-10, 11) for _ in range(a_cols)] for __ in range(randint(1, 10))]
    print(*a, sep='\n')
    print(' ')
    for i in range(len(a)-1, -1, -1):
        if sorted(a[i], reverse=True) == a[i]:
            print(i+1)
            break
