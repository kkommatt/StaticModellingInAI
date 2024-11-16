import numpy as np


def flip_coin():
    return np.random.choice(['Герб', 'Цифра'])


def simulate_game(num_flips):
    winnings = 0
    for _ in range(num_flips):
        coin1 = flip_coin()
        coin2 = flip_coin()
        if coin1 == 'Герб' and coin2 == 'Цифра':
            winnings += 4  # Гравець отримує $5, але платить $1 за кожен фліп
        else:
            winnings -= 1  # Гравець платить 1 долар за один фліп
    return winnings


def simulate_multiple_games(num_flips, num_players):
    results = []
    for _ in range(num_players):
        result = simulate_game(num_flips)
        results.append(result)
    return results


# Параметри
num_flips = 100
num_players = 10

results = simulate_multiple_games(num_flips, num_players)
print("Виграш для кожного гравця", results)
print("Середній виграш на одного гравця", np.mean(results))


def simulate_new_game(num_flips):
    winnings = 0
    for _ in range(num_flips):
        coin1 = flip_coin()
        coin2 = flip_coin()
        if coin1 == 'Герб' and coin2 == 'Герб':
            winnings += 4  # Гравець отримує $5, але платить $1 за кожен фліп
        else:
            winnings -= 1  # Гравець платить $1 за кожне обертання
    return winnings


def simulate_multiple_new_games(num_flips, num_players):
    results = []
    for _ in range(num_players):
        result = simulate_new_game(num_flips)
        results.append(result)
    return results


new_results = simulate_multiple_new_games(num_flips, num_players)
print("Виграш для кожного гравця за новими правилами:", new_results)
print("Середній виграш на гравця за новими правилами:", np.mean(new_results))
