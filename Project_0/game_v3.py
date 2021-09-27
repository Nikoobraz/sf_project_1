"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

gold = (1 + 5**0.5) / 2   # We'll use golden ratio method.


def random_predict(number: int= 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    edges = [0, 100]
    predict_number = round((edges[1] - edges[0]) / gold)

    while True:
        count += 1
        if number > predict_number:
            edges[0] = predict_number
            predict_number += round((edges[1] - edges[0]) / gold)
        elif number < predict_number:
            edges[1] = predict_number
            predict_number -= round((edges[1] - edges[0]) / gold)
        else:
            break

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 10000 подходов 
    угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали числа

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
