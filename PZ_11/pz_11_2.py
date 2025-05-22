# Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.

# Читаем исходный файл и выводим его содержимое
with open('11_2.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)

    # Подсчет количества символов
    char_count = len(content)
    print(f"\nКоличество символов в тексте: {char_count}")

    # Находим самую длинную строку
    lines = content.split('\n')
    longest_line = max(lines, key=len)

# Создаем новый файл с самой длинной строкой
with open('longest_line.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(longest_line)

print(f"\nСамая длинная строка (длина {len(longest_line)} символов):")
print(longest_line)
print("Она была сохранена в файл 'longest_line.txt'")