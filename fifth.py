# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

    
def str_to_list(string):
    str_list = string.split(' ')
    i = 0
    while i <= len(str_list) - 1:
        str_list[i] = int(str_list[i])
        i += 1
    return str_list


full_list = [0]
while True:
    string = input('Введите числа через пробел (s для выхода) ')
    if 's' in string and len(string) > 1:
        full_list.extend(str_to_list(string[:-2]))
        print(f'Сумма введёных чисел {sum(full_list)}')
        break
    elif 's' in string and len(string) == 1:
        print(f'Сумма введёных чисел {sum(full_list)}')
        break
    else:
        full_list.extend(str_to_list(string))
        print(f'Сумма введёных чисел {sum(full_list)}')
