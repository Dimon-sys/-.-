import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=4, suppress=True)


# ============================================================================
# Вспомогательные функции (из заданий 1-5)
# ============================================================================

def rotx(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

def roty(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])

def rotz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

class Transform:
    def __init__(self, matrix=None):
        self.M = np.eye(4) if matrix is None else np.asarray(matrix, dtype=float)
    
    @classmethod
    def from_Rt(cls, R, t):
        R = np.asarray(R, dtype=float)
        t = np.asarray(t, dtype=float).flatten()[:3]
        M = np.eye(4)
        M[:3, :3] = R
        M[:3, 3] = t
        return cls(M)
    
    @property
    def R(self):
        return self.M[:3, :3]
    
    @property
    def t(self):
        return self.M[:3, 3]
    
    def __matmul__(self, other):
        return Transform(self.M @ other.M)
    
    def inverse(self):
        R_inv = self.R.T
        M_inv = np.eye(4)
        M_inv[:3, :3] = R_inv
        M_inv[:3, 3] = -R_inv @ self.t
        return Transform(M_inv)


# ============================================================================
# Задание 6: Накопление погрешности
# ============================================================================

print("=" * 70)
print("Задание 6: Накопление погрешности при многократной композиции")
print("=" * 70)

# ----------------------------------------------------------------------------
# 6.1. Преобразование малого шага
# ----------------------------------------------------------------------------

# Поворот порядка 10⁻³ рад и сдвиг порядка 10⁻³
STEP_ANGLE = 1e-3
STEP_TRANSLATION = 1e-3

Tstep = Transform.from_Rt(
    rotz(STEP_ANGLE) @ roty(0.5 * STEP_ANGLE) @ rotx(0.3 * STEP_ANGLE),
    [STEP_TRANSLATION, 0.7 * STEP_TRANSLATION, -0.5 * STEP_TRANSLATION]
)

print("\nПреобразование малого шага Tstep:")
print(Tstep)
print(f"\nУгол поворота: ~{STEP_ANGLE:.1e} рад")
print(f"Сдвиг: ~{STEP_TRANSLATION:.1e} м")
print(f"Машинный эпсилон: {np.finfo(float).eps:.3e}")


# ----------------------------------------------------------------------------
# 6.2. Сетка значений N (логарифмическая)
# ----------------------------------------------------------------------------

# Логарифмическая сетка от 10 до 10^5
N_values = np.unique(np.round(np.logspace(1, 5, 25)).astype(int))
print(f"\nКоличество значений N: {len(N_values)}")
print(f"Диапазон N: от {N_values[0]} до {N_values[-1]}")


# ----------------------------------------------------------------------------
# 6.3. Вычисление накопления погрешности
# ----------------------------------------------------------------------------

def accumulate_and_reverse(N, Tstep):
    """
    Выполняет N раз умножение на Tstep, затем N раз на Tstep.inverse().
    Возвращает итоговое преобразование (теоретически — единичная матрица).
    """
    T_acc = Transform()  # начинаем с единичной матрицы
    Tstep_inv = Tstep.inverse()
    
    # N раз умножаем на Tstep
    for _ in range(N):
        T_acc = T_acc @ Tstep
    
    # N раз умножаем на Tstep.inverse()
    for _ in range(N):
        T_acc = T_acc @ Tstep_inv
    
    return T_acc


# Массивы для результатов
errors_matrix = []       # ||T_acc - I||
errors_orth = []         # ||R^T R - I||

print("\nВычисление...")
print(f"{'N':>8} | {'||T-I||':>12} | {'||R^T R - I||':>15} | {'det(R)':>10}")
print("-" * 60)

for N in N_values:
    T_acc = accumulate_and_reverse(N, Tstep)
    
    # Ошибка относительно единичной матрицы
    err_matrix = np.linalg.norm(T_acc.M - np.eye(4))
    
    # Потеря ортогональности
    R = T_acc.R
    err_orth = np.linalg.norm(R.T @ R - np.eye(3))
    
    # Определитель
    det_R = np.linalg.det(R)
    
    errors_matrix.append(err_matrix)
    errors_orth.append(err_orth)
    
    print(f"{N:>8} | {err_matrix:>12.3e} | {err_orth:>15.3e} | {det_R:>10.6f}")

errors_matrix = np.array(errors_matrix)
errors_orth = np.array(errors_orth)


# ----------------------------------------------------------------------------
# 6.4. Оценка наклона (показателя степени)
# ----------------------------------------------------------------------------

log_N = np.log10(N_values)
log_err_matrix = np.log10(np.maximum(errors_matrix, 1e-300))  # чтобы избежать log(0)
log_err_orth = np.log10(np.maximum(errors_orth, 1e-300))

# Линейная регрессия: log(error) = k * log(N) + b
# Наклон k показывает степень роста: error ∝ N^k
slope_matrix, intercept_matrix = np.polyfit(log_N, log_err_matrix, 1)
slope_orth, intercept_orth = np.polyfit(log_N, log_err_orth, 1)

print("\n" + "=" * 70)
print("Оценка наклона (показатель степени роста погрешности):")
print("=" * 70)
print(f"\n||T - I||:           наклон k = {slope_matrix:.4f}")
print(f"||R^T R - I||:       наклон k = {slope_orth:.4f}")
print(f"\nИнтерпретация:")
print(f"  k ≈ 0.5  →  погрешность ∝ √N (случайное блуждание)")
print(f"  k ≈ 1.0  →  погрешность ∝ N  (линейное накопление)")
print(f"  k > 1.0  →  сверхлинейный рост")


# ----------------------------------------------------------------------------
# 6.5. Построение графиков
# ----------------------------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# --- График 1: ||T - I|| ---
ax1 = axes[0]
ax1.loglog(N_values, errors_matrix, 'o-', color='crimson', 
           linewidth=2, markersize=6, label='Измеренная погрешность')

# Референсные линии
N_ref = np.array([N_values[0], N_values[-1]])
# Линия ~ N
ref_N = errors_matrix[0] * (N_ref / N_values[0]) ** 1.0
ax1.loglog(N_ref, ref_N, '--', color='gray', linewidth=1.5, label='~ N (наклон 1)')
# Линия ~ √N
ref_sqrtN = errors_matrix[0] * (N_ref / N_values[0]) ** 0.5
ax1.loglog(N_ref, ref_sqrtN, ':', color='blue', linewidth=1.5, label='~ √N (наклон 0.5)')

# Аппроксимация
fit_line = 10 ** (intercept_matrix + slope_matrix * log_N)
ax1.loglog(N_values, fit_line, '-', color='darkgreen', linewidth=2, 
           label=f'Аппроксимация: k = {slope_matrix:.3f}')

ax1.set_xlabel('N (число шагов)', fontsize=12)
ax1.set_ylabel('||T - I||', fontsize=12)
ax1.set_title('Накопление погрешности матрицы', fontsize=13, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, which='both', alpha=0.3)

# --- График 2: ||R^T R - I|| ---
ax2 = axes[1]
ax2.loglog(N_values, errors_orth, 's-', color='darkblue', 
           linewidth=2, markersize=6, label='Потеря ортогональности')

# Референсные линии
ref_N2 = errors_orth[0] * (N_ref / N_values[0]) ** 1.0
ax2.loglog(N_ref, ref_N2, '--', color='gray', linewidth=1.5, label='~ N (наклон 1)')
ref_sqrtN2 = errors_orth[0] * (N_ref / N_values[0]) ** 0.5
ax2.loglog(N_ref, ref_sqrtN2, ':', color='blue', linewidth=1.5, label='~ √N (наклон 0.5)')

# Аппроксимация
fit_line2 = 10 ** (intercept_orth + slope_orth * log_N)
ax2.loglog(N_values, fit_line2, '-', color='darkgreen', linewidth=2, 
           label=f'Аппроксимация: k = {slope_orth:.3f}')

ax2.set_xlabel('N (число шагов)', fontsize=12)
ax2.set_ylabel('||RᵀR - I||', fontsize=12)
ax2.set_title('Потеря ортогональности матрицы поворота', fontsize=13, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.savefig('error_accumulation.png', dpi=120, bbox_inches='tight')
plt.show()
print("\nРисунок сохранён в файл 'error_accumulation.png'")


# ----------------------------------------------------------------------------
# 6.6. Сравнение с машинным эпсилон
# ----------------------------------------------------------------------------

eps = np.finfo(float).eps

print("\n" + "=" * 70)
print("Сравнение с машинным эпсилон:")
print("=" * 70)
print(f"Машинный эпсилон: eps = {eps:.3e}")
print(f"\nОтношение погрешности к eps:")
print(f"{'N':>8} | {'||T-I||/eps':>15} | {'||R^T R-I||/eps':>18}")
print("-" * 50)
for i, N in enumerate(N_values):
    print(f"{N:>8} | {errors_matrix[i]/eps:>15.2f} | {errors_orth[i]/eps:>18.2f}")


# ----------------------------------------------------------------------------
# 6.7. Оценка опасности погрешности для робота
# ----------------------------------------------------------------------------

print("\n" + "=" * 70)
print("Оценка опасности погрешности для робота")
print("=" * 70)

# Возьмём наибольшее N
N_max = N_values[-1]
T_acc_max = accumulate_and_reverse(N_max, Tstep)

# Ошибка в положении начала координат
origin = np.array([0.0, 0.0, 0.0])
pos_error = np.linalg.norm(T_acc_max.apply_point(origin) - origin)

# Ошибка в ориентации: угол между R и I
R_acc = T_acc_max.R
# Угол поворота матрицы R: arccos((tr(R)-1)/2)
cos_angle = np.clip((np.trace(R_acc) - 1) / 2, -1, 1)
angle_error = np.arccos(cos_angle)

print(f"Для N = {N_max}:")
print(f"  Ошибка положения начала координат: {pos_error:.3e} м")
print(f"  Ошибка угла поворота:              {angle_error:.3e} рад")
print(f"  Ошибка положения в долях атома:    {pos_error / 1e-10:.3e}")
print(f"\nДля робота с рабочей зоной 1 м:")
print(f"  Относительная ошибка:              {pos_error / 1.0:.3e}")
print(f"  Это {'ОПАСНО' if pos_error > 1e-6 else 'БЕЗОПАСНО'}")


# ----------------------------------------------------------------------------
# 6.8. Проверка с другой амплитудой шага
# ----------------------------------------------------------------------------

print("\n" + "=" * 70)
print("Дополнительно: сравнение с разными амплитудами шага")
print("=" * 70)

step_amplitudes = [1e-2, 1e-3, 1e-4]
N_test = 1000

print(f"\nДля N = {N_test}:")
print(f"{'Амплитуда шага':>18} | {'||T-I||':>12} | {'||R^T R-I||':>15}")
print("-" * 55)

for amp in step_amplitudes:
    T_s = Transform.from_Rt(
        rotz(amp) @ roty(0.5 * amp) @ rotx(0.3 * amp),
        [amp, 0.7 * amp, -0.5 * amp]
    )
    T_res = accumulate_and_reverse(N_test, T_s)
    err_m = np.linalg.norm(T_res.M - np.eye(4))
    err_o = np.linalg.norm(T_res.R.T @ T_res.R - np.eye(3))
    print(f"{amp:>18.1e} | {err_m:>12.3e} | {err_o:>15.3e}")