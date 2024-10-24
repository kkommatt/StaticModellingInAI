import numpy as np


def monte_carlo_integral(p, num_samples=100000):
    x = np.random.uniform(0, 1, num_samples)

    f_x = (1 - x ** 2) ** p

    integral_estimate = np.mean(f_x)

    return integral_estimate


p = 2
integral_estimate = monte_carlo_integral(p)
print(f"Приблизне значення інтегралу для p={p}: {integral_estimate}")
