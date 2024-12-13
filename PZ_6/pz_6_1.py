# Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
# арифметическое элементов список с номерами от K до L включительно.

def calculate_average(lst, K, L):
    # Проверяем, что K и L находятся в допустимых границах
    if not (1 < K < L < len(lst)):
        raise ValueError("Некорректные значения K и L! Должно быть 1 < K < L < N.")

    # Выбираем нужные элементы списка (K-1 и L включительно)
    selected_elements = lst[K-1:L]  # Индексы K-1 и L-1 из-за нулевой индексации в Python

    # Находим среднее арифметическое
    average = sum(selected_elements) / len(selected_elements)

    return average, selected_elements

# Главный блок программы
while True:
    try:
        # Ввод данных
        N = int(input("Введите размер списка: "))  # Запрашиваем размер списка у пользователя
        my_list = list(map(int, input(f"Введите {N} целых чисел через пробел: ").split()))  # Вводим элементы списка

        # Проверка, что введено ровно N чисел
        if len(my_list) != N:
            raise ValueError(f"Вы должны ввести ровно {N} чисел.")

        # Ввод индексов K и L
        K = int(input("Введите число K: "))
        L = int(input("Введите число L: "))

        # Вычисляем среднее арифметическое
        average, selected_elements = calculate_average(my_list, K, L)

        # Выводим результат
        print(f"Среднее арифметическое элементов списка с индексами от {K} до {L} равно: {average}")

        break  # Выход из цикла, если все прошло успешно

    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректные значения.")

