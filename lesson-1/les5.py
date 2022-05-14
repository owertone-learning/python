revenue = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))
profit = revenue - costs  # сразу считаем прибыль
benefit = 0

if profit > 0:
    print(f'Компания приносит прибыль! Вы заработали {profit} тысяч миллионов!')
    benefit = (profit / revenue) * 100
    print(f'Рентабельность компании {benefit:.0f} процентов')
    personal = int(input('Введите количество сотрудников компании: '))
    print(f'Прибыль на сотрудника {profit / personal:.2f} тысяч миллионов')  # оставил округление до второй цифры
elif profit == 0:
    print('Вышли в ноль...')
else:
    print(f'Компания в убытках на {profit} тысяч миллионов, нужно что-то делать!')
