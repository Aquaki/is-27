# В последовательности на n целых элементов в первой ее половине найти количество положительных элементов.

def p_e(sequence):
    half = len(sequence) // 2
    return sum(map(lambda x: 1, filter(lambda x: x > 0, sequence[:half])))

numbers = [4, -2, 7, 8, 5, -1, 3, 9, -8, 2]
print(p_e(numbers))
