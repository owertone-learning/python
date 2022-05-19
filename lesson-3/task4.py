def my_func(x, y):
    print(x ** y)


my_func(4, -5)


def my_func_alt(x, y):
    result = 1
    for i in range(abs(y)):
        result = (1 / x) * result
    print(result)


my_func_alt(4, -5)
