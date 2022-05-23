class Worker:

    def __init__(self, nm, sm, pos, wage, bonus):
        self.name = nm
        self.surename = sm
        self.position = pos
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.position} {" ".join([self.name, self.surename])}')

    def get_total_income(self):
        print(f'Доход: {sum(self._income.values())}')


work = Position(input('Введите имя:'), input('Введите фамилию:'), input('Введите должность:'), 3000, 2000)
work.get_full_name()
work.get_total_income()
