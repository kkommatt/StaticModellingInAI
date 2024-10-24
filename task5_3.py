import numpy as np

def f(x1, x2):
    return 5 * x1**2 + 3 * x2**2 - np.cos(x1 / 2) * np.cos(x2 / np.sqrt(3)) + 1

num_samples = 100000
x1_samples = np.random.uniform(-10, 10, num_samples)
x2_samples = np.random.uniform(-10, 10, num_samples)

f_values = f(x1_samples, x2_samples)

min_index = np.argmin(f_values)
max_index = np.argmax(f_values)

min_value = f_values[min_index]
max_value = f_values[max_index]

min_point = (x1_samples[min_index], x2_samples[min_index])
max_point = (x1_samples[max_index], x2_samples[max_index])

print(f"Мінімум: {min_value} в точці {float(min_point[0]), float(min_point[1])}")
print(f"Максимум: {max_value} в точці {float(max_point[0]), float(max_point[1])}")
