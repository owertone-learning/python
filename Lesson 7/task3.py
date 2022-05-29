class Cell():
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return f'Сумма: {self.cell + other.cell}'

    def __sub__(self, other):
        if self.cell > other.cell:
            return f'Разность: {self.cell - other.cell}'
        else:
            return f'Разность: {other.cell - self.cell}'


    def __mul__(self, other):
        return f'Произведение: {self.cell * other.cell}'

    def __truediv__(self, other):
        return f'Деление: {round((self.cell / other.cell), 3)}'

    def make_order(self, row):
        super().__init__()
        cr = int(self.cell / row)
        return ''.join(['*' * row + '\n' for i in range(cr)]) + ''.join(['*' * (self.cell - (cr * row))])


cell_1 = Cell(15)
cell_2 = Cell(21)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(int(input('Задайте количество ячеек в ряду: '))))
