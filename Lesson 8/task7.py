class ComplexNumber:
    def __init__(self, cmplx1, cmplx2):
        self.cmplx1 = cmplx1
        self.cmplx2 = cmplx2

    def __add__(self, other):
        return f'Сумма комплексных чисел: {complex(self.cmplx1, self.cmplx2) + complex(other.cmplx1, other.cmplx2)}'

    def __mul__(self, other):
        mul_1 = self.cmplx1*other.cmplx1 - self.cmplx2*other.cmplx2
        mul_2 = self.cmplx1*other.cmplx2 + self.cmplx2*other.cmplx1
        return f'Произведение комплексных чисел: {complex(mul_1, mul_2)}'

num_1 = ComplexNumber(7, 8)
num_2 = ComplexNumber(-5, 5)
print(num_1+num_2)
print(num_1*num_2)