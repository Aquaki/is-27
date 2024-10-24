try:
    c = int(input())
    if c >= 100 and c <=999:
        s = str(c)
        res = int(s[2::-1])
        print(f"Получилось число {res}")
    else:
        print("Введенно не трёхзначное число")
except ValueError:
    print("Ввели не целое число")
