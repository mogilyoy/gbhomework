#  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#  Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input('Введите число'))
number_100 = number * 111
number_10 = number * 11
print('Считаем {} + {} + {} = {}'.format(number, number_10, number_100, number + number_10 + number_100))