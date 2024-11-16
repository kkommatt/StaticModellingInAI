import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom, chisquare
p = 0.5
realization_X = np.random.geometric(p, 1000)
realization_Y = realization_X - 1
values_X, counts_X = np.unique(realization_X, return_counts=True)
experimental_frequencies_X = counts_X / len(realization_X)

values_Y, counts_Y = np.unique(realization_Y, return_counts=True)
experimental_frequencies_Y = counts_Y / len(realization_Y)

plt.hist(realization_X, bins=range(1, max(realization_X)+2), density=True, alpha=0.6, color='g', edgecolor='black')

x = np.arange(1, max(realization_X)+1)
plt.plot(x, geom.pmf(x, p), 'bo', ms=8, label='Геометричний розподіл')
plt.vlines(x, 0, geom.pmf(x, p), colors='b', lw=5, alpha=0.5)

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Геометричний розподіл та експерементальний для X')
plt.legend()
plt.show()
plt.hist(realization_Y, bins=range(0, max(realization_Y)+2), density=True, alpha=0.6, color='g', edgecolor='black')

y = np.arange(0, max(realization_Y)+1)
plt.plot(y, geom.pmf(y+1, p), 'bo', ms=8, label='geometric pmf')
plt.vlines(y, 0, geom.pmf(y+1, p), colors='b', lw=5, alpha=0.5)

plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Геометричний розподіл та експерементальний розподіл для Y')
plt.legend()
plt.show()

expected_frequencies_X = geom.pmf(values_X, p) * len(realization_X)
expected_frequencies_X *= counts_X.sum() / expected_frequencies_X.sum()
chi2_stat_X, p_value_X = chisquare(counts_X, expected_frequencies_X)

print(f"Хі квадрат для X: {chi2_stat_X}")
print(f"p для X: {p_value_X}")

if p_value_X > 0.05:
    print("Експерементальний розподіл відповідає геометричному для X")
else:
    print("Експерементальний розподіл не відповідає геометричному для X")
expected_frequencies_Y = geom.pmf(values_Y+1, p) * len(realization_Y)
expected_frequencies_Y *= counts_Y.sum() / expected_frequencies_Y.sum()
chi2_stat_Y, p_value_Y = chisquare(counts_Y, expected_frequencies_Y)

print(f"Хі квадрат для Y: {chi2_stat_Y}")
print(f"р для Y: {p_value_Y}")

if p_value_Y > 0.05:
    print("Експерементальний розподіл відповідає геометричному для Y")
else:
    print("Експерементальний розподіл відповідає геометричному для Y")
