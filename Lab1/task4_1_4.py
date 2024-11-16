import numpy as np


def monte_carlo_integral(m, n, num_samples=100000):
    x = np.random.uniform(0, 1, num_samples)

    f_x = (x ** (m - 1) + x ** (n - 1)) / (1 + x) ** (m + n)

    integral_estimate = np.mean(f_x)

    return integral_estimate


m = 2
n = 3
integral_estimate = monte_carlo_integral(m, n)
print(f"Приблизне значення інтегралу для m={m} та n={n}: {integral_estimate}")
