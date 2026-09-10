import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)
print(arr.ndim)
arr_1x6 = arr.reshape(1, -1)  # 1 строка, столбцов: 6/1 = 6
print(arr_1x6)
print(arr_1x6.ndim)