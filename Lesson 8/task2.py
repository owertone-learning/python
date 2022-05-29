class Oper:
    def __init__(self, del_1, del_2):
        self.del_1 = del_1
        self.del_2 = del_2

    def justdoit(self):
        if self.del_2 != 0:
            return f'Деление: {round((self.del_1 / self.del_2), 3)}'
        else:
            raise DataCheck(self)


class DataCheck(Exception):
    def __str__(self):
        return f'На ноль делить нельзя!'


try:
    go = Oper(int(input('Введите делимое: ')), int(input('Введите делитель: ')))
    print(go.justdoit())
except DataCheck:
    print(f'Деление на ноль запрещено!')
