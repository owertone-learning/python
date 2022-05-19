from functools import reduce

my_list = [num for num in range(100, 1001, 1) if num % 2 == 0]
print(my_list)


def func(el1, el2):
    return el1 * el2


print(reduce(func, my_list))
