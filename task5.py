# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint

with open('file5.txt', 'w') as f:
    num_list = [randint(100, 1000) for el in range(1,20)]
    summa = sum(num_list)
    f.write(' '.join(f'{num_list}'))
    print(f'Сумма чисел {summa}')

