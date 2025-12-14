#Вариант10
if __name__ == '__main__':
    from random import *
    n=int(input('количество столбцов = '))
    m=int(input('количество строк (>3) = '))
    a = [[randint(-10, 11) for _ in range(n)] for __ in range(m)]
    print(*a, sep='\n')
    print(' ')

    def max_in_col(k, l): 
        "k - номер столбца, l - список"
        col = [l[j][k-1] for j in range(m)]
        return col.index(max(col))
    
    id_max_1 = max_in_col(1, a)
    id_max_2 = max_in_col(3, a)
    max_1 = a[id_max_1][0]
    max_2 = a[id_max_2][2]
    a[id_max_1][0] = max_2
    a[id_max_2][2] = max_1
    print(*a, sep='\n')


