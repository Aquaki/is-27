# Составить функцию, которая напечатает сорок любых символов.

import random  # Импортируем библиотеку random для генерации случайных чисел
import string  # Импортируем библиотеку string для доступа к наборам символов

def generate_random_string(length=40, chars=None):
    # Генерирует случайную строку заданной длины из указанного набора символов.
    # length: Длина генерируемой строки (по умолчанию 40)
    # chars: Набор символов для генерации (по умолчанию используется набор букв, цифр и знаков препинания)

    try:
        # Если набор символов не указан, используем стандартный набор
        if chars is None:
            # Объединяем буквы, цифры и знаки препинания в один набор символов
            chars = string.ascii_letters + string.digits + string.punctuation

        # Генерируем строку из случайных символов
        random_string = ''.join(random.choices(chars, k=length))  # Выбираем случайные символы и объединяем их в строку

        return random_string  # Возвращаем сгенерированную строку
    except Exception as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return f"Произошла ошибка: {e}"

# Вызываем функцию для генерации случайной строки
result = generate_random_string()
# Выводим результат на экран
print(result)
