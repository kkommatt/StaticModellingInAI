import numpy as np
import matplotlib.pyplot as plt

num_steps = 1000
T = 1
dt = T / num_steps
num_implementations = 200
target_level = 1.0

# Симуляція Віннерівського процесу
time = np.linspace(0, T, num_steps)
wiener_processes = []

for _ in range(num_implementations):
    increments = np.random.normal(loc=0, scale=np.sqrt(dt), size=num_steps)
    # Обрахунок Віннерівського процесу за допомогою кумулятивної суми
    wiener_process = np.cumsum(increments)
    wiener_process = np.insert(wiener_process, 0, 0)
    wiener_processes.append(wiener_process)

wiener_processes = np.array(wiener_processes)

# Обчислення середнього та дисперсії
average_values = np.mean(wiener_processes, axis=0)
variance_values = np.var(wiener_processes, axis=0)

# Оновлення масиву time
time_with_initial = np.insert(time, 0, 0)

plt.figure(figsize=(14, 6))
plt.plot(time_with_initial, average_values, label="Середнє", color="blue")
plt.plot(time_with_initial, variance_values, label="Дисперсія", color="red")
plt.xlabel("Кількість")
plt.ylabel("Значення")
plt.legend()
plt.title("Середнє і дисперсія Віннерівського процесу")
plt.show()

# Перший вихід
first_passage_times = []

for process in wiener_processes:
    crossing_times = time[process[1:] >= target_level]
    if len(crossing_times) > 0:
        first_passage_times.append(crossing_times[0])
    else:
        first_passage_times.append(np.nan)

first_passage_times = np.array(first_passage_times)
first_passage_times = first_passage_times[~np.isnan(first_passage_times)]

# Розподіл ймовірностей часу першого виходу вінерівського процесу
plt.figure(figsize=(14, 6))
plt.hist(first_passage_times, bins=30, color='purple', edgecolor='black', density=True)
plt.xlabel("Вихід")
plt.ylabel("Щільність")
plt.title(f"Розподіл ймовірностей часу першого виходу вінерівського процесу {target_level}")
plt.show()
