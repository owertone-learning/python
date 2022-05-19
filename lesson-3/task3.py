"""простой перебор по условиям, много нужно писать, но мало нужно думать
    если количество элементов изменить, то нужно будет переписывать"""


def my_func(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print(f'Сумма 2х максимальных чисел: {num1 + num2}')
        else:
            print(f'Сумма 2х максимальных чисел: {num1 + num3}')
    elif num2 > num1:
        if num1 > num3:
            print(f'Сумма 2х максимальных чисел: {num2 + num1}')
        else:
            print(f'Сумма 2х максимальных чисел: {num2 + num3}')
    elif num3 > num1:
        if num1 > num2:
            print(f'Сумма 2х максимальных чисел: {num3 + num1}')
        else:
            print(f'Сумма 2х максимальных чисел: {num3 + num2}')


my_func(6, 10, 7)

""" создаем последовательность, находим по очереди от нее максимальное число и складываем их
    плюс в том, что ее можно масштабировать на неопределенное количество элементов не переписывая код
    
    def my_func_alt (*args):
        sum = [*args]
        print(f'альтернативная функция: {sum.pop(sum.index(max(sum))) + sum.pop(sum.index(max(sum)))}')
    my_func_alt(6, 10, 4, 40, 2)
    
    """


def my_func_alt(num1, num2, num3):
    sum = [num1, num2, num3]
    print(f'альтернативная функция: {sum.pop(sum.index(max(sum))) + sum.pop(sum.index(max(sum)))}')


my_func_alt(6, 10, 7)
