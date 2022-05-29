class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join([f'{item}' for item in items]) for items in self.matrix)

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result.append(self.matrix[i][j] + other.matrix[i][j])
        step = 2
        matrix_sum = [' '.join(map(str, result[i:i + step])) for i in range(0, len(result), step)]
        return '\n'.join(matrix_sum)


matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix1)
print('---------')
matrix2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix2)
print('--------- 1+2 -----------')
print(matrix1 + matrix2)
