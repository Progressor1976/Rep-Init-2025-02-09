"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

# Объявим функцию random_predict(), которая на вход будет принимать загаданное число number.
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        # print(number)
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')
      
# Подведём итог по созданному коду
# На самом деле мы с вами создали маленькую библиотеку game_v2.py. Она содержит в себе две документированные функции: 
# random_predict() и score_game(). 
# Мы можем импортировать их из других файлов и использовать в дальнейшем. Этим мы с вами займёмся в следующем юните.
# После выполнения пары заданий мы рассмотрим, как можно производить отладку кода в VS Code ↓)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
# score_game(random_predict)
# изменение