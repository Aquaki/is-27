# пз5, в11, з1
# Составить функцию, которая напечатает сорок любых символов.

import tkinter as tk
import random
import string


def print_forty_random_characters():
    # Создаем главное окно
    root = tk.Tk()
    root.title("40 случайных символов")

    # Создаем текстовый виджет
    text_widget = tk.Text(root, height=2, width=50)
    text_widget.pack(padx=10, pady=10)

    # Генерируем 40 случайных символов
    random_characters = ''.join(random.choices(
        string.ascii_letters + string.digits + string.punctuation,
        k=40
    ))

    # Вставляем символы в текстовый виджет
    text_widget.insert(tk.END, random_characters)

    # Делаем текстовый виджет только для чтения
    text_widget.config(state=tk.DISABLED)

    # Добавляем кнопку для закрытия окна
    close_button = tk.Button(root, text="Закрыть", command=root.destroy)
    close_button.pack(pady=5)

    # Запускаем главный цикл
    root.mainloop()
# Вызываем функцию
print_forty_random_characters()