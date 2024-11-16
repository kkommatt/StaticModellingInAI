import numpy as np

# Перехідна матриця для поглинаючого ланцюга Маркова
P_absorbing = np.array([
    [0.5, 0.5, 0, 0, 0, 0, 0],
    [0.2, 0.5, 0.3, 0, 0, 0, 0],
    [0, 0.3, 0.4, 0.3, 0, 0, 0],
    [0, 0, 0.3, 0.4, 0.3, 0, 0],
    [0, 0, 0, 0.3, 0.4, 0.3, 0],
    [0, 0, 0, 0, 0.3, 0.4, 0.3],
    [0, 0, 0, 0, 0, 0, 1]
])

# Початковий вектор стану (без поглинання)
initial_state = np.array([1, 0, 0, 0, 0, 0, 0])

# Кількість реалізацій
num_realizations = 100


def simulate_markov_chain(P, initial_state, num_realizations):
    num_states = P.shape[0]
    realizations = []

    for _ in range(num_realizations):
        state = initial_state
        states_sequence = [state]
        while not np.isclose(state[-1], 1):  # До поглинання
            state = np.dot(state, P)
            states_sequence.append(state)
        realizations.append(states_sequence)
    return realizations


absorbing_realizations = simulate_markov_chain(P_absorbing, initial_state, num_realizations)


def calculate_transient_probabilities(realizations):
    num_states = len(realizations[0][0])
    transient_matrix = np.zeros((num_states, num_states))

    for sequence in realizations:
        for i in range(len(sequence) - 1):
            transient_matrix += np.outer(sequence[i], sequence[i + 1])

    transient_matrix /= len(realizations)
    return transient_matrix


transient_prob_matrix = calculate_transient_probabilities(absorbing_realizations)
print("Матриця перехідних ймовірностей:\n", transient_prob_matrix)


def calculate_time_spent(realizations):
    num_states = len(realizations[0][0])
    time_spent = np.zeros(num_states)

    for sequence in realizations:
        for state in sequence:
            time_spent += state

    time_spent /= len(realizations)
    return time_spent


time_spent_in_states = calculate_time_spent(absorbing_realizations)
print("Час витрачений у кожному стані:\n", time_spent_in_states)


def calculate_absorption_characteristics(realizations):
    absorption_times = []
    for sequence in realizations:
        absorption_times.append(len(sequence))

    absorption_time = np.mean(absorption_times)
    absorption_probability = np.array([state[-1] for state in realizations[-1]])

    return absorption_time, absorption_probability


absorption_time, absorption_probability = calculate_absorption_characteristics(absorbing_realizations)
print("Час поглинання:", absorption_time)
print("Ймовірність поглинання:", absorption_probability)

# Матриця переходів для ланцюга Маркова
P_regular = np.array([
    [0.2, 0.3, 0.2, 0.1, 0.1, 0.05, 0.05],
    [0.3, 0.3, 0.2, 0.1, 0.05, 0.05, 0],
    [0.2, 0.2, 0.3, 0.2, 0.05, 0.05, 0],
    [0.1, 0.2, 0.2, 0.3, 0.1, 0.1, 0],
    [0.1, 0.1, 0.2, 0.2, 0.3, 0.1, 0],
    [0.05, 0.1, 0.1, 0.2, 0.3, 0.25, 0],
    [0.05, 0, 0, 0.1, 0.2, 0.65, 0]
])

initial_state_regular = np.array([1, 0, 0, 0, 0, 0, 0])

# Кількість реалізацій
num_realizations = 100

regular_realizations = simulate_markov_chain(P_regular, initial_state_regular, num_realizations)


def calculate_steady_state_characteristics(P):
    eigvals, eigvecs = np.linalg.eig(P.T)
    steady_state = np.real(eigvecs[:, np.isclose(eigvals, 1)].flatten().real)
    steady_state /= steady_state.sum()
    return steady_state


steady_state_probabilities = calculate_steady_state_characteristics(P_regular)
print("Ймовірності стаціонарного стану:\n", steady_state_probabilities)
