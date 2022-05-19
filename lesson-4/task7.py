number = int(input('Введите число: '))


def fact(number):
    fact_num = 1
    for n in range(1, number + 1):
        fact_num *= n
        yield n
    print(f'Факториал {number}: {fact_num}')


fact(number)
for n in fact(number):
    print(n)
