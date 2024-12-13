# Дан список размера N, все элементы которого, кроме одного, упорядочены по убыванию. Сделать список упорядоченным, переместив элемент, нарушающий
# упорядоченность, на новую позицию.

def fix_ordered_list(lst):
    # Проходим по списку, чтобы найти индекс первого элемента, который нарушает порядок
    for i in range(len(lst) - 1):
        # Если текущий элемент меньше следующего, значит порядок нарушен
        if lst[i] < lst[i + 1]:
            out_of_order_index = i + 1  # Сохраняем индекс элемента, который нарушает порядок
            break
    else:
        return lst  # Если порядок не нарушен, возвращаем оригинальный список

    out_of_order_element = lst[out_of_order_index]  # Извлекаем элемент, который нарушает порядок

    lst.pop(out_of_order_index) # Удаляем его из списка

    # Находим правильную позицию для этого элемента в отсортированном списке
    insert_index = 0
    while insert_index < len(lst) and lst[insert_index] > out_of_order_element:
        insert_index += 1  # Увеличиваем индекс, пока не найдем место для вставки

    lst.insert(insert_index, out_of_order_element)  # Вставляем элемент на правильную позицию

    return lst  # Возвращаем исправленный список

while True:
    try:
        N = int(input("Введите размер списка: "))
        # Проверка, что размер списка положительный
        if N <= 0:
            raise ValueError("Размер списка должен быть положительным числом.")

        # Ввод элементов списка через пробел и преобразование их в целые числа
        lst = list(map(int, input(f"Введите {N} чисел через пробел: ").split()))

        # Проверка, что введено ровно N чисел
        if len(lst) != N:
            raise ValueError(f"Вы должны ввести ровно {N} чисел.")
        # Вызываем функцию для упорядочивания списка
        sorted_list = fix_ordered_list(lst)
        print("Упорядоченный список:", sorted_list)  # Выводим упорядоченный список
        break  # Выход из цикла, если все прошло успешно

    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, попробуйте еще раз.")  # Обработка ошибок ввода

