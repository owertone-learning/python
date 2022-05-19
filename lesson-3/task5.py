def calc():
    global result
    result = 0
    while True:
        numbers = input('Введите числа через пробел (чтобы остановить программу введите q): ')
        num_list = numbers.split()
        total = []
        if 'q' in num_list:
            print(
                f'Программа остановлена. Сумма введенных чисел: {int(result) if result - int(result) == 0 else result}')
            break
        else:
            for num in num_list:
                if num.replace('.', '').isdigit():
                    total.append(float(num))
            result += sum(total)
            print(f'Сумма введенных чисел: {int(result) if result - int(result) == 0 else result}')
    return result


calc()
print(f'Итоговая сумма: {int(result) if result - int(result) == 0 else result}')
