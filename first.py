# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

answer = 'y'
while answer == 'y':

    num1 = int(input('Введите делимое'))
    num2 = int(input('Введите делитель'))

    if num2 == 0:
        print('Нельзя делить на ноль!')
        continue

    division = lambda a,b: round(a/b, 2)
    print(f'{num1} поделить на {num2} = {division(num1, num2)}')

    answer = input('Еще раз? y/n')