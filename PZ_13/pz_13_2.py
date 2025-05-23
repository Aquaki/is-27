# В двумерном списке найти минимальный и максимальные элементы.

# Исходная матрица
matrix = [
    [5, 3, 8],
    [2, 7, 1],
    [9, 4, 6]
]

# Находим минимальный и максимальный элементы
min_e = min(min(row) for row in matrix)
max_e = max(max(row) for row in matrix)

# Результирующая матрица (исходная + строка с min и max)
r_m = [row.copy() for row in matrix]
r_m.append(["Минимальный элемент:", min_e])
r_m.append(["Максимальный элемент:", max_e])

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nРезультирующая матрица:")
for row in r_m:
    print(row)