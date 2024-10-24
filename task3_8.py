import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy, kstest

eta1 = np.random.normal(0, 1, 1000)
eta2 = np.random.normal(0, 1, 1000)

realization_X = eta1 / eta2

estimated_mean = np.mean(realization_X)
estimated_variance = np.var(realization_X)

print(f"Експерементальне середнє: {estimated_mean}")
print(f"Експерементальне відхилення: {estimated_variance}")

plt.hist(realization_X, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')

x = np.linspace(min(realization_X), max(realization_X), 100)
plt.plot(x, cauchy.pdf(x), 'r-', lw=2, label='Розподіл Коші')

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Коші розподіл та експерементальний розподіл')
plt.legend()
plt.show()

ks_stat, p_value = kstest(realization_X, 'cauchy')

print(f"Колмогоров-Смірнов: {ks_stat}")
print(f"p: {p_value}")

if p_value > 0.05:
    print("Експерементальний розподіл відповідає розподілу Коші")
else:
    print("Експерементальний розподіл не відповідає розподілу Коші")
