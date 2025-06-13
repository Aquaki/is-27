# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово «произведение»

import re

def extract_writers():
    with open('writer.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    # Универсальный шаблон для поиска фамилий писателей
    pattern = re.compile(
        r'(?:^|\n)([А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?)(?:\s[А-ЯЁ][.,]?[А-ЯЁ][.,]?)?\s*(?=\()'
    )
    writers = pattern.findall(content)

    # Удаляем возможные ложные срабатывания
    filtered_writers = [w for w in writers if len(w) > 2 and not w.endswith('ские')]

    return filtered_writers


def replace_novel_to_work():
    with open('writer.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    # Замена слова "роман" на "произведение"
    new_content = re.sub(
        r'\bроман\b',
        'произведение',
        content
    )
    return new_content


def main():
    # Извлекаем фамилии писателей
    writers = extract_writers()
    print(f"Найдено {len(writers)} фамилий писателей.")
    print("Список фамилий:", ', '.join(writers))

    # Создаем новый файл с заменой
    new_content = replace_novel_to_work()

    with open('writer_processed.txt', 'w', encoding='utf-8') as file:
        file.write(new_content)
        file.write(f"\n\nВсего найдено фамилий писателей: {len(writers)}\n")
        file.write("Список фамилий:\n")
        file.write("\n".join(f"- {w}" for w in writers))

    print("Новый файл 'writer_processed.txt' успешно создан.")


if __name__ == "__main__":
    main()