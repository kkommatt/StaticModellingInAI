import numpy as np
import matplotlib.pyplot as plt
from scipy.special import beta as beta_function


def beta_distribution(x, alpha, beta):
    return (x ** (alpha - 1) * (1 - x) ** (beta - 1)) / beta_function(alpha, beta)


def metropolis_hastings(beta_dist, alpha, beta, num_samples=1000):
    samples = []
    current_sample = np.random.rand()

    for _ in range(num_samples):
        proposed_sample = current_sample + np.random.normal(0, 0.1)
        proposed_sample = np.clip(proposed_sample, 0, 1)

        acceptance_ratio = beta_dist(proposed_sample, alpha, beta) / beta_dist(current_sample, alpha, beta)

        if np.random.rand() < acceptance_ratio:
            current_sample = proposed_sample

        samples.append(current_sample)

    return np.array(samples)


alpha = 2
beta = 5
num_samples = 1000

samples = metropolis_hastings(beta_distribution, alpha, beta, num_samples)

x = np.linspace(0, 1, 1000)
y = beta_distribution(x, alpha, beta)

plt.figure(figsize=(10, 6))
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Гістограма вибірок')
plt.plot(x, y, 'r-', lw=2, label='Щільність розподілу бета')
plt.xlabel('x')
plt.ylabel('Щільність')
plt.title('Розподіл бета за допомогою алгоритму Метрополіса-Хастінгса')
plt.legend()
plt.show()
