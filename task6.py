# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('file6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

dict = {}
full_list = []
lessons = []
for line in lines: 
    a = 0
    partial = line.split(':')
    lessons.append(partial[0])
    separate = partial[1].strip().split('(')
    for sep in separate:
        num = sep.split(') ')
        
        for el in num:
            try:
                a += int(el.strip())
            except ValueError:
                continue
    full_list.append(a)

i = 0
for lesson in lessons:
    dict[lesson] = full_list[i] 
    i+=1
print(dict)

         



