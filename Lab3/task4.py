import numpy as np


def setup_boxes():
    return np.random.permutation(100) + 1


def prisoner_random_choice(boxes, num_prisoners, max_attempts):
    success_count = 0
    for prisoner in range(1, num_prisoners + 1):
        attempts = np.random.choice(100, max_attempts, replace=False)
        if prisoner in boxes[attempts]:
            success_count += 1
    return success_count


def prisoner_algorithm_choice(boxes, num_prisoners, max_attempts):
    success_count = 0
    for prisoner in range(1, num_prisoners + 1):
        current_box = prisoner
        for attempt in range(max_attempts):
            if boxes[current_box - 1] == prisoner:
                success_count += 1
                break
            current_box = boxes[current_box - 1]
    return success_count


def simulate_game(num_simulations, num_prisoners, max_attempts, choice_function):
    success_rate = []
    for _ in range(num_simulations):
        boxes = setup_boxes()
        success_count = choice_function(boxes, num_prisoners, max_attempts)
        success_rate.append(success_count == num_prisoners)
    return np.mean(success_rate)


num_simulations = 1000
num_prisoners = 100
max_attempts = 50

# Ймовірність випадкового вибору
random_success_rate = simulate_game(num_simulations, num_prisoners, max_attempts, prisoner_random_choice)
print("Ймовірність виживання при випадковому виборі:", random_success_rate)

# Ймовірність алгоритму ув'язнених
algorithm_success_rate = simulate_game(num_simulations, num_prisoners, max_attempts, prisoner_algorithm_choice)
print("Ймовірність виживання за алгоритмом ув'язнених:", algorithm_success_rate)

max_attempts_60 = 60
max_attempts_75 = 75

# 60
algorithm_success_rate_60 = simulate_game(num_simulations, num_prisoners, max_attempts_60, prisoner_algorithm_choice)
print("Ймовірність виживання за алгоритмом ув'язнених (60 спроб):", algorithm_success_rate_60)

# 75
algorithm_success_rate_75 = simulate_game(num_simulations, num_prisoners, max_attempts_75, prisoner_algorithm_choice)
print("Ймовірність виживання за алгоритмом ув'язнених (75 спроб):", algorithm_success_rate_75)
