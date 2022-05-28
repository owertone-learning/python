class Stationery:

    def __init__(self, title):
        self.title = title
        print(f'Если хотите взять {self.title} напишите {self.title}')

    def drow(self):
        print(f'Пора начать отрисовку!')


class Pen(Stationery):
    def drow(self):
        super().drow()
        print(f'Запускаем отрисовку {self.title}')


class Pencil(Stationery):
    def drow(self):
        super().drow()
        print(f'Запускаем отрисовку {self.title}')


class Handle(Stationery):
    def drow(self):
        super().drow()
        print(f'Запускаем отрисовку {self.title}')


drowing1 = Pen('Pen')
drowing2 = Pencil('Pencil')
drowing3 = Handle('Handle')
drowing = input('Чем рисуем?:')

if drowing.lower() == 'pen':
    drowing1.drow()
elif drowing.lower() == 'pencil':
    drowing2.drow()
elif drowing.lower() == 'handle':
    drowing3.drow()
else:
    print('Что-то ввели не так')
