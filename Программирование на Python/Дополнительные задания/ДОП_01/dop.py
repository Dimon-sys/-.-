from random import *

def sort_by_diagonals_right_to_left_(matrix):
    n = len(matrix)
    result = []
    
    #Всего 2n-1 диагоналей
    for d in range(2 * n - 1):
        if d < n:
            #Диагонали, начинающиеся в верхней строке
            row = 0
            col = n - 1 - d
        else:
            #Диагонали, начинающиеся в левом столбце
            row = d - n + 1
            col = 0
        
        #Проходим по текущей диагонали
        while row < n and col < n:
            result.append(matrix[row][col])
            row += 1
            col += 1
    
    return result


k = int(input('Номер искомого элемента среди чётных k= '))
n = int(input('Размер двумерного массива n = '))

matrix = [[randint(-10, 10) for _ in range(n)] for __ in range(n)]
print(*matrix, sep='\n')

sorted_m = sort_by_diagonals_right_to_left_(matrix)
print(f'Обход матрицы: {sorted_m}')
chet_elems = [x for x in sorted_m if x % 2 == 0]

try:
    print(abs(chet_elems.index(k-1)))
except ValueError:
    print('Чётного элемента с таким индексом нет')
    matrix_r = [r[::-1] for r in matrix]
    for row in range(n):
        for col in range(n):
            if row > col and matrix_r[row][col] < 0:
                matrix_r[row][col] = 0
    print(*[r[::-1] for r in matrix_r], sep='\n')

