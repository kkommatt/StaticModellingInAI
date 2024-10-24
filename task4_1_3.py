import numpy as np


def monte_carlo_integral(num_samples=100000):
    x = np.random.uniform(0, 1, num_samples)

    f_x = 1 / (1 - x + x ** 2)

    integral_estimate = np.mean(f_x)

    return integral_estimate

integral_estimate = monte_carlo_integral()
print(f"Приблизне значення інтегралу: {integral_estimate}")
