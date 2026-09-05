import numpy as np
import math

def rotx(a):
    if a < 0:
        raise ValueError
    return np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])


def roty(a):
    if a < 0:
        raise ValueError
    return np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])


def rotz(a):
    if a < 0:
        raise ValueError
    return np.array([[math.cos(a), -math.sin(a), 0], [math.sin(a), math.cos(a), 0], [0, 0, 1]])


class Transform:
    """Жёсткое преобразование как элемент SE(3), хранимое матрицей 4x4."""

    def __init__(self, matrix=None):
        self.M = np.eye(4) if matrix is None else np.asarray(matrix, dtype=float)
        if self.M.shape != (4, 4):
            raise ValueError('нужна матрица 4x4, получено %s' % (self.M.shape,))

    @classmethod
    def from_Rt(cls, R, t):
        return np.array([R, t], [np.transpose(0), 1])

    @property
    def R(self):
        return self.M[:3, :3]

    @property
    def t(self):
        return self.M[:3, 3]

    def __matmul__(self, other):
        return Transform(np.matmul(self.M, other.M))

    def inverse(self):
        return np.array([np.transpose(self.R), -np.transpose(self.R)*self.t], [np.transpose(0), 1])

    def apply_point(self, p):
        p_hom = np.append(p, 1)
        return self.M @ p_hom

    def apply_vector(self, v):
        # TODO: однородная координата w = 0
        raise NotImplementedError

    def __repr__(self):
        return 'Transform(\n%s)' % np.array2string(self.M, precision=4, suppress_small=True)