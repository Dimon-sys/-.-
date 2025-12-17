from math import *

if __name__ == "__main__":
    def create_matrix(n, m) -> int:
        return [[((sin(i)**3 - cos(j))**3 + 7.4 * log10(abs((i-5)/(j+3)) + 1)) for i in range(n)] for j in range(m)]

    matrix = create_matrix(4, 6)
    print(*matrix, sep='\n')
    print(' ')

    columns = []

    for i in range(4):
        column = []
        for j in range(6):
            column.append(matrix[j][i])
        columns.append(column)
    
    print(columns)
    print(' ')

    l = min(columns, key=sum)
    print(l, end='\n')
    print(' ')
    print(sum(i ** 2 for i in l if i < 0))
    
