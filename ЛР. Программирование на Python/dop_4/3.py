#Вариант10
if __name__ == '__main__':
    from random import *
    a = [randint(-10, 11) for _ in range(randint(1, 10))]
    b = [randint(-10, 11) for _ in range(randint(1, 10))]
    c = [randint(-10, 11) for _ in range(randint(1, 10))]
    print('a =', a)
    print('b =', b)
    print('c =', c)
    n=int(input('n = '))
    sum_a = sum((i for i in a if i % n == 0))
    sum_b = sum((i for i in b if i % n == 0))
    sum_c = sum((i for i in c if i % n == 0))
    d = {
        sum_a : 'a',
        sum_b : 'b',
        sum_c : 'c'
    }
    print(f'Массив с наибольшей суммой элементов, кратных n - {d[max([sum_a, sum_b, sum_c])]}; сумма - {max([sum_a, sum_b, sum_c])}')

    print(f'Наименьшее значение суммы элементов, кратных n - {min([sum_a, sum_b, sum_c])}, в массиве {d[min([sum_a, sum_b, sum_c])]}')

    if max([sum_a, sum_b, sum_c]) == min([sum_a, sum_b, sum_c]):
        print(f'Значения экстремумов (массивы {d[max([sum_a, sum_b, sum_c])]} и {d[min([sum_a, sum_b, sum_c])]}) совпадают')