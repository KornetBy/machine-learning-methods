"""
Найдите индексы первого вхождения максимального элемента.
Выведите два числа: номер строки и номер столбца, в которых стоит
наибольший элемент в двумерном массиве.
"""

def find_max_index(matrix):
    max_value = matrix[0][0]
    max_row, max_col = 0, 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row, max_col = i, j

    return max_row, max_col

def input_matrix():
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
        while len(row) != cols:
            print(f"Ошибка: Введите {cols} элементов для строки")
            row = list(map(int, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
        matrix.append(row)

    return matrix

# Ввод и обработка матрицы
matrix = input_matrix()
max_row, max_col = find_max_index(matrix)
print(f"Индексы первого вхождения максимального элемента: строка {max_row}, столбец {max_col}")
