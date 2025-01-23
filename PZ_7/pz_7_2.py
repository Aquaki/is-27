#Дана строка, состоящая из русских слов, набранных заглавными буквами и
#разделенных пробелами (одним или несколькими). Преобразовать каждое слово в
#строке, заменив в нем все последующие вхождения его первой буквы на символ «.»
#(точка). Например, слово «МИНИМУМ» надо преобразовать в «МИНИ.У».
#Количество пробелов между словами не изменять.

def transform_word(word): #функция отвечает за преобразование одного слова
    if not word:
        return word #Если слово пустое (например, если это пробел), функция возвращает его без изменений.
    first_char = word[0] #Первая буква слова сохраняется в переменной first_char
    transformed = first_char  # Начинаем с первой буквы
    for char in word[1:]: # цикл, который проходит по всем символам слова, начиная со второго
        if char == first_char:
            transformed += '.' #Если символ равен first_char (первой букве), к строке transformed добавляется символ «.»
        else:
            transformed += char #Если символ не равен first_char, он добавляется в transformed без изменений.
    return transformed #возвращает преобразованное слово

def transform_string(input_string): #функция отвечает за преобразование всей строки, состоящей из нескольких слов
    words = input_string.split(' ')  # Разбиваем строку на слова по пробелам
    transformed_words = [transform_word(word) for word in words] #применяется функция transform_word ко всем словам в списке words, создавая новый список transformed_words
    return ' '.join(transformed_words)  # Соединяем слова обратно с пробелами

input_string = input("Введите строку: ")

result_string = transform_string(input_string) #Введенная строка передается в функцию transform_string, и результат сохраняется в переменной result_string

print("Исходная строка:", input_string)
print("Результирующая строка:", result_string)
