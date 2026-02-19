#Вариант10
if __name__ == '__main__':
    from random import *
    a_cols = randint(1, 10)
    b_cols = randint(1, 10)
    c_cols = randint(1, 10)
    a = [[randint(-10, 11) for _ in range(a_cols)] for __ in range(randint(1, 10))]
    b = [[randint(-10, 11) for _ in range(b_cols)] for __ in range(randint(1, 10))]
    c = [[randint(-10, 11) for _ in range(c_cols)] for __ in range(randint(1, 10))]

    print(*a, sep='\n')
    print(' ')
    print(*b, sep='\n')
    print(' ')
    print(*c, sep='\n')
    print(' ')

    def mult_no_main_diag(matrix):
        strs = len(matrix)
        cols = len(matrix[0])
        mult = 1
        for i in range(strs):
            for j in range(cols):
                if i != j and matrix[i][j] > 0:
                    mult *= matrix[i][j]
        return mult
    
    p_a = mult_no_main_diag(a)
    p_b = mult_no_main_diag(b)
    p_c = mult_no_main_diag(c)

    print(p_a, p_b, p_c)

    print(p_a + 2 * p_b - p_c)
