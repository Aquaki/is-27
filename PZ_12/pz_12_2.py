# В последовательности на n целых элементов в первой ее половине найти количество положительных элементов.

import string

text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

l_c = filter(lambda c: c in string.ascii_lowercase, text) # проверяем, является ли символ строчной буквой
print(''.join(l_c)) # Объединяем выбранные строчные буквы в одну строку и выводим результат