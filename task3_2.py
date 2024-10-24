import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest

a = 2
b = 10

u = np.random.uniform(0, 1, 1000)
realization_X = a + (b - a) * u

estimated_mean = np.mean(realization_X)
estimated_variance = np.var(realization_X)

theoretical_mean = (a + b) / 2
theoretical_variance = ((b - a) ** 2) / 12

print(f"Експерементальне середнє: {estimated_mean}")
print(f"Theoretical Mean: {theoretical_mean}")
print(f"Експерементальне відхилення: {estimated_variance}")
print(f"Теоретичне відхилення: {theoretical_variance}")

plt.hist(realization_X, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')

x = np.linspace(a, b, 100)
plt.plot(x, np.ones_like(x) / (b - a), 'r-', lw=2, label='Теоретичний розподіл')

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Універсальний розподіл та теоретичний розподіл')
plt.legend()
plt.show()

ks_stat, p_value = kstest(realization_X, 'uniform', args=(a, b-a))

print(f"Колмогоров-Смірнов: {ks_stat}")
print(f"р: {p_value}")

if p_value > 0.05:
    print("Експерементальний розподіл відповідає універсальному")
else:
    print("Експерементальний розподіл не відповідає універсальному")