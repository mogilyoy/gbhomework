# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def data(name, surname, birth, sity, email, num):
    print(f'{name} {surname} {birth} {sity} {email} {num}')

answer = 'y'

while answer == 'y':
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    birth = input('Введите дату рождения: ')
    sity = input('Введите ваш город: ')
    email = input('Введите почту: ')
    num = input('Введите телеон: ')    
    data(name, surname, birth, sity, email, num)
    answer = input('Ещё раз? y/n')