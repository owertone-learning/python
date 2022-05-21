with open('text_3.txt') as f:
    content = f.readlines()
    salary = []
    name = []
    limit = 20000
for line in content:
    new = line.split()
    salary.append(float(new[1]))
    name.append(new[0])
counter = 0
loosers = {}
for money in salary:
    if money < limit:
        print(f'Меньше 20к получает: {name[counter]} - {money}')
        loosers[name[counter]] = money
    counter += 1
print(f'Список зарабатывающих меньше 20 000: {loosers}')
print(f'Средняя величина дохода сотрудника: {sum(salary) / len(salary)}')
