class Cell:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f'{self.param}'

    def __add__(self, other):
        result = self.param + other.param
        return Cell(result)

    def __sub__(self, other):
        if (self.param - other.param) > 0:
            return Cell(self.param - other.param)
        else:
            return "Error"

    def __mul__(self, other):
        return Cell(self.param * other.param)

    def __floordiv__(self, other):
        return Cell(self.param / other.param)

    def make_order(self, space):
        x = self.param // space
        for i in range(x):
            print('*' * space + '\n')
        print("*" * (self.param % space))


cell_1 = Cell(10)
cell_2 = Cell(11)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
cell_2.make_order(5)
cell_1.make_order(3)
