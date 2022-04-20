# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
list_num = []
number = input('Введите число:')
i = 0
while i < len(number):
    list_num.append(int(number[i]))
    i += 1
    print(list_num)
print('Наибольшая цифра:', max(list_num))
