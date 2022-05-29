# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from copy import copy

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        line = []
        matrix = []
        for i in range(0, len(self.matrix_list)):
            line = []
            for k in range(0, len(self.matrix_list[i])):
                line.append(f'{self.matrix_list[i][k]}')
            matrix.append(' '.join(line) + '\n')
        
        matrix = ''.join(matrix)
        return matrix

    def __add__(self,other):
        matrix = copy(self.matrix_list) 
        for i in range(0, len(self.matrix_list)):
            for k in range(0, len(self.matrix_list[i])):
                matrix[i][k] = self.matrix_list[i][k] + other.matrix_list[i][k]

        return Matrix(matrix)


matrix_1 = [[3, 4, 5], [1, 3, 4]]
matrix_2 = [[7, 6, 5], [9, 7, 6]]
matrix_3 = [[10, 10, 10], [100, 100, 100]]
a = Matrix(matrix_1)
b = Matrix(matrix_2)
c = Matrix(matrix_3)
print(a + b + c)


