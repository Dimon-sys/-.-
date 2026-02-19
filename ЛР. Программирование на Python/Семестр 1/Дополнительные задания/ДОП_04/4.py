#Вариант10
if __name__ == '__main__':
    from random import *
    a = [randint(-10, 11) for _ in range(randint(1, 10))]
    b = [randint(-10, 11) for _ in range(randint(1, 10))]
    c = [randint(-10, 11) for _ in range(randint(1, 10))]
    a1 = int(input('Диапазон от (включительно)... '))
    a2 = int(input('...до (включительно) '))

    print(a)
    print(b)
    print(c)
    print(' ')
    
    def new_list_and_his_len(l, a1, a2):
        return [[i for i in l if a1 <= i <= a2], len([i for i in l if a1 <= i <= a2])]
    
    a_new = new_list_and_his_len(a, a1, a2)
    b_new = new_list_and_his_len(b, a1, a2)
    c_new = new_list_and_his_len(c, a1, a2)

    print(*a_new)
    print(*b_new)
    print(*c_new)



