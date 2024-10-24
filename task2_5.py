import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, chisquare

lambda_param = 5
realization = np.random.poisson(lambda_param, 1000)

values, counts = np.unique(realization, return_counts=True)
experimental_frequencies = counts / len(realization)

plt.hist(realization, bins=range(0, max(realization)+1), density=True, alpha=0.6, color='g', edgecolor='black')
x = np.arange(0, max(realization)+1)
plt.plot(x, poisson.pmf(x, lambda_param), 'bo', ms=8, label='Пуассон')
plt.vlines(x, 0, poisson.pmf(x, lambda_param), colors='b', lw=5, alpha=0.5)

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Розподіл Пуасона та експерементальний розподіл')
plt.legend()
plt.show()

expected_frequencies = poisson.pmf(values, lambda_param) * len(realization)

expected_frequencies *= counts.sum() / expected_frequencies.sum()

chi2_stat, p_value = chisquare(counts, expected_frequencies)

print(f"Хі квадрат: {chi2_stat}")
print(f"p: {p_value}")

if p_value > 0.05:
    print("Експерементальний розподіл відповідає Пуассону")
else:
    print("Експерементальний розподіл не відповідає Пуассону")
