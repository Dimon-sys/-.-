import numpy as np

def rotx(a):
    return np.array([[1, 0, 0], [0, np.cos(a), -np.sin(a)], [0, np.sin(a), np.cos(a)]])


def roty(a):
    return np.array([[np.cos(a), 0, np.sin(a)], [0, 1, 0], [-np.sin(a), 0, np.cos(a)]])


def rotz(a):
    return np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]])


class Transform:
    """Жёсткое преобразование как элемент SE(3), хранимое матрицей 4x4."""

    def __init__(self, matrix=None):
        self.M = np.eye(4) if matrix is None else np.asarray(matrix, dtype=float)
        if self.M.shape != (4, 4):
            raise ValueError('нужна матрица 4x4, получено %s' % (self.M.shape,))

    @classmethod
    def from_Rt(cls, R, t):
        R = np.asarray(R, dtype=float)
        t = np.asarray(t, dtype=float)
        if R.shape != (3, 3):
            raise ValueError(f'R должна быть 3x3, получено {R.shape}')
        if t.shape != (3,):
            t = t.flatten()
            if t.shape != (3,):
                raise ValueError(f't должен быть вектором длины 3, получено {t.shape}')
        
        M = np.eye(4) #единичная матрица 4x4
        M[:3, :3] = R
        M[:3, 3] = t
        return cls(M) #объект класса Transform

    @property
    def R(self):
        return self.M[:3, :3]

    @property
    def t(self):
        return self.M[:3, 3]

    def __matmul__(self, other):
        if not isinstance(other, Transform):
            return NotImplemented
        return Transform(self.M @ other.M)

    def inverse(self):
        M_inv = np.eye(4)
        M_inv[:3, :3] = self.R.T
        M_inv[:3, 3] = -self.R.T @ self.t
        return Transform(M_inv)

    def apply_point(self, p):
        p = np.asarray(p, dtype=float)
        original_shape = p.shape
        
        # Приводим к (N, 3) (трёхмерный массив из N точек)
        if p.ndim == 1: #степень вложенности (просто точка)
            p = p.reshape(1, -1) #пересобираем в матрицу с 1 строкой   #матрица с одной точкой ≠ одна точка
        elif p.ndim == 2:
            pass
        else:
            raise ValueError('p должен быть (3,) или (N, 3)')
        
        if p.shape[1] != 3:
            raise ValueError('последняя размерность должна быть 3')
        
        # Добавляем однородную координату w=1
        ones = np.ones((p.shape[0], 1))
        p_hom = np.hstack([p, ones])  # (N, 4)
        
        # Применяем преобразование
        result_hom = (self.M @ p_hom.T).T  # (N, 4)
        
        # Убираем однородную координату
        result = result_hom[:, :3]
        
        # Восстанавливаем исходную форму
        if original_shape == (3,): #если был дан набор точек
            return result[0]
        return result #если была дана одна точка

    def apply_vector(self, v):
        v = np.asarray(v, dtype=float)
        original_shape = v.shape
        
        # Приводим к (N, 3)
        if v.ndim == 1:
            v = v.reshape(1, -1)
        elif v.ndim == 2:
            pass
        else:
            raise ValueError('v должен быть (3,) или (N, 3)')
        
        if v.shape[1] != 3:
            raise ValueError('последняя размерность должна быть 3')
        
        # Добавляем однородную координату w=0
        zeros = np.zeros((v.shape[0], 1))
        v_hom = np.hstack([v, zeros])  # (N, 4)
        
        # Применяем преобразование
        result_hom = (self.M @ v_hom.T).T  # (N, 4)
        
        # Убираем однородную координату
        result = result_hom[:, :3]
        
        # Восстанавливаем исходную форму
        if original_shape == (3,):
            return result[0]
        return result

    def __repr__(self):
        return 'Transform(\n%s)' % np.array2string(self.M, precision=4, suppress_small=True)
    
if __name__ == "__main__":
    T = Transform.from_Rt(rotz(np.pi / 6) @ rotx(np.pi / 4), [1.0, -2.0, 0.5])
    resid = np.linalg.norm((T @ T.inverse()).M - np.eye(4))
    print('||T @ T^-1 - I|| = %.3e' % resid)
    assert resid < 1e-12, 'обращение реализовано неверно'
    print('OK')