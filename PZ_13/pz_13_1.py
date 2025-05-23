# В двумерном списке найти сумму элементов первых двух строк.

# Исходная матрица
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Вычисляем сумму элементов первых двух строк
sum_first_two_rows = sum(sum(row) for row in matrix[:2])

# Результирующая матрица (исходная матрица + сумма первых двух строк в конце)
r_m = [row.copy() for row in matrix]
r_m.append(["Сумма первых двух строк:", sum_first_two_rows])

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nРезультирующая матрица:")
for row in r_m:
    print(row)