import numpy as np
import matplotlib.pyplot as plt
from one import Transform, rotz, roty, rotx

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(42)


def random_transform(rng):
    """
    Создаёт случайный элемент SE(3).
    Использует случайные углы Эйлера и случайный сдвиг.
    """
    # Случайные углы
    alpha = rng.uniform(-np.pi, np.pi)
    beta = rng.uniform(-np.pi, np.pi)
    gamma = rng.uniform(-np.pi, np.pi)
    
    # Случайный сдвиг в диапазоне [-5, 5]
    t = rng.uniform(-5, 5, 3)
    
    # Матрица поворота
    R = rotz(alpha) @ roty(beta) @ rotx(gamma)
    
    return Transform.from_Rt(R, t)


# Генерируем три случайных преобразования
A = random_transform(rng)
B = random_transform(rng)
C = random_transform(rng)

print("=== Сгенерированные преобразования ===")
print("A:")
print(A)
print("\nB:")
print(B)
print("\nC:")
print(C)


# 1. Проверка ассоциативности: (AB)C = A(BC)
print("\n" + "="*60)
print("1. Проверка ассоциативности: (AB)C = A(BC)")

AB = A @ B
BC = B @ C

left = (AB) @ C   # (A @ B) @ C
right = A @ (BC)  # A @ (B @ C)

# Сравниваем матрицы
diff_asso = np.linalg.norm(left.M - right.M)
print(f"||(AB)C - A(BC)|| = {diff_asso:.3e}")

# Проверяем, что это близко к машинной точности
eps = np.finfo(float).eps
if diff_asso < 1e-12:
    print("Ассоциативность выполняется с точностью до машинной погрешности")
else:
    print("Погрешность больше ожидаемой")


# 2. Проверка некоммутативности: AB ≠ BA
print("\n" + "="*60)
print("2. Проверка некоммутативности: AB ≠ BA")

AB = A @ B
BA = B @ A

diff_comm = np.linalg.norm(AB.M - BA.M)
print(f"||AB - BA|| = {diff_comm:.3e}")

if diff_comm > 1e-3:
    print("Группа некоммутативна (AB ≠ BA)")
    print(f"   Разница значительная: {diff_comm:.3e}")
else:
    print("Преобразования случайно оказались близкими к коммутирующим")

# Показываем конкретный контрпример (разницу в координатах точки)
p_test = np.array([1.0, 0.0, 0.0])
p_AB = AB.apply_point(p_test)
p_BA = BA.apply_point(p_test)
diff_point = np.linalg.norm(p_AB - p_BA)

print(f"\nКонтрпример на точке p = (1, 0, 0):")
print(f"  (AB)·p = {p_AB}")
print(f"  (BA)·p = {p_BA}")
print(f"  ||(AB)·p - (BA)·p|| = {diff_point:.3e}")


# 3. Проверка замкнутости: произведение AB ∈ SE(3)
print("\n" + "="*60)
print("3. Проверка замкнутости: произведение AB ∈ SE(3)")

AB = A @ B
R_AB = AB.R

# Проверка ортогональности: R^T · R = I
orth_error = np.linalg.norm(R_AB.T @ R_AB - np.eye(3))
print(f"||R^T·R - I|| = {orth_error:.3e}")

# Проверка определителя: det(R) = 1
det_R = np.linalg.det(R_AB)
print(f"det(R) = {det_R:.6f}")

if orth_error < 1e-12 and abs(det_R - 1.0) < 1e-12:
    print("Произведение AB является корректным элементом SE(3)")
    print("   (R ортогональна, det(R) = 1)")
else:
    print("Произведение не является идеальным элементом SE(3)")