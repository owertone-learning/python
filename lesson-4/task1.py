from sys import argv

salary, trade_in_hour, pay_in_hour, bonus = argv
print(f'Выработка часов: {trade_in_hour}')
print(f'Ставка в час: {pay_in_hour}')
print(f'Премия: {bonus}')
try:
    salary = int(trade_in_hour) * int(pay_in_hour) + int(bonus)
    print(f'Зарплата итого: {salary}')
except ValueError:
    print('Данные введены неверно: введите 3 числа')

