import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from one import Transform, rotz, roty, rotx
from four import PARENT, LOCAL, chain_to_root, world_from, lookup

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(0)

# ============================================================================
# Задание 5: Визуализация дерева координат
# ============================================================================

# Все кадры, включая мировой
ALL_FRAMES = ['world'] + list(PARENT.keys())

# Цвета для осей X, Y, Z (RGB)
AXIS_COLORS = ['red', 'green', 'blue']
AXIS_LABELS = ['X', 'Y', 'Z']

# Длина осей на рисунке
AXIS_LENGTH = 0.18


def draw_frame(ax, T_world_frame, name, axis_length=AXIS_LENGTH):
    """
    Рисует координатный триэдр для кадра.
    
    T_world_frame: преобразование из кадра в мировой
    name: имя кадра (для подписи)
    axis_length: длина осей
    """
    # Начало кадра в мировых координатах
    origin = T_world_frame.apply_point(np.array([0.0, 0.0, 0.0]))
    
    # Концы осей: используем apply_point!
    # Точка (axis_length, 0, 0) в кадре → в мировых координатах
    x_end = T_world_frame.apply_point(np.array([axis_length, 0.0, 0.0]))
    y_end = T_world_frame.apply_point(np.array([0.0, axis_length, 0.0]))
    z_end = T_world_frame.apply_point(np.array([0.0, 0.0, axis_length]))
    
    # Рисуем три отрезка
    for end, color in zip([x_end, y_end, z_end], AXIS_COLORS):
        ax.plot([origin[0], end[0]],
                [origin[1], end[1]],
                [origin[2], end[2]],
                color=color, linewidth=2.5)
    
    # Рисуем точку в начале кадра
    ax.scatter(*origin, color='black', s=30, zorder=5)
    
    # Подписываем кадр
    ax.text(origin[0], origin[1], origin[2] + 0.03, name,
            fontsize=10, fontweight='bold', color='black',
            ha='center', va='bottom')


def draw_tree_connections(ax, parent, world_transforms):
    """Рисует линии, соединяющие кадры (структуру дерева)."""
    for child, p in parent.items():
        if p in world_transforms:
            child_pos = world_transforms[child].apply_point(np.array([0.0, 0.0, 0.0]))
            parent_pos = world_transforms[p].apply_point(np.array([0.0, 0.0, 0.0]))
            
            ax.plot([parent_pos[0], child_pos[0]],
                    [parent_pos[1], child_pos[1]],
                    [parent_pos[2], child_pos[2]],
                    color='gray', linewidth=1.0, linestyle='--', alpha=0.6)


# Вычисляем мировые преобразования для всех кадров
world_transforms = {frame: world_from(frame) for frame in ALL_FRAMES}


# ============================================================================
# Создаём трёхмерный рисунок
# ============================================================================

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Рисуем связи между кадрами (под триэдрами)
draw_tree_connections(ax, PARENT, world_transforms)

# Рисуем триэдр для каждого кадра
for frame in ALL_FRAMES:
    draw_frame(ax, world_transforms[frame], frame)

# Настраиваем оси
ax.set_xlabel('X, м', fontsize=11)
ax.set_ylabel('Y, м', fontsize=11)
ax.set_zlabel('Z, м', fontsize=11)
ax.set_title('Дерево систем координат робота с камерой\n'
             '(оси: X — красный, Y — зелёный, Z — синий)',
             fontsize=13, fontweight='bold')

# Равный масштаб по осям
all_points = np.array([
    world_transforms[f].apply_point(np.array([0.0, 0.0, 0.0]))
    for f in ALL_FRAMES
])
max_range = np.ptp(all_points, axis=0).max() / 2.0
mid = all_points.mean(axis=0)
ax.set_xlim(mid[0] - max_range, mid[0] + max_range)
ax.set_ylim(mid[1] - max_range, mid[1] + max_range)
ax.set_zlim(mid[2] - max_range, mid[2] + max_range)

# Легенда для цветов осей
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='red', lw=2.5, label='Ось X'),
    Line2D([0], [0], color='green', lw=2.5, label='Ось Y'),
    Line2D([0], [0], color='blue', lw=2.5, label='Ось Z'),
    Line2D([0], [0], color='gray', lw=1.0, linestyle='--', label='Связи дерева'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

# Хороший угол обзора
ax.view_init(elev=20, azim=-60)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('frame_tree.png', dpi=120, bbox_inches='tight')
plt.show()

print("Рисунок сохранён в файл 'frame_tree.png'")

# ============================================================================
# Дополнительно: положения кадров и их ориентации
# ============================================================================

print("\n" + "=" * 70)
print("Положения кадров в мировых координатах:")
print("=" * 70)

for frame in ALL_FRAMES:
    T = world_transforms[frame]
    pos = T.apply_point(np.array([0.0, 0.0, 0.0]))
    print(f"  {frame:10}: начало = ({pos[0]:+.3f}, {pos[1]:+.3f}, {pos[2]:+.3f})")

print("\n" + "=" * 70)
print("Ориентации кадров (направления осей в мировых координатах):")
print("=" * 70)

for frame in ALL_FRAMES:
    T = world_transforms[frame]
    # Оси кадра в мировых координатах — это столбцы матрицы R
    x_axis = T.apply_vector(np.array([1.0, 0.0, 0.0]))
    y_axis = T.apply_vector(np.array([0.0, 1.0, 0.0]))
    z_axis = T.apply_vector(np.array([0.0, 0.0, 1.0]))
    print(f"  {frame:10}:")
    print(f"      X_local → ({x_axis[0]:+.3f}, {x_axis[1]:+.3f}, {x_axis[2]:+.3f})")
    print(f"      Y_local → ({y_axis[0]:+.3f}, {y_axis[1]:+.3f}, {y_axis[2]:+.3f})")
    print(f"      Z_local → ({z_axis[0]:+.3f}, {z_axis[1]:+.3f}, {z_axis[2]:+.3f})")

# ============================================================================
# Отдельный рисунок: сравнение кадров wrist и camera
# ============================================================================

print("\n" + "=" * 70)
print("Анализ поворота camera относительно wrist:")
print("=" * 70)

T_camera = LOCAL['camera']
print("\nЛокальное преобразование camera (относительно wrist):")
print("R_camera =")
print(T_camera.R)
print(f"\nt_camera = {T_camera.t}")

print("\nЧто это означает:")
print("  R = rotz(-π/2) @ roty(π/2)")
print("  - Сначала поворот на +90° вокруг Y (roty(π/2))")
print("  - Затем поворот на -90° вокруг Z (rotz(-π/2))")
print("\n  Проверим, куда направлены оси camera в системе wrist:")
x_cam = T_camera.apply_vector(np.array([1.0, 0.0, 0.0]))
y_cam = T_camera.apply_vector(np.array([0.0, 1.0, 0.0]))
z_cam = T_camera.apply_vector(np.array([0.0, 0.0, 1.0]))
print(f"  X_camera в wrist: ({x_cam[0]:+.3f}, {x_cam[1]:+.3f}, {x_cam[2]:+.3f})")
print(f"  Y_camera в wrist: ({y_cam[0]:+.3f}, {y_cam[1]:+.3f}, {y_cam[2]:+.3f})")
print(f"  Z_camera в wrist: ({z_cam[0]:+.3f}, {z_cam[1]:+.3f}, {z_cam[2]:+.3f})")


# ============================================================================
# Второй рисунок: только локальные оси каждого кадра с относительными связями
# ============================================================================

fig2 = plt.figure(figsize=(14, 10))
ax2 = fig2.add_subplot(111, projection='3d')

# Рисуем связи между кадрами
draw_tree_connections(ax2, PARENT, world_transforms)

# Рисуем триэдры с увеличенной длиной осей
for frame in ALL_FRAMES:
    draw_frame(ax2, world_transforms[frame], frame, axis_length=0.22)

ax2.set_xlabel('X, м', fontsize=11)
ax2.set_ylabel('Y, м', fontsize=11)
ax2.set_zlabel('Z, м', fontsize=11)
ax2.set_title('Дерево систем координат (увеличенные триэдры)',
              fontsize=13, fontweight='bold')

# Равный масштаб
ax2.set_xlim(mid[0] - max_range, mid[0] + max_range)
ax2.set_ylim(mid[1] - max_range, mid[1] + max_range)
ax2.set_zlim(mid[2] - max_range, mid[2] + max_range)

ax2.legend(handles=legend_elements, loc='upper left', fontsize=10)
ax2.view_init(elev=20, azim=-60)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('frame_tree_large.png', dpi=120, bbox_inches='tight')
plt.show()