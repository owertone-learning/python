def print_data(first_name, second_name, year, city, email, phone):
    print(' '.join([first_name, second_name, year, city, email, phone]))

    print(
        f'{first_name} {second_name}, {year} года рождения, проживает в городе {city}, e-mail: {email}, телефон: {phone}')


print_data('Mакс', 'Пэйн', '1937', 'Нью-Йорк', 'max@pain.com', '911-02-02')
