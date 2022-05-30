def print_data(first_name, second_name, year, city, email, phone):
    print(' '.join([first_name, second_name, year, city, email, phone]))

    print(
        f'{first_name} {second_name}, {year} года рождения, проживает в городе {city}, e-mail: {email}, телефон: {phone}')


print_data(first_name='Mакс', second_name='Пэйн', year='1937', city='Нью-Йорк', email='max@pain.com', phone='911-02-02')
