from itertools import count, cycle

numbers = []
for number in count(3, 1):
    if number > 10:
        break
    else:
        numbers += [number]
print(numbers)

item = 0
for items in cycle(numbers):
    if item > 31:
        break
    print(items)
    item += 1