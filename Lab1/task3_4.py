import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, kstest
mean_param = 0
std_dev_param = 1

realization_X = np.random.normal(mean_param, std_dev_param, 1000)

estimated_mean = np.mean(realization_X)
estimated_variance = np.var(realization_X)

theoretical_mean = mean_param
theoretical_variance = std_dev_param ** 2

print(f"Експерементальне середнє: {estimated_mean}")
print(f"Теоретичне середнє: {theoretical_mean}")
print(f"Експерементальне відхилення: {estimated_variance}")
print(f"Теоретичне відхилення: {theoretical_variance}")

plt.hist(realization_X, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')

x = np.linspace(min(realization_X), max(realization_X), 100)
plt.plot(x, norm.pdf(x, mean_param, std_dev_param), 'r-', lw=2, label='Нормальний розподіл')

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Нормальний розподіл та експерементальний розподіл')
plt.legend()
plt.show()

ks_stat, p_value = kstest(realization_X, 'norm', args=(mean_param, std_dev_param))

print(f"Колмогоров-Смірнов: {ks_stat}")
print(f"р: {p_value}")

if p_value > 0.05:
    print("Експерементальний розподіл відповідає нормальному розподілу")
else:
    print("Експерементальний розподіл не відповідає нормальному розподілу")
