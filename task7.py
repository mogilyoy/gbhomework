# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json


comp_dict = {}
aver_dict = {}

with open('file7.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

i = 0
for line in lines:
    lines[i] = line.split()
    i+=1
all_income = 0

for i in range(0, len(lines)):
    profit = int(lines[i][2]) - int(lines[i][3])
    print(f'Прибыль {lines[i][1]} {lines[i][0]} составила {profit}')
    comp_dict[lines[i][0]] = profit
    all_income += profit
aver_dict['average_profit'] = all_income/len(lines)
print(f'Средняя прибыль компаний:{all_income/len(lines)}')

company_list = [comp_dict, aver_dict]
with open('data.json', 'w') as f:
    json_data = json.dumps(company_list, indent=4)
    print(json_data)
    f.write(json_data)
    
