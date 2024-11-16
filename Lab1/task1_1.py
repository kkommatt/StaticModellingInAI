import numpy as np


def coin_toss_simulation(N, K):
    tosses = np.random.randint(0, 2, size=(K, N))

    coat_of_arms_count = np.sum(tosses, axis=1)

    total_coat_of_arms = np.sum(coat_of_arms_count)

    return coat_of_arms_count, total_coat_of_arms


N = 100
K = 1000

coat_of_arms_count_per_simulation, total_coat_of_arms = coin_toss_simulation(N, K)

print("Count of coat of arms in each simulation:", coat_of_arms_count_per_simulation)
print("Total count of coat of arms across all simulations:", total_coat_of_arms)
