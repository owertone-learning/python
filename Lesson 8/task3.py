class Numbers:
    def __init__(self, num_list):
        self.num_list = num_list

    @property
    def calc(self):
        numbers = self.num_list
        num_list = numbers.split()
        total = []
        for num in num_list:
            if num.replace('.', '').isdigit():
                total.append(num)
            elif num.lower() == 'stop':
                raise NumCheck(num)
            else:
                raise NumCheck(num)
        return total


class NumCheck(Exception):

    def __init__(self, numlist):
        self.numlist = numlist


final_list = []
while True:
    try:
        first = Numbers(input('Напишите число или строку (чтобы остановить программу введите stop):'))
        final_list.extend(first.calc)
        print(f'Итоговый список: {final_list}')

    except NumCheck as f:
        if f.numlist == 'stop':
            print(f'Выполнение программы прервано!\nИтоговый список: {final_list}')
            break
        else:
            print(f'получены неверные данные: {f.numlist}\nИтоговый список: {final_list}')
