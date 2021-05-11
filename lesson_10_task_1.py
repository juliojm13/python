class Matrix:
    def __init__(self, matrix=None, n=None, m=None):
        if n and m:
            self.n = n
            self.m = m
            self.matrix = []
            for i in range(n):
                column = []
                for j in range(m):
                    column.append(input(f'enter element {i, j}'))
                self.matrix.append(column)
        else:
            self.matrix = matrix
            self.n = len(self.matrix)
            self.m = len(self.matrix[0])

    def __str__(self):
        result = ''
        for col in self.matrix:
            for el in col:
                el = str(el)
                result += el + "  "
            result += '\n'

        return result

    def __add__(self, other):
        result = []
        for i in range(self.n):
            result.append([])
            for j in range(self.m):
                result[i].append(int(self.matrix[i][j]) + int(other.matrix[i][j]))

        return Matrix(matrix=result)


matrix_1 = Matrix(n=2, m=2)
print(matrix_1)
matrix_2 = Matrix(n=2, m=2)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2 + matrix_2 + matrix_1
print(matrix_1 + matrix_3)
