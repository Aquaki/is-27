def swap_hundreds_and_tens(number):
    # Проверяем, что число трехзначное
    if 100 <= number <= 999:
        # Извлекаем цифры
        hundreds = number // 100  # Цифра сотен
        tens = (number // 10) % 10  # Цифра десятков
        units = number % 10  # Цифра единиц

        # Формируем новое число с переставленными сотнями и десятками
        new_number = tens * 100 + hundreds * 10 + units
        return new_number
    else:
        raise ValueError("Число должно быть трехзначным.")


# Пример
input_number = 123
result = swap_hundreds_and_tens(input_number)
print(result)  # Вывод: 213