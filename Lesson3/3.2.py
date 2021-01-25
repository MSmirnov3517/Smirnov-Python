def my_func(name, surname, year, city, email, phone):
    print(f'имя - {name}/ фамилия - {surname}/ год рождения - {year}/ город - {city}/ email - {email}/ номер телефона - {phone}')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city= input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите номер телефона: ')

my_func(name, surname, year, city, email, phone)