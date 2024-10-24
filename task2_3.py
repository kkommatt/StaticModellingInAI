import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

theoretical_probs = np.array([1/16, 1/4, 3/8, 1/4, 1/16])
x_values = np.array([0, 1, 2, 3, 4])

n_simulations = 1000
n_coins = 4

tosses = np.random.randint(0, 2, (n_simulations, n_coins))
heads_count = tosses.sum(axis=1)

experimental_counts = np.zeros(5)
for count in heads_count:
    experimental_counts[count] += 1

experimental_probs = experimental_counts / n_simulations

plt.bar(x_values - 0.2, theoretical_probs, width=0.4, label='Теоретичний розподіл', alpha=0.7)
plt.bar(x_values + 0.2, experimental_probs, width=0.4, label='Експерементальний розподіл', alpha=0.7)
plt.xticks(x_values)
plt.xlabel('Кількість')
plt.ylabel('Ймовірність')
plt.title('Теоретичний і експерементальний розподіли')
plt.legend()
plt.show()

chi2_stat, p_value = chisquare(f_obs=experimental_probs, f_exp=theoretical_probs)
print(f"Хі квадрат: {chi2_stat}, p: {p_value}")

alpha = 0.05
if p_value > alpha:
    print("Експерементальний розподіл відповідає теоретичному")
else:
    print("Експерементальний розподіл не відповідає теоретичному")
