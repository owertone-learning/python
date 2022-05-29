from abc import ABC, abstractmethod

class Clothes (ABC):

    def __init__(self):
        ...

    @abstractmethod
    def calc(self):
        ...

    def __add__(self, other):
        return self.calc + other.calc

class Coat (Clothes):

    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def calc(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit (Clothes):

    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def calc(self):
        return round(self.height * 2 + 0.3, 2)

out1 = Coat(int(input('Введите размер:')))
out1.calc
out2 = Suit(int(input('Введите рост:')))
out2.calc
print(f'{out1 + out2} метров ткани нам понадобится')