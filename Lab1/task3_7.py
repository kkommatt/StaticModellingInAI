import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rayleigh, kstest

sigma = 1

eta1 = np.random.normal(0, sigma, 1000)
eta2 = np.random.normal(0, sigma, 1000)

realization_X = np.sqrt(eta1**2 + eta2**2)

estimated_mean = np.mean(realization_X)
estimated_variance = np.var(realization_X)

theoretical_mean = sigma * np.sqrt(np.pi / 2)
theoretical_variance = (2 - np.pi / 2) * sigma**2

print(f"Експерементальне середнє: {estimated_mean}")
print(f"Теоретичне середнє: {theoretical_mean}")
print(f"Експерементальне відхилення: {estimated_variance}")
print(f"Теоретичне відхилення: {theoretical_variance}")

plt.hist(realization_X, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')

x = np.linspace(0, max(realization_X), 100)
plt.plot(x, rayleigh.pdf(x, scale=sigma), 'r-', lw=2, label='Рейля розподіл')

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Розподіл Рейля та експерементальний розподіл')
plt.legend()
plt.show()

ks_stat, p_value = kstest(realization_X, 'rayleigh', args=(0, sigma))

print(f"Колмогоров-Смірнов: {ks_stat}")
print(f"р: {p_value}")

if p_value > 0.05:
    print("Експерементальний розподіл відповідає розподілу Рейля")
else:
    print("Експерементальний розподіл не відповідає розподілу Рейля")
