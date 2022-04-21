# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите время в секундах'))

seconds = time % 60
minutes_time = time//60
hours = minutes_time//60
minutes = minutes_time % 60

print('Это {}:{}:{}'.format(hours, minutes, seconds))

