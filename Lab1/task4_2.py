import numpy as np
from scipy.integrate import quad

def integrand(u):
    return np.exp(-u**2 / 2)

def f(x):
    integral_value, _ = quad(integrand, 0, x)
    return (1 / np.sqrt(2 * np.pi)) * integral_value

m = 3
xi_values = [round(i * m * 0.1, 2) for i in range(1, 6)]

results = {xi: f(xi) for xi in xi_values}

for xi, value in results.items():
    print(f"f({xi}) = {value}")
