# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


num_dict = {
'one': 'Один', 
'two': 'Два', 
'three': 'Три', 
'four': 'Четыре',
'five': 'Пять',
'six': 'Шесть',
'seven': 'Семь',
'eight': 'Восемь',
'nine': 'Девять',
'ten': 'Десять'
}

with open('file4.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
new_list = []

for line in lines:
    line_lit = line.lower().split(' — ')
    for key in num_dict:
        if key in line_lit:
            line_lit[line_lit.index(key)] = num_dict[key]
            line = ' - '.join(line_lit)
            new_list.append(line)

with open('file4.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(new_list)

    