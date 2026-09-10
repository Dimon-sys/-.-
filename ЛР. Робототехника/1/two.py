from one import Transform
import numpy as np

R = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]) #поворот на 90 градусов вокруг Z
t = np.array([10, 0, 0])

T = Transform.from_Rt(R, t)

point = np.array([0, 0, 0])
result = T.apply_point(point)
print(result)

vector = np.array([1, 0, 0])
result = T.apply_vector(vector)
print(result)
