# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
# При нечётном количестве элементов последний сохранить на своём месте. 
# Для заполнения списка элементов нужно использовать функцию input().

go = 'y'
while go == 'y' or go == 'н':
    list_ = []
    answer = input('Сколько элементов в вашем списке?')
    if answer.isnumeric():  # Проверяем что нам ввели
        i = 1
        while i - 1 < int(answer):
            list_.append(input(f'Вставьте {i}-ый элемент списка'))
            i += 1

        print(f'Вы ввели список: {list_}')

        i = 0
        while i <= (len(list_)/2 - 1):  # 
            list_[2*i], list_[2*i+1] = list_[2*i+1], list_[2*i]  # Замена чётных элементов на нечётные
            i += 1
        print(f'Полученный список: {list_}')
        go = input('Ещё раз? y/n')
    else: 
        print('Введите число!')
        continue
    

print('Пока!')


