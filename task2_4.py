import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, chisquare

n = 10
p = 0.3
n_simulations = 1000

results = np.random.binomial(n, p, n_simulations)

experimental_counts = np.zeros(n + 1)
for count in results:
    experimental_counts[count] += 1

experimental_probs = experimental_counts / n_simulations

theoretical_probs = binom.pmf(np.arange(n + 1), n, p)

x_values = np.arange(n + 1)
plt.bar(x_values - 0.2, theoretical_probs, width=0.4, label='Теоретичний розподіл', alpha=0.7)
plt.bar(x_values + 0.2, experimental_probs, width=0.4, label='Експерементальний розподіл', alpha=0.7)
plt.xticks(x_values)
plt.xlabel('Кількість успіхів')
plt.ylabel('Ймовірність')
plt.title('Теоретичний і есперементальний розподіли')
plt.legend()
plt.show()

chi2_stat, p_value = chisquare(f_obs=experimental_probs, f_exp=theoretical_probs)
print(f"Хі квадрат: {chi2_stat}, p: {p_value}")

alpha = 0.05
if p_value > alpha:
    print("Експерементальний розподіл відповідає теоретичному")
else:
    print("Експерементальний розподіл не відповідає теоретичному")
