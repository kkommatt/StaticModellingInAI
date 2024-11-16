import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import chisquare

data = pd.read_csv("countries.csv", delimiter=";")

# Витягнення стовпчика площі
country_areas = data['area'].astype(int)


# Витягнення першої цифри
def first_digit(x):
    return int(str(x)[0])


first_digits = np.array([first_digit(area) for area in country_areas])

# Розрахунок розподілу першої цифри
digit_counts = np.bincount(first_digits)[1:]
digit_probabilities = digit_counts / sum(digit_counts)

# Ймовірності за законом Бенфорда
benford_probabilities = np.log10(1 + 1 / np.arange(1, 10))

# Побудова графіків результатів
plt.figure(figsize=(10, 6))
plt.bar(np.arange(1, 10), digit_probabilities, alpha=0.7, label='Дані')
plt.plot(np.arange(1, 10), benford_probabilities, 'ro-', label='Бенфорд')
plt.xlabel('Перша цифра')
plt.ylabel('Ймовірність')
plt.title('Розподіл першої цифри та закон Бенфорда')
plt.legend()
plt.show()

print("Ймовірність даних: ", digit_probabilities)
print("Ймовірність Бенфорда: ", benford_probabilities)

# Ймовірності за законом Бенфорда
benford_probs = np.array([np.log10(1 + 1 / d) for d in range(1, 10)])


np.random.seed(42)

# Розподіл Бернуллі
p = 0.5
n_trials = 10
bernoulli_numbers = 100000 * np.random.binomial(n_trials-1, p, 10000)

# Розподіл Пуассона
lambda_param = 1
poisson_numbers = 100000 * np.random.poisson(lambda_param, 10000)

all_numbers = np.concatenate([bernoulli_numbers, poisson_numbers])

leading_digits = [int(str(num)[0]) for num in all_numbers]

# Обрахування частот появи
observed_counts = np.bincount(leading_digits, minlength=10)[1:]
observed_probs = observed_counts / sum(observed_counts)

# Критерій хі-квадрат
chi2_stat, p_value = chisquare(observed_probs, f_exp=benford_probs)

print("Спостережувана частота:", observed_probs)
print("Очікувана частота Бенфорда:", benford_probs)
print(f"Хі-квадрат: {chi2_stat:.4f}, P: {p_value:.4f}")

digits = np.arange(1, 10)
plt.bar(digits - 0.2, observed_probs, width=0.4, label="Спостережуване", color="skyblue")
plt.bar(digits + 0.2, benford_probs, width=0.4, label="Бенфорд", color="orange")
plt.xlabel("Перша цифра")
plt.ylabel("Ймовірність")
plt.title("Спостережувана перша цифра та закон Бенфорда")
plt.xticks(digits)
plt.legend()
plt.show()
