import numpy as np
import matplotlib.pyplot as plt

intensity = 2
num_events = 1000
n_event_appearance = 10

inter_arrival_times = np.random.exponential(scale=1 / intensity, size=num_events)

arrival_times = np.cumsum(inter_arrival_times)

# Гістограма появи n-ї події
plt.figure(figsize=(14, 6))
plt.hist(arrival_times[:n_event_appearance], bins=15, color='skyblue', edgecolor='black')
plt.title(f"Гістограма появи {n_event_appearance} події")
plt.xlabel("Час")
plt.ylabel("Частота")
plt.show()

# Гістограма інтервалів між подіями
plt.figure(figsize=(14, 6))
plt.hist(inter_arrival_times, bins=30, color='salmon', edgecolor='black')
plt.title("Гістограма інтервалів між подіями")
plt.xlabel("Довжина інтервалу")
plt.ylabel("Частота")
plt.show()

# Поява точно n подій в проміжку часу
time_window = 1
num_simulations = 10000

event_counts = np.random.poisson(lam=intensity * time_window, size=num_simulations)

# Гістограма появи точно n подій в проміжку часу
plt.figure(figsize=(14, 6))
plt.hist(event_counts, bins=range(min(event_counts), max(event_counts) + 1), color='lightgreen', edgecolor='black')
plt.title("Гістограма появи точно n подій в проміжку часу")
plt.xlabel("Кількість подій")
plt.ylabel("Частота")
plt.show()
