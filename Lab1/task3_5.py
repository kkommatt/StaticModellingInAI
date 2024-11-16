import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma, kstest

shape_param = 2
scale_param = 2

realization_X = np.random.gamma(shape_param, scale_param, 1000)

estimated_mean = np.mean(realization_X)
estimated_variance = np.var(realization_X)

theoretical_mean = shape_param * scale_param
theoretical_variance = shape_param * (scale_param ** 2)

print(f"Експерементальне середнє: {estimated_mean}")
print(f"Теоретичне середнє: {theoretical_mean}")
print(f"Експерементальне відхилення: {estimated_variance}")
print(f"Теоретичне відхилення: {theoretical_variance}")

plt.hist(realization_X, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')

x = np.linspace(0, max(realization_X), 100)
plt.plot(x, gamma.pdf(x, shape_param, scale=scale_param), 'r-', lw=2, label='Гамма розподіл')

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Гамма розподіл та експерементальний розподіл')
plt.legend()
plt.show()

ks_stat, p_value = kstest(realization_X, 'gamma', args=(shape_param, 0, scale_param))

print(f"Колмогоров-Смірно: {ks_stat}")
print(f"р: {p_value}")

if p_value > 0.05:
    print("Експерементальний розподіл відповідає Гамма розподілу")
else:
    print("Експерементальний розподіл не відповідає Гамма розподілу")
