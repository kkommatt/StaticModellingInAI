import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto, kstest

shape_param = 2.5
scale_param = 1

u = np.random.uniform(0, 1, 1000)
realization_X = scale_param / (u ** (1 / shape_param))

estimated_mean = np.mean(realization_X)
estimated_variance = np.var(realization_X)

if shape_param > 1:
    theoretical_mean = shape_param * scale_param / (shape_param - 1)
else:
    theoretical_mean = np.inf

if shape_param > 2:
    theoretical_variance = (shape_param * scale_param**2) / ((shape_param - 1)**2 * (shape_param - 2))
else:
    theoretical_variance = np.inf

print(f"Експерементальне середнє: {estimated_mean}")
print(f"Теоретичне середнє: {theoretical_mean}")
print(f"Експерементальне відхилення: {estimated_variance}")
print(f"Теоретичне відхилення: {theoretical_variance}")

plt.hist(realization_X, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')

x = np.linspace(scale_param, max(realization_X), 100)
plt.plot(x, pareto.pdf(x, shape_param, scale=scale_param), 'r-', lw=2, label='Розподіл Парета')

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Парето розподіл та екперементальний розподіл')
plt.legend()
plt.show()

ks_stat, p_value = kstest(realization_X, 'pareto', args=(shape_param,))

print(f"Колмогоров-Смірнов: {ks_stat}")
print(f"р: {p_value}")

if p_value > 0.05:
    print("Експерементальний розподіл відповідає Парето")
else:
    print("Експерементальний розподіл не відповідає Парето")