number = int(input('Введите целое положительное число:'))
num1 = 0
num2 = 0
while number != 0:
    num1 = number % 10
    number = number // 10
    if num1 > num2:
        num2 = num1
print('Наибольшее число', num2)
