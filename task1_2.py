import numpy as np


def die_roll_simulation(N, K):
    rolls = np.random.randint(1, 7, size=(K, N))

    count_per_digit = np.zeros(6, dtype=int)

    for i in range(1, 7):
        count_per_digit[i - 1] = np.sum(rolls == i)

    return count_per_digit


N = 100
K = 11

digit_counts = die_roll_simulation(N, K)

for i in range(1, 7):
    print(f"Count of {i}: {digit_counts[i - 1]}")

print("Total rolls across all simulations:", N * K)
