import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

theoretical_distribution = np.zeros(13)

for die1 in range(1, 7):
    for die2 in range(1, 7):
        theoretical_distribution[die1 + die2] += 1

theoretical_distribution = theoretical_distribution / theoretical_distribution.sum()

n_simulations = 1000
rolls = np.random.randint(1, 7, (n_simulations, 2))
sums = rolls.sum(axis=1)

experimental_distribution = np.zeros(13)
for sum_value in sums:
    experimental_distribution[sum_value] += 1

experimental_distribution = experimental_distribution / n_simulations

x = np.arange(2, 13)
plt.bar(x - 0.2, theoretical_distribution[2:13], width=0.4, label='Теоретичний розподіл', alpha=0.7)
plt.bar(x + 0.2, experimental_distribution[2:13], width=0.4, label='Експерементальний розподіл', alpha=0.7)
plt.xticks(x)
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Теоретичний і експерементальний розподіли')
plt.legend()
plt.show()

chi2_stat, p_value = chisquare(f_obs=experimental_distribution[2:13], f_exp=theoretical_distribution[2:13])
print(f"Хі квадрат: {chi2_stat}, p: {p_value}")

alpha = 0.05
if p_value > alpha:
    print("Експерементальний розподіл відповідає теоретичному")
else:
    print("Експерементальний розподіл не відповідає теоретичному")
