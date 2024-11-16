import numpy as np
from scipy.integrate import quad

def integrand(x, n):
    return x**(n - 1) * np.exp(-x)

n_values = [1/2, 1, 3/2, 2, 4]
results = {n: quad(integrand, 0, np.inf, args=(n))[0] for n in n_values}

for n, value in results.items():
    print(f"Значення інтегралу для n={n}: {round(value, 2)}")
