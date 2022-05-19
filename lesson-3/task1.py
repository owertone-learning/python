def my_func(a, b):
    try:
        c = a / b
        print(c)
    except ZeroDivisionError:
        print('Деление на ноль запрещено')


my_func(int(input('Введите первое число:')), int(input('Введите второе число:')))
