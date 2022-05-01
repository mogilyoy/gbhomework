# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументоv

def my_func(arg1, arg2, arg3):
    list = [arg1, arg2, arg3]
    list.remove(min(list))
    return sum(list)

answer = 'y'
while answer == 'y':
    num1 = int(input('Введите первое число'))
    num2 = int(input('Введите второе число'))
    num3 = int(input('Введите третье число'))

    print(f'Сумма двух максимальных чисел: {my_func(num1, num2, num3)}')

    answer = input('Ещё раз? y/n')
    
    