import numpy as np
import matplotlib.pyplot as plt
from one import Transform, rotz, roty, rotx

PARENT = {'base': 'world', 'table': 'world', 'shoulder': 'base', 'elbow': 'shoulder',
          'wrist': 'elbow', 'camera': 'wrist', 'object': 'table'}

LOCAL = {
    'base':     Transform.from_Rt(rotz(0.30), [0.00, 0.00, 0.20]),
    'table':    Transform.from_Rt(np.eye(3),  [1.20, 0.40, 0.00]),
    'shoulder': Transform.from_Rt(roty(0.45), [0.00, 0.00, 0.35]),
    'elbow':    Transform.from_Rt(roty(-0.80), [0.40, 0.00, 0.00]),
    'wrist':    Transform.from_Rt(rotx(0.60), [0.35, 0.00, 0.00]),
    'camera':   Transform.from_Rt(rotz(-np.pi / 2) @ roty(np.pi / 2), [0.05, 0.00, 0.10]),
    'object':   Transform.from_Rt(rotz(1.10), [0.10, -0.15, 0.75]),
}


def chain_to_root(frame):
    chain = []
    current = frame
    while current in PARENT:  # пока есть родитель
        chain.append(current)
        current = PARENT[current]
    chain.append(current)  # добавляем корень (world)
    return chain


# ----------------------------------------------------------------------------
# 4.2. Функция world_from(frame)
# ----------------------------------------------------------------------------

def world_from(frame):
    """
    Возвращает преобразование из кадра frame в мировой кадр (world).
    T_world_frame = T_world_parent · T_parent_grandparent · ... · T_frame_parent
    """
    if frame == 'world':
        return Transform()  # единичная матрица
    
    # Получаем цепочку от frame до корня
    chain = chain_to_root(frame)
    # chain = ['frame', 'parent', ..., 'world']
    # Нам нужны преобразования вдоль цепи
    # T_world_frame = T_world_parent @ T_parent_grandparent @ ... @ T_frame_parent
    
    result = Transform()  # начинаем с единичной матрицы
    # Идём от корня к frame (в обратном порядке)
    # chain = ['camera', 'wrist', 'elbow', 'shoulder', 'base', 'world']
    # Нужно перемножить: LOCAL['world'] @ LOCAL['base'] @ LOCAL['shoulder'] @ ...
    # Но LOCAL не содержит 'world', поэтому начинаем со следующего
    
    # Идём от frame к корню и собираем преобразования
    transforms = []
    current = frame
    while current in PARENT:
        transforms.append(LOCAL[current])  # добавляем локальное преобразование
        current = PARENT[current]
    # transforms = [LOCAL[frame], LOCAL[parent], ..., LOCAL[child_of_world]]
    
    # Перемножаем в правильном порядке: от корня к frame
    # T_world_frame = T_world_parent @ T_parent_grandparent @ ... @ T_frame_parent
    result = Transform()
    for T in reversed(transforms):
        result = result @ T  # применяем преобразования от корня к frame
    
    return result


# ----------------------------------------------------------------------------
# 4.3. Функция lookup(target, source)
# ----------------------------------------------------------------------------

def lookup(target, source):
    """
    Возвращает преобразование из системы координат source в target.
    T_target_source = T_target_world @ T_world_source
    где T_target_world = inverse(T_world_target)
    """
    if target == source:
        return Transform()  # если один и тот же кадр — единичное преобразование
    
    T_world_target = world_from(target)
    T_world_source = world_from(source)
    
    # T_target_source = T_target_world @ T_world_source
    # T_target_world = inverse(T_world_target)
    T_target_world = T_world_target.inverse()
    
    return T_target_world @ T_world_source

# ============================================================================
# Проверка 1: lookup(a,b) @ lookup(b,a) = I
# ============================================================================

print("\n" + "-" * 70)
print("Проверка 1: lookup(a,b) @ lookup(b,a) = I")

# Проверяем для всех пар кадров
frames = list(PARENT.keys()) + ['world']
errors = []

for a in frames:
    for b in frames:
        Tab = lookup(a, b)
        Tba = lookup(b, a)
        product = Tab @ Tba
        error = np.linalg.norm(product.M - np.eye(4))
        errors.append(error)

max_error = max(errors)
print(f"Максимальная ошибка ||lookup(a,b)@lookup(b,a) - I|| = {max_error:.3e}")

if max_error < 1e-12:
    print("Проверка пройдена! Все преобразования взаимно обратны.")
else:
    print(f"Ошибка больше ожидаемой: {max_error:.3e}")


# ============================================================================
# Проверка 2: результат через lookup совпадает с ручным пересчётом
# ============================================================================

print("\n" + "-" * 70)
print("Проверка 2: результат через lookup совпадает с ручным пересчётом")

# Ручной пересчёт: T_camera_object = inverse(T_world_camera) @ T_world_object
T_world_camera = world_from('camera')
T_world_object = world_from('object')
T_camera_object_manual = T_world_camera.inverse() @ T_world_object

# Сравниваем с lookup
T_camera_object_lookup = lookup('camera', 'object')
diff = np.linalg.norm(T_camera_object_lookup.M - T_camera_object_manual.M)

print(f"Разница между lookup и ручным пересчётом: {diff:.3e}")

# Проверяем положение точки
origin = np.array([0.0, 0.0, 0.0])
p_lookup = T_camera_object_lookup.apply_point(origin)
p_manual = T_camera_object_manual.apply_point(origin)
point_diff = np.linalg.norm(p_lookup - p_manual)

print(f"Положение object в camera через lookup: {p_lookup}")
print(f"Положение object в camera вручную:      {p_manual}")
print(f"Разница в положении точки: {point_diff:.3e}")

if diff < 1e-12:
    print("Проверка пройдена! Результаты совпадают.")
else:
    print(f"Результаты отличаются: {diff:.3e}")

