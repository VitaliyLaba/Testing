import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Функція, яку ми максимізуємо
def objective_function(x, y):
    return -4 * x**2 - 2 * x * y - y**2 + 16 * x + 10 * y - 2

# Початкова точка x = 0.0, y = 0.0
x, y = 0.0, 0.0

# Запускаємо оптимізацію для максимізації
result = minimize_scalar(lambda alpha: -objective_function(x - alpha * (8*x + 2), y - alpha * (8*y - 4)))

# Знайдений максимум та його значення
max_alpha = result.x
max_x, max_y = x - max_alpha * (8*x + 2), y - max_alpha * (8*y - 4)
max_value = objective_function(max_x, max_y)

print(f"Максимум знайдений в точці ({max_x}, {max_y}) зі значенням {max_value}")

# Створюємо масив точок для графіку
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = objective_function(X, Y)

# Побудова графіку
plt.contour(X, Y, Z, levels=50, cmap='viridis')  # Контурний графік функції
plt.scatter(max_x, max_y, color='red', label=f'Maximum: ({max_x:.2f}, {max_y:.2f})')  # Позначаємо максимум червоним кругом
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Контурний графік функції з максимумом (за допомогою методу золотого перетину)')
plt.show()
