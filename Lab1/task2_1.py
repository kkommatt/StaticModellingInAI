import numpy as np

n = 100
probabilities = [1 / 6] * 6
values = [1, 2, 3, 4, 5, 6]

realizations = np.random.choice(values, size=n, p=probabilities)

sample_mean = np.mean(realizations)

theoretical_mean = 3.5

print(f"Середнє: {sample_mean}")
print(f"Теоретичне середнє: {theoretical_mean}")
