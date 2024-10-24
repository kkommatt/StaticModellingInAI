import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest

realization_X = np.random.uniform(0, 1, 1000)

estimated_mean = np.mean(realization_X)
estimated_variance = np.var(realization_X)
theoretical_mean = 0.5
theoretical_variance = 1/12

print(f"Експерементальне середнє: {estimated_mean}")
print(f"Theoretical Mean: {theoretical_mean}")
print(f"Експерементальне відхилення: {estimated_variance}")
print(f"Теоретичне відхилення: {theoretical_variance}")

plt.hist(realization_X, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')

x = np.linspace(0, 1, 100)
plt.plot(x, np.ones_like(x), 'r-', lw=2, label='Теоретичне відхилення')

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Універсальний розподіл та експерементальний розподіл')
plt.legend()
plt.show()

ks_stat, p_value = kstest(realization_X, 'uniform', args=(0, 1))

print(f"Колмогоров-Смірнов: {ks_stat}")
print(f"р: {p_value}")

if p_value > 0.05:
    print("Експерементальний розподіл відповідає універсальному")
else:
    print("Експерементальний розподіл не відповідає універсальному")
