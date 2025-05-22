# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Числа кратные трем:
# Количество чисел кратных трем:

import random

# 1. Создаем исходный файл с числами
with open('numbers.txt', 'w', encoding='utf-8') as f:
    # Генерируем 20 случайных чисел от -100 до 100
    numbers = [str(random.randint(-100, 100)) for _ in range(20)]
    f.write(' '.join(numbers))

# 2. Обрабатываем файл и создаем отчет
with open('numbers.txt', 'r', encoding='utf-8') as f_in, \
        open('report.txt', 'w', encoding='utf-8') as f_out:
    # Читаем числа из файла
    numbers = list(map(int, f_in.read().split()))

    # Вычисляем требуемые значения
    count = len(numbers)
    min_num = min(numbers)
    multiples_of_3 = [num for num in numbers if num % 3 == 0]
    count_multiples = len(multiples_of_3)

    # Записываем отчет в файл
    f_out.write(f"Исходные данные: {' '.join(map(str, numbers))}\n")
    f_out.write(f"Количество элементов: {count}\n")
    f_out.write(f"Минимальный элемент: {min_num}\n")
    f_out.write(f"Числа кратные трем: {' '.join(map(str, multiples_of_3))}\n")
    f_out.write(f"Количество чисел кратных трем: {count_multiples}\n")
