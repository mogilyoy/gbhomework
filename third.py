# Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и dict.

go = 'y'
while go == 'y':
    month = input('Введите месяц в формате 1-12')
    year = {
    'зима': ['1', '2', '12'],
    'весна': ['3', '4', '5'],
    'лето': ['6', '7', '8'],
    'осень': ['9', '10', '11']
    }
    if 0<int(month)<13:
       for key, value in year.items():
           for num in value: 
               if num == month:
                   print(f'Сейчас {key}')
    else:
        continue
    go = input('Ещё раз? y/n')
print('Пока!')
